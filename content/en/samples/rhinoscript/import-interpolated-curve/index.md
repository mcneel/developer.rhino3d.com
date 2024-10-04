+++
aliases = ["/en/5/samples/rhinoscript/import-interpolated-curve/", "/en/6/samples/rhinoscript/import-interpolated-curve/", "/en/7/samples/rhinoscript/import-interpolated-curve/", "/wip/samples/rhinoscript/import-interpolated-curve/"]
authors = [ "dale" ]
categories = [ "Curves" ]
description = "Demonstrates how to read a point file and create an interpolated curve using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Import Interpolated Curve"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/importinterpcrv"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
Option Explicit

Sub ImportInterpCrv()

  Dim strFilter, strFileName
  strFilter = "Text File (*.txt)|*.txt|All Files (*.*)|*.*|"
  strFileName = Rhino.OpenFileName("Open Point File", strFilter)
  If IsNull(strFileName) Then Exit Sub

  Dim objFSO, objFile
  Set objFSO = CreateObject("Scripting.FileSystemObject")

  On Error Resume Next
  Set objFile = objFSO.OpenTextFile(strFileName, 1)
  If Err Then
    MsgBox Err.Description
    Exit Sub
  End If

  Dim strLine, arrPt, arrPoints(), nCount
  nCount = 0  
  Do While objFile.AtEndOfStream <> True
    strLine = objFile.ReadLine
    If Not IsNull(strLine) Then
      strLine = Replace(strLine, Chr(34), , 1)
      arrPt = Rhino.Str2Pt(strLine)
      If IsArray(arrPoint) Then
        ReDim Preserve arrPoints(nCount)
        arrPoints(nCount) = arrPt
        nCount = nCount + 1
      End If
    End If
  Loop

  If IsArray(arrPoints) Then
    Rhino.AddInterpCurveEx arrPoints
  End If

  objFile.Close

  Set objFile = Nothing
  Set objFSO = Nothing

End Sub
```
