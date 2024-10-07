+++
aliases = ["/en/5/samples/rhinoscript/export-curve-control-points/", "/en/6/samples/rhinoscript/export-curve-control-points/", "/en/7/samples/rhinoscript/export-curve-control-points/", "/en/wip/samples/rhinoscript/export-curve-control-points/"]
authors = [ "dale" ]
categories = [ "Curves" ]
description = "Demonstrates how to export the 3D coordinates of a curve's control points to a text file using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Export Curve Control Points"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/exportcontrolpoints"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0
+++

```vbnet
Sub ExportControlPoints()

  'Pick a curve object
  Dim strObject
  strObject = Rhino.GetObject("Select curve", 4)
  If IsNull(strObject) Then Exit Sub

  ' Get the curve's control points
  Dim arrPoints
  arrPoints = Rhino.CurvePoints(strObject)
  If Not IsArray(arrPoints) Then Exit Sub

  ' Prompt the user to specify a file name    
  Dim strFilter, strFileName
  strFilter = "Text File (*.txt)|*.txt|All Files (*.*)|*.*|"
  strFileName = Rhino.SaveFileName("Save Control Points As", strFilter)
  If IsNull(strFileName) Then Exit Sub

  ' Get the file system object
  Dim objFSO, objStream
  Set objFSO = CreateObject("Scripting.FileSystemObject")

  ' Open a text file to write to
  On Error Resume Next
  Set objStream = objFSO.CreateTextFile(strFileName, True)
  If Err Then
    MsgBox Err.Description
    Exit Sub
  End If

  ' Write each point as text to the file
  Dim strPoint, strText
  For Each strPoint In arrPoints
    strText = Rhino.Pt2Str(strPoint)
    objStream.WriteLine(strText)
  Next

  ' Close the file
  objStream.Close

End Sub
```
