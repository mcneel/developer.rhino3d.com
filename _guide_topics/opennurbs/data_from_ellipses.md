---
title: Data from Ellipses
description: This guide discusses ellipses and their representation in openNURBS.
authors: ['Dale Lear']
author_contacts: ['dalelear']
apis: ['openNURBS']
languages: ['C/C++']
platforms: ['Windows', 'Mac']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/onellipse
order: 1
keywords: ['openNURBS', 'Ellipses']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## Problem

You have drawn an ellipse in Rhino, using the *Ellipse* command.  While reading the *.3dm* file, using openNURBS, the ellipse is classified as as `ON::curve_object`.  How does one get the ellipse's construction data, such as center point, major and minor axes, etc?

## Solution

Unlike some curve types (e.g. Lines, Arcs, Polylines, etc.) which have their own `ON_Curve`-derived classes, there is no special class that is used to represent elliptical curves.  Ellipses and elliptical arcs are simply NURBS, or `ON_NurbsCurve`, curves.

To test to see if a curve is an ellipse or an elliptical arc, first try to cast the `ON_Curve` object as an `ON_NurbsCurve` object.  If successful, then use `ON_NurbsCurve::IsEllipse()` to verify the NURBS curve is an ellipse and to obtain its construction data.

## Sample

```cpp
ONX_Model model;

//...

const ON_Curve* curve = //...;

//...

const ON_NurbsCurve* nurb = ON_NurbsCurve::Cast( curve );
if( nurb )
{
  ON_Ellipse ellipse;
  double tolerance = model.m_settings.m_ModelUnitsAndTolerances.m_absolute_tolerance;
  bool rc = nurb->IsEllipse( 0, &ellipse, tolerance );
  if( rc )
  {
    // Center
    ON_3dPoint origin = ellipse.plane.origin;

    // Major and minor axes
    ON_3dVector xaxis = ellipse.radius[0] * ellipse.plane.xaxis;
    ON_3dVector yaxis = ellipse.radius[1] * ellipse.plane.yaxis;

    // Quad points
    ON_3dPoint p0( origin - xaxis );
    ON_3dPoint p1( origin + xaxis );
    ON_3dPoint p2( origin - yaxis );
    ON_3dPoint p3( origin + yaxis );

    // Foci
    ON_3dPoint f1, f2;
    ellipse.GetFoci( f1, f2 );
  }
}
```
