+++
aliases = ["/en/5/samples/rhinoscript/batch-convert-autocad-files/", "/en/6/samples/rhinoscript/batch-convert-autocad-files/", "/en/7/samples/rhinoscript/batch-convert-autocad-files/", "/en/wip/samples/rhinoscript/batch-convert-autocad-files/"]
authors = [ "dale" ]
categories = [ "Other" ]
description = "Demonstrates how to convert a folder of AutoCAD files to Rhino 3dm files using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Batch Convert AutoCAD Files"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/batchconvertautocad"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0
+++

```vbnet
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' BatchConvertAutoCAD script for Rhinoceros
' Robert McNeel & Associates
' www.rhino3d.com
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Option Explicit

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' BatchConvertAutoCAD
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub BatchConvertAutoCAD()

  ' Make sure RhinoScript does not reinitialize when opening models,
  ' otherwise this script will only process one file.
  Rhino.Command "_-Options _RhinoScript _Reinitialize=_No _Enter _Enter", 0

  ' Allow the user to interactively pick a folder
  Dim sFolder
  sFolder = Rhino.BrowseForFolder(, "Select folder to process", "Batch Convert AutoCAD")
  If VarType(sFolder) <> vbString Then Exit Sub

  ' Create a file system object
  Dim oFSO
  Set oFSO = CreateObject("Scripting.FileSystemObject")

  ' Get a folder object based on the selected folder
  Dim oFolder
  Set oFolder = oFSO.GetFolder(sFolder)

  ' Process the folder
  ProcessFolder oFSO, oFolder

  ' Release the objects
  Set oFolder = Nothing
  Set oFSO = Nothing

  ' Close the last file processed
  Rhino.DocumentModified False
  Rhino.Command "_-New _None", 0

End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' ProcessFolder
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub ProcessFolder(oFSO, oFolder)

  ' Process all .dwg files in the selected folder
  Dim oFile, strOpen, strSave
  For Each oFile In oFolder.Files
    If LCase(oFSO.GetExtensionName(oFile.Path)) = "dwg" Then
      strOpen = LCase(oFile.Path)
      strSave = LCase(Replace(strOpen, ".dwg", ".3dm", 1, -1, 1))
      ProcessFile strOpen, strSave
    End If
  Next

  ' Comment out the following lines if you do not
  ' want to recursively process the selected folder.
  Dim oSubFolder
  For Each oSubFolder In oFolder.SubFolders
    ProcessFolder oFSO, oSubFolder
  Next

End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' ProcessFile
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub ProcessFile(strOpen, strSave)
  Rhino.DocumentModified False
  Rhino.Command "_-Open " & Chr(34) & strOpen & Chr(34), 0
  Rhino.Command "_-Zoom _All _Extents", 0
  Rhino.Command "_-SetActiveView _Top", 0
  Rhino.Command "_-Save " & Chr(34) & strSave & Chr(34), 0
End Sub
```
