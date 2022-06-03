+++
authors = [ "dale" ]
categories = [ "Miscellaneous", "Advanced" ]
description = "This guide demonstrates how to determine a point on a curve that is a specified distance from another point using RhinoScript."
keywords = [ "script", "Rhino", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Distance on a Curve from a Point"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/curvearclengthpoint"
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

 
## Problem

How do you create a point that is a given distance from another point, where the distance is to be measured along the curve?

## Solution

The problem can be easily solved by using RhinoScript's `CurveArcLengthPoint` function.  The `CurveArcLengthPoint` function returns the point on the curve that is a specified arc length from the start of the curve.  By first determining the distance of the known point from the start of the curve, you can then determine how far to offset another point.

For example:

```vbnet
Option Explicit

Sub OffsetPointOnCurve

  ' Select the curve
  Dim crv : crv = Rhino.GetObject("Select curve", 4)
  If IsNull(crv) Then Exit Sub

  ' Select a point on the curve to offset from      
  Dim pt : pt = Rhino.GetPointOnCurve(crv, "Select point on curve")
  If IsNull( pt) Then Exit Sub

  ' Specify the offset distance    
  Dim dist : dist = Rhino.GetReal("Distance to offset point")
  If IsNull(dist) Then Exit Sub

  ' Get the closest point on the curve from the test point      
  Dim t : t = Rhino.CurveClosestPoint(crv, pt)

  ' Get the curve's domain
  Dim d : dom = Rhino.CurveDomain(crv)

  ' Get the total length of the curve
  Dim l : l = Rhino.CurveLength(crv)

  ' Determine the length from the start of the curve to the test point
  Dim ls : ls = Rhino.CurveLength(crv,,Array(Dom(0),t))

  ' Offset a point in each direction    
  Rhino.AddPoint Rhino.CurveArcLengthPoint(crv, ls + dist, True)
  Rhino.AddPoint Rhino.CurveArcLengthPoint(crv, l - ls + dist, False)

  ' Add the test point for reference
  Rhino.AddPoint pt

End Sub
```
