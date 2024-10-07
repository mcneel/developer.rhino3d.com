+++
aliases = ["/en/5/samples/rhinoscript/batch-render/", "/en/6/samples/rhinoscript/batch-render/", "/en/7/samples/rhinoscript/batch-render/", "/en/wip/samples/rhinoscript/batch-render/"]
authors = [ "dale" ]
categories = [ "Other" ]
description = "Demonstrates how to recurse through a folder and render every Rhino file using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Batch Render"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/batchrender"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0
+++

```vbnet
Option Explicit

' Run the subroutine
Call BatchRender

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' BatchRender
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub BatchRender()

  ' Allow the user to interactively pick a folder
  Dim sFolder
  sFolder = Rhino.BrowseForFolder(, "Select folder to process", "Batch Render" )
  If VarType( sFolder ) <> vbString Then Exit Sub

  ' Create a file system object
  Dim oFSO
  Set oFSO = CreateObject( "Scripting.FileSystemObject" )

  ' Get a folder object based on the selected folder
  Dim oFolder
  Set oFolder = oFSO.GetFolder( sFolder )

  ' Process the folder
  RecurseFolder oFolder

  ' Open an empty model
  Rhino.Command "_-New _None", 0

  ' Release the objects
  Set oFolder = Nothing
  Set oFSO = Nothing

End Sub

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' RecurseFolder
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub RecurseFolder( oFolder )

  ' Process each file in the folder
  Dim oFile
  For Each oFile In oFolder.Files
    ProcessFile oFile.Path
  Next

  ' Remark out the following lines if you do not want
  ' to recursively process the folder

  ' Process each subfolder in this folder
  Dim oSubFolder
  For Each oSubFolder In oFolder.SubFolders
    RecurseFolder( oSubFolder )
  Next

End Sub

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' ProcessFile
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub ProcessFile( sFile )

  ' Once we have gotten here, we have a valid file name.
  ' In this case, we are interested in just 3DM files.

  Dim sBitmap
  If (InStr(LCase(sFile), ".3dm") > 0) Then
    sBitmap = Replace(sFile, ".3dm", ".jpg", 1, -1, 1)
    Rhino.DocumentModified False
    Rhino.Command "_-Open " & Chr(34) & sFile & Chr(34), 0
    Rhino.Command "_-Render", 0
    Rhino.Command "_-SaveRenderWindowAs " & Chr(34) & sBitmap & Chr(34), 0
    Rhino.Command "_-CloseRenderWindow", 0
    Rhino.DocumentModified False
  End If  

End Sub
```
