+++
aliases = ["/en/5/samples/rhinoscript/select-multiple-files/", "/en/6/samples/rhinoscript/select-multiple-files/", "/en/7/samples/rhinoscript/select-multiple-files/", "/en/wip/samples/rhinoscript/select-multiple-files/"]
authors = [ "dale" ]
categories = [ "Other" ]
description = "Demonstrates how to use RhinoScript's MultiListBox function to select multiple files."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Select Multiple Files"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/multilistbox"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0
+++

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
