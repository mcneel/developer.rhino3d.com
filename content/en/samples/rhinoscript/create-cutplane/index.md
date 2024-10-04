+++
aliases = ["/en/5/samples/rhinoscript/create-cutplane/", "/en/6/samples/rhinoscript/create-cutplane/", "/en/7/samples/rhinoscript/create-cutplane/", "/wip/samples/rhinoscript/create-cutplane/"]
authors = [ "dale" ]
categories = [ "Other" ]
description = "Demonstrates how to script the CutPlane command using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Create CutPlane"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/cutplane"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

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
