+++
aliases = ["/en/5/samples/rhinoscript/arc-point-distribution/", "/en/6/samples/rhinoscript/arc-point-distribution/", "/en/7/samples/rhinoscript/arc-point-distribution/", "/en/wip/samples/rhinoscript/arc-point-distribution/"]
authors = [ "dale" ]
categories = [ "Other" ]
description = "Demonstrates arc point distribution."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Arc Point Distribution"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/arcpointdistribution"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0
+++

```vbnet
Option Explicit

Sub ArcPointDistribution
   ' Local variables
   Dim arc, cnt, rads
   Dim n_t(), n, i, a0, a1
   Dim line, dom, t

   ' Select arc curve  
   arc = Rhino.GetObject("Select arc", 4)
   If IsNull(arc) Then Exit Sub
   If Not Rhino.IsArc(arc) Then Exit Sub

   ' Get number of points to calculate
   cnt = Rhino.GetInteger("Number of points", 2)
   If IsNull(cnt) Then Exit Sub   

   rads = Rhino.ToRadians(Rhino.ArcAngle(arc))
   n = cnt - 1
   ReDim n_t(n)

   ' Calculate normalized parameters
   For i = 0 To n
     a0 = Sin(rads/2)
     a1 = Sin(i*rads/n - rads/2)
     n_t(i) = (a0+a1)/(2*a0)
   Next

   Rhino.EnableRedraw False

   line = Rhino.AddLine(Rhino.CurveStartPoint(arc), Rhino.CurveEndPoint(arc))
   dom = Rhino.CurveDomain(line)

   For i = 0 To n
     ' Convert normalized parameter to domain value
     t = (1.0 - n_t(i)) * dom(0) + n_t(i) * dom(1)
     Rhino.AddPoint Rhino.EvaluateCurve(line, t)
   Next

   Rhino.EnableRedraw True
End Sub
```
