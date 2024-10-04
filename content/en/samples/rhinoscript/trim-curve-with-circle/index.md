+++
aliases = ["/en/5/samples/rhinoscript/trim-curve-with-circle/", "/en/6/samples/rhinoscript/trim-curve-with-circle/", "/en/7/samples/rhinoscript/trim-curve-with-circle/", "/wip/samples/rhinoscript/trim-curve-with-circle/"]
authors = [ "dale" ]
categories = [ "Curves" ]
description = "Demonstrates how to trim a closed curve with a circle using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Trim Curve with Circle"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/circletrimmer"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
Option Explicit

Sub CircleTrimmer

  ' Local variable declarations
  Dim curve, circle, ccx, ccx_t(1), interval

  ' Select closed curve to split
  curve = Rhino.GetObject("Select closed curve to split", 4)
  If IsNull(curve) Then Exit Sub
  If Not Rhino.IsCurveClosed(curve) Then Exit Sub

  ' Select circle to split with    
  circle = Rhino.GetObject("Select circle to split with", 4)
  If IsNull(circle) Then Exit Sub
  If Not Rhino.IsCircle(circle) Then Exit Sub

  ' Intersect the two curves
  ccx = Rhino.CurveCurveIntersection(curve, circle)
  If IsNull(ccx) Then
    Rhino.Print "Curve and circle do not intersect"
    Exit Sub
  End If

  ' Make sure there are only two intersection events
  If UBound(ccx) <> 1 Then
    Rhino.Print "Unable to split curve"
    Exit Sub
  End If

  ' Get two intersection parameters on the curve
  ccx_t(0) = ccx(0,5)
  ccx_t(1) = ccx(1,5)

  ' If the input curve is closed and the interval is decreasing,
  ' then the portion of the curve across the start and end of the
  ' curve is returned.
  If ccx_t(0) < ccx_t(1) Then
    interval = Array(ccx_t(1), ccx_t(0))
  Else
    interval = Array(ccx_t(0), ccx_t(1))
  End If

  ' Trim the curve
  Rhino.TrimCurve curve, interval

End Sub
```
