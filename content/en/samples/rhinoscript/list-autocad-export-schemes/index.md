+++
aliases = ["/en/5/samples/rhinoscript/list-autocad-export-schemes/", "/en/6/samples/rhinoscript/list-autocad-export-schemes/", "/en/7/samples/rhinoscript/list-autocad-export-schemes/", "/wip/samples/rhinoscript/list-autocad-export-schemes/"]
authors = [ "dale" ]
categories = [ "Other" ]
description = "Demonstrates how to build a list of AutoCAD export schemes using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "List AutoCAD Export Schemes"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/acadschemes"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

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
