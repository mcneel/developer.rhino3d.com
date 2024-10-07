+++
aliases = ["/en/5/samples/rhinoscript/splitting-curves-to-segments/", "/en/6/samples/rhinoscript/splitting-curves-to-segments/", "/en/7/samples/rhinoscript/splitting-curves-to-segments/", "/en/wip/samples/rhinoscript/splitting-curves-to-segments/"]
authors = [ "dale" ]
categories = [ "Curves" ]
description = "Demonstrates how to split a curve into multiple segments using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Splitting Curves into Segments"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/curvesplitter"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0
+++

```vbnet
Option Explicit

Sub CurveSplitter

  Const rhCurveObject = 4

  Dim sCurve
  sCurve = Rhino.GetObject("Select curve to split", rhCurveObject)
  If IsNull(sCurve) Then Exit Sub

  Dim nSegments
  nSegments = Rhino.GetInteger("Number of segments", 2, 2)
  If IsNull(nSegments) Then Exit Sub

  Dim aPoints
  aPoints = Rhino.DivideCurve(sCurve, nSegments)
  If Not IsArray(aPoints) Then Exit Sub

  Rhino.EnableRedraw False

  Dim i, t0, t1
  For i = 0 To UBound(aPoints) - 1
    t0 = Rhino.CurveClosestPoint(sCurve, aPoints(i))
    t1 = Rhino.CurveClosestPoint(sCurve, aPoints(i+1))
    Rhino.TrimCurve sCurve, Array(t0, t1), vbFalse
  Next

  Rhino.DeleteObject sCurve
  Rhino.EnableRedraw True

End Sub
```
