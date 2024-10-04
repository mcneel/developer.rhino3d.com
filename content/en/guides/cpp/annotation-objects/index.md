+++
aliases = ["/en/5/guides/cpp/annotation-objects/", "/en/6/guides/cpp/annotation-objects/", "/en/7/guides/cpp/annotation-objects/", "/wip/guides/cpp/annotation-objects/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This guide discusses the annotation objects provided by the Rhino SDK."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Annotation Objects"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = ""
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
 
## Overview

There are two virtual and seven concrete annotation objects. The seven concrete classes are:

- `Text`: Created by the Rhino Text command.
- `Leader`: Created by the Rhino Leader command.
- `Linear dimension`: Created by the Rhino Dim, DimAligned, and DimRotated commands.
- `Angular dimension`: Created by the Rhino DimAngle command.
- `Radial dimension`: Created by the Rhino DimRadius and DimDiameter commands.
- `Ordinate dimension`: Created by the Rhino DimOrdinate command.
- `Centermark`: Created by the Rhino Centermark command.

The two virtual classes are:

- `Annotation `: Contains text content, plane, and dimension style information. This is the base class for all annotation objects.
- `Dimension`: Contains information common to the linear, angular, radial, ordinate, and centermark dimensions, primarily associated with the measured value (distance, angle).

The annotation geometry class hierarchy in openNURBS is:

- `ON_Annotation`: Pure virtual class derived from `ON_Geometry`.
  - `ON_Text`: Text geometry.
  - `ON_Leader`: Leader geometry.
  - `ON_Dimension`: Pure virtual class derived from `ON_Annotation`.
    - `ON_DimLinear`: Linear dimension geometry.
    - `ON_DimAngular`: Angular dimension geometry.
    - `ON_DimRadial`: Radial dimension geometry.
    - `ON_DimOrdinate`: Ordinate dimension geometry.
    - `ON_Centermark`: Centermark geometry.

Other openNURBS classes and useful member functions:

- `ON_TextContent`: Class that manages the RTF text and related text information and is a member of `ON_Annotation`.
- `ON_Annotation.Text()`: Rreturns a pointer to the object's text content.
- `ON_Annotation.RichText()`: Returns the "raw" rich text string.
- `ON_Annotation.PlainText()`: Returns the "string" part formatting instructions are removed.

The Rhino annotation object class hierarchy, including their geometry class member, in the Rhino SDK is:

- `CRhinoAnnotation, ON_Annotation`: Pure virtual class derived from `CRhinoObject`.
  - `CRhinoText, ON_Text`: Text object.
  - `CRhinoLeader, ON_Leader`: Leader object.
  - `CRhinoDimension, ON_Dimension`: Pure virtual class derived from `CRhinoAnnotation`.
    - `CRhinoDimLinear, ON_DimLinear`: Linear dimension object.
    - `CRhinoDimAngular, ON_DimAngular`: Angular dimension object.
    - `CRhinoDimRadial, ON_DimRadial`: Radial dimension object.
    - `CRhinoDimOrdinate, ON_DimOrdinate`: Ordinate dimension object.
    - `CRhinoCentermark, ON_Centermark`: Centermark object.

## Creating Annotation Objects

Every annotation object needs a plane, dimension style, location, and text content. In addition, each specific type of annotation needs its specific information.

Here are simple examples showing how to create annotation objects. Below, doc is a `CRhinoDoc` reference.

### Text

Creates a text object that says “Hello world” with the upper left corner at (1,2,3). The font, text height, and so on all use the current dimension style - `CRhinoDimStyleTable::CurrentDimStyle()`.

```cpp
doc.AddTextObject(
  L"Hello world",
  ON_Plane::World_xy,
  ON_3dPoint(1, 2, 3)
);
```

### Leader

Create leader object with the arrow tip at (0,0,11) and text that says “Hello world” to the right of (8,-5,11).

```cpp
ON_3dPoint leader_polyline[] = 
{ 
  ON_3dPoint(0,0,11), 
  ON_3dPoint(5,-5,11), 
  ON_3dPoint(8,-5,11) 
};
doc.AddLeaderObject(
  L"Hello world",
  ON_Plane::World_xy,
  3,
  Leader_polyline
);
```

### Angular Dimension

Create from an arc and an offset.

```cpp
CArgsRhinoGetArc args;
ON_Arc arc;
cmdrc = RhinoGetArc(args, arc, nullptr);
if (CRhinoCommand::success != cmdrc)
  return cmdrc;
double offset = arc.Radius() / 10.0;
doc.AddDimAngularObject(arc, offset);
```

Create from two lines and a point on the angular dimension.

```cpp
ON_Line line1(ON_3dPoint::Origin, ON_3dPoint(20, 0, 0));
ON_Line line2(ON_3dPoint::Origin, ON_3dPoint(20, 20, 0));
// Acute angle has arc point "between" the line segments.
ON_3dPoint acute_angle_point(10, 5, 0);
doc.AddDimAngularObject(line1, ON_3dPoint::UnsetPoint, line2, ON_3dPoint::UnsetPoint, acute_angle_point, false);
// Obtuse angle has arc point "outside" the line segments.
ON_3dPoint obtuse_angle_point(-10, -5, 0);
doc.AddDimAngularObject(line1, ON_3dPoint::UnsetPoint, line2, ON_3dPoint::UnsetPoint, obtuse_angle_point, false);
```

### Aligned Linear Dimensions

Create an aligned linear dimension from the extension points and a point on the dimension line.

```cpp
const CRhinoDimLinear* dim = doc.AddDimLinearObject(
  ON_3dPoint(0,0,0), ON_3dPoint(50,20,0),
  ON_3dPoint(25,25,0),
  ON_3dVector::ZAxis
  );
```

### Rotated Linear Dimensions

Create a rotated linear dimensions from the extension points and a dimension lines.

```cpp
ON_3dPoint ext_points[5] = 
{
  ON_3dPoint(0,-20,0),
  ON_3dPoint(12,-8,0),
  ON_3dPoint(25,4,0),
  ON_3dPoint(38,9,0),
  ON_3dPoint(50,-3,0) 
};

const ON_Line dim_line(ON_3dPoint(0, 0, 0), ON_3dPoint(1, 0, 0));
for (int i = 0; i < 4; i++)
{
  doc.AddDimLinearObject(
    ext_points[i],
    ext_points[i+1], 
    dim_line, 
    ON_3dVector::ZAxis
  );
}
```

## Using Styles

When you need to customize annotation appearance, use override styles.

Create a text object that says “Hello world” in bold comic sans 7 units high.

```cpp
const ON_Font* comic_sans_bold = 
  ON_Font::GetManagedFont(L"Comic Sans MS",true, false);
ON_DimStyle style =
  doc.m_dimstyle_table.CurrentDimStyle().CreateOverrideCandidate();
style.SetFont(*comic_sans_bold);
style.SetTextHeight(7);
doc.AddTextObject(
  L"Hello world",
  ON_Plane::World_xy,
  ON_3dPoint::Origin,
  &style
);

```

## Customization

If you need to make something the `CRhinoDoc::AddObject()` functions cannot produce, then you make your own annotation geometry. 

Here is an example that makes a blue leader with a curved line.

```cpp
const ON_DimStyle parent_style = doc.m_dimstyle_table.CurrentDimStyle();
ON_3dPoint leader_control_points[]= 
{ 
  ON_3dPoint(0,0,0), 
  ON_3dPoint(10,0,0), 
  ON_3dPoint(5,5,0), 
  ON_3dPoint(15,5,0) 
};
ON_Leader leader;
leader.Create(
  L"Wiggle", &parent_style,
  4, leader_control_points,
  ON_Plane::World_xy, false, 0.0);
leader.SetLeaderCurveType(&parent_style, ON_DimStyle::leader_curve_type::Spline);
ON_3dmObjectAttributes attributes;
doc.GetDefaultObjectAttributes(attributes);
attributes.SetColorSource(ON::object_color_source::color_from_object);
attributes.m_color = ON_Color::SaturatedBlue;
CRhinoLeader* rhino_leader = doc.CreateLeaderObject(
  Leader,
  &attributes
  );
doc.AddObject(rhino_leader);
```

## Annotation Details

### Plane

Every annotation object is planar and the plane specifies where that plane is located in model space.

```cpp
ON_Plane plane = CRhinoAnnotation.Plane();
```

### Dimension Style

The dimension style specifies all appearance properties like the text font, size, and alignment, arrow head shape, and so on. 

There are about 100 appearance properties in a dimension style. 

The model contains several basic dimension styles and every annotation object references one of the basic model dimension styles. 

If an annotation object requires some customized dimension style, those are set using a property setting function on `ON_Annotation`.
