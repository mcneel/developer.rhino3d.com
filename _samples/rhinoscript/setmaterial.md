---
layout: code-sample-rhinoscript
title: Assign Material To Object
author: dale@mcneel.com
platforms: ['Windows']
apis: ['RhinoScript']
languages: ['VBScript']
keywords: ['rhinoscript', 'vbscript', 'flamingo']
categories: ['Flamingo']
description: Demonstrates how to assign a Flamingo nXt material to an object using RhinoScript.
origin: http://wiki.mcneel.com/flamingo/flamingosdk/setmaterial
order: 1
---

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
  strMaterial = objPlugIn.ModalMaterialBrowser()
  If Not IsNull(strMaterial) And Not strMaterial = "" Then
	  strObject = Rhino.GetObject("Select object")
    If Not IsNull(strObject) And Not strObject = "" Then
      If objPlugIn.SetMaterialId(strObject, strMaterial) Then
        Rhino.Print("Object assigned to material " + objPlugIn.GetMaterialName(strMaterial))
      Else
        Rhino.Print("Error assigning material to object")
      End If
    End If
  End If
	Set objPlugIn = Nothing
End Sub
```
