---
layout: code-sample-rhinoscript
title: Display the Flamingo nXt legacy plant browser
author: dale@mcneel.com
platforms: ['Windows']
apis: ['RhinoScript']
languages: ['VBScript']
keywords: ['rhinoscript', 'vbscript', 'flamingo']
categories: ['Flamingo']
description: Demonstrates how to display the Flamingo nXt legacy plant browser using RhinoScript.
TODO: 0
origin: http://wiki.mcneel.com/flamingo/flamingosdk/getflamingo2plant
order: 1
---

```vbnet
Option Explicit

Call Main()

Sub Main()
	Dim objPlugIn, plant
	On Error Resume Next
	Set objPlugIn = Rhino.GetPluginObject("8008880f-8d13-4b2d-92b0-727e12878a4c")
	If Err Then
		MsgBox Err.Description
		Exit Sub
	End If
  plant = objPlugIn.ModalFlamingo2PlantBrowser("", "", "")
  If Not IsNull(plant) Then
    Rhino.Print("Library(" & plant(0) & ") Folder(" & plant(1) & ") Plant(" & plant(2) & ")")
	End If
	Set objPlugIn = Nothing
End Sub
```
