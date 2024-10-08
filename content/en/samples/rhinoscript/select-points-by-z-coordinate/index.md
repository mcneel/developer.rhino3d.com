+++
aliases = ["/en/5/samples/rhinoscript/select-points-by-z-coordinate/", "/en/6/samples/rhinoscript/select-points-by-z-coordinate/", "/en/7/samples/rhinoscript/select-points-by-z-coordinate/", "/en/wip/samples/rhinoscript/select-points-by-z-coordinate/"]
authors = [ "dale" ]
categories = [ "Picking and Selection" ]
description = "Demonstrates how to select point objects with a user-specified z coordinate using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Select Points by Z Coordinate"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/selz"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0
+++

```vbnet
Option Explicit

Sub SelZ()

  Dim arr
  arr = Rhino.ObjectsByType(1)
  If Not IsArray(arr) Then
    Rhino.Print "No point objects to select"
    Exit Sub
  End If

  Const zero_tol = 1.0e-12

  Dim z, obj, pt
  z = Rhino.GetReal("Z coordinate", 0.0)
  If IsNumeric(z) Then
    For Each obj In arr
      pt = Rhino.PointCoordinates(obj)
      If IsArray(pt) Then
        If Abs(pt(2)-z) <= zero_tol Then
          Rhino.SelectObject obj
        End If
      End If
    Next
  End If

End Sub
```
