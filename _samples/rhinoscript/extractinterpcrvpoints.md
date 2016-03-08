---
title: Extracting Interpolated Curve Construction Points
description: Demonstrates how to reverse engineer an interpolated curve using RhinoScript.
author: dale@mcneel.com
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/scriptsamples/extractinterpcrvpoints
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

```vbnet
Function ExtractInterpCrvPoints(curve)

' local variables
Dim points(), knots, i

' default result
ExtractInterpCrvPoints = Null

' verify the curve
If Not IsNull(curve) And Rhino.IsCurve(curve) Then

  ' verify the degree of the curve
  If Rhino.CurveDegree(curve) = 3 Then

    ' get the curve's knots
    knots = Rhino.CurveKnots(curve)

    ' verify the curve's knots
    If IsArray(knots) Then

      ' evaluate the curve at each knot value      
      ReDim points(UBound(knots))
      For i = 0 To UBound(knots)
        points(i) = Rhino.EvaluateCurve(curve, knots(i))
      Next

      ' cull any duplicate points
      ExtractInterpCrvPoints = Rhino.CullDuplicatePoints(points)

    End If

  End If

End If

End Function
```
