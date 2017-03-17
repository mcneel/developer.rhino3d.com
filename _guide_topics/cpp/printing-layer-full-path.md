---
title: Printing a Layer's Full Path
description: This brief guide demonstrates now to obtain a layer's full path using C/C++.
authors: ['Dale Fugier']
author_contacts: ['dale']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/sdksamples/layerfullpath
order: 1
keywords: ['rhino', 'layer', 'printing']
layout: toc-guide-page
---

 
## Problem

You could like to print a layer's full path.  That is, if a layer "MyLayer"”" is nested, I would like to print out the nesting like this:

`"GreatGrandParent / GrandParent / Parent / MyLayer"`

## Solution

The following sample function ought to do the trick:

```cpp
static ON_wString RhinoFullLayerPath( CRhinoDoc& doc, const CRhinoLayer& layer )
{
  ON_wString layer_path;

  CRhinoLayerNode layer_node;
  layer_node.Create(layer.m_layer_index, 2, 0, true );
  if( layer_node.m_parent_count > 0 )
  {
    int i, layer_index = -1;
    for( i = layer_node.m_parent_count - 1; i >= 0; i-- )
    {
      layer_index = layer_node.m_parent_list[i];
      layer_path += doc.m_layer_table[layer_index].LayerName();
      layer_path += L" / ";
    }
  }
  layer_path += layer.LayerName();

  return layer_path;
}
```

You can use the function like this...

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  ON_wString s = RhinoFullLayerPath( context.m_doc, context.m_doc.m_layer_table.CurrentLayer() );
  RhinoApp().Print( L"%s\n", s.Array() );
  return CRhinoCommand::success;
```
