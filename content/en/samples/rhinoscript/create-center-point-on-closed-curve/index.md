+++
aliases = ["/en/5/samples/rhinoscript/create-center-point-on-closed-curve/", "/en/6/samples/rhinoscript/create-center-point-on-closed-curve/", "/en/7/samples/rhinoscript/create-center-point-on-closed-curve/", "/en/wip/samples/rhinoscript/create-center-point-on-closed-curve/"]
authors = [ "dale" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to mark the center points of closed planar curves with a point object using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Create Center Point on Closed Curve"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/createcenterpoint"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0
+++

```vbnet
Sub MarkCenterPoints()
  Dim curves, crv, pt, arr
  curves = Rhino.GetObjects("Select closed planar curves", 4, ,True)
  If IsArray(curves) Then
    Rhino.EnableRedraw False
    For Each crv In curves
      pt = vbNull
      If Rhino.IsCircle(crv) Then
        pt = Rhino.CircleCenterPoint(crv)
      Else
        arr = Rhino.CurveAreaCentroid(crv)
        If IsArray(arr) Then pt = arr(0)
      End If
      If IsArray(pt) Then
        Rhino.SelectObject Rhino.AddPoint(pt)
      End If
    Next        
    Rhino.EnableRedraw True
  End If
End Sub
```
