---
layout: code-sample-rhinoscript
title: Un-tag an Object as a Flamingo nXt Plant
author: dale@mcneel.com
platforms: ['Windows']
apis: ['RhinoScript']
languages: ['VBScript']
keywords: ['rhinoscript', 'vbscript', 'flamingo']
categories: ['Flamingo']
description: Demonstrates how to un-tag an object as a Flamingo nXt plant using RhinoScript.
TODO: 0
origin: http://wiki.mcneel.com/flamingo/flamingosdk/untagobjectasplant
order: 1
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
		If objPlugIn.UnTagObjectAsPlant(strObject) Then
      Rhino.Print("Plant tags removed from object")
    End If
	End If
	Set objPlugIn = Nothing
End Sub
```
