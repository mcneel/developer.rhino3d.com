+++
aliases = ["/en/5/samples/cpp/select-objects-by-layer/", "/en/6/samples/cpp/select-objects-by-layer/", "/en/7/samples/cpp/select-objects-by-layer/", "/wip/samples/cpp/select-objects-by-layer/"]
authors = [ "dale" ]
categories = [ "Layers" ]
description = "Demonstrates how to select all of the objects on a specified layer."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Select Objects by Layer"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/sellayer"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  // Get a reference to the layer table
  CRhinoLayerTable& layer_table = context.m_doc.m_layer_table;
  // Get the current layer
  const CRhinoLayer& current_layer = layer_table.CurrentLayer();

  // Prompt for a layer name
  CRhinoGetString gs;
  gs.SetCommandPrompt( L"Name of layer to select object" );
  gs.SetDefaultString( current_layer.LayerName() );
  gs.AcceptNothing( TRUE );
  gs.GetString();
  if( gs.CommandResult() != CRhinoCommand::success )
    return gs.CommandResult();

  // Validate the string
  ON_wString layer_name = gs.String();
  layer_name.TrimLeftAndRight();
  if( layer_name.IsEmpty() )
    return CRhinoCommand::cancel;

  // Find the layer
  int layer_index = layer_table.FindLayer( layer_name );
  if( layer_index < 0 )
  {
    RhinoApp().Print( L"\"%s\" does not exists.\n", layer_name );
    return CRhinoCommand::cancel;
  }

  // Get the layer
  const CRhinoLayer& layer = layer_table[layer_index];

  // Get all of the objects on the layer
  ON_SimpleArray<CRhinoObject*> obj_list;
  int i, obj_count = context.m_doc.LookupObject( layer, obj_list );

  // Select all of the layer objects
  for( i = 0; i < obj_count; i++ )
  {
    CRhinoObject* obj = obj_list[i];
    if( obj && obj->IsSelectable() )
      obj->Select();
  }

  if( obj_count )
    context.m_doc.Redraw();
  return CRhinoCommand::success;
}
```
