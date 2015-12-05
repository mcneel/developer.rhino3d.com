---
layout: code-sample-rhinoscript
title: Import Flamingo nXt Material
author: dale@mcneel.com
platforms: ['Windows']
apis: ['RhinoScript']
languages: ['VBScript']
keywords: ['rhinoscript', 'vbscript', 'flamingo']
categories: ['Flamingo']
description: Demonstrates how import a ArMaterial file using RhinoScript.
TODO: 0
origin: http://wiki.mcneel.com/flamingo/flamingosdk/importmaterial
order: 1
---

```vbnet
Option Explicit

Call Main()

Sub Main()
	Dim objPlugIn, strMaterial, strMaterialId, material
	On Error Resume Next
	Set objPlugIn = Rhino.GetPluginObject("8008880f-8d13-4b2d-92b0-727e12878a4c")
	If Err Then
		MsgBox Err.Description
		Exit Sub
	End If
  strMaterial = "C:\ProgramData\McNeel\Flamingo nXt\Language Packs\en-US\Materials\Basics\Basic Car Paint Red.ArMaterial"
  strMaterialId = objPlugIn.ImportMaterial(strMaterial, true)
  if Not IsNull(strMaterialId) And Not strMaterialId = "" Then
    Set material = objPlugIn.GetMaterial(strMaterialId)
		Rhino.Print("Object assigned to Flamingo nXt material ID: " & material.Id & " Name: " & material.Name)
  End If
  Set material = Nothing
	Set objPlugIn = Nothing
End Sub
```
