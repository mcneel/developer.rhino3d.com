---
layout: toc-guide-page
title: Lengths of Curves
author: dale@mcneel.com
categories: ['Miscellaneous', 'Intermediate']
platforms: ['Windows']
apis: ['RhinoScript']
languages: ['VBScript']
keywords: ['script', 'Rhino', 'vbscript']
TODO: 0
origin: http://wiki.mcneel.com/developer/scriptsamples/curvelength
order: 1
---

# Lengths of Curves

This guide demonstrates how to calculate the lengths of curve objects using RhinoScript.

## Problem

Imagine you wish to list of lengths for a selected series of curves.  The Length command gives a composite length and the list command does not give the curve lengths.  You can work around these limitations with a RhinoScript.

## Solution

The following RhinoScript code demonstrates how to do the above...

```vbnet
Option Explicit

Sub CurveLength ()
  Dim arrCurves, dblTotal, dblLength, i
  dblTotal = 0.0
  arrCurves = Rhino.GetObjects("Select curves for length calculation", 4, True, True)
  If IsArray(arrCurves) Then
    For i = 0 To UBound(arrCurves)
      dblLength = Rhino.CurveLength(arrCurves(i))
      Rhino.Print("Curve" & CStr(i) & " = " & CStr(dblLength))
      dblTotal = dblTotal + dblLength
    Next
    Rhino.Print "Total length: " & " = " & CStr(dblTotal)
  End If
End Sub
```
