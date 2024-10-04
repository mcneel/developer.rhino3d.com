+++
aliases = ["/en/5/samples/cpp/creating-nurbs-cage-objects/", "/en/6/samples/cpp/creating-nurbs-cage-objects/", "/en/7/samples/cpp/creating-nurbs-cage-objects/", "/wip/samples/cpp/creating-nurbs-cage-objects/"]
authors = [ "dale" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to create a NURBS Cage objects."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Creating NURBS Cage Objects"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/addcage"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```cpp
CRhinoCommand::result CCommandFooBar::RunCommand( const CRhinoCommandContext& context )
{
  ON_3dPoint box_corners[8];
  CArgsRhinoGetBox args;

  CRhinoCommand::result rc = RhinoGetBox( args, box_corners, 0 );
  if( rc == CRhinoCommand::success )
  {
    int degree[3] = {3,3,3};   // defaults
    int cv_count[3] = {4,4,4}; // defaults

    ON_NurbsCage nurbs_cage;
    if( nurbs_cage.Create( box_corners,
        degree[0]+1, degree[1]+1, degree[2]+1,
        cv_count[0], cv_count[1], cv_count[2])
        )
    {
      CRhinoCageObject* cage_object = new CRhinoCageObject();
      if( cage_object )
      {
        cage_object->SetCage( nurbs_cage );
        context.m_doc.AddObject( cage_object );
        context.m_doc.Redraw();
      }
    }
  }

  return rc;
}
```
