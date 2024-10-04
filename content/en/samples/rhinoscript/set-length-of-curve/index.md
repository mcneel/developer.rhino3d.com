+++
aliases = ["/en/5/samples/rhinoscript/set-length-of-curve/", "/en/6/samples/rhinoscript/set-length-of-curve/", "/en/7/samples/rhinoscript/set-length-of-curve/", "/wip/samples/rhinoscript/set-length-of-curve/"]
authors = [ "dale" ]
categories = [ "Picking and Selection", "Curves" ]
description = "Demonstrates how to set the length of a curve object using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Set Length of Curve"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/setcrvlength"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
Option Explicit

Sub SetCrvLength

  Dim crv, lold, lnew, dom, pts, t

  crv = Rhino.GetCurveObject("Select curve to set length", 4, True)
  If Not IsArray(crv) Then Exit Sub

  If Rhino.IsCurveClosed(crv(0)) Then
    Rhino.Print "Cannot set the length of closed curves."
    Exit Sub
  End If

  lold = Rhino.CurveLength(crv(0))
  lnew = Rhino.GetReal("New curve length", lold, 0.0, lold)
  If Not IsNumeric(lnew) Then Exit Sub
  If (lnew <= 0) Or (lnew >= lold) Then Exit Sub

  dom = Rhino.CurveDomain(crv(0))
  If (dom(1)-crv(4)) < (crv(4)-dom(0)) Then
    Rhino.ReverseCurve crv(0)
    dom = Rhino.CurveDomain(crv(0))
  End If

  pts = Rhino.DivideCurveLength(crv(0), lnew)
  t = Rhino.CurveClosestPoint(crv(0), pts(1))
  Rhino.TrimCurve crv(0), Array(dom(0), t), True

End Sub
```
