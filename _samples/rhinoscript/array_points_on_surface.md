---
title: Array Points on Surface
description: Demonstrates how to array points on a surface with a RhinoScript.
author: dale@mcneel.com
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Adding Objects', 'Surfaces']
origin: http://wiki.mcneel.com/developer/scriptsamples/arraypointsonsurface
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

```vbnet
Option Explicit

Sub ArrayPointsOnSurface()
   ' Get the surface object
   Dim srf : srf = Rhino.GetObject("Select surface", 8, vbTrue)
   If IsNull(srf) Then Exit Sub

   ' Get the number of rows
   Dim rows : rows = Rhino.GetInteger("Number of rows", 2, 2)
   If IsNull(rows) Then Exit Sub
   rows = rows - 1

   ' Get the number of columns
   Dim cols : cols = Rhino.GetInteger("Number of columns", 2, 2)
   If IsNull(cols) Then Exit Sub
   cols = cols - 1

   ' Get the domain of the surface
   Dim U : U = Rhino.SurfaceDomain(srf, 0)
   Dim V : V = Rhino.SurfaceDomain(srf, 1)
   If Not IsArray(U) Or Not IsArray(V) Then Exit Sub

   ' Turn off redrawing (faster)
   Rhino.EnableRedraw vbFalse

   ' Add the points
   Dim i, j, t(1), pt, obj
   For i = 0 To rows
     t(0) = U(0) + (((U(1) - U(0)) / rows) * i)
     For j = 0 To cols
       t(1) = V(0) + (((V(1) - V(0)) / cols) * j)
       pt = Rhino.EvaluateSurface(srf, t)
       If IsArray(pt) Then
         obj = Rhino.AddPoint(pt) ' add the point
         Rhino.SelectObject obj   ' select the point
       End If
     Next
   Next

   ' Turn on redrawing
   Rhino.EnableRedraw vbTrue
End Sub
```
