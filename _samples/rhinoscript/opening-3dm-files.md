---
title: Opening 3DM Files
description: Demonstrates how to open 3DM files using RhinoScript.
authors: ['dale_fugier']
sdk: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/scriptsamples/fileopen
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

```vbnet
Sub TestFileOpen()

  ' Local variable declarations
  Dim strFile

  ' Let the user pick a 3dm file. If the return value is null,
  ' then the user picked the "Cancel" button...
  strFile = Rhino.OpenFileName("Open", "Rhino 3D Models (*.3dm)|*.3dm|")
  If IsNull(strFile) Then Exit Sub

  ' To keep Rhino from displaying the dreaded
  ' "Save changes to <filename>" dialog, we can fool it
  ' into thinking that the document was never modified
  ' by doing the following.
  Call Rhino.DocumentModified(False)

  ' If the picked a file that has a space character in its name,
  ' or resides in a folder that has a space character, then we
  ' need to surround the file string in double-quotes so Rhino's
  ' command line parser will interpret the string correctly.
  strFile = Chr(34) & strFile & Chr(34)

  ' Now we can simply script Rhino's Open command to open the file.
   Call Rhino.Command("_-Open " & strFile, 0)

End Sub
```
