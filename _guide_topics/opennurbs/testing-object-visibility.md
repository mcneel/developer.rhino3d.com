---
title: Testing for Object Visibility
description: This guide demonstrates how to detect whether or not an object is visible using openNURBS.
authors: ['Dale Lear']
author_contacts: ['dalelear']
sdk: ['openNURBS']
languages: ['C/C++']
platforms: ['Windows', 'Mac']
categories: ['Advanced']
origin: http://wiki.mcneel.com/developer/onisobjectvisible
order: 1
keywords: ['openNURBS', 'object', 'visibility']
layout: toc-guide-page
---

 
## Question

I have created a sample model this has a parent layer and a sublayer.  If I add objects to each of these two layer and then turn off the parent layer in Rhino, the objects on both layers do not appear.  But, when I read the .3dm file using openNURBS, the objects on the sublayer report as being visible.  How can I correctly detect the visibility of an object?

## Answer

A Rhino object is considered visible if:

1. The object's mode is not set to hidden.
1. If the object's layer is not hidden.
1. If the object's layer does not have a parent layer that is hidden.

## Example

The following example code can be used to detect an object's true visibility when using the openNURBS toolkit:

```cpp
static bool IsLayerVisible(const ONX_Model& model, ON_UUID layer_id)
{
  bool rc = false;
  const ON_ModelComponentReference& model_component_ref = model.ComponentFromId(ON_ModelComponent::Type::Layer, layer_id);
  if (!model_component_ref.IsEmpty())
  {
    const ON_Layer* layer = ON_Layer::Cast(model_component_ref.ModelComponent());
    if (nullptr != layer)
    {
      rc = layer->IsVisible();
      if (rc && layer->ParentIdIsNotNil())
        return IsLayerVisible(model, layer->ParentId());
    }
  }
  return rc;
}

static bool IsLayerVisible(const ONX_Model& model, int layer_index)
{
  bool rc = false;
  const ON_ModelComponentReference& model_component_ref = model.ComponentFromIndex(ON_ModelComponent::Type::Layer, layer_index);
  if (!model_component_ref.IsEmpty())
  {
    const ON_Layer* layer = ON_Layer::Cast(model_component_ref.ModelComponent());
    if (nullptr != layer)
    {
      rc = layer->IsVisible();
      if (rc && layer->ParentIdIsNotNil())
        return IsLayerVisible(model, layer->ParentId());
    }
  }
  return rc;
}

static bool IsModelGeometryVisible(const ONX_Model& model, const ON_ModelGeometryComponent* model_geometry)
{
  bool rc = false;
  if (nullptr != model_geometry)
  {
    const ON_3dmObjectAttributes* attributes = model_geometry->Attributes(nullptr);
    if (nullptr != attributes)
    {
      switch (attributes->Mode())
      {
      case ON::normal_object:
      case ON::idef_object:
      case ON::locked_object:
        rc = IsLayerVisible(model, attributes->m_layer_index);
        break;
      }
    }
  }
  return rc;
}
```

You can test the above static functions by adding the following sample code to the *Example_Read* project included with the openNURBS toolkit:

```cpp
ONX_Model model = ...;

ONX_ModelComponentIterator it(model, ON_ModelComponent::Type::ModelGeometry);
const ON_ModelComponent* model_component = nullptr;
for (model_component = it.FirstComponent(); nullptr != model_component; model_component = it.NextComponent())
{
  const ON_ModelGeometryComponent* model_geometry = ON_ModelGeometryComponent::Cast(model_component);
  if (nullptr != model_geometry)
  {
    bool bVisible = IsModelGeometryVisible(model, model_geometry);
    if (bVisible)
    {
      // TODO...
    }
  }
}
```
