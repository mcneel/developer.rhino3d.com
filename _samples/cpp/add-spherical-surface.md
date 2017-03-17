---
title: Add Spherical Surface
description: Demonstrates how to create a sphere using ON_RevSurface and add it to Rhino.
authors: ['Dale Fugier']
author_contacts: ['dale']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Adding Objects', 'Surfaces']
origin: http://wiki.mcneel.com/developer/sdksamples/addsphere
order: 1
keywords: ['rhino']
layout: code-sample-cpp
---

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  CRhinoCommand::result rc = CRhinoCommand::cancel;

  ON_3dPoint center( 0.0, 0.0, 0.0 );
  double radius = 5.0;
  ON_Sphere sphere( center, radius );
  ON_RevSurface* sphere_srf = sphere.RevSurfaceForm();
  if( !sphere_srf )
    return rc;

  CRhinoSurfaceObject* sphere_obj = new CRhinoSurfaceObject();
  sphere_obj->SetSurface( sphere_srf );

  if( context.m_doc.AddObject(sphere_obj) )
  {
    context.m_doc.Redraw();
    rc = CRhinoCommand::success;
  }
  else
  {
    delete sphere_obj;
    sphere_obj = NULL;
  }

  return rc;
}
```
