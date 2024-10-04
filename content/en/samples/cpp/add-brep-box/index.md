+++
aliases = ["/en/5/samples/cpp/add-brep-box/", "/en/6/samples/cpp/add-brep-box/", "/en/7/samples/cpp/add-brep-box/", "/wip/samples/cpp/add-brep-box/"]
authors = [ "dale" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to add a Brep Box from a Rhino C++ plugin."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Add a Brep Box"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/addbrepbox"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```cpp
CRhinoCommand::result CCommandTestSdk::RunCommand(const CRhinoCommandContext& context)
{
  CRhinoCommand::result rc = CRhinoCommand::nothing;

  // define the corners of the box
  ON_3dPointArray corners;
  corners.Append( ON_3dPoint( 0.0,  0.0,  0.0) );
  corners.Append( ON_3dPoint(10.0,  0.0,  0.0) );
  corners.Append( ON_3dPoint(10.0, 10.0,  0.0) );
  corners.Append( ON_3dPoint( 0.0, 10.0,  0.0) );
  corners.Append( ON_3dPoint( 0.0,  0.0, 10.0) );
  corners.Append( ON_3dPoint(10.0,  0.0, 10.0) );
  corners.Append( ON_3dPoint(10.0, 10.0, 10.0) );
  corners.Append( ON_3dPoint( 0.0, 10.0, 10.0) );

  // Build the brep  
  ON_Brep* pBrep = ON_BrepBox( corners );
  if( pBrep )
  {
    CRhinoBrepObject* pObject = new CRhinoBrepObject();
    pObject->SetBrep( pBrep );
    if( context.m_doc.AddObject(pObject) )
    {
      context.m_doc.Redraw();
      rc = CRhinoCommand::success;
    }
    else
    {
      delete pObject;
      pObject = 0;
      rc = CRhinoCommand::failure;
    }
  }
  return rc;
}
```
