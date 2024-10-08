+++
aliases = ["/en/5/samples/cpp/add-a-cone-surface/", "/en/6/samples/cpp/add-a-cone-surface/", "/en/7/samples/cpp/add-a-cone-surface/", "/en/wip/samples/cpp/add-a-cone-surface/"]
authors = [ "dale" ]
categories = [ "Adding Objects", "Surfaces" ]
description = "Demonstrates how to create a cone using ON_BrepCone."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Add a Cone Surface"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/addcone"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0
+++

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
