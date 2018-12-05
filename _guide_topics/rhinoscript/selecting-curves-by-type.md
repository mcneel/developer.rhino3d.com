---
title: Selecting Curves by Type
description: This brief guide demonstrates how to select linear and non-linear curves using RhinoScript.
authors: ['dale_fugier']
sdk: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Miscellaneous', 'Intermediate']
origin: http://wiki.mcneel.com/developer/scriptsamples/selcurve
order: 1
keywords: ['script', 'Rhino', 'vbscript']
layout: toc-guide-page
---

 
## Non-Linear Curves

The following RhinoScript subroutine will select all non-linear curves in the document:

```vbnet
Sub SelNonLinearCrv()
  Dim arrCurves, strCurve
  arrCurves = Rhino.ObjectsByType(4)
  If IsArray(arrCurves) Then
    Rhino.EnableRedraw False
    For Each strCurve In arrCurves
      If Not Rhino.IsCurveLinear(strCurve) Then
        Rhino.SelectObject strCurve
      End If
    Next
    Rhino.EnableRedraw True
  End If
End Sub
```

## Linear Curves

The following RhinoScript subroutine will select all linear curves in the document:

```vbnet
Sub SelLinearCrv()
  Dim arrCurves, strCurve
  arrCurves = Rhino.ObjectsByType(4)
  If IsArray(arrCurves) Then
    Rhino.EnableRedraw False
    For Each strCurve In arrCurves
      If Rhino.IsCurveL
      inear(strCurve) Then
        Rhino.SelectObject strCurve
      End If
    Next
    Rhino.EnableRedraw True
  End If
End Sub
```
