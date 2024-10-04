+++
aliases = ["/en/5/samples/rhinoscript/divide-curve-to-dashed/", "/en/6/samples/rhinoscript/divide-curve-to-dashed/", "/en/7/samples/rhinoscript/divide-curve-to-dashed/", "/wip/samples/rhinoscript/divide-curve-to-dashed/"]
authors = [ "dale" ]
categories = [ "Curves" ]
description = "Demonstrates how to chop up a curve into segments and spaces."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Divide Curve to Dashed"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/dividecurvedashed"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' DivideCurveDashed.rvb -- October 2010
' If this code works, it was written by Dale Fugier.
' If not, I don't know who wrote it.
' Works with Rhino 4.0 and 5.0.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Option Explicit

' Divides a curve into "dashed" segments
Sub DivideCurveDashed

  Dim curve, slength, dlength
  Dim i, length, pt, t, dom, results

  curve = Rhino.GetObject("Select curve to divide", 4, True)
  If IsNull(curve) Then Exit Sub

  slength = Rhino.GetReal("Segment length", 1.0)
  If IsNull(slength) Then Exit Sub
  If (slength <= 0) Then Exit Sub  

  dlength = Rhino.GetReal("Dash length", 1.0)
  If IsNull(dlength) Then Exit Sub
  If (dlength <= 0) Then Exit Sub

  Call Rhino.EnableRedraw(False)
  i = 0

  Do

    If (i Mod 2 = 0) Then
      length = slength
    Else
      length = dlength
    End If

    pt = Rhino.CurveArcLengthPoint(curve, length)
    If IsNull(pt) Then Exit Do

    t = Rhino.CurveClosestPoint(curve, pt)

    If (i Mod 2 = 0) Then
      results = Rhino.SplitCurve(curve, t, True)
      curve = results(1)
    Else
      dom = Rhino.CurveDomain(curve)
      curve = Rhino.TrimCurve(curve, Array(t, dom(1)), True)
    End If

    i = i + 1

  Loop While True    

  Call Rhino.EnableRedraw(True)

End Sub

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Drag & drop and alias creation stuff
Rhino.AddStartUpScript Rhino.LastLoadedScriptFile
Rhino.AddAlias "DivideCurveDashed", "_-RunScript (DivideCurveDashed)"
```
