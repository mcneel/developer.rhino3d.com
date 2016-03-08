---
title: Scripting the FlowAlongSrf Command
description: Demonstrates how to script the FlowAlongSrf command using RhinoScript.
author: dale@mcneel.com
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Surfaces']
origin: http://wiki.mcneel.com/developer/scriptsamples/flowalongsrf
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

```vbnet
Function DoFlowAlongSrf(arrObjects, strBase, strTarget)

  ' Declare local variables
  Dim saved, cmd

  ' For speed, turn of screen redrawing
  Rhino.EnableRedraw False

  ' Save any selected objects
  saved = Rhino.SelectedObjects

  ' Unselect all objects
  Rhino.UnSelectAllObjects

  ' Select the brep
  Rhino.SelectObjects arrObjects

  ' Script the split command
  cmd = "_FlowAlongSrf _SelID " & strBase & " _SelID " & strTarget
  Rhino.Command cmd, 0

  ' By preselecting the brep, the results of
  ' Split will be selected. So, get the selected
  ' objects and return them to the caller.
  DoFlowAlongSrf = Rhino.SelectedObjects

  ' Unselect all objects
  Rhino.UnSelectAllObjects

  ' If any objects were selected before calling
  ' this function, re-select them
  If IsArray(saved) Then Rhino.SelectObjects(saved)

  ' Don't forget to turn redrawing back on
  Rhino.EnableRedraw True

End Function
```
