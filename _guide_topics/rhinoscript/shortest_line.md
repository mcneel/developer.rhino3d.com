---
layout: toc-guide-page
title: Shortest Line between two Lines
author: dale@mcneel.com
categories: ['Miscellaneous', 'Advanced']
platforms: ['Windows']
apis: ['RhinoScript']
languages: ['VBScript']
keywords: ['script', 'Rhino', 'vbscript']
TODO: 0
origin: http://wiki.mcneel.com/developer/scriptsamples/shortestline
order: 1
---

# Shortest Line between two Lines

This brief guide demonstrates how to calculate the shortest line between two lines.

## Overview

Two lines in three dimensions generally do not intersect at a point.  They may be parallel (no intersections) or they may be coincident (infinite intersections) but most often only their projection onto a plane intersects.  When they do not exactly intersect at a point they can be connected by a line segment, the shortest line segment is unique and is often considered to be their intersection in 3D.

## Example

The following example code demonstrates how to calculate the shortest line between two line segments using RhinoScript...

```vbnet
Option Explicit

' Description:
'   Returns the shortest line segment between
'   two infinite line segments.
' Parameters:
'   p1 - the starting point of the first line
'   p2 - the ending point of the first line
'   p3 - the starting point of the second line
'   p4 - the ending point of the second line
' Returns
'   Array - the shortest line segment if successful
'   Null - if not successful or on error

Function LineLineIntersect(p1, p2, p3, p4)

  LineLineIntersect = Null

  Const EPS = 2.2204460492503131e-016  
  Dim p13(2), p43(2), p21(2)
  Dim d1343, d4321, d1321, d4343, d2121, numer, denom, mua, mub
  Dim pa(2), pb(2)

  p13(0) = p1(0) - p3(0)
  p13(1) = p1(1) - p3(1)
  p13(2) = p1(2) - p3(2)
  p43(0) = p4(0) - p3(0)
  p43(1) = p4(1) - p3(1)
  p43(2) = p4(2) - p3(2)

  If Abs(p43(0)) < EPS And Abs(p43(1)) < EPS And Abs(p43(2)) < EPS Then Exit Function

  p21(0) = p2(0) - p1(0)
  p21(1) = p2(1) - p1(1)
  p21(2) = p2(2) - p1(2)

  If Abs(p21(0)) < EPS And Abs(p21(1)) < EPS And Abs(p21(2)) < EPS Then Exit Function

  d1343 = p13(0) * p43(0) + p13(1) * p43(1) + p13(2) * p43(2)
  d4321 = p43(0) * p21(0) + p43(1) * p21(1) + p43(2) * p21(2)
  d1321 = p13(0) * p21(0) + p13(1) * p21(1) + p13(2) * p21(2)
  d4343 = p43(0) * p43(0) + p43(1) * p43(1) + p43(2) * p43(2)
  d2121 = p21(0) * p21(0) + p21(1) * p21(1) + p21(2) * p21(2)

  denom = d2121 * d4343 - d4321 * d4321
  If Abs(denom) < EPS Then Exit Function

  numer = d1343 * d4321 - d1321 * d4343
  mua = numer / denom
  mub = (d1343 + d4321 * mua) / d4343

  pa(0) = p1(0) + mua * p21(0)
  pa(1) = p1(1) + mua * p21(1)
  pa(2) = p1(2) + mua * p21(2)
  pb(0) = p3(0) + mub * p43(0)
  pb(1) = p3(1) + mub * p43(1)
  pb(2) = p3(2) + mub * p43(2)

  LineLineIntersect = Array(pa, pb)

End Function
```

You can test the above function as follows:

```vbnet
Sub Test

  Dim l0 : l0 = Rhino.GetObject("Select first line", 4)
  Dim l1 : l1 = Rhino.GetObject("Select second line", 4)

  Dim p1 : p1 = Rhino.CurveStartPoint(l0)
  Dim p2 : p2 = Rhino.CurveEndPoint(l0)
  Dim p3 : p3 = Rhino.CurveStartPoint(l1)
  Dim p4 : p4 = Rhino.CurveEndPoint(l1)

  Dim rc : rc = LineLineIntersect(p1, p2, p3, p4)
  If IsArray(rc) Then
    Rhino.AddPoints rc
  End If

End Sub
```
