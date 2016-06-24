---
title: Testing for Object Visibility
description: This guide demonstrates how to detect whether or not an object is visible using openNURBS.
author: dalelear@mcneel.com
apis: ['openNURBS']
languages: ['C/C++']
platforms: ['Windows', 'Mac']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/onisobjectvisible
order: 1
keywords: ['openNURBS', 'object', 'visibility']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## Question

I have created a sample model this has a parent layer and a sublayer.  If I add objects to each of these two layer and then turn off the parent layer in Rhino, the objects on both layers do not appear.  But, when I read the .3DM file using openNURBS, the objects on the sublayer report as being visible.  How can I correctly detect the visibility of an object?

## Answer

A Rhino object is considered visible if:

1. The object's mode is not set to hidden.
1. If the object's layer is not hidden.
1. If the object's layer does not have a parent layer that is hidden.

## Example

The following example code can be used to detect an object's true visibility when using the openNURBS toolkit:

```cpp
static bool IsLayerVisible( const ON_ObjectArray<ON_Layer>& layer_table, int layer_index )
{
  bool rc = false;
  // Validate the layer index
  if( layer_index >= 0 && layer_index < layer_table.Count() )
  {
    // Get the layer
    const ON_Layer& layer = layer_table[layer_index];
    // Get the layer's visibility
    rc = layer.IsVisible();
    // If the layer is visible, see if the layer has a parent. If so,
    // check to see if the layer's parent is visible. If not, then
    // the layer is also not visible.
    if( rc && ON_UuidIsNotNil(layer.m_parent_layer_id) )
    {
      int i, layer_count = layer_table.Count();
      for( i = 0; i < layer_count; i++ )
      {
        if( 0 == ON_UuidCompare(layer.m_parent_layer_id, layer_table[i].m_layer_id) )
          return IsLayerVisible( layer_table, i ); // recursive
      }
    }
  }
  return rc;
}

static bool IsModelObjectVisible( const ONX_Model& model, const ONX_Model_Object& model_object )
{
  bool rc = false;
  switch( model_object.m_attributes.Mode() )
  {
  case ON::normal_object:
  case ON::idef_object:
  case ON::locked_object:
    {
      // Get the object's layer
      int layer_index = model_object.m_attributes.m_layer_index;
      // See if the layer is visible
      rc = IsLayerVisible( model.m_layer_table, layer_index );
    }
    break;
  }
  return rc;
}
```

You can test the above static functions by adding the following sample code to the *Example_Read* project included with the openNURBS toolkit:

```cpp
// create a text dump of the model
if ( bVerboseTextDump )
{
  //dump->PushIndent();
  //model.Dump(*dump);
  //dump->PopIndent();

  int i, object_count = model.m_object_table.Count();
  for( i = 0; i < object_count; i++ )
  {
    const ONX_Model_Object& model_object = model.m_object_table[i];
    if( model_object.m_object )
    {
      bool bVisible = IsModelObjectVisible( model, model_object );
      dump->Print("Object uuid: ");
      dump->Print( model_object.m_attributes.m_uuid );
      dump->Print(", visible: %s", bVisible ? "true" : "false" );
      dump->Print("\n");
    }
  }
}
```
