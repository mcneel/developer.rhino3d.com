---
layout: code-sample-rhinoscript
title: Matching Text Properties
author: dale@mcneel.com
platforms: ['Windows']
apis: ['RhinoScript']
languages: ['VBScript']
keywords: ['rhinoscript', 'vbscript']
categories: ['Uncategorized']
description: Demonstrates how to match text object properties in RhinoScript.
TODO: 0
origin: http://wiki.mcneel.com/developer/scriptsamples/matchtext
order: 1
---

```vbnet
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' MatchText.rvb -- July 2009
' If this code works, it was written by Dale Fugier.
' If not, I don't know who wrote it.
' Works with Rhino 4.0 and 5.0
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Option Explicit

Sub MatchText()

  Dim objects, source, match, items, values, i
  Dim font, height, style

  objects = Rhino.GetObjects("Select text objects to modify", 512,, True)
  If IsNull(objects) Then Exit Sub

  source = Rhino.GetObject("Select source object", 512)
  If IsNull(source) Then Exit Sub

  items = Array("Font", "Height", "Style")
  values = Array(True, True, True)
  match = Rhino.CheckListBox(items, values, "Properties to match:", "Match Text")
  If IsNull(match) Then Exit Sub

  font = Rhino.TextObjectFont(source)
  height = Rhino.TextObjectHeight(source)
  style = Rhino.TextObjectStyle(source)

  Call Rhino.EnableRedraw(False)

  For i = 0 To UBound(objects)
    If match(0) = True Then Call Rhino.TextObjectFont(objects(i), font)
    If match(1) = True Then Call Rhino.TextObjectHeight(objects(i), height)
    If match(2) = True Then Call Rhino.TextObjectStyle(objects(i), style)
  Next

  Call Rhino.EnableRedraw(True)

End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Rhino.AddStartupScript Rhino.LastLoadedScriptFile
Rhino.AddAlias "MatchText", "_NoEcho _-RunScript (MatchText)"
```
