---
title: Batch Save Small
description: Demonstrates how to recurse through a folder and save small every Rhino file using RhinoScript.
authors: ['dale_fugier']
sdk: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/scriptsamples/batchsavesmall
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

```vbnet
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' BatchSaveSmall.rvb -- October 2008
' If this code works, it was written by Dale Fugier.
' If not, I don't know who wrote it.
' Works with Rhino 4.0.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Option Explicit

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Main subroutine
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub BatchSaveSmall()

  Dim sFolder, oFSO, oFolder

  sFolder = Rhino.BrowseForFolder(, "Select folder to recurse", "Batch SaveSmall")
  If IsNull(sFolder) Then Exit Sub

  Set oFSO = CreateObject("Scripting.FileSystemObject")
  Set oFolder = oFSO.GetFolder(sFolder)

  Call RecurseSaveSmall(oFolder)

  Call Rhino.DocumentModified(False)
  Call Rhino.Command("_-New _None", 0)
  Call Rhino.Print("Done!")

End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' RecurseSaveSmall
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub RecurseSaveSmall(oFolder)

  Dim oFile, oSubFolder, dModified

  For Each oFile In oFolder.Files
    ' Save file modified date
    dModified = oFile.DateLastModified

    ' Do the "save small"
    Call DoSaveSmall(oFile.Path)

    ' Reset file modified date
    Call TouchDateModified(oFile.Path, dModified)
  Next

  ' If you want to recurse folders,
  ' just un-comment the following lines.
  'For Each oSubFolder In oFolder.SubFolders
  '  Call RecurseSaveSmall(oSubFolder)
  'Next

End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' DoSaveSmall
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub DoSaveSmall(sPath)

  Dim aViews, sView

  If InStr(LCase(sPath), ".3dm") > 0 Then
    ' Open the file
    Call Rhino.DocumentModified(False)
    Call Rhino.Command("_-Open " & Chr(34) & sPath & Chr(34), 0)

    ' Set all of the viewports to wireframe before saving
    aViews = Rhino.ViewNames
    For Each sView In aViews
      Call Rhino.ViewDisplayMode(sView, 0)
    Next

    ' Save it
    Call Rhino.Command("_-SaveSmall _Enter", 0)
  End If

End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' TouchDateModified
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub TouchDateModified(sPath, dModified)

  Dim oShell, oFolder, oFile
  Dim sDir, sFile, nPos

  nPos = InStrRev(sPath, "\")
  sDir = Left(sPath, nPos)
  sFile = Mid(sPath, nPos + 1)

  Set oShell = CreateObject("Shell.Application")
  Set oFolder = oShell.NameSpace(sDir)
  Set oFile = oFolder.ParseName(sFile)
  oFile.ModifyDate = dModified

End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Rhino.AddStartupScript Rhino.LastLoadedScriptFile
Rhino.AddAlias "BatchSaveSmall", "_NoEcho _-RunScript (BatchSaveSmall)"
```
