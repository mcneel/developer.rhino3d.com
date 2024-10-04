+++
aliases = ["/en/5/samples/rhinoscript/create-an-ellipsoid-parametrically/", "/en/6/samples/rhinoscript/create-an-ellipsoid-parametrically/", "/en/7/samples/rhinoscript/create-an-ellipsoid-parametrically/", "/wip/samples/rhinoscript/create-an-ellipsoid-parametrically/"]
authors = [ "dale" ]
categories = [ "Adding Objects" ]
description = "Demonstrates one way of creating a Ellipsoid using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Create an Ellipsoid Parametrically"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/parametricellipsoid"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
'------------------------------------------------------------------------------
' ParametricEllipsoid.rvb -- February 2012
' If this code works, it was written by Dale Fugier.
' If not, I don't know who wrote it.
' Works with Rhino 4.0.
'
' Notes, the surface of the ellipsoid may be parameterized in several ways.
' One possible choice which singles out the 'z'-axis is:
'   x = a * Cos(u) * Cos(v)
'   y = b * Cos(u) * Sin(v)
'   z = c * Sin(u)
' where:
'  -pi/2 <= u <= pi/2, And -pi <= v <= pi
'------------------------------------------------------------------------------

Option Explicit

'------------------------------------------------------------------------------
' ParametricEllipsoid
'------------------------------------------------------------------------------
Sub ParametricEllipsoid()

  ' Variables
  Dim a, b, c
  Dim dom_u(1), dom_v(1), num_u(1), num_v(1)
  Dim i, j, st(1), uv(1), pts(), crvs()

  ' Prompt for coefficents
  a = Rhino.GetInteger("A Coefficient", 1, 1)
  If IsNull(a) Then Exit Sub

  b = Rhino.GetInteger("B Coefficient", 1, 1)
  If IsNull(b) Then Exit Sub

  c = Rhino.GetInteger("C Coefficient", 1, 1)
  If IsNull(c) Then Exit Sub

  ' Define domain of ellipsoid
  dom_u(0) = -(Rhino.PI / 2.0)
  dom_u(1) = Rhino.PI / 2.0
  dom_v(0) = -(Rhino.PI)
  dom_v(1) = Rhino.PI

  ' Define a domain of point samples
  ' To sample more points, increase num_u(1) and num_v(1)
  num_u(0) = 0
  num_u(1) = 20
  num_v(0) = 0
  num_v(1) = 20

  ' Storate for calculated point and temporary curves
  ReDim pts(num_u(1))
  ReDim crvs(num_v(1))

  ' Calculate ellipsoid points and interpolate
  For j = num_v(0) To num_v(1)
    For i = num_u(0) To num_u(1)
      st(0) = NormalizedAt(num_u(0), num_u(1), i)
      st(1) = NormalizedAt(num_v(0), num_v(1), j)
      uv(0) = ParameterAt(dom_u(0), dom_u(1), st(0))
      uv(1) = ParameterAt(dom_v(0), dom_v(1), st(1))
      pts(i) = PointAt(a, b, c, uv(0), uv(1))
    Next
    crvs(j) = Rhino.AddInterpCurve(pts)
  Next

  ' Loft the results
  Call Rhino.AddLoftSrf(crvs)

  ' Delete the temporary curves
  'Call Rhino.DeleteObjects(crvs)

End Sub

'------------------------------------------------------------------------------
' PointAt
' Evaluates an ellipsoid at a parameter
'------------------------------------------------------------------------------
Function PointAt(a, b, c, u, v)
  Dim pt(2)
  pt(0) = a * Cos(u) * Cos(v)
  pt(1) = b * Cos(u) * Sin(v)
  pt(2) = c * Sin(u)
  PointAt = pt
End Function

'------------------------------------------------------------------------------
' ParameterAt
' Converts a normalized parameter to a domain value
'------------------------------------------------------------------------------
Function ParameterAt(t0, t1, x)
  ParameterAt = (1.0 - x) * t0 + x * t1
End Function

'------------------------------------------------------------------------------
' NormalizedAt
' Converts a domain value to a normalized parameter
'------------------------------------------------------------------------------
Function NormalizedAt(t0, t1, t)
  Dim x : x = t0
  If (t0 <> t1) Then
    If (t = t1) Then
      x = 1.0
    Else
      x = (t - t0)/(t1 - t0)
    End If
  End If
  NormalizedAt = x
End Function

'------------------------------------------------------------------------------
Rhino.AddStartUpScript Rhino.LastLoadedScriptFile
Rhino.AddAlias "ParametricEllipsoid", "_-RunScript (ParametricEllipsoid)"
```
