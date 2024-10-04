+++
aliases = ["/en/5/samples/rhinoscript/unrolling-surfaces-and-polysurfaces/", "/en/6/samples/rhinoscript/unrolling-surfaces-and-polysurfaces/", "/en/7/samples/rhinoscript/unrolling-surfaces-and-polysurfaces/", "/wip/samples/rhinoscript/unrolling-surfaces-and-polysurfaces/"]
authors = [ "dale" ]
categories = [ "Surfaces" ]
description = "Demonstrates how to unroll surfaces and polysurfaces using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Unrolling Surfaces and Polysurfaces"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/unrollsrf"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
' Description:
'   Unroll a surface or polysurface.
' Parameters:
'   strSurface - String, The identifier of the surface or polysurface to unroll.
'   arrCurves  - Array, The identifiers of one or more curves to unroll.
'   blnExplode - Boolean, Explode the resulting objects.
'   blnLabels  - Boolean, Label the resulting objects with numbered dots.
' Returns:
'   Array, The identifiers of the unrolled objects if successful.
'   Null on error

Option Explicit

Function RhinoUnrollSurface(strSurface, arrCurves, blnExplode, blnLabels)

  ' Default return value  
  RhinoUnrollSurface = Null

  ' For speed, turn of screen redrawing
  Call Rhino.EnableRedraw(False)

  ' Save any selected objects
  Dim arrSaved : arrSaved = Rhino.SelectedObjects

  ' Unselect all objects
  Rhino.UnSelectAllObjects

  ' Select the surface to unroll
  Rhino.SelectObject strSurface

  ' Format curve string
  Dim i : i = 0
  Dim strCurves
  If IsArray(arrCurves) Then
    For i = 0 To UBound(arrCurves)
      strCurves = strCurves & " _SelId " & arrCurves(i)
    Next
    strCurves = strCurves & " _Enter"
  End If

  ' Format explode string
  Dim strExplode : strExplode = " _Explode=_Yes"
  If (blnExplode = False) Then strExplode = " _Explode=_No"

  ' Format labels string
  Dim strLabels : strLabels = " _Labels=_No"
  If (blnLabels = True) Then strLabels = " _Labels=_Yes"

 ' Script the command
  Dim strCommand : strCommand = "_-UnrollSrf" & strExplode & strLabels & strCurves
  Call Rhino.Command(strCommand, 0)

  ' Return the results
  RhinoUnrollSurface = Rhino.LastCreatedObjects

  ' Unselect all objects
  Rhino.UnSelectAllObjects

  ' If any objects were selected before calling
  ' this function, re-select them
  If IsArray(arrSaved) Then Rhino.SelectObjects(arrSaved)

  ' Don't forget to turn redrawing back on
  Call Rhino.EnableRedraw(True)

End Function
```
