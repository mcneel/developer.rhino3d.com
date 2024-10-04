+++
aliases = ["/en/5/samples/rhinoscript/straightening-circles/", "/en/6/samples/rhinoscript/straightening-circles/", "/en/7/samples/rhinoscript/straightening-circles/", "/wip/samples/rhinoscript/straightening-circles/"]
authors = [ "dale" ]
categories = [ "Curves" ]
description = "Demonstrates how to create lines based on circle geometry using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Straightening Circles"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/straightencircles"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' StraightenCircles.rvb -- September 2008
' If this code works, it was written by Dale Fugier.
' If not, I don't know who wrote it.
' Works with Rhino 4.0.

Option Explicit

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' StraightenCircles
' Creates lines based on the circumferences of circles.
' Lines will be oriented based on the plane of the circle.

Sub StraightenCircles

  Dim obj_list, obj
  Dim length, plane, origin, xaxis
  Dim endpt, line

  obj_list = Rhino.GetObjects("Select circles to straighten", 4, True, True)
  If IsArray(obj_list) Then

    Call Rhino.EnableRedraw(False)

    For Each obj In obj_list
      If Rhino.IsCircle(obj) Then
        ' Gather data
        length = Rhino.CurveLength(obj)
        plane = Rhino.CurvePlane(obj)
        origin = plane(0)
        xaxis = plane(1)
        ' Calculate
        xaxis = Rhino.VectorUnitize(xaxis)
        xaxis = Rhino.VectorScale(xaxis, length)
        endpt = Rhino.PointAdd(origin, xaxis)
        line = Rhino.AddLine(origin, endpt)
        Call Rhino.SelectObject(line)
      End If

    Next

    Call Rhino.EnableRedraw(True)

  End If

End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Rhino.AddStartupScript Rhino.LastLoadedScriptFile
Rhino.AddAlias "StraightenCircles", "_NoEcho _-RunScript (StraightenCircles)"
```
