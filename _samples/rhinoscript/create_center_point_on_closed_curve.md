---
title: Create Center Point on Closed Curve
description: Demonstrates how to mark the center points of closed planar curves with a point object using RhinoScript.
author: dale@mcneel.com
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Adding Objects']
origin: http://wiki.mcneel.com/developer/scriptsamples/createcenterpoint
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

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
