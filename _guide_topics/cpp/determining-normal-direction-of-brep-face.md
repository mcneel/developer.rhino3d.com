---
title: Determining the Normal Direction of a Brep Face
description: This guide demonstrates how to determine the normal direction of a Brep face using C/C++.
authors: ['dale_fugier']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/sdksamples/evnormal
order: 1
keywords: ['rhino', 'normal', 'brep']
layout: toc-guide-page
---

 
## Overview

To determine the normal direction of a surface, you can use one of the following functions:

```cpp
ON_Surface::NormalAt()
ON_Surface::EvNormal()
```

To determine the normal direction of a face which is part of a Brep, you can also use the above functions, as an `ON_BrepFace` object is derived from `ON_Surface`. But, you will also need to take into account the orientation of the Brep face.  If the orientation of the Brep face is opposite of the underlying, natural surface orientation, then you will need to reverse the direction of the calculated normal vector.

It should also be noted that most surfaces in Rhino are really Breps with a single face.

## Sample

The following sample code demonstrates how to interactively determine the normal direction of a selected surface or Brep face.

```cpp
CRhinoCommand::result CCommandNormal::RunCommand( const CRhinoCommandContext& context )
{
  // Select a surface
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select surface" );
  go.SetGeometryFilter( CRhinoGetObject::surface_object );
  go.GetObjects( 1, 1 );
  if( go.CommandResult() != success )
    return go.CommandResult();

  // Get the selected face
  const CRhinoObjRef& ref = go.Object(0);
  const ON_BrepFace* face = ref.Face();
  if( 0 == face )
    return failure;

  // Pick a point on the surface. Constrain
  // picking to the face.
  CRhinoGetPoint gp;
  gp.SetCommandPrompt( L"Select point on surface" );
  gp.Constrain( *face );
  gp.GetPoint();
  if( gp.CommandResult() != success )
    return gp.CommandResult();

  ON_3dPoint pt = gp.Point();

  // Get the parameters of the point on the
  // surface that is closest to pt
  double u, v;
  if( face->GetClosestPoint(pt, &u, &v) )
  {
    ON_3dPoint pt;
    ON_3dVector du, dv, dir;
    if( face->EvNormal(u, v, pt, du, dv, dir) )
    {
      // if the face orientation is opposite of
      // the natural surface orientation, then
      // reverse the direction of the vector.
      if( face->m_bRev )
        dir.Reverse();

      RhinoApp().Print(
        L"Surface normal at uv(%.2f,%.2f) = (%.2f,%.2f,%.2f)\n",
        u,
        v,
        dir.x,
        dir.y,
        dir.z
        );
    }
  }

  return success;
}
```
