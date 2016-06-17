---
title: Closest Axis Point
description: This guide demonstrates how to find the closest point on a planar curve to an axis.
author: dale@mcneel.com
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Miscellaneous', 'Advanced']
origin: http://wiki.mcneel.com/developer/scriptsamples/closestaxispoint
order: 1
keywords: ['script', 'Rhino', 'vbscript']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## Problem

You have a bunch of 2-D curves that are planar to the world x-y plane, and you need to find a point in each curve that is closest to the world y-axis.  For example:

![Closest Axis Point]({{ site.baseurl }}/images/closest_axis_point_01.png)

What can you do to calculate this point?

## Solution

After selecting the curves and verifying that they are both planar and line in the world x-y plane, calculate the world axis-aligned bounding box for each curve.  Using the results of the bounding box calculation, create a line, using the first two points from the results, that is parallel to the world y-axis.  Intersect this line with the curve.  The results of the intersection will be at the point that is closest to the world y-axis.

The following example demonstrates the above algorithm...

```vbnet
Option Explicit

 Sub ClosestAxisPoint

   Dim arrCurves
   arrCurves = Rhino.GetObjects("Select planar curves", 4, True, True)
   If Not IsArray(arrCurves) Then Exit Sub

   Dim strCurve, arrPlane(3), arrBox, strLine, arrCCX
   arrPlane(0) = Array(0,0,0)
   arrPlane(1) = Array(1,0,0)
   arrPlane(2) = Array(0,1,0)
   arrPlane(3) = Array(0,0,1)

   Rhino.EnableRedraw False

   For Each strCurve In arrCurves
     If Rhino.IsCurvePlanar(strCurve) Then
       If Rhino.IsCurveInPlane(strCurve, arrPlane) Then
         arrBox = Rhino.BoundingBox(strCurve)
         strLine = Rhino.AddLine(arrBox(0), arrBox(1))
         arrCCX = Rhino.CurveCurveIntersection(strCurve, strLine)
         If IsArray(arrCCX) Then
           Rhino.AddPoint arrCCX(0,1)
         End If
         Rhino.DeleteObject strLine
       End If
     End If
   Next

   Rhino.EnableRedraw True      

 End Sub
```
