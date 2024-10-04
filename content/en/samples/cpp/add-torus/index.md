+++
aliases = ["/en/5/samples/cpp/add-torus/", "/en/6/samples/cpp/add-torus/", "/en/7/samples/cpp/add-torus/", "/wip/samples/cpp/add-torus/"]
authors = [ "dale" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to create a torus using ON_BrepTorus and add it to Rhino."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Add Torus"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/addtorus"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

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
