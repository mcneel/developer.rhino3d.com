---
title: Select Points with a Specified Z Coordinate
description: Demonstrates how to select point objects with a user-specified z coordinate using RhinoScript.
author: dale@mcneel.com
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Uncategorized']
origin: http://wiki.mcneel.com/developer/scriptsamples/selz
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

```vbnet
Option Explicit

Sub SelZ()

  Dim arr
  arr = Rhino.ObjectsByType(1)
  If Not IsArray(arr) Then
    Rhino.Print "No point objects to select"
    Exit Sub
  End If

  Const zero_tol = 1.0e-12

  Dim z, obj, pt
  z = Rhino.GetReal("Z coordinate", 0.0)
  If IsNumeric(z) Then
    For Each obj In arr
      pt = Rhino.PointCoordinates(obj)
      If IsArray(pt) Then
        If Abs(pt(2)-z) <= zero_tol Then
          Rhino.SelectObject obj
        End If
      End If
    Next
  End If

End Sub
```
