---
title: Creating Sublayers
description: This brief guide demonstrates how to create sublayers of a parent layer using C/C++.
authors: ['Dale Fugier']
author_contacts: ['dale']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/sdksamples/childlayer
order: 1
keywords: ['rhino', 'layers']
layout: toc-guide-page
---

 
## Problem

You would like to create a "sublayer" (or a "child layer") of a parent layer.

## Solution

All layers have a layer id field, returned by `ON_Layer::Id()`, that uniquely identifies that layer. Layers also maintain a parent id field, returned by `ON_Layer::ParentLayerId()`, that identifies the layer's parent.  If a layer's parent id is a `null` UUID, then the layer does not have a parent and, thus, is considered a root layer.

## Sample

The following sample demonstrates how to add a parent layer then then add a child layer to that parent.

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
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
