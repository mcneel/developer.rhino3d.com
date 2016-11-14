---
title: Offsetting Curves on Surfaces
description: This guide demonstrates how to offset a curve on a surface using C/C++.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/sdksamples/offsetcrvonsrf
order: 1
keywords: ['rhino', 'offset', 'curve', 'surface']
layout: toc-guide-page
---

 
## Problem

You are using the `RhinoOffsetCurveOnSrf` function to offset a curve which was interpolated on a cylindrical surface.  The problem is that the results do not seem to match those of Rhino's `OffsetCrvOnSrf` command.  That is, the offset curve does not extend to the edges of the surfaces.  Why is this?

## Solution

After calculating the offset curve, the `OffsetCrvOnSrf` command extends both ends of that curve to the surface edge using `RhinoExtendCrvOnSrf`.  Below is an sample of how you can do this using the SDK...

## Sample

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  // Select curve on surface
  CRhinoGetObject gc;
  gc.SetCommandPrompt( L"Select curve on surface" );
  gc.SetGeometryFilter( CRhinoGetObject::curve_object );
  gc.GetObjects( 1, 1 );
  if( gc.CommandResult() != CRhinoCommand::success )
    return gc.CommandResult();

  // Validate curve
  const ON_Curve* crv = gc.Object(0).Curve();
  if( 0 == crv )
    return CRhinoCommand::failure;

  // Select base surface
  CRhinoGetObject gs;
  gs.SetCommandPrompt( L"Select base surface" );
  gs.SetGeometryFilter( CRhinoGetObject::surface_object );
  gs.EnablePreSelect( false );
  gs.EnableDeselectAllBeforePostSelect( false );
  gs.GetObjects( 1, 1 );
  if( gs.CommandResult() != CRhinoCommand::success )
    return gs.CommandResult();

  // Validate face
  const ON_BrepFace* face = gs.Object(0).Face();
  if( 0 == face )
    return CRhinoCommand::failure;

  // Validate brep
  const ON_Brep* brep = face->Brep();
  if( 0 == brep )
    return CRhinoCommand::failure;

  // Specify offset distance
  CRhinoGetNumber gd;
  gd.SetCommandPrompt( L"Offset distance" );
  gd.SetDefaultNumber( 1.0 );
  gd.GetNumber();
  if( gd.CommandResult() != CRhinoCommand::success )
    return gd.CommandResult();

  double dist = gd.Number();

  // Do offset curve on surface
  double tol = context.m_doc.AbsoluteTolerance();
  ON_SimpleArray<ON_Curve*> offset_curves;
  CRhinoCommand::result cmdrc = RhinoOffsetCurveOnSrf( crv, brep, face->m_face_index, dist, tol, offset_curves );
  if( cmdrc == CRhinoCommand::success )
  {
    int i = 0;
    ON_SimpleArray<const ON_Curve*> curves_to_join;
    curves_to_join.Append( offset_curves.Count(), offset_curves.Array() );

    // Try joining the offset curves
    ON_SimpleArray<ON_Curve*> joined_curves;
    BOOL rc = RhinoMergeCurves( curves_to_join, joined_curves, 2.0 * tol, TRUE );

    for( i = 0; i < curves_to_join.Count(); i++ )
      curves_to_join[i] = 0;

    if( rc )
    {
      for( i = 0; i < joined_curves.Count(); i++ )
      {
        ON_Curve* pC = joined_curves[i];
        if( pC )
        {
          // Extend both ends to edge of the surface
          if( !pC->IsClosed() )
            RhinoExtendCrvOnSrf( *face, pC );

          // Add to document
          CRhinoCurveObject* crv_obj = new CRhinoCurveObject();
          crv_obj->SetCurve( pC );
          context.m_doc.AddObject( crv_obj );

          joined_curves[i] = 0;
        }
      }

      // Do not leak memory
      for( i = 0; i < offset_curves.Count(); i++ )
      {
        if( offset_curves[i] )
        {
          delete offset_curves[i];
          offset_curves[i] = 0;
        }
      }
    }
    else
    {
      for( i = 0; i < offset_curves.Count(); i++)
      {
        ON_Curve* pC = offset_curves[i];
        if( pC )
        {
          // Extend both ends to edge of the surface
          if( !pC->IsClosed() )
            RhinoExtendCrvOnSrf( *face, pC );

          // Add to document
          CRhinoCurveObject* crv_obj = new CRhinoCurveObject();
          crv_obj->SetCurve( pC );
          context.m_doc.AddObject( crv_obj );

          offset_curves[i] = 0;
        }
      }
    }
  }

  context.m_doc.Redraw();

  return CRhinoCommand::success;
}
```
