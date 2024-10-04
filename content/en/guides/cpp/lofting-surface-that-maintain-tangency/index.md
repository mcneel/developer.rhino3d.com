+++
aliases = ["/en/5/guides/cpp/lofting-surface-that-maintain-tangency/", "/en/6/guides/cpp/lofting-surface-that-maintain-tangency/", "/en/7/guides/cpp/lofting-surface-that-maintain-tangency/", "/wip/guides/cpp/lofting-surface-that-maintain-tangency/"]
authors = [ "dale" ]
categories = [ "Advanced" ]
description = "This guide demonstrates how to loft surfaces that maintain tangency using C/C++."
keywords = [ "rhino", "loft", "tangent" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Lofting Surfaces that Maintain Tangency"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/lofttangent"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

 
## Overview

When trying to loft a surface with starting or ending tangency, it is not enough just to set `CArgsRhinoLoft` object's `m_start_condition` and `m_end_condition` members to `CArgsRhinoLoft::leTangent`.  You also need to tell Rhino's lofter what it is that this lofted surface need to be tangent to.  You do this by setting the `m_trim` parameter of the starting and ending `CRhinoLoftCurve` objects.  This is a constant `ON_BrepTrim` pointer.  If you are lofting curves that you have picked using a `CRhinoGetObject` object, you can retrieve this pointer by simply calling `CRhinoObjRef::Trim()`.

## Sample

The following sample code demonstrates how to loft surfaces that maintain tangency with adjacent surfaces using the `CArgsRhinoLoft` class and the `RhinoSdkLoftSurface` function.  The definitions of these are in *rhinoSdkLoft.h*.

**NOTE**: This sample does not perform any curve sorting or direction matching.  This is the responsibility of the plugin developer.

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  // Select curves to loft
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select curves to loft" );
  go.SetGeometryFilter( CRhinoGetObject::curve_object | CRhinoGetObject::edge_object);
  go.SetGeometryAttributeFilter( CRhinoGetObject::open_curve );
  go.EnablePreSelect( false );
  go.GetObjects( 2, 0 );
  if( go.CommandResult() != CRhinoCommand::success )
    return go.CommandResult();

  // Create loft arguments object
  const int obj_count = go.ObjectCount();
  CArgsRhinoLoft args;
  args.m_loftcurves.SetCapacity( obj_count );

  // Add curves to loft arguments object
  int i;
  for( i = 0; i < obj_count; i++ )
  {
    const CRhinoObjRef& ref = go.Object(i);
    const ON_Curve* crv = ref.Curve();
    if( crv )
    {
      // New loft curve
      CRhinoLoftCurve* lc = new CRhinoLoftCurve;

      // Duplicate the selected curve. Note,
      // the loft curve will delete this curve.
      lc->m_curve = crv->DuplicateCurve();
      lc->m_curve->RemoveShortSegments( ON_ZERO_TOLERANCE );

      // Set other loft curve parameters
      lc->m_bPlanar = ( lc->m_curve->IsPlanar(&lc->m_plane) ? true : false );

      // If referenced geometry is a surface edge,
      // assign associated brep trim.
      lc->m_trim = ref.Trim();

      // Append loft curve to loft argument
      args.m_loftcurves.Append( lc );
    }
  }

  // If we do not have enough loft curves,
  // clean up and bail.
  const int lc_count = args.m_loftcurves.Count();
  if( lc_count < 2 )
  {
    for( i = 0; i < lc_count; i++ )
      delete args.m_loftcurves[i];
    return failure;
  }

  // If the starting loft curve has a trim,
  // set the start condition to tangent.
  if( args.m_loftcurves[0] && args.m_loftcurves[0]->m_trim )
  {
    args.m_start_condition = CArgsRhinoLoft::leTangent;
    args.m_bAllowStartTangent = TRUE;
  }

  // If the ending loft curve has a trim,
  // set the end condition to tangent.
  if( args.m_loftcurves[lc_count-1] && args.m_loftcurves[lc_count-1]->m_trim )
  {
    args.m_end_condition = CArgsRhinoLoft::leTangent;
    args.m_bAllowEndTangent = TRUE;
  }

  // Do the loft calculation
  ON_SimpleArray<ON_NurbsSurface*> srf_list;
  bool rc = RhinoSdkLoftSurface( args, srf_list );

  // Delete the loft curves so we do not leak memory.
  for( i = 0; i < args.m_loftcurves.Count(); i++ )
    delete args.m_loftcurves[i];
  args.m_loftcurves.Empty();

  // If the loft operation failed, bail.
  if( !rc )
    return failure;

  // If only one surface was calculated, add it to Rhino
  if( srf_list.Count() == 1 )
  {
    context.m_doc.AddSurfaceObject( *srf_list[0] );

    // CRhinoDoc::AddSurfaceObject() make a copy.
    // So, delete original so memory is not leaked.
    delete srf_list[0];
  }
  else
  {
    // If more than one surface was calculated,
    // create a list of breps.
    ON_SimpleArray<ON_Brep*> brep_list;
    for( i = 0; i < srf_list.Count(); i++)
    {
      if( srf_list[i]->IsValid() )
      {
        ON_Brep* brep = ON_Brep::New();
        brep->NewFace( *srf_list[i] );

        // ON_Brep::NewFace() make a copy.
        // So, delete original so memory is not leaked.
        delete srf_list[i];

        brep_list.Append( brep );
      }
    }

    // Try joining all breps
    double tol = context.m_doc.AbsoluteTolerance();
    ON_Brep* brep = RhinoJoinBreps( brep_list, tol );
    if( brep )
    {
      context.m_doc.AddBrepObject( *brep );

      // CRhinoDoc::AddBrepObject() make a copy.
      // So, delete original so memory is not leaked.
      delete brep;
    }
    else
    {
      // Othewise just add the individual breps to Rhino.
      for( i = 0; i < brep_list.Count(); i++ )
      {
        if( brep_list[i] )
        {
          context.m_doc.AddBrepObject( *brep_list[i] );

          // CRhinoDoc::AddBrepObject() make a copy.
          // So, delete original so memory is not leaked.
          delete brep_list[i];
        }
      }
    }
  }

  context.m_doc.Redraw();

  return success;
}
```
