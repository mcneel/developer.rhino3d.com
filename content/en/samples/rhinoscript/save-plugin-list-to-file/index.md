+++
aliases = ["/en/5/samples/rhinoscript/save-plugin-list-to-file/", "/en/6/samples/rhinoscript/save-plugin-list-to-file/", "/en/7/samples/rhinoscript/save-plugin-list-to-file/", "/wip/samples/rhinoscript/save-plugin-list-to-file/"]
authors = [ "dale" ]
categories = [ "Other" ]
description = "Demonstrates how to save the names of loaded and unloaded plugins to a text file using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Save Plugin List to File"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/savepluginlist"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' SavePlugInInfo.rvb -- April 2008
' If this code works, it was written by Dale Fugier.
' If not, I don't know who wrote it.
' Works with Rhino 4.0.

Option Explicit

Sub SavePlugInInfo()

  Dim objShell, objNetwork, objFSO, objFolder, objStream
  Dim arrPlugIns, arrSorted, strPlugIn, strDesktop, strFile, strName, strMsg

  Set objShell = CreateObject("WScript.Shell")
  Set objNetwork = CreateObject("WScript.Network")
  Set objFSO = CreateObject("Scripting.FileSystemObject")

  strName = "RhinoPlugInInfo.txt"
  strDesktop = objShell.SpecialFolders("Desktop")
  strFile = strDeskTop & "\" & strName

  'On Error Resume Next
  Set objStream = objFSO.CreateTextFile(strFile, True)
  If Err Then
    MsgBox Err.Description
    Exit Sub
  End If

  objStream.WriteLine "**************************"
  objStream.WriteLine "Rhino Plug-in Info"
  objStream.WriteLine
  objStream.WriteLine "Computer Name = " & objNetwork.ComputerName
  objStream.WriteLine "Date and Time = " & CStr(Now)
  objStream.WriteLine "Rhino Build Date = " & CStr(Rhino.BuildDate)
  objStream.WriteLine "Rhino SDK Version = " & CStr(Rhino.SdkVersion)
  objStream.WriteLine "**************************"
  objStream.WriteLine

  objStream.WriteLine "**************************"
  objStream.WriteLine "Loaded Plug-ins"
  objStream.WriteLine "**************************"
  objStream.WriteLine

  arrPlugIns = Rhino.PlugIns(0, 1)
  If IsArray(arrPlugIns) Then
    arrSorted = Rhino.SortStrings(arrPlugIns)
    For Each strPlugIn In arrSorted
      objStream.WriteLine strPlugIn
    Next
  End If

  objStream.WriteLine
  objStream.WriteLine "**************************"
  objStream.WriteLine "Unloaded Plug-ins"
  objStream.WriteLine "**************************"
  objStream.WriteLine

  arrPlugIns = Rhino.PlugIns(0, 2)
  If IsArray(arrPlugIns) Then
    arrSorted = Rhino.SortStrings(arrPlugIns)
    For Each strPlugIn In arrSorted
      objStream.WriteLine strPlugIn
    Next
  End If

  objStream.Close

  strMsg = "A file named " & Chr(34) & strName & Chr(34) & VbCrLf
  strMsg = strMsg & "has been saved to your desktop." & VbCrLf & VbCrLf
  strMsg = strMsg & "If you are experiencing problems with Rhino," & VbCrLf
  strMsg = strMsg & "email this file to " & Chr(34) & "tech@mcneel.com" & Chr(34) & VbCrLf
  strMsg = strMsg & "along with a detailed description" & VbCrLf
  strMsg = strMsg & "of your problem."
  MsgBox strMsg, 64, "Rhinoceros"

End Sub

' Rhino.AddStartUpScript Rhino.LastLoadedScriptFile
' Rhino.AddAlias "SavePlugInInfo", "_-RunScript (SavePlugInInfo)"

' Run it!
Call SavePlugInInfo
```
