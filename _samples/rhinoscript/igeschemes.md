---
layout: code-sample-rhinoscript
title: List IGES Export Schemes
author: dale@mcneel.com
platforms: ['Windows']
apis: ['RhinoScript']
languages: ['VBScript']
keywords: ['rhinoscript', 'vbscript']
categories: ['Uncategorized']
description: Demonstrates how to build a list of IGES export schemes using RhinoScript.
origin: http://wiki.mcneel.com/developer/scriptsamples/igeschemes
order: 1
---

```vbnet
Option Explicit

Function GetIgesExportSchemes()
  Const HKEY_CURRENT_USER = &H80000001

  Dim objReg, strComputer, strKey, arrSubKeys
  strComputer = "."
  strKey = "Software\McNeel\Rhinoceros\4.0\Scheme: Default\Plug-ins\7f0ca561-0c7c-4cea-b822-b95ebe71c409\Settings"

  On Error Resume Next   
  Set objReg = GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\root\default:StdRegProv")
  If Err.Number = 0 Then
    Call objReg.EnumKey(HKEY_CURRENT_USER, strKey, arrSubKeys)
  End If

  If IsArray(arrSubKeys) Then
    GetIgesExportSchemes = Rhino.SortStrings(arrSubKeys)
  Else
    GetIgesExportSchemes = Null
  End If

End Function
```
