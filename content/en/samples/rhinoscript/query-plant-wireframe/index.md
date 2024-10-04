+++
aliases = ["/en/5/samples/rhinoscript/query-plant-wireframe/", "/en/6/samples/rhinoscript/query-plant-wireframe/", "/en/7/samples/rhinoscript/query-plant-wireframe/", "/wip/samples/rhinoscript/query-plant-wireframe/"]
authors = [ "dale" ]
categories = [ "Flamingo" ]
description = "Demonstrates how to generate a wire-frame representation of a Flamingo 2.0 plant using RhinoScript."
keywords = [ "rhinoscript", "vbscript", "flamingo" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Query Plant Wireframe"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/flamingo/flamingosdk/flamingo2plantwireframe"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
Option Explicit

Call Main()

Sub Main()
	Dim objPlugIn, plant, lines, line, i, count
	On Error Resume Next
	Set objPlugIn = Rhino.GetPluginObject("8008880f-8d13-4b2d-92b0-727e12878a4c")
	If Err Then
		MsgBox Err.Description
		Exit Sub
	End If
  plant = objPlugIn.ModalFlamingo2PlantBrowser("", "", "")
  If Not IsNull(plant) Then
    lines = objPlugIn.GetFlamingo2PlantWireframe(plant(0), plant(1), plant(2))
    If Not IsNull(lines) Then
      count = UBound(lines)
      If count > 0 Then
        For i = 0 to count
          Rhino.Print("Line " & (i + 1) & " of " & (count + 1))
          Rhino.AddLine Array(lines(i,0), lines(i,1), lines(i,2)), Array(lines(i,3), lines(i,4), lines(i,5))
        Next
      	Rhino.Redraw()
      End If
    End If
	End If
	Set objPlugIn = Nothing
End Sub
```
