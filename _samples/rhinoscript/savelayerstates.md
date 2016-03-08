---
title: Save and Restore Layer States
description: Demonstrates how to save and restore the states of layers using RhinoScript.
author: dale@mcneel.com
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/scriptsamples/savelayerstates
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

```vbnet
Option Explicit

'--------------------------------------------------------------------
' Subroutine: SaveLayerStates
' Purpose:    Saves a "named" layer state to an INI-style file.
'--------------------------------------------------------------------
Sub SaveLayerStates

  If StrComp(Rhino.DocumentName, "untitled", 1) = 0 Then
    Rhino.MessageBox "You must save your model before using _
                             this script.", 48, "LayerStates"
    Exit Sub
  End If

  Dim arrLayers
  arrLayers = Rhino.LayerNames
  If Not IsArray(arrLayers) Then Exit Sub

  Dim strName
  strName = Rhino.StringBox("Save Layer State As", , "LayerStates")
  If IsNull(strName) Then Exit Sub

  Dim strFile
  strFile = Rhino.DocumentPath & Rhino.DocumentName
  strFile = Replace(strFile, ".3dm", ".layer", 1, -1, 1)

  Dim strLayer, strValue
  For Each strLayer In arrLayers
    strValue = CStr(CInt(Rhino.IsLayerCurrent(strLayer)))
    strValue = strValue & ";" & CStr(Rhino.LayerMode(strLayer))
    strValue = strValue & ";" & CStr(Rhino.LayerColor(strLayer))
    Rhino.SaveSettings strFile, strName, strLayer, strValue
  Next

End Sub

'--------------------------------------------------------------------
' Subroutine: RestoreLayerStates
' Purpose:    Restores a "named" layer state from an INI-style file.
'--------------------------------------------------------------------
Sub RestoreLayerStates

  If StrComp(Rhino.DocumentName, "untitled", 1) = 0 Then
    Rhino.MessageBox "This script only works on saved models.", _
                             48, "LayerStates"
    Exit Sub
  End If

  Dim strFile
  strFile = Rhino.DocumentPath & Rhino.DocumentName
  strFile = Replace(strFile, ".3dm", ".layer", 1, -1, 1)

  Dim arrNames
  arrNames = Rhino.GetSettings(strFile)
  If Not IsArray(arrNames) Then
    Rhino.MessageBox "No layer states to restore.", 64, "LayerStates"
    Exit Sub
  End If

  Dim strName
  strName = Rhino.ListBox(arrNames, "Layer state to restore", _
                                 "LayerStates")
  If IsNull(strName) Then Exit Sub  

  Dim arrLayers
  arrLayers = Rhino.GetSettings(strFile, strName)
  If Not IsArray(arrLayers) Then
    Rhino.MessageBox "No layers to restore.", 64, "LayerStates"
    Exit Sub
  End If

  Dim strLayer, strValue, arrValues
  For Each strLayer In arrLayers
    strValue = Rhino.GetSettings(strFile, strName, strLayer)
    arrValues = Split(strValue, ";")
    If CBool(arrValues(0)) = True Then Rhino.CurrentLayer strLayer
    Rhino.LayerMode strLayer, CInt(arrValues(1))
    Rhino.LayerColor strLayer, CLng(arrValues(2))
  Next

End Sub
```
