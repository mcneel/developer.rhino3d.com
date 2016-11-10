---
title: Rotate Object Around Point
description: Demonstrates how to rotate an object around the centroid of its bounding box using RhinoScript.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/scriptsamples/rotateone
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

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
