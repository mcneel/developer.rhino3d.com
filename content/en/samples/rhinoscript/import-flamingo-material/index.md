+++
aliases = ["/en/5/samples/rhinoscript/import-flamingo-material/", "/en/6/samples/rhinoscript/import-flamingo-material/", "/en/7/samples/rhinoscript/import-flamingo-material/", "/wip/samples/rhinoscript/import-flamingo-material/"]
authors = [ "dale" ]
categories = [ "Flamingo" ]
description = "Demonstrates how import a ArMaterial file using RhinoScript."
keywords = [ "rhinoscript", "vbscript", "flamingo" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Import Flamingo Material"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/flamingo/flamingosdk/importmaterial"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

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
