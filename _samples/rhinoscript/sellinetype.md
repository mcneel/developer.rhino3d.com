---
title: Selecting Objects by Linetype
description: Demonstrates how to select objects by linetype using RhinoScript.
author: dale@mcneel.com
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/scriptsamples/sellinetype
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

```vbnet
Sub SelLinetype

  Dim strLinetype
  strLineType = Rhino.GetString("Object linetype name to select")
  If Not IsString(strLinetype) Then Exit Sub
  If Not Rhino.IsLinetype(strLinetype) Then Exit Sub

  Dim arrObjects, strObject

  ' If you want to filter on all visible objects,
  ' use the following line of code.
  arrObjects = Rhino.NormalObjects

  ' Or, if you want to filter on just curve objects
  ' use the following line of code.
  ' arrObjects = Rhino.ObjectsByType(4)

  If IsArray(arrObjects) Then
    Rhino.EnableRedraw False
    For Each strObject In arrObjects
      If StrComp(Rhino.ObjectLinetype(x), strLinetype, 1) = 0 Then
        Rhino.SelectObject(strObject)
      End If
    Next
    Rhino.EnableRedraw True
  End If

End Sub

Function IsString(ByVal str)
  IsString = False
  If VarType(str) = vbString Then IsString = True
End Function
```
