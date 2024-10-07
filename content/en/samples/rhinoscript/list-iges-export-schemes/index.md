+++
aliases = ["/en/5/samples/rhinoscript/list-iges-export-schemes/", "/en/6/samples/rhinoscript/list-iges-export-schemes/", "/en/7/samples/rhinoscript/list-iges-export-schemes/", "/en/wip/samples/rhinoscript/list-iges-export-schemes/"]
authors = [ "dale" ]
categories = [ "Other" ]
description = "Demonstrates how to build a list of IGES export schemes using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "List IGES Export Schemes"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/igeschemes"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0
+++

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
