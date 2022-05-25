+++
authors = [ "dale" ]
categories = [ "Curves" ]
description = "Demonstrates equidistance curve division using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Divide Curve With Equidistant Points"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/divideequidistance"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
Option Explicit

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' ''''''''''  
' Description
'   Divides a curve based on the linear distance between points.
'
Sub DivideCurveEquiDistant

  Dim crv
  crv = Rhino.GetObject("Select curve to divide", 4, True)
  If IsNull(crv) Then Exit Sub

  Dim crv_length
  crv_length = Rhino.CurveLength(crv)

  Dim length
  length = Rhino.GetReal("Curve length is " & CStr(crv_length) & ". Division length", 1.0)
  If Not IsNumeric(length) Then Exit Sub

  If (crv_length < length) Then
    Rhino.Print "Specified divison length exceeds curve length."
    Exit Sub
  End If    

  Rhino.EnableRedraw False  

  Dim dom, t, pt
  dom = Rhino.CurveDomain(crv)
  t = dom(0)
  pt = Rhino.EvaluateCurve(crv, t)
  Rhino.AddPoint pt

  Dim bDone: bDone = False
  While (bDone = False)
    t = EquiDistantParameter(crv, t, length)
    If IsNull(t) Then
      bDone = True
    Else
      pt = Rhino.EvaluateCurve(crv, t)
      Rhino.AddPoint pt
    End If
  Wend

  Rhino.EnableRedraw True

End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Description
'   Finds the parameter on a curve that is a specified
'   linear distance from a known parameter.
'
Function EquiDistantParameter(crv, t, length)

  EquiDistantParameter = Null

  Dim pt
  pt = Rhino.EvaluateCurve(crv, t)

  Dim sphere
  sphere = Rhino.AddSphere(pt, length)

  Dim csx
  csx = Rhino.CurveSurfaceIntersection(crv, sphere)

  Rhino.DeleteObject sphere
  If Not IsArray(csx) Then Exit Function

  Dim i
  For i = 0 To UBound(csx)
    If csx(i,0) = 1 Then
      If (csx(i,5) > t) Then
        EquiDistantParameter = csx(i,5)
        Exit Function
      End If
    End If
  Next

End Function
```
