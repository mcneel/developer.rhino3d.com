+++
aliases = ["/en/5/samples/rhinoscript/script-flowalongsrf/", "/en/6/samples/rhinoscript/script-flowalongsrf/", "/en/7/samples/rhinoscript/script-flowalongsrf/", "/wip/samples/rhinoscript/script-flowalongsrf/"]
authors = [ "dale" ]
categories = [ "Surfaces" ]
description = "Demonstrates how to script the FlowAlongSrf command using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Script FlowAlongSrf"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/flowalongsrf"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

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
