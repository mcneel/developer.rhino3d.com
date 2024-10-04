+++
aliases = ["/en/5/samples/rhinoscript/query-flamingo-plant-object/", "/en/6/samples/rhinoscript/query-flamingo-plant-object/", "/en/7/samples/rhinoscript/query-flamingo-plant-object/", "/wip/samples/rhinoscript/query-flamingo-plant-object/"]
authors = [ "dale" ]
categories = [ "Flamingo" ]
description = "Demonstrates how query a plant object using RhinoScript."
keywords = [ "rhinoscript", "vbscript", "flamingo" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Query Flamingo Plant Objects"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/flamingo/flamingosdk/plantfromobject"
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
	Dim objPlugIn, strObject, plant
	On Error Resume Next
	Set objPlugIn = Rhino.GetPluginObject("8008880f-8d13-4b2d-92b0-727e12878a4c")
	If Err Then
		MsgBox Err.Description
		Exit Sub
	End If
	strObject = Rhino.GetObject("Select object")
  If Not IsNull(strObject) And Not strObject = "" Then
		Set plant = objPlugIn.PlantFromObject(strObject)
    If IsNull(plant) Then
      Rhino.Print("Object is not a plant")
    Else
  		Rhino.Print("Plant assignment: " & plant.FileName & "  XML: " & plant.Xml)
    End If
    Set plant = Nothing
	End If
	Set objPlugIn = Nothing
End Sub
```
