+++
aliases = ["/en/5/samples/rhinoscript/move-curve-grips/", "/en/6/samples/rhinoscript/move-curve-grips/", "/en/7/samples/rhinoscript/move-curve-grips/", "/wip/samples/rhinoscript/move-curve-grips/"]
authors = [ "dale" ]
categories = [ "Curves" ]
description = "Demonstrates how to move a curve's grips using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Move Curve Grips"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/movecurvegrip"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
Sub MoveCurveGrip
  Const rhCurve = 4

  Dim sCurve : sCurve = Rhino.GetObject("Select a curve", rhCurve)
  If IsNull(sCurve) Then Exit Sub

  Dim bGripsOn : bGripsOn = Rhino.ObjectGripsOn(sCurve)
  If (bGripsOn = False) Then
    bGripsOn = Rhino.EnableObjectGrips(sCurve, True)
  End If

  Dim aGrip : aGrip = Rhino.GetObjectGrip("Select a curve grip")
  If IsArray(aGrip) Then
    Dim aPt : aPt = aGrip(2)
    aPt(2) = aPt(2) + 1.0
    Rhino.ObjectGripLocation sCurve, aGrip(1), aPt
  End If

  If (bGripsOn = True) Then
    Rhino.EnableObjectGrips sCurve, False
  End If

End Sub
```
