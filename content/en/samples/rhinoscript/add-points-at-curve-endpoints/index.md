+++
aliases = ["/en/5/samples/rhinoscript/add-points-at-curve-endpoints/", "/en/6/samples/rhinoscript/add-points-at-curve-endpoints/", "/en/7/samples/rhinoscript/add-points-at-curve-endpoints/", "/wip/samples/rhinoscript/add-points-at-curve-endpoints/"]
authors = [ "dale" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to add point at the starting and ending locations of curves."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Add Points at Curve Endpoints"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/addcurveendpoints"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
Option Explicit

Sub AddCurveEndPoints()
  Const rhCurve = 4

  ' Get all the curve objects in the document
  Dim arrCurves
  arrCurves = Rhino.ObjectsByType(rhCurve)
  If IsNull(arrCurves) Then Exit Sub

  ' For better performance, turn off screen redrawing  
  Call Rhino.EnableRedraw(False)

  ' Process each curve       
  Dim strCurve
  For Each strCurve In arrCurves
    ' Add a point at the start of the curve
    Call Rhino.AddPoint(Rhino.CurveStartPoint(strCurve))
    ' If not closed, add a point at the end of the curve
    If Not Rhino.IsCurveClosed(strCurve) Then
      Call Rhino.AddPoint(Rhino.CurveEndPoint(strCurve))
    End If
  Next

  ' Turn screen redrawing back on  
  Call Rhino.EnableRedraw(True)
End Sub
```
