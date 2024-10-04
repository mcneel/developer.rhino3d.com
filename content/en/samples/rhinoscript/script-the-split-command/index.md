+++
aliases = ["/en/5/samples/rhinoscript/script-the-split-command/", "/en/6/samples/rhinoscript/script-the-split-command/", "/en/7/samples/rhinoscript/script-the-split-command/", "/wip/samples/rhinoscript/script-the-split-command/"]
authors = [ "dale" ]
categories = [ "Surfaces" ]
description = "Demonstrates how to script the Split command using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Script the Split Command"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/splitbrep"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
Function DoBrepSplit(brep, cutter)

   ' Declare local variables
   Dim saved, cmd

   ' Set default return value  
   DoBrepSplit = Null

   ' For speed, turn of screen redrawing
   Rhino.EnableRedraw False

   ' Save any selected objects
   saved = Rhino.SelectedObjects

   ' Unselect all objects
   Rhino.UnSelectAllObjects

   ' Select the brep
   Rhino.SelectObject brep

   ' Script the split command
   cmd = "_Split _SelID " & cutter & " _Enter"
   Rhino.Command cmd, 0

   ' By preselecting the brep, the results of
   ' Split will be selected. So, get the selected
   ' objects and return them to the caller.
   DoBrepSplit = Rhino.SelectedObjects

   ' Unselect all objects
   Rhino.UnSelectAllObjects

   ' If any objects were selected before calling
   ' this function, re-select them
   If IsArray(saved) Then Rhino.SelectObjects(saved)

   ' Don't forget to turn redrawing back on
   Rhino.EnableRedraw True

End Function
```
