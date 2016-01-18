---
title: Renaming Layers
description: This brief guide discusses how to rename a layer using C/C++.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Miscellaneous']
origin: http://wiki.mcneel.com/developer/sdksamples/renamelayer
order: 1
keywords: ['rhino']
layout: toc-guide-page
---

# Renaming Layers

{{ page.description }}

## Overview

Rhino layers (`CRhinoLayer`) are stored on a layer table (`CRhinoLayerTable`) which is located on the active document.  The process for modifying an existing layer, such as changing its name, is:

1. Get the existing layer.
1. Make a copy of it.
1. Modify the copy.
1. Call `CRhinoLayerTable::ModifyLayer()`.

## Sample

The following code sample demonstrates how to rename an existing layer...

```cpp
CRhinoCommand::result CCommandTestSdk::RunCommand(const CRhinoCommandContext& context)
{
  // Get the layer name
  CRhinoGetString gs;
  gs.SetCommandPrompt( L"Name of layer to rename" );
  gs.GetString();
  if( gs.CommandResult() != CRhinoCommand::success )
    return gs.CommandResult();

  // Validate the string
  ON_wString layer_name = gs.String();
  layer_name.TrimLeftAndRight();
  if( layer_name.IsEmpty() )
    return CRhinoCommand::nothing;

  // Get a reference to the layer table  
  CRhinoLayerTable& layer_table = context.m_doc.m_layer_table;

  // Find the layer
  int layer_index = layer_table.FindLayer( layer_name );
  if( layer_index < 0 )
  {
    RhinoApp().Print( L"Layer \"%s\" does not exist.\n", layer_name );
    return CRhinoCommand::cancel;
  }

  // Get the new layer name  
  gs.SetCommandPrompt( L"New layer name" );
  gs.GetString();
  if( gs.CommandResult() != CRhinoCommand::success )
    return gs.CommandResult();

  // Validate the string
  ON_wString new_name = gs.String();
  layer_name.TrimLeftAndRight();
  if( layer_name.IsEmpty() )
    return CRhinoCommand::nothing;

  // Compare both names  
  if( layer_name.CompareNoCase(new_name) == 0 )
    return CRhinoCommand::nothing;

  // Get the layer
  const CRhinoLayer& layer = layer_table[layer_index];

  // Make a copy of it, and modify the name
  ON_Layer onlayer( layer );
  onlayer.SetLayerName( new_name );

  // Modify the exising layer with the new definition  
  CRhinoCommand::result rc = CRhinoCommand::cancel;
  if( layer_table.ModifyLayer(onlayer, layer_index) )
    rc = CRhinoCommand::success;

  return rc;
}
```
