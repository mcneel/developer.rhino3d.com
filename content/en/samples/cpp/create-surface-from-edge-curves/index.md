+++
aliases = ["/en/5/samples/cpp/create-surface-from-edge-curves/", "/en/6/samples/cpp/create-surface-from-edge-curves/", "/en/7/samples/cpp/create-surface-from-edge-curves/", "/wip/samples/cpp/create-surface-from-edge-curves/"]
authors = [ "dale" ]
categories = [ "Adding Objects", "Curves", "Surfaces" ]
description = "Demonstrates how to create a surface object from four edge curves."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Create Surface from Edge Curves"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/edgesrf"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```cpp
CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
{
  // Pick four curve objects
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select 4 curves" );
  go.SetGeometryFilter( CRhinoGetObject::curve_object);
  go.GetObjects( 4, 4 );
  if( go.CommandResult() != CRhinoCommand::success )
    return go.CommandResult();

  // Validate results
  int i, count = go.ObjectCount();
  if( count != 4 )
    return CRhinoCommand::failure;

  ON_NurbsCurve nc[4];
  // Get nurb form of each curve
  for( i = 0; i < count; i++)
  {
    const ON_Curve* crv = go.Object(i).Curve();
    if( !crv )
      return CRhinoCommand::failure;
    if( !crv->GetNurbForm(nc[i]) )
      return CRhinoCommand::failure;
  }

  // Create the surface
  ON_Brep* brep = RhinoCreateEdgeSrf( 4, nc );
  if( !brep )
  {
    RhinoApp().Print( L"Unable to create surface.\n" );
    return CRhinoCommand::failure;
  }

  // Ready new brep object
  CRhinoBrepObject* obj = new CRhinoBrepObject;
  obj->SetBrep( brep );

  // Add new objet to document
  if( !context.m_doc.AddObject( obj ) )
  {
    delete obj;
    RhinoApp().Print( L"Unable to create surface.\n" );
    return CRhinoCommand::failure;
  }

  context.m_doc.Redraw();
  return CRhinoCommand::success;
}
```
