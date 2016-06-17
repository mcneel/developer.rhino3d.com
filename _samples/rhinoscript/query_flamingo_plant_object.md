---
title: Query Flamingo Plant Objects
description: Demonstrates how query a plant object using RhinoScript.
author: dale@mcneel.com
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Flamingo']
origin: http://wiki.mcneel.com/flamingo/flamingosdk/plantfromobject
order: 1
keywords: ['rhinoscript', 'vbscript', 'flamingo']
layout: code-sample-rhinoscript
---

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
