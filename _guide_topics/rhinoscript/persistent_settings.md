---
title: Persistent Settings
description: This brief guide demonstrates how to use private variables for persistent settings in RhinoScript.
author: JessMaertterer
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Miscellaneous', 'Advanced']
origin: http://wiki.mcneel.com/developer/scriptsamples/persistentsettings
order: 1
keywords: ['script', 'Rhino', 'vbscript']
layout: toc-guide-page
---

# Persistent Settings

{{ page.description }}

## Problem

It can be annoying to enter the same custom parameter each time you run a script.  

## Solution

The following script demonstrates how to use a private variable to store a parameter during a Rhino session.

```vbnet
' How to script with persisting settings
' Jess Maertterer - 20.12.2004
Option Explicit
Private dblLength

If IsEmpty(dblLength) Then
  dblLength = 2.00
End If

'/////////////////////////////////////////////////////////////
Sub Extend_Curve_Length_Persist
  Dim arrCurves, strCurve, dblResult
  arrCurves = Rhino.GetObjects("Select curves to extend", 4)
  If Not IsNull(arrCurves) Then
    dblResult = Rhino.GetReal("Length to extend", dblLength,0.00)
    If Not IsNull(dblResult) Then
      dblLength = dblResult
      For Each strCurve in arrCurves
        Rhino.ExtendCurveLength strCurve, 2, 2, dblLength
      Next
    End If
  End If
End Sub
```

If your script should remember the settings from the last session, then you have to use the RhinoScript methods `SaveSettings` and `GetSettings` to access a separate *.ini* file.
