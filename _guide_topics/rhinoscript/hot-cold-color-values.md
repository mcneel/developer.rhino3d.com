---
title: Hot & Cold Colors
description: This guide demonstrates how calculate colors for analysis using RhinoScript.
authors: ['Dale Fugier']
author_contacts: ['dale']
sdk: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Miscellaneous', 'Advanced']
origin: http://wiki.mcneel.com/developer/scriptsamples/hotcoldcolor
order: 1
keywords: ['script', 'Rhino', 'vbscript']
layout: toc-guide-page
---

 
## Problem

It is often useful to show the curvature of a curve with a color index. For example, if you divide a curve into 500 points and measure the curvature at each point, you can assign a “curvature radius” color to each of the points using RhinoScript.  Let's take a look at house this is done.

## Solution

One solution you might consider is to determine the minimum and maximum curvature values for your samples. Then, you can use this function to calculate a color value for each point.

```vbnet
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Return a RGB color given a scalar v in the range [vmin, vmax].
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Function GetHotColdColor(v, vmin, vmax)

  Dim r, g, b, dv
  r = 1.0 : g = 1.0 : b = 1.0 'white

  If (v < vmin) Then v = vmin
  If (v > vmax) Then v = vmax
  dv = vmax - vmin

  If (v < (vmin + 0.25 * dv)) Then
    r = 0
    g = 4 * (v - vmin) / dv
  ElseIf (v < (vmin + 0.5 * dv)) Then
    r = 0
    b = 1 + 4 * (vmin + 0.25 * dv - v) / dv
  ElseIf (v < (vmin + 0.75 * dv)) Then
    r = 4 * (v - vmin - 0.5 * dv) / dv
    b = 0
  Else
    g = 1 + 4 * (vmin + 0.75 * dv - v) / dv
    b = 0
  End If

  GetHotColdColor = RGB(Int(r*255), Int(g*255), Int(b*255))

End Function
```

Here is a sample script that you can use to test the above function...

```vbnet
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Test procedure creates a "hot-to-cold" color ramp mesh.
' To see the results, set a viewport to "rendered" display.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub TestGetHotColdColor()

  ' Mesh with 200 vertices and 100 faces
  Dim v(199), f(99), c(199), ub, i

  ' Fill in arrays
  ub = UBound(v)
  For i = 0 To UBound(v) Step 2
    v(i) = Array(i/2,0,0)
    v(i+1) = Array(i/2,10,0)
    c(i) = GetHotColdColor(i,0,ub)
    c(i+1) = c(i)
    f(i/2) = Array(i,i+2,i+3,i+1)
  Next

  ' Create the mesh object
  Call Rhino.AddMesh(v,f,,,c)

End Sub
```
