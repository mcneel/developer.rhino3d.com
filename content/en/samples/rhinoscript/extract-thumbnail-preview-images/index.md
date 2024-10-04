+++
aliases = ["/en/5/samples/rhinoscript/extract-thumbnail-preview-images/", "/en/6/samples/rhinoscript/extract-thumbnail-preview-images/", "/en/7/samples/rhinoscript/extract-thumbnail-preview-images/", "/wip/samples/rhinoscript/extract-thumbnail-preview-images/"]
authors = [ "dale" ]
categories = [ "Other" ]
description = "Demonstrates how to extract the thumbnail preview image from .3DM files using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Extract Thumbnail Preview Images"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/batchextractthumbnails"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' BatchExtractThumbnails.rvb -- October 2008
' If this code works, it was written by Dale Fugier.
' If not, I don't know who wrote it.
' Works with Rhino 4.0.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Option Explicit

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' BatchExtractThumbnails
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub BatchExtractThumbnails()

  ' Allow the user to interactively pick a folder
  Dim sFolder : sFolder = Rhino.WorkingFolder
  sFolder = Rhino.BrowseForFolder(sFolder, "Select folder to process", "Batch Extract Thumbnails" )
  If IsNull(sFolder) Then Exit Sub

  ' Create a file system object
  Dim oFSO : Set oFSO = CreateObject("Scripting.FileSystemObject")

  ' Get a folder object based on the selected folder
  Dim oFolder : Set oFolder = oFSO.GetFolder(sFolder)

  ' Process the entire folder
  Call DoThumbnailExtraction(oFSO, oFolder)

  ' Done
  Call Rhino.Print("Done!")  

End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' DoThumbnailExtraction
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub DoThumbnailExtraction(oFSO, oFolder)

  ' Process all 3dm files in the folder
  Dim oFile, strOpen, strSave
  For Each oFile In oFolder.Files
    If LCase(oFSO.GetExtensionName(oFile.Path)) = "3dm" Then
      strOpen = LCase(oFile.Path)
      strSave = LCase(Replace(strOpen, ".3dm", ".jpg", 1, -1, 1))
      Call Rhino.Print("Processing " & strOpen & "...")
      Call Rhino.ExtractPreviewImage(strSave, strOpen)
    End If
  Next

  ' Un-comment the following if you want to recurse this folder
  'Dim oSubFolder
  'For Each oSubFolder In oFolder.SubFolders
  '  Call DoThumbnailExtraction(oFSO, oSubFolder)
  'Next

End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Rhino.AddStartupScript Rhino.LastLoadedScriptFile
Rhino.AddAlias "BatchExtractThumbnails", "_NoEcho _-RunScript (BatchExtractThumbnails)"
```
