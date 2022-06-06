+++
aliases = ["/5/samples/cpp/block-definition-geometry/", "/6/samples/cpp/block-definition-geometry/", "/7/samples/cpp/block-definition-geometry/", "/wip/samples/cpp/block-definition-geometry/"]
authors = [ "dale" ]
categories = [ "Blocks" ]
description = "Demonstrates how to obtain a block instance's definition geometry."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Block Definition Geometry"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/instancedefinitionobjects"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

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
