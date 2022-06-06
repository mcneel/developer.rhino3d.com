+++
aliases = ["/5/samples/rhinoscript/multiple-pipe/", "/6/samples/rhinoscript/multiple-pipe/", "/7/samples/rhinoscript/multiple-pipe/", "/wip/samples/rhinoscript/multiple-pipe/"]
authors = [ "rajaa" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to Pipe on multiple curves at a time using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Multiple Pipe"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/pipeall"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PipeAll.rvb -- September 2008
' If this code works, it was written by Rajaa Issa.
' If not, I don't know who wrote it.
' Works with Rhino 4.0.

Option Explicit

Sub PipeOne(strRail, strRadius)
  Dim strCmd
  strCmd = "! _-Pipe _SelID " & strRail & " " & strRadius & " _Cap=_Round _Enter _Enter"
  Call Rhino.Command(strCmd, 0)
End Sub

Sub PipeAll
 Dim arrCurves, name, pipeRadius
 arrCurves = Rhino.GetObjects("Select curves to pipe", 4)
 pipeRadius = Rhino.GetReal("Pipe radius")

 'PIPE
 If IsArray(arrCurves) Then
  For Each name In arrCurves
   Call PipeOne(name, pipeRadius)
  Next
 End If
End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Rhino.AddStartupScript Rhino.LastLoadedScriptFile
Rhino.AddAlias "PipeAll", "_NoEcho _-RunScript (PipeAll)"
```
