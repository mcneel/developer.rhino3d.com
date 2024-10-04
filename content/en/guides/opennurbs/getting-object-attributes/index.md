+++
aliases = ["/en/5/guides/opennurbs/getting-object-attributes/", "/en/6/guides/opennurbs/getting-object-attributes/", "/en/7/guides/opennurbs/getting-object-attributes/", "/wip/guides/opennurbs/getting-object-attributes/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This guide demonstrates how to obtain attributes from model geometry objects."
keywords = [ "openNURBS", "Attributes", "Importing" ]
languages = [ "C/C++" ]
sdk = [ "openNURBS" ]
title = "Getting Object Attributes"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++


## Question

With prior version of openNURBS, it was easy to find the properties associated to geometry objects, such layer, material and groups, once the reference of the objects were available using ```ONX_Model_object```.

What is the correct way of finding the layer, material and groups, when we have a ```ON_ModelGeometryComponent``` object?

## Answer

In order to lookup referenced components, such as Layers, Materials, Groups, etc., you first must obtain the model geometry attributes, or ```ON_3dmObjectAttributes``` object. 

If you are referencing the ```Example_read``` sample included with the openNURBS toolkit, then after the 3DM file has been read, you can query an object’s render material as follows:

```cpp
ONX_Model model = ...

for (model_component = it.FirstComponent(); nullptr != model_component; model_component = it.NextComponent())
{
  const ON_ModelGeometryComponent* model_geometry = ON_ModelGeometryComponent::Cast(model_component);
  if (nullptr != model_geometry)
  {
    const ON_3dmObjectAttributes* attributes = model_geometry->Attributes(nullptr);
    if (nullptr != attributes)
    {
      // TODO
    }
  }      
}
```

Now that you have the attributes, you can use the helper functions on ```ONX_Model``` to access these components.

Here are a couple of helper functions you might find useful:

```cpp
/*
Description:
  Returns a pointer to an ON_Layer object, given an object's attributes.
*/
static const ON_Layer* ON_LayerFromAttributes(
  const ONX_Model& model, 
  const ON_3dmObjectAttributes& attributes
)
{
  const ON_Layer* layer = nullptr;
  const ON_ModelComponentReference& model_component_ref = model.LayerFromAttributes(attributes);
  if (!model_component_ref.IsEmpty())
    layer = ON_Layer::Cast(model_component_ref.ModelComponent());
  return layer;
}

/*
Description:
  Returns a pointer to an ON_Material object, given an object's attributes.
*/
static const ON_Material* ON_MaterialFromAttributes(
  const ONX_Model& model, 
  const ON_3dmObjectAttributes& attributes
)
{
  const ON_Material* material = nullptr;
  const ON_ModelComponentReference& model_component_ref = model.RenderMaterialFromAttributes(attributes);
  if (!model_component_ref.IsEmpty())
    material = ON_Material::Cast(model_component_ref.ModelComponent());
  return material;
}

/*
Description:
  Returns pointers to ON_Group objects, given an object's attributes.
*/
static int ON_GroupsFromAttributes(const ONX_Model& model, const ON_3dmObjectAttributes& attributes, ON_SimpleArray<const ON_Group*>& groups)
{
  const int group_count = groups.Count();
  ON_SimpleArray<int> group_indices;
  if (attributes.GetGroupList(group_indices) > 0)
  {
    for (int i = 0; i < group_indices.Count(); i++)
    {
      ON_ModelComponentReference model_component_ref = model.ComponentFromIndex(ON_ModelComponent::Type::Group, i);
      if (!model_component_ref.IsEmpty())
      {
        const ON_Group* group = ON_Group::Cast(model_component_ref.ModelComponent());
        if (nullptr != group)
          groups.Append(group);
      }
    }
  }
  return groups.Count() - group_count;
}
```

Here is an example of their usage:

```cpp
const ON_3dmObjectAttributes* attributes = model_geometry->Attributes(nullptr);
if (nullptr != attributes)
{
    // Try getting layer
    const ON_Layer* layer = ON_LayerFromAttributes(model, *attributes);
    if (nullptr != layer)
    {
      // TODO...
    }

    // Try getting material
    const ON_Material* material = ON_MaterialFromAttributes(model, *attributes);
    if (nullptr != material)
    {
      // TODO...
    }

    // Try getting groups
    ON_SimpleArray<const ON_Group*> groups;
    const int group_count = ON_GroupsFromAttributes(model, *attributes, groups);
    for (int i = 0; i < group_count; i++)
    {
      const ON_Group* group = groups[i];
      if (nullptr != group)
      {
        // TODO...
      }
    }
  }
}
```

