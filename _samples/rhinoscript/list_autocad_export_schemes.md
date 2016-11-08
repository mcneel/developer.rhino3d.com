---
title: List AutoCAD Export Schemes
description: Demonstrates how to build a list of AutoCAD export schemes using RhinoScript.
author: ['Dale Fugier', '@dale']
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/scriptsamples/acadschemes
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

```vbnet
Option Explicit

Function GetAcadExportSchemes()
  Const HKEY_CURRENT_USER = &H80000001

  Dim objReg, strComputer, strKey, arrSubKeys
  strComputer = "."
  strKey = "Software\McNeel\Rhinoceros\4.0\Scheme: Default\Plug-ins\39a88493-9e97-4f15-bd62-ad25896a2632\Settings"

  On Error Resume Next   
  Set objReg = GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\root\default:StdRegProv")
  If Err.Number = 0 Then
    Call objReg.EnumKey(HKEY_CURRENT_USER, strKey, arrSubKeys)
  End If

  If IsArray(arrSubKeys) Then
    GetAcadExportSchemes = Rhino.SortStrings(arrSubKeys)
  Else
    GetAcadExportSchemes = Null
  End If

End Function
```
