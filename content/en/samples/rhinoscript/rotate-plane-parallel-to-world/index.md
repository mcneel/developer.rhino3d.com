+++
aliases = ["/en/5/samples/rhinoscript/rotate-plane-parallel-to-world/", "/en/6/samples/rhinoscript/rotate-plane-parallel-to-world/", "/en/7/samples/rhinoscript/rotate-plane-parallel-to-world/", "/wip/samples/rhinoscript/rotate-plane-parallel-to-world/"]
authors = [ "dale" ]
categories = [ "Other" ]
description = "Demonstrates how to rotate a plane so its x-axis is parallel to the world using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Rotate Plane Parallel to World"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/rotateplaneparallel"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
Option Explicit

'------------------------------------------------------------------------------
' Subroutine: XParallelPlane
' Purpose:    Rotate a plane about it's z-axis so that it's x-axis
              is parallel with the world xy-plane.
' Parameters:
'             plane - A valid plane to rotate
'             dir   - Direction (True = positive, False = negative)
' Returns:
'             A valid plane if successful, Null otherwise.
'------------------------------------------------------------------------------
Function XParallelPlane(plane, dir)

  Dim xaxis, yaxis, zaxis
  XParallelPlane = Null 'default return value

  zaxis = Rhino.VectorUnitize(plane(3))
  If (dir = True) Then
    xaxis = Rhino.VectorUnitize(Array(zaxis(1), -zaxis(0), 0.0))
  Else
    xaxis = Rhino.VectorUnitize(Array(-zaxis(0), zaxis(1), 0.0))
  End If

  yaxis = Rhino.VectorCrossProduct(zaxis, xaxis)
  If IsArray(yaxis) Then
    yaxis = Rhino.VectorUnitize(yaxis)
    XParallelPlane = Rhino.PlaneFromFrame(plane(0), xaxis, yaxis)
  End If

End Function
```
