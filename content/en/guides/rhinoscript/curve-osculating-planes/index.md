+++
aliases = ["/5/guides/rhinoscript/curve-osculating-planes/", "/6/guides/rhinoscript/curve-osculating-planes/", "/7/guides/rhinoscript/curve-osculating-planes/", "/wip/guides/rhinoscript/curve-osculating-planes/"]
authors = [ "dale" ]
categories = [ "Miscellaneous", "Advanced" ]
description = "This guide demonstrates how to calculate osculating planes."
keywords = [ "script", "Rhino", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Curve Osculating Planes"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/osculatingplane"
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

Is it possible to calculate the osculating plane at point {{< mathjax >}}$$P$${{< /mathjax >}} on a given curve with the methods provided by RhinoScript?

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
