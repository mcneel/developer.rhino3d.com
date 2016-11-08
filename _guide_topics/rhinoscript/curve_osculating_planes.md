---
title: Curve Osculating Planes
description: This guide demonstrates how to calculate osculating planes.
author: ['Dale Fugier', '@dale']
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Miscellaneous', 'Advanced']
origin: http://wiki.mcneel.com/developer/scriptsamples/osculatingplane
order: 1
keywords: ['script', 'Rhino', 'vbscript']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## Problem

Is it possible to calculate the osculating plane at point $$P$$ on a given curve with the methods provided by RhinoScript?

## Solution

Yes. There are a number of methods included in RhinoScript that can be used to calculate a curve's osculating plane, such as `CurveClosestPoint`, `CurveTangent`, `CurveCurvature`, and `CurveEvaluate`.  In this example, we will use the `CurveEvaluate` function to calculate the 2nd derivative of a curve at a parameter...

```vbnet
Function CurveOsculatingPlane(crv, t)
  CurveOsculatingPlane = Null ' default return value
  If Not Rhino.IsCurveLinear(crv) Then
    Dim rc : rc = Rhino.CurveEvaluate(crv, t, 2)
    If IsArray(rc) Then
      CurveOsculatingPlane = Rhino.PlaneFromFrame(rc(0), rc(1), rc(2))
    End If
  End If
End Function
```

The following is an example of how you might use this function...

```vbnet
Sub TestCurveOsculatingPlane
  Dim segs : segs = 10
  Dim crv : crv = Rhino.GetObject("Select non-linear curve", 4)
  If Not IsNull(crv) Then
    Dim pts : pts = Rhino.DivideCurve(crv, segs)
    If IsArray(pts) Then
      Dim i, t, p
      For i = 0 To UBound(pts)
        t = Rhino.CurveClosestPoint(crv, pts(i))
        p = CurveOsculatingPlane(crv, t)
        Rhino.AddPlaneSurface p, 1.0, 1.0
      Next
    End If
  End If
End Sub
```
