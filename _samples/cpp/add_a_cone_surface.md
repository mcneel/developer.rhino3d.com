---
layout: code-sample-cpp
title: Add a Cone Surface
author: dale@mcneel.com
platforms: ['Windows']
apis: ['C/C++']
languages: ['C/C++']
keywords: ['rhino']
categories: ['Unsorted']
origin: http://wiki.mcneel.com/developer/sdksamples/addcone
description: Demonstrates how to create a cone using ON_BrepCone.
order: 1
---

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  ON_Plane plane = ON_xy_plane;
  double height = 10.0;
  double radius = 5.0;
  BOOL bCapBottom = FALSE;

  ON_Cone cone( plane, height, radius );
  if( cone.IsValid() )
  {
    ON_Brep* cone_brep = ON_BrepCone( cone, bCapBottom );
    if( cone_brep )
    {
      CRhinoBrepObject* cone_object = new CRhinoBrepObject();
      cone_object->SetBrep( cone_brep );
      context.m_doc.AddObject( cone_object );
      context.m_doc.Redraw();
    }
  }

  return CRhinoCommand::success;
}
```
