+++
aliases = ["/en/5/samples/rhinoscript/find-closest-curve-to-point/", "/en/6/samples/rhinoscript/find-closest-curve-to-point/", "/en/7/samples/rhinoscript/find-closest-curve-to-point/", "/wip/samples/rhinoscript/find-closest-curve-to-point/"]
authors = [ "dale" ]
categories = [ "Curves" ]
description = "Demonstrates how to find the closest curve to test point using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Find Closest Curve to Point"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/findclosestcurve"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
Sub FindClosestCurve

  Const rhPoint = 1
  Const rhCurve = 4

  'Dim arrCurves : arrCurves = Rhino.ObjectsByType(rhCurve)
  Dim arrCurves: arrCurves = Rhino.GetObjects("Select curves to test", rhCurve)
  If Not IsArray(arrCurves) Then Exit Sub

  Dim strPoint : strPoint = Rhino.GetObject("Select test point", rhPoint)
  If IsNull(strPoint) Then Exit Sub

  Dim arrPoint : arrPoint = Rhino.PointCoordinates(strPoint)

  Dim dblDistance : dblDistance = Null
  Dim strCurve : strCurve = Null
  Dim dblParameter : dblParameter = Null
  Dim arrPt : arrPt = Null

  Dim i, b, t, pt, d
  For i = 0 To UBound(arrCurves)
    b = vbFalse
    t = Rhino.CurveClosestPoint( arrCurves(i), arrPoint )
    If Not IsNull(t) Then
      pt = Rhino.EvaluateCurve( arrCurves(i), t )
      If IsArray(pt) Then
        d = Rhino.Distance(pt, arrPoint)
        If IsNull(dblDistance) Then
          b = vbTrue
        ElseIf (d < dblDistance) Then
          b = vbTrue
        End If

        If (b = vbTrue) Then
          dblDistance = d
          strCurve = arrCurves(i)
          dblParameter = t
          arrPt = pt
        End If
      End If
    End If
  Next

  If Not IsNull(dblDistance) Then
    Rhino.Print "Closest curve = " & CStr(strCurve)
    Rhino.Print "Curve parameter = " & CStr(dblParameter)
    Rhino.Print "Point = " & Rhino.Pt2Str(arrPt)
    Rhino.Print "Distance = " & CStr(dblDistance)

    Rhino.SelectObject strCurve
    Rhino.SelectObject Rhino.AddPoint(arrPt)
  End If

End Sub
```
