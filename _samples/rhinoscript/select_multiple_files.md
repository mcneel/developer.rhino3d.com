---
title: Select Multiple Files
description: Demonstrates how to use RhinoScript's MultiListBox function to select multiple files.
author: dale@mcneel.com
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/scriptsamples/multilistbox
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

```vbnet
Sub Test
  Dim sFolder
  sFolder = Rhino.BrowseForFolder( , "Select folder with 3DM files" )
  If VarType( sFolder ) <> vbString Then Exit Sub

  Dim oFSO
  Set oFSO = CreateObject( "Scripting.FileSystemObject" )

  Dim oFolder
  Set oFolder = oFSO.GetFolder( sFolder )

  Dim oFile, aFiles(), nCount
  nCount = 0
  For Each oFile In oFolder.Files
    ReDim Preserve aFiles(nCount)
    aFiles(nCount) = oFile.Name
    nCount = nCount + 1
  Next

  If nCount = 0 Then
    Rhino.Print "Selected folder contained no 3DM files."
    Exit Sub
  End If

  Dim aSelected, sSelected
  aSelected = Rhino.MultiListBox(aFiles, oFolder.Path)
  If IsArray(aSelected) Then
    For Each sSelected In aSelected
      Rhino.Print sSelected
    Next
  End If

End Sub
```
