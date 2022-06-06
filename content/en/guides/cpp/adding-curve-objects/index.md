+++
aliases = ["/5/guides/cpp/adding-curve-objects/", "/6/guides/cpp/adding-curve-objects/", "/7/guides/cpp/adding-curve-objects/", "/wip/guides/cpp/adding-curve-objects/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This guide discusses how to add curve objects to Rhino using the Rhino C/C++ SDK."
keywords = [ "rhino", "curve" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Adding Curve Objects"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/addcurve"
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

Curve objects can be added to Rhino by using the following functions found on `CRhinoDoc`:

1. `CRhinoDoc::AddCurveObject`
1. `CRhinoDoc::AddObject`

For `CRhinoDoc::AddCurveObject`, there are six overridden versions that will make curve objects from a variety of inputs, including:

1. `ON_Line`: line definition objects
1. `ON_Polyline`: polyline definition objects
1. `ON_Arc`: arc definition objects
1. `ON_Circle`: circle definition objects
1. `ON_BezierCurve`: bezier curve objects
1. `ON_Curve`: `ON_Curve`-derived curve objects

## Examples

The following code samples will demonstrate three different ways of adding curves to Rhino. In these examples, we will create circle curves; but, there is no reason that we could create lines, polylines, arcs or any other type of curve.

### Example 1

In this example, we define a circle, using `ON_Circle`, and pass the definition off to `CRhinoDoc::AddCurveObject`.

```cpp
ON_3dPoint center(0.0, 0.0, 0.0);
double radius = 10.0;

ON_Circle circle( center, radius );

CRhinoCurveObject* curve_object = context.m_doc.AddCurveObject( circle );
context.m_doc.Redraw();
```

### Example 2

In this example, we first define a circle.  Then we create an `ON_ArcCurve` object from the circle definition. `ON_ArcCurve` is one of the many curve classes this is derived from `ON_Curve`. We then pass the `ON_ArcCurve` object off to `CRhinoDoc::AddCurveObject`.

```cpp
ON_3dPoint center(0, 0, 0);
double radius = 10.0;

ON_Circle circle( center, radius );

ON_ArcCurve arc_curve( circle );

CRhinoCurveObject* curve_object = context.m_doc.AddCurveObject( arc_curve );
context.m_doc.Redraw();
```

### Example 3

In this example, we will add a circle curve the brute force way.  We first define a circle. Then we allocate a new `ON_ArcCurve` and pass the circle definition to its constructor.  We then allocate a new `CRhinoCurveObject` and assign our `ON_ArcCurve` object pointer to it.  Finally, we pass the pointer to the `CRhinoCurveObject` to `CRhinoDoc::AddObject`.

```cpp
ON_3dPoint center(0.0, 0.0, 0.0);
double radius = 10.0;

ON_Circle circle( center, radius );

ON_ArcCurve* arc_curve = new ON_ArcCurve( circle );
if( arc_curve )
{
  CRhinoCurveObject* curve_object = new CRhinoCurveObject();
  if( curve_object )
  {
    // Set the curve to the curve object. Note,
    // curve_object will delete arc_curve.
    curve_object->SetCurve( arc_curve );
    if( context.m_doc.AddObject(curve_object) )
      context.m_doc.Redraw();
    else
      delete curve_object;
  }
}
```

## Discussion

What is interesting to note is that the code found in [Example 3](#example-3) is essentially what Rhino does inside of `CRhinoDoc::AddCurveObject`.  All of the `CRhinoDoc::AddCurveObject` overrides are simply provided to make it easier for SDK developers to add curves to Rhino.
