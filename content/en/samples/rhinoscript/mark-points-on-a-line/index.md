+++
aliases = ["/en/5/samples/rhinoscript/mark-points-on-a-line/", "/en/6/samples/rhinoscript/mark-points-on-a-line/", "/en/7/samples/rhinoscript/mark-points-on-a-line/", "/wip/samples/rhinoscript/mark-points-on-a-line/"]
authors = [ "dale" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to mark points on a line using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Mark Points on a Line"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/markline"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

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
