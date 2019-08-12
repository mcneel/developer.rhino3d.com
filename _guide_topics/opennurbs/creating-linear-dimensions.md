---
title: Creating Linear Dimensions
description: This guide demonstrates how to create linear dimensions using openNURBS.
authors: ['dale_fugier']
sdk: ['openNURBS']
languages: ['C/C++']
platforms: ['Windows', 'Mac']
categories: ['Advanced']
origin: unset
order: 1
keywords: ['openNURBS', 'dimension']
layout: toc-guide-page
---


## Question

The annotation classes are different in openNURBS 6. A sample on how to create a linear dimension would be really helpful.

## Answer

The annotation classes have been overhauled in Rhino 6. For an overview of what's new and what's changed, see the following:

[Annotation Objects](http://developer.rhino3d.com/guides/cpp/annotation-objects/)

Every annotation object needs a plane, dimension style, location, and text content. In addition, each specific type of annotation needs its specific information.

## Example

The following example code can be used to create linear dimensions using the openNURBS toolkit:

```cpp
/*
Description:
  Add an aligned linear dimension to the model. The dimension line is
  parallel to the segment connecting the dimension points.
Parameters:
  model - [in] 
    The model object.
  point0 - [in]
  point1 - [in]
    Locations of one of the points being dimensioned.
    The dimension line will be parallel to the segment
    connecting these points.
  line_point - [in]
    A point on the linear dimension line.
  plane_normal - [in]
    A vector perpendcular to the line between the extension points
    that defines the orientation of the dimension's plane.
  dim_style - [in]
    nullptr, model dimension style, or a valid override style.
    If invalid, then the current dimension style will be used.
  attributes - [in]
    nullptr or object attributes.
*/
static bool AddDimLinear(
  ONX_Model& model,
  ON_3dPoint point0,
  ON_3dPoint point1,
  ON_3dPoint line_point,
  ON_3dVector plane_normal,
  const ON_DimStyle* dim_style,
  const ON_3dmObjectAttributes* attributes
)
{
  if (nullptr == dim_style)
  {
    const ON_ModelComponentReference& dim_style_ref = model.CurrentDimensionStyle();
    dim_style = ON_DimStyle::Cast(dim_style_ref.ModelComponent());
  }

  if (nullptr == dim_style)
    return false;

  const ON_UUID parent_id
    = dim_style->ParentIdIsNotNil()
    ? dim_style->ParentId()
    : dim_style->Id();

  const ON_ModelComponentReference& parent_dim_style_ref = model.DimensionStyleFromId(parent_id);
  const ON_DimStyle* parent_dim_style = ON_DimStyle::Cast(parent_dim_style_ref.ModelComponent());
  if (nullptr == parent_dim_style)
    return false;

  ON_DimLinear dim_linear;
  if (nullptr == ON_DimLinear::CreateAligned(point0, point1, line_point, plane_normal, parent_dim_style->Id(), &dim_linear))
    return false;

  if (dim_style->ContentHash() != parent_dim_style->ContentHash())
  {
    ON_DimStyle* override_style = new ON_DimStyle(*dim_style);
    override_style->SetParentId(parent_dim_style->Id());
    override_style->ClearId();
    override_style->ClearName();
    override_style->OverrideFieldsWithDifferentValues(*dim_style, *parent_dim_style);
    if (override_style->HasOverrides())
      dim_linear.SetOverrideDimensionStyle(override_style);
    else
      delete override_style;
  }

  if (nullptr == attributes)
    attributes = &ON_3dmObjectAttributes::DefaultAttributes;

  // 'model' will copy input and manage this memory
  const ON_ModelComponentReference& geometry_ref = model.AddModelGeometryComponent(&dim_linear, attributes);
  return !geometry_ref.IsEmpty();
}
```

You can test the above static functions by adding the following sample code to the *Example_Write* project included with the openNURBS toolkit:

```cpp
ONX_Model model = ...;

model.AddDefaultLayer(L"Default", ON_Color::Black);
model.AddDefaultDimensionStyle(L"Default", ON::LengthUnitSystem::Millimeters, 0.001);

ON_3dPoint point0(0.0, 0.0, 0.0);
ON_3dPoint point1(10.0, 0.0, 0.0);
ON_3dPoint line_point(5.0, 5.0, 0.0);
ON_3dVector plane_normal = ON_3dVector::ZAxis;
bool rc = AddDimLinear(model, point0, point1, line_point, plane_normal, nullptr, nullptr);

model.Write(archive, 60);
```
