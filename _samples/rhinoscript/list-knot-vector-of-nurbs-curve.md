---
title: List Knot Vector of NURBS Curve
description: Demonstrates how to print the knot vector of NURBS curve using RhinoScript.
authors: ['dale_fugier']
sdk: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Curves']
origin: http://wiki.mcneel.com/developer/scriptsamples/listknotvector
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

```vbnet
Option Explicit

Sub ListKnotVector

  Dim curve : curve = Rhino.GetObject("Select curve", 4)
  If IsNull(curve) Then Exit Sub

  Dim knot : knot = Rhino.CurveKnots(curve)
  If Not IsArray(knot) Then
    Rhino.Print "NULL knot vector"
  End If

  ' order = degree + 1
  Dim order : order = Rhino.CurveDegree(curve) + 1
  If (order < 2) Then
    Rhino.Print "knot vector order < 2"
  End If

  Dim cv_count : cv_count = Rhino.CurvePointCount(curve)
  If (cv_count < order) Then
    Rhino.Print "knot vector cv_count < order"
  End If

  Dim knot_count, i, i0, mult
  If (order >= 2) And (cv_count >= order) And IsArray(knot) Then
    knot_count = order + cv_count - 2
    i = 0
    i0 = 0
    Rhino.Print "index, value, mult, delta"
    While (i < knot_count)
      mult = 1
      Do While (i + mult < knot_count)
        If (i + mult < knot_count) Then
          If (knot(i) = knot(i+mult)) Then
            mult = mult + 1
          Else
            Exit Do
          End If
        Else
          Exit Do
        End If
      Loop
      If (i = 0) Then
        Rhino.Print CStr(i) & ", " & CStr(knot(i)) & ", " & CStr(mult)
      Else
        Rhino.Print CStr(i) & ", " & CStr(knot(i)) & ", " & CStr(mult) & ", " & CStr(knot(i)-knot(i0))
      End If
      i0 = i
      i = i + mult
    Wend
  End If

End Sub
```
