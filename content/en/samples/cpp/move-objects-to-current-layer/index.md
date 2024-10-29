+++
aliases = ["/en/5/samples/cpp/move-objects-to-current-layer/", "/en/6/samples/cpp/move-objects-to-current-layer/", "/en/7/samples/cpp/move-objects-to-current-layer/", "/en/wip/samples/cpp/move-objects-to-current-layer/"]
authors = [ "dale" ]
categories = [ "Layers" ]
description = "Demonstrates how to iterate through the Rhino geometry table and modify the layer of selected objects."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Move Objects to the Current Layer"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/moveobjectstocurrentlayer"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0
+++

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  // Get the current layer index
  const CRhinoLayerTable& layer_table = context.m_doc.m_layer_table;
  int layer_index = layer_table.CurrentLayerIndex();

  // Create an object iterator that filters on selected,
  // non-light objects in the current document only
  CRhinoObjectIterator it( CRhinoObjectIterator::normal_objects,
                           CRhinoObjectIterator::active_objects  );
  it.EnableSelectedFilter( TRUE );
  it.IncludeLights( FALSE );
  CRhinoObject* obj = NULL;
  int count = 0;

  // Walk the geometry table
  for( obj = it.First(); obj; obj = it.Next() )
  {
    // Ignore select objects that are already on the current layer
    if( obj->Attributes().m_layer_index == layer_index )
      continue;
    // Copy the object's attributes and set the new layer index
    CRhinoObjectAttributes atts( obj->Attributes() );
    atts.m_layer_index = layer_index;
    // Modify the object's attributes
    CRhinoObjRef ref(obj);
    if( context.m_doc.ModifyObjectAttributes(ref, atts) )
      count++;
  }
  if( count > 0 )
    context.m_doc.Redraw();
 return CRhinoCommand::success;
}
```
