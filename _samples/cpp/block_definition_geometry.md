---
layout: code-sample-cpp
title: Block Definition Geometry
author: dale@mcneel.com
platforms: ['Windows']
apis: ['C/C++']
languages: ['C/C++']
keywords: ['rhino']
categories: ['Unsorted']
TODO: 0
origin: http://wiki.mcneel.com/developer/sdksamples/instancedefinitionobjects
description: Demonstrates how to obtain a block instance's definition geometry.
order: 1
---

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  CRhinoGetObject go;
  go.SetCommandPrompt(L"Select instance");
  go.SetGeometryFilter(CRhinoGetObject::instance_reference);
  go.GetObjects(1, 1);
  if (go.CommandResult() != CRhinoCommand::success)
    return go.CommandResult();

  const CRhinoInstanceObject* iref = CRhinoInstanceObject::Cast(go.Object(0).Object());
  if (iref == 0)
    return CRhinoCommand::failure;

  const CRhinoInstanceDefinition* idef = iref->InstanceDefinition();
  if (idef == 0)
    return CRhinoCommand::failure;

  ON_SimpleArray<const CRhinoObject*> objects;
  int count = idef->GetObjects(objects);
  for (int i = 0; i < count; i++ )
  {
    const CRhinoObject* obj = objects[i];
    if (obj != 0)
    {
      ON_wString str;
      ON_UuidToString( obj->Attributes().m_uuid, str );
      RhinoApp().Print(L"Object %d = %s\n", i, str);
    }
  }

  return CRhinoCommand::success;
}
```
