+++
aliases = ["/5/guides/opennurbs/data-from-ellipses/", "/6/guides/opennurbs/data-from-ellipses/", "/7/guides/opennurbs/data-from-ellipses/", "/wip/guides/opennurbs/data-from-ellipses/"]
authors = [ "dalelear" ]
categories = [ "Advanced" ]
description = "This guide discusses ellipses and their representation in openNURBS."
keywords = [ "openNURBS", "Ellipses" ]
languages = [ "C/C++" ]
sdk = [ "openNURBS" ]
title = "Data from Ellipses"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/onellipse"
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

 
## Problem

You have drawn an ellipse in Rhino, using the *Ellipse* command.  While reading the *.3dm* file, using openNURBS, the ellipse is classified as as `ON::curve_object`.  How does one get the ellipse's construction data, such as center point, major and minor axes, etc?

## Solution

Unlike some curve types (e.g. Lines, Arcs, Polylines, etc.) which have their own `ON_Curve`-derived classes, there is no special class that is used to represent elliptical curves.  Ellipses and elliptical arcs are simply NURBS, or `ON_NurbsCurve`, curves.

To test to see if a curve is an ellipse or an elliptical arc, first try to cast the `ON_Curve` object as an `ON_NurbsCurve` object.  If successful, then use `ON_NurbsCurve::IsEllipse()` to verify the NURBS curve is an ellipse and to obtain its construction data.

## Sample

```cpp
ONX_Model model = ...

ONX_ModelComponentIterator it(model, ON_ModelComponent::Type::ModelGeometry);
const ON_ModelComponent* model_component = nullptr;
for (model_component = it.FirstComponent(); nullptr != model_component; model_component = it.NextComponent())
{
  const ON_ModelGeometryComponent* model_geometry = ON_ModelGeometryComponent::Cast(model_component);
  if (nullptr != model_geometry)
  {
    // Test for NURBS curve object
    const ON_NurbsCurve* nurb = ON_NurbsCurve::Cast(model_geometry->Geometry(nullptr));
    if (nullptr != nurb)
    {
      ON_Ellipse ellipse;
      double tolerance = model.m_settings.m_ModelUnitsAndTolerances.m_absolute_tolerance;
      bool rc = nurb->IsEllipse(nullptr, &ellipse, tolerance);
      if (rc)
      {
        // Center
        ON_3dPoint origin = ellipse.plane.origin;

        // Major and minor axes
        ON_3dVector xaxis = ellipse.radius[0] * ellipse.plane.xaxis;
        ON_3dVector yaxis = ellipse.radius[1] * ellipse.plane.yaxis;

        // Quad points
        ON_3dPoint p0(origin - xaxis);
        ON_3dPoint p1(origin + xaxis);
        ON_3dPoint p2(origin - yaxis);
        ON_3dPoint p3(origin + yaxis);

        // Foci
        ON_3dPoint f1, f2;
        ellipse.GetFoci(f1, f2);

        // TODO: do something with ellipse
      }
    }
  }
}
```
