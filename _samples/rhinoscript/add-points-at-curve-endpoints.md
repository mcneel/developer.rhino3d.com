---
title: Add Points at Curve Endpoints
description: Demonstrates how to add point at the starting and ending locations of curves.
authors: ['dale_fugier']
sdk: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Adding Objects']
origin: http://wiki.mcneel.com/developer/scriptsamples/addcurveendpoints
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

```vbnet
Option Explicit

Sub AddCurveEndPoints()
  Const rhCurve = 4

  ' Get all the curve objects in the document
  Dim arrCurves
  arrCurves = Rhino.ObjectsByType(rhCurve)
  If IsNull(arrCurves) Then Exit Sub

  ' For better performance, turn off screen redrawing  
  Call Rhino.EnableRedraw(False)

  ' Process each curve       
  Dim strCurve
  For Each strCurve In arrCurves
    ' Add a point at the start of the curve
    Call Rhino.AddPoint(Rhino.CurveStartPoint(strCurve))
    ' If not closed, add a point at the end of the curve
    If Not Rhino.IsCurveClosed(strCurve) Then
      Call Rhino.AddPoint(Rhino.CurveEndPoint(strCurve))
    End If
  Next

  ' Turn screen redrawing back on  
  Call Rhino.EnableRedraw(True)
End Sub
```
