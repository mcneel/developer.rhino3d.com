---
title: Pull Curve to Surface
description: Demonstrates how to use ON_Surface::Pullback() to pull a curve object to a surface object.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Curves', 'Surfaces']
origin: http://wiki.mcneel.com/developer/sdksamples/pullcurve
order: 1
keywords: ['rhino']
layout: code-sample-cpp
---

```cpp
CRhinoCommand::result CCommandTestSdk::RunCommand( const CRhinoCommandContext& context )
{
  CRhinoGetObject gc;
  gc.SetCommandPrompt( L"Select a curve on a surface" );
  gc.SetGeometryFilter( CRhinoGetObject::curve_object );
  gc.GetObjects( 1, 1 );
  if( gc.CommandResult() != CRhinoCommand::success )
    return gc.CommandResult();

  const ON_Curve* pC3d = gc.Object(0).Curve();
  if( !pC3d )
    return CRhinoCommand::failure;

  CRhinoGetObject gs;
  gs.SetCommandPrompt(L"Select the surface" );
  gs.EnableHighlight();
  gs.SetGeometryFilter( CRhinoGetObject::surface_object );
  gs.EnableDeselectAllBeforePostSelect( false );
  gs.EnablePreSelect( FALSE );
  gs.GetObjects( 1, 1 );
  if( gs.CommandResult() != CRhinoCommand::success )
    return gs.CommandResult();

  const ON_Surface* pS = gs.Object(0).Surface();
  if( !pS )
    return CRhinoCommand::failure;

  ON_Curve* pC2d = pS->Pullback( *pC3d, context.m_doc.AbsoluteTolerance() );
  if( !pC2d )
  {
    RhinoApp().Print( L"Unable to pull curve to surface.\n" );
    return CRhinoCommand::failure;
  }

  // At this point we now have a 2D curve to do with what we want.
  // In this case, we will just add it to the document.
  pC2d->ChangeDimension(3);
  if( pC2d->IsValid() )
  {
    CRhinoCurveObject* crv_obj = new CRhinoCurveObject();
    crv_obj->SetCurve( pC2d );
    if( !context.m_doc.AddObject(crv_obj) )
    {
      delete crv_obj;
      return CRhinoCommand::failure;
    }
  }

  context.m_doc.Redraw();

  return CRhinoCommand::success;
}
```
