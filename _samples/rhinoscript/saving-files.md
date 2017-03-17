---
title: Saving Files
description: Demonstrates how to save a file using RhinoScript.
authors: ['Dale Fugier']
author_contacts: ['dale']
sdk: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/scriptsamples/savefile
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

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
