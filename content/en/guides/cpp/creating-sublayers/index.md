+++
aliases = ["/5/guides/cpp/creating-sublayers/", "/6/guides/cpp/creating-sublayers/", "/7/guides/cpp/creating-sublayers/", "/wip/guides/cpp/creating-sublayers/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This brief guide demonstrates how to create sublayers of a parent layer using C/C++."
keywords = [ "rhino", "layers" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Creating Sublayers"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/childlayer"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

 
## Problem

You would like to create a "sublayer" (or a "child layer") of a parent layer.

## Solution

All layers have a layer id field, returned by `ON_Layer::Id()`, that uniquely identifies that layer. Layers also maintain a parent id field, returned by `ON_Layer::ParentLayerId()`, that identifies the layer's parent.  If a layer's parent id is a `null` UUID, then the layer does not have a parent and, thus, is considered a root layer.

## Sample

The following sample demonstrates how to add a parent layer then then add a child layer to that parent.

```cpp
CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
{
  CRhinoLayerTable& layer_table = context.m_doc.m_layer_table;

  // Define parent layer
  ON_Layer parent_layer;
  parent_layer.SetName(L"Parent");

  // Add parent layer
  int parent_layer_index = layer_table.AddLayer(parent_layer);
  if (parent_layer_index >= 0) 
  {
    // Get the layer we just added
    const CRhinoLayer& layer = layer_table[parent_layer_index];

    // Define child layer
    ON_Layer child_layer;
    child_layer.SetName(L"Child");

    // Assign parent layer's id as child's parent id
    child_layer.SetParentLayerId(layer.Id());

    // Add child layer
    layer_table.AddLayer(child_layer);
  }

  return CRhinoCommand::success;
}
```
