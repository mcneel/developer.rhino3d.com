+++
authors = [ "dale" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to create polar arrays of objects using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Polar Arrays"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/arraypolar"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
Option Explicit

Sub MyArrayPolar

  Dim arrObjects, arrCenter, nCount
  Dim dAngle, arrAxis, arrXform, i

  arrObjects = Rhino.GetObjects("Select objects to array")
  If IsNull(arrObjects) Then Exit Sub

  arrCenter = Rhino.GetPoint("Center of polar array")
  If IsNull(arrCenter) Then Exit Sub

  nCount = Rhino.GetInteger("Number of items",,2)
  If IsNull(nCount) Then Exit Sub

  dAngle = 360.0 / nCount

  Rhino.EnableRedraw False

  For i = 1 To nCount - 1
    arrAxis = Array(0,0,1) ' world z-axis
    arrXform = Rhino.XformRotation(dAngle * i, arrAxis, arrCenter)
    Rhino.TransformObjects arrObjects, arrXform, True
  Next

  Rhino.EnableRedraw True

End Sub
```
