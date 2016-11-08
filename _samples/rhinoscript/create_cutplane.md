---
title: Create CutPlane
description: Demonstrates how to script the CutPlane command using RhinoScript.
author: ['Dale Fugier', '@dale']
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/scriptsamples/cutplane
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

```vbnet
Function CreateCutPlane(objs, p0, p1)

  ' Declare local variables
  Dim saved, s0, s1, cmd

  ' Set default return value  
  CreateCutPlane = Null

  ' For speed, turn of screen redrawing
  Rhino.EnableRedraw False

  ' Save any selected objects
  saved = Rhino.SelectedObjects

  ' Unselect all objects
  Rhino.UnSelectAllObjects

  ' Select the objects to create the cut plane through
  Rhino.SelectObjects objs

  ' Script the cutplane command
  s0 = Rhino.Pt2Str(p0,,True)
  s1 = Rhino.Pt2Str(p1,,True)
  cmd = "_CutPlane " & s0 & s1 & "_Enter"
  Rhino.Command cmd, 0

  ' Get the object created by CutPlane
  CreateCutPlane = Rhino.FirstObject

  ' Unselect all objects
  Rhino.UnSelectAllObjects

  ' If any objects were selected before calling
  ' this function, re-select them
  If IsArray(saved) Then Rhino.SelectObjects(saved)

  ' Don't forget to turn redrawing back on
  Rhino.EnableRedraw True

End Function
```
