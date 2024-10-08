+++
aliases = ["/en/5/samples/rhinoscript/import-text-from-file/", "/en/6/samples/rhinoscript/import-text-from-file/", "/en/7/samples/rhinoscript/import-text-from-file/", "/en/wip/samples/rhinoscript/import-text-from-file/"]
authors = [ "dale" ]
categories = [ "Other" ]
description = "Demonstrates how to import text from a file using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Import Text from File"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/importtext"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0
+++

```vbnet
Sub ImportText

  Const ForReading = 1
  Dim strFile, strText
  Dim objFSO, objFile
  Dim arrOrigin

  strFile = Rhino.OpenFileName("Open", "Text Files (*.txt)|*.txt|")
  If IsNull(strFile) Then Exit Sub

  arrOrigin = Rhino.GetPoint("Start point")
  If Not IsArray(arrOrigin) Then Exit Sub

  Set objFSO = CreateObject("Scripting.FileSystemObject")

  On Error Resume Next
  Set objFile = objFSO.OpenTextFile(strFile, ForReading)
  If Err Then
    MsgBox Err.Description
    Exit Sub
  End If

  While Not objFile.AtEndOfStream
    strText = strText & objFile.ReadLine
    If Not objFile.AtEndOfStream Then
      strText = strText & VbCrLf
    End If
  Wend

  objFile.Close

  Set objFile = Nothing
  Set objFSO = Nothing

  If Len(strText) > 0 Then
    Rhino.AddText strText, arrOrigin
  End If

End Sub
```
