---
title: Splitting Curves into Segments
description: Demonstrates how to split a curve into multiple segments using RhinoScript.
authors: ['dale_fugier']
author_contacts: ['dale']
sdk: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Curves']
origin: http://wiki.mcneel.com/developer/scriptsamples/curvesplitter
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

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
