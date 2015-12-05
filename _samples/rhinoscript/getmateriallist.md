---
layout: code-sample-rhinoscript
title: Get Material List
author: dale@mcneel.com
platforms: ['Windows']
apis: ['RhinoScript']
languages: ['VBScript']
keywords: ['rhinoscript', 'vbscript', 'flamingo']
categories: ['Flamingo']
description: Demonstrates how to get a the Flamingo nXt material list from the current document using RhinoScript.
TODO: 0
origin: http://wiki.mcneel.com/flamingo/flamingosdk/getmateriallist
order: 1
---

```vbnet
Option Explicit

Call Main()

Sub Main()
	Dim objPlugIn, materials, i, count, material
  On Error Resume Next
  Set objPlugIn = Rhino.GetPluginObject("8008880f-8d13-4b2d-92b0-727e12878a4c")
  If Err Then
		MsgBox Err.Description
		Exit Sub
	End If
  materials = objPlugIn.GetMaterials()
  If IsNull(materials) Then
    Rhino.Print("Error getting Flamingo nXt material list")
  Else
    count = UBound(materials)
    Rhino.Print("==============================================================================")
    Rhino.Print("Flamingo nXt Material List")
    Rhino.Print("------------------------------------------------------------------------------")
    If count < 0 Then
      Rhino.Print("No Flamingo materials in the current document")
    End If
    For i = 0 to count
      Set material = materials(i)
      If IsObject(material) Then
        Rhino.Print("Material " & (i + 1) & ": ID: " & material.Id & " Name: " & material.Name)
      End If
    Next
  End If
	Set material = Nothing
	Set objPlugIn = Nothing
End Sub
```
