---
title: Picking Surface Point
description: This brief guide discusses how to pick points on a surface using C/C++.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/picksurfacepoint
order: 1
keywords: ['rhino', 'picking', 'points']
layout: toc-guide-page
---

# {{ page.title }}

{% include byline.html %}

{{ page.description }}

## Problem

You want to pick a point on the surface of an object.

## Solution

There are a couple of ways to do this:

- Use a `CRhinoGetObject` class.
- Use a `CRhinoGetPoint` class.

## Using CRhinoGetObject

When picking objects with a `CRhinoGetObject` object, the `CRhinoObjRef` returned by the object contains picking information, such as the location of the pick...

```cpp
CRhinoCommand::result CCommandTestPick1::RunCommand( const CRhinoCommandContext& context )
{
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select a surface or a polysurface" );
  go.SetGeometryFilter( CRhinoGetObject::surface_object | CRhinoGetObject::polysrf_object );
  go.EnablePreSelect( FALSE );
  go.GetObjects( 1, 1 );
  if( go.CommandResult() != CRhinoCommand::success )
    return go.CommandResult();

  const CRhinoObjRef& ref = go.Object(0);

  // If the object was selected by picking a point on it, then
  // SelectionPoint() returns true and the point where the selection
  // occured.
  ON_3dPoint pt;
  if( ref.SelectionPoint(pt) )
  {
    context.m_doc.AddPointObject( pt );
    context.m_doc.Redraw();
  }

  return CRhinoCommand::success;
}
```

## Using CRhinoGetPoint

When picking points with a `CRhinoGetPoint` object, you can constrain the point picking to a surface...

```cpp
CRhinoCommand::result CCommandTestPick2::RunCommand( const CRhinoCommandContext& context )
{
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select a surface" );
  go.SetGeometryFilter( CRhinoGetObject::surface_object );
  go.EnablePreSelect( FALSE );
  go.GetObjects( 1, 1 );
  if( go.CommandResult() != CRhinoCommand::success )
    return go.CommandResult();

  const CRhinoObjRef& ref = go.Object(0);
  const ON_BrepFace* face = ref.Face();
  if( 0 == face )
    return CRhinoCommand::failure;

  CRhinoGetPoint gp;
  gp.SetCommandPrompt( L"Select point on surface" );
  gp.Constrain( *face );
  gp.GetPoint();
  if( gp.CommandResult() != CRhinoCommand::success )
    return gp.CommandResult();

  ON_3dPoint pt = gp.Point();
  context.m_doc.AddPointObject( pt );
  context.m_doc.Redraw();

  return CRhinoCommand::success;
}
```
