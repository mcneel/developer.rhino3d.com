---
layout: code-sample-rhinoscript
title: Get Mapping Information From Object
author: dale@mcneel.com
platforms: ['Windows']
apis: ['RhinoScript']
languages: ['VBScript']
keywords: ['rhinoscript', 'vbscript', 'flamingo']
categories: ['Flamingo']
description: Demonstrates how to get Flamingo nXt mapping information from an object using RhinoScript.
TODO: 0
origin: http://wiki.mcneel.com/flamingo/flamingosdk/mappinginformation
order: 1
---

```vbnet
Option Explicit

Call Main()

Sub Main()
	Dim objPlugIn, strObject, origin
	On Error Resume Next
	Set objPlugIn = Rhino.GetPluginObject("8008880f-8d13-4b2d-92b0-727e12878a4c")
	If Err Then
		MsgBox Err.Description
		Exit Sub
	End If
	strObject = Rhino.GetObject("Select object")
  If Not IsNull(strObject) And Not strObject = "" Then
  	origin = objPlugIn.GetMappingOrigin(strObject)
	  If IsNull(origin) Then
      Rhino.Print("Object has no mapping data")
    Else
      Rhino.Print("Object mapping origin: " & Rhino.Pt2Str(origin))
    End If
	End If
	Set objPlugIn = Nothing
End Sub
```
