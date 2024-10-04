+++
aliases = ["/en/5/samples/cpp/determine-objects-layer-name/", "/en/6/samples/cpp/determine-objects-layer-name/", "/en/7/samples/cpp/determine-objects-layer-name/", "/wip/samples/cpp/determine-objects-layer-name/"]
authors = [ "dale" ]
categories = [ "Layers" ]
description = "Demonstrates how to determine a selected object's layer name using C++."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Determine an Object's Layer Name"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/objectlayer"
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
  go.SetCommandPrompt( L"Select object" );
  go.GetObjects( 1, 1 );
  if( go.CommandResult() != CRhinoCommand::success )
    return go.CommandResult();

  const CRhinoObjRef& objref = go.Object(0);
  const CRhinoObject* object = objref.Object();
  if( !object )
    return CRhinoCommand::failure;

  const CRhinoObjectAttributes& attributes = object->Attributes();
  int layer_index = attributes.m_layer_index;

  const CRhinoLayerTable& layer_table = context.m_doc.m_layer_table;
  const CRhinoLayer& layer = layer_table[layer_index];
  ON_wString layer_name = layer.LayerName();
  RhinoApp().Print( L"The selected object's layer is \"%s\"\n", layer_name );

  return CRhinoCommand::success;
}
```
