+++
aliases = ["/5/guides/opennurbs/finding-annotation-font/", "/6/guides/opennurbs/finding-annotation-font/", "/7/guides/opennurbs/finding-annotation-font/", "/wip/guides/opennurbs/finding-annotation-font/"]
authors = [ "dale" ]
categories = [ "Advanced" ]
description = "This guide demonstrates how to get an Annotation object's font using openNURBS."
keywords = [ "openNURBS", "object", "visibility" ]
languages = [ "C/C++" ]
sdk = [ "openNURBS" ]
title = "Finding an Annotation object's font"
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

There are many changes to ```ONX_Model``` in openNURBS. In prior versions, I was getting the font and its id information for ```ON_Leader2``` with:

```cpp
ONX_Model model = ...
const ON_Leader2* leader = ...
const ON_Font& font = model.m_font_table[leader->Index()];
```

How can I do this with the current openNURBS?

## Answer

In openNURBS, the the dimension style, or ```ON_DimStyle```, specifies all appearance properties like the text font, size, and alignment, arrow head shape, and so on. To obtain the font used by an Annotation object, such as an ```ON_Leader```, you just need to query the object's effective dimension style.

## Example

The following example code can be used to get the ```ON_Font``` used by an ```ON_Leader``` using the openNURBS toolkit:

```cpp
ONX_Model model = ...

// Create a model geometry interator
ONX_ModelComponentIterator it(model, ON_ModelComponent::Type::ModelGeometry);
const ON_ModelComponent* model_component = nullptr;
for (model_component = it.FirstComponent(); nullptr != model_component; model_component = it.NextComponent())
{
  // Get the model geometry
  const ON_ModelGeometryComponent* model_geometry = ON_ModelGeometryComponent::Cast(model_component);
  if (nullptr == model_geometry)
    continue;

  // Try getting an annotation leader
  const ON_Leader* leader = ON_Leader::Cast(model_geometry->Geometry(nullptr));
  if (nullptr == leader)
    continue;

  // Get the parent dimension style
  const ON_ModelComponentReference& parent_dim_style_ref = model.DimensionStyleFromId(leader->DimensionStyleId());
  const ON_DimStyle* parent_dim_style = ON_DimStyle::Cast(parent_dim_style_ref.ModelComponent());
  if (nullptr == parent_dim_style)
    continue;
    
  // Get the effective dimension style
  const ON_DimStyle& dim_style = leader->DimensionStyle(*parent_dim_style);

  // Get the font
  const ON_Font& font = dim_style.Font();

  // TODO...
}
```
