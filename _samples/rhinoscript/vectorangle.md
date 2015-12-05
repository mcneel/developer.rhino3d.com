---
layout: code-sample-rhinoscript
title: Calculate the Angle Between Two Vectors
author: dale@mcneel.com
platforms: ['Windows']
apis: ['RhinoScript']
languages: ['VBScript']
keywords: ['rhinoscript', 'vbscript']
categories: ['Uncategorized']
description: Demonstrates how to calculate the angle between two vectors using RhinoScript.
TODO: 0
origin: http://wiki.mcneel.com/developer/scriptsamples/vectorangle
order: 1
---

```vbnet
' Description:
'  Calculates the angle between two 3-D vectors.
' Parameters:
'   v0 - [in] - the first vector.
'   v1 - [in] - the second vector.
' Returns:
'   the angle in degrees.

Function VectorAngle(v0, v1)

  Dim u0  : u0  = Rhino.VectorUnitize(v0)
  Dim u1  : u1  = Rhino.VectorUnitize(v1)  
  Dim dot : dot = Rhino.VectorDotProduct(u0, u1)

  ' Force the dot product of the two input vectors to
  ' fall within the domain for inverse cosine, which
  ' is -1 <= x <= 1. This will prevent runtime
  ' "domain error" math exceptions.
  If (dot < -1.0) Then
    dot = -1.0
  ElseIf (dot > 1.0) Then
    dot = 1.0
  End If

  VectorAngle = Rhino.ToDegrees(Rhino.ACos(dot))

End Function
```
