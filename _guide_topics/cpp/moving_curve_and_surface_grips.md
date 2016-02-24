---
title: Moving Curve and Surface Grips
description: This guide demonstrates how to move curve and surface object grips using C/C++.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Advanced']
origin: http://wiki.mcneel.com/developer/sdksamples/movegrips
order: 1
keywords: ['rhino', 'moving', 'grips']
layout: toc-guide-page
---

# Moving Curve and Surface Grips

{{ page.description }}

## Problem

You would like to move the control points of a curve or surface object using the Rhino C/C++ SDK.

## Solution

The curve and surface grips you see on the screen, after running Rhino's *PointsOn* command, are represented by `CRhinoGripObject`-derived objects.  To move a grip object, you have to do a few things:

1. Get a `CRhinoGripObject`.  You can use a `CRhinoGetObject` object to do this.
1. Call `CRhinoGripObject::MoveGrip` to transform the grip's location.
1. Call `CRhinoGripObject::Owner` to get the grips owning `CRhinoObject` object.
1. Call `CRhinoObject::NewObject` to create a new `CRhinoObject` object based on the new grip location.
1. Call `CRhinoDoc::ReplaceObject` to replace the original owning object with the new one.

## Sample

The following sample code demonstrates this.  

**NOTE**: This sample uses a `CRhinoXformObjectList` object to maintain the list of grips and grip owners.

```cpp
CRhinoCommand::result CCommandMoveGrips::RunCommand( const CRhinoCommandContext& context )
{
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select grips to move" );
  go.SetGeometryFilter( CRhinoGetObject::grip_object );
  go.GetObjects( 1, 0 );
  if( go.CommandResult() != success )
    return go.CommandResult();

  CRhinoXformObjectList xform_list;
  if( xform_list.AddObjects(go, true) < 1 )
    return failure;

  CRhinoGetPoint gp;
  gp.SetCommandPrompt( L"Point to move from" );
  gp.GetPoint();
  if( gp.CommandResult() != success )
    return gp.CommandResult();

  ON_3dPoint from = gp.Point();

  gp.SetCommandPrompt( L"Point to move to" );
  gp.SetBasePoint( from );
  gp.DrawLineFromPoint( from, TRUE );
  gp.GetPoint();
  if( gp.CommandResult() != success )
    return gp.CommandResult();

  ON_3dPoint to = gp.Point();

  ON_Xform xform;
  xform.Translation( to - from );
  if( xform.IsValid() )
  {
    // Transform the grip objects
    int i;
    for( i = 0; i < xform_list.m_grips.Count(); i++ )
      xform_list.m_grips[i]->MoveGrip( xform );

    // Replace the old owner with a new one
    for( i = 0; i < xform_list.m_grip_owners.Count(); i++ )
    {
      CRhinoObject* old_object = xform_list.m_grip_owners[i];
      if( old_object )
      {
        CRhinoObject* new_object = old_object->m_grips->NewObject();
        if( new_object )
          context.m_doc.ReplaceObject( CRhinoObjRef(old_object), new_object, true );
      }
    }

    context.m_doc.Redraw();
  }

  return success;
}
```
