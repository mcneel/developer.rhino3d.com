---
title: Get Material List
description: Demonstrates how to get a the Flamingo nXt material list from the current document using RhinoScript.
authors: ['dale_fugier']
sdk: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Flamingo']
origin: http://wiki.mcneel.com/flamingo/flamingosdk/getmateriallist
order: 1
keywords: ['rhinoscript', 'vbscript', 'flamingo']
layout: code-sample-rhinoscript
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
