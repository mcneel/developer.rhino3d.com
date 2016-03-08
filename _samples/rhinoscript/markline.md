---
title: Marking Points on a Line
description: Demonstrates how to mark points on a line using RhinoScript.
author: dale@mcneel.com
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/scriptsamples/markline
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

```vbnet
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' MarkLine.rvb -- March 2010
' If this code works, it was written by Dale Fugier.
' If not, I don't know who wrote it.
' Works with Rhino 4.0.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub MarkLine()
  Dim arrLast
  Call Rhino.Command("_Line _Pause _Pause")
  If (Rhino.LastCommandResult() = 0) Then
    Call Rhino.EnableRedraw(False)
    arrLast = Rhino.LastCreatedObjects()
    If IsArray(arrLast) Then
      Call Rhino.AddPoint(Rhino.CurveStartPoint(arrLast(0)))
      Call Rhino.AddPoint(Rhino.CurveMidPoint(arrLast(0)))
      Call Rhino.AddPoint(Rhino.CurveEndPoint(arrLast(0)))
      Call Rhino.DeleteObjects(arrLast)
    End If
    Call Rhino.EnableRedraw(True)
  End If
End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Call Rhino.AddStartupScript(Rhino.LastLoadedScriptFile)
Call Rhino.AddAlias("MarkLine", "_NoEcho _-RunScript (MarkLine)")
```
