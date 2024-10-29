+++
aliases = ["/en/5/samples/rhinoscript/calculate-the-angle-between-two-vectors/", "/en/6/samples/rhinoscript/calculate-the-angle-between-two-vectors/", "/en/7/samples/rhinoscript/calculate-the-angle-between-two-vectors/", "/en/wip/samples/rhinoscript/calculate-the-angle-between-two-vectors/"]
authors = [ "dale" ]
categories = [ "Other" ]
description = "Demonstrates how to calculate the angle between two vectors using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Calculate the Angle Between Two Vectors"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/vectorangle"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0
+++

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
