+++
authors = [ "dale" ]
categories = [ "Flamingo" ]
description = "Demonstrates how get an objects Flamingo nXt material assignment using RhinoScript."
keywords = [ "rhinoscript", "vbscript", "flamingo" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Get Flamingo Material"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/flamingo/flamingosdk/getmaterial"
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
	Dim objPlugIn, strObject, strMaterial
	On Error Resume Next
	Set objPlugIn = Rhino.GetPluginObject("8008880f-8d13-4b2d-92b0-727e12878a4c")
	If Err Then
		MsgBox Err.Description
		Exit Sub
	End If
	strObject = Rhino.GetObject("Select object")
  If Not IsNull(strObject) And Not strObject = "" Then
		strMaterial = objPlugIn.GetMaterialId(strObject)
    If Not IsNull(strMaterial) And Not strMaterial = "" Then
			Rhino.Print("Object assigned to Flamingo nXt material ID: " + strMaterial + " Name: " + objPlugIn.GetMaterialName(strMaterial))
    Else
      Rhino.Print("Object does not have a Flamingo nXt material assigned")
		End If
	End If
	Set objPlugIn = Nothing
End Sub
```
