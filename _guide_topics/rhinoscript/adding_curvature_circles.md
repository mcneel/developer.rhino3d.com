---
layout: toc-guide-page
title: Adding Curvature Circles
author: dale@mcneel.com
categories: ['Tasks', 'Analysis', 'Curves', 'Advanced']
platforms: ['Windows']
apis: ['RhinoScript']
languages: ['VBScript']
keywords: ['script', 'Rhino', 'vbscript']
origin: http://wiki.mcneel.com/developer/scriptsamples/curvaturecircle
order: 1
---

# Adding Curvature Circles

This guide demonstrates how to add curvature circles using RhinoScript.

## Overview

Rhino's Curvature command is very useful for analyzing the curvature at a point on a curve.  This script shows how to add the circle to the document when the curve is picked (instead of just drawing it dynamically).

There is no option on the Curvature command for leaving the circle that it draw dynamically. But, with the help of a script, you can write a subroutine that will. The following example demonstrates how to do just this.

## Sample

```vbnet
Option Explicit

Sub CurvatureCircle
  Dim crv, crv_pt, crv_t
  Dim arr, crv_pl, pl

  crv = Rhino.GetObject("Select curve for curvature measurement", 4, True)
  If IsNull(crv) Then Exit Sub

  Do    
    crv_pt = Rhino.GetPointOnCurve(crv, "Select point on curve for curvature measurement")
    If IsNull(crv_pt) Then Exit Do

    crv_t = Rhino.CurveClosestPoint(crv, crv_pt)
    If IsNull(crv_t) Then Exit Do

    arr = Rhino.CurveCurvature(crv, crv_t)
    If IsNull(arr) Then
      Rhino.Print("Unable to compute curve curvature.")
      Exit Do
    End If

    crv_pl = Rhino.PlaneFromFrame(arr(0), arr(1), arr(4))
    pl = Rhino.MovePlane(crv_pl, arr(2))

    Rhino.AddCircle pl, arr(3)
    Rhino.AddPoint arr(0)
  Loop While Not IsNull(crv_pt)
End Sub
```
