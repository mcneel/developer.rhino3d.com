---
layout: code-sample-rhinoscript
title: Modify an existing Flamingo nXt plant
author: dale@mcneel.com
platforms: ['Windows']
apis: ['RhinoScript']
languages: ['VBScript']
keywords: ['rhinoscript', 'vbscript', 'flamingo']
categories: ['Flamingo']
description: Demonstrates how to modify an existing Flamingo nXt plant using RhinoScript.
TODO: 0
origin: http://wiki.mcneel.com/flamingo/flamingosdk/modifyplant
order: 1
---

```vbnet
Option Explicit

Call Main()

Sub Main()
	Dim objPlugIn, strObject, plant, xml, xmlDoc, node
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
      xml = plant.XmlWithoutHeader
      If IsNull(xml) Then
        Rhino.Print("Error extracting plant XML")
      Else
        Set xmlDoc = CreateObject("Microsoft.XMLDOM")
        If IsNull(xmlDoc) Then
          Rhino.Print("Error creating XML document")
        Else
          xmlDoc.LoadXml(xml)
          Set node = xmlDoc.SelectSingleNode("ArPlantDef/PlantDef/nTrunks")
          If IsNull(node) Or IsEmpty(node) Then
            Rhino.Print("Error getting plant XML")
          Else
            'Mofiy the trunk value changing it to 3 trunks
            node.Text = "3"
            If objPlugIn.ModifyPlantObject(strObject, xmlDoc.xml) Then
              Rhino.Print("Plant now has three trunks...")
            Else
              Rhino.Print("Error modifing plant...")
            End If
          End If
        End If
      End If
    End If
	End If
  Set plant = Nothing
	Set objPlugIn = Nothing
End Sub
```
