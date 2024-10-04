+++
aliases = ["/en/5/samples/rhinoscript/rotate-object-around-point/", "/en/6/samples/rhinoscript/rotate-object-around-point/", "/en/7/samples/rhinoscript/rotate-object-around-point/", "/wip/samples/rhinoscript/rotate-object-around-point/"]
authors = [ "dale" ]
categories = [ "Other" ]
description = "Demonstrates how to rotate an object around the centroid of its bounding box using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Rotate Object Around Point"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/rotateone"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
Sub Rotate1
  Dim sObj, aBox, aMin, aMax, aCen
  sObj = Rhino.GetObject("Select object to rotate 1 degree", 0, True)
  If Not IsNull(sObj) Then
    aBox = Rhino.BoundingBox(sObj)
    If IsArray(aBox) Then
      aMin = aBox(0)
      aMax = aBox(6)
      aCen = Array( _
          0.5*(aMax(0)+aMin(0)), _
          0.5*(aMax(1)+aMin(1)), _
          0.5*(aMax(2)+aMin(2)) _
          )
      Rhino.RotateObject sObj, aCen, 1.0
    End If
  End If      
End Sub
```
