+++
aliases = ["/en/5/samples/rhinoscript/offset-curve/", "/en/6/samples/rhinoscript/offset-curve/", "/en/7/samples/rhinoscript/offset-curve/", "/wip/samples/rhinoscript/offset-curve/"]
authors = [ "dale" ]
categories = [ "Curves" ]
description = "Demonstrates how to offset a curve inside or outside using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Offset Curve"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/offsetcurve"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
' Description:
'   Offsets a closed planar curve inside or outside.
' Parameters:
'   strSurface  - String, The identifier of the closed planar curve to offset.
'   dblDistance - Number, The distance to offset.
'   blnOutside  - Boolean, Offset outside (true) or inside (false).
' Returns:
'   Array, An array containing the identifiers of the new objects if successful.
'   Null on error

Option Explicit

Function RhinoOffsetClosedPlanarCurve(ByVal strCurve, ByVal dblDistance, ByVal blnOutside)

  ' Local variables
  Dim arrPlane, arrOldPlane, strView, arrBox, arrPoint

  ' Default return value
  RhinoOffsetClosedPlanarCurve = Null

  ' Quick parameter validation
  If (VarType(strCurve) <> vbString) Then Exit Function
  If Not IsNumeric(dblDistance) Then Exit Function
  If (VarType(blnOutside) <> vbBoolean) Then Exit Function

  ' Curve validation
  If (Rhino.IsCurve(strCurve) = False) Then Exit Function
  If (Rhino.IsCurveClosed(strCurve) = False) Then Exit Function
  arrPlane = Rhino.CurvePlane(strCurve)
  If Not IsArray(arrPlane) Then Exit Function

  ' Calculate plane-based bounding box
  strView = Rhino.CurrentView()
  arrOldPlane = Rhino.ViewCPlane(strView, arrPlane)
  arrBox = Rhino.BoundingBox(strCurve, strView)
  Call Rhino.ViewCPlane(strView, arrOldPlane)

  ' Offset point so its outside of bounding box
  arrPoint = Rhino.PointAdd(arrBox(0), Rhino.VectorCreate(arrBox(0), arrBox(2)))

  ' Offset the curve
  If (blnOutside = False) Then dblDistance = -dblDistance
  RhinoOffsetClosedPlanarCurve = Rhino.OffsetCurve(strCurve, arrPoint, dblDistance, arrPlane(3))

End Function
```
