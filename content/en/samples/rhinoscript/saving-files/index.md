+++
authors = [ "dale" ]
categories = [ "Other" ]
description = "Demonstrates how to save a file using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Saving Files"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/savefile"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
Option Explicit

Sub SaveRhinoFile

  ' Declare local variables
  Dim strFileName, strCommand

  ' Prompt the user for the name of the file to save  
  strFileName = Rhino.SaveFileName("Save", "Rhino 3D Models (*.3dm)|*.3dm||")
  If IsNull(strFileName) Then Exit Sub

  ' Since filenames can contain spaces, we need to
  ' surround the string with double-quote characters,
  ' or "", when scripting.    
  strFileName = Chr(34) & strFileName & Chr(34)

  ' Build the command script
  strCommand = "_-Save " & strFileName

  ' Script the save command
  Call Rhino.Command(strCommand, 0)

End Sub
```
