+++
aliases = ["/en/5/samples/rhinoscript/get-flamingo-plant-points/", "/en/6/samples/rhinoscript/get-flamingo-plant-points/", "/en/7/samples/rhinoscript/get-flamingo-plant-points/", "/wip/samples/rhinoscript/get-flamingo-plant-points/"]
authors = [ "dale" ]
categories = [ "Flamingo" ]
description = "Demonstrates how get a list of points that represent a Flamingo nXt plant in RhinoScript."
keywords = [ "rhinoscript", "vbscript", "flamingo" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Get Plant Points"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/flamingo/flamingosdk/getplantpointcloud"
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
	Dim objPlugIn, plant, points, count
	On Error Resume Next
	Set objPlugIn = Rhino.GetPluginObject("8008880f-8d13-4b2d-92b0-727e12878a4c")
	If Err Then
		MsgBox Err.Description
		Exit Sub
	End If
  plant = objPlugIn.GetPlantFileName("")
  If Not IsNull(plant) Then
    points = objPlugIn.GetPlantPointCloud(plant)
    If Not IsNull(points) Then
      count = UBound(points)
      If count > 0 Then
        Rhino.AddPointCloud points
      	Rhino.Redraw()
      End If
    End If
	End If
	Set objPlugIn = Nothing
End Sub
```
