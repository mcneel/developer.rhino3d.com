---
title: Move Curve Grips
description: Demonstrates how to move a curve's grips using RhinoScript.
authors: ['dale_fugier']
sdk: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Curves']
origin: http://wiki.mcneel.com/developer/scriptsamples/movecurvegrip
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

```vbnet
Sub MoveCurveGrip
  Const rhCurve = 4

  Dim sCurve : sCurve = Rhino.GetObject("Select a curve", rhCurve)
  If IsNull(sCurve) Then Exit Sub

  Dim bGripsOn : bGripsOn = Rhino.ObjectGripsOn(sCurve)
  If (bGripsOn = False) Then
    bGripsOn = Rhino.EnableObjectGrips(sCurve, True)
  End If

  Dim aGrip : aGrip = Rhino.GetObjectGrip("Select a curve grip")
  If IsArray(aGrip) Then
    Dim aPt : aPt = aGrip(2)
    aPt(2) = aPt(2) + 1.0
    Rhino.ObjectGripLocation sCurve, aGrip(1), aPt
  End If

  If (bGripsOn = True) Then
    Rhino.EnableObjectGrips sCurve, False
  End If

End Sub
```
