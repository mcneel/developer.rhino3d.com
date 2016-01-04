---
title: Add Torus
description: Demonstrates how to create a torus using ON_BrepTorus and add it to Rhino.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Unsorted']
origin: http://wiki.mcneel.com/developer/sdksamples/addtorus
order: 1
keywords: ['rhino']
layout: code-sample-cpp
---

```cpp
CRhinoCommand::result CCommandTest::RunCommand(
        const CRhinoCommandContext& context
        )
{
  double major_radius = 4.0;
  double minor_radius = 2.0;
  ON_Plane plane( ON_origin, ON_zaxis );
  ON_Circle circle( plane, major_radius );
  ON_Torus torus( circle, minor_radius );
  ON_Brep* brep = ON_BrepTorus( torus );
  if( brep )
  {
    CRhinoBrepObject* torus_object = new CRhinoBrepObject();
    torus_object->SetBrep( brep );
    if( context.m_doc.AddObject(torus_object) )
      context.m_doc.Redraw();
    else
      delete torus_object;
  }
  return CRhinoCommand::success;
}
```
