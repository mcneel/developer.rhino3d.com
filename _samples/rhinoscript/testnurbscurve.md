---
title: Add a NURBS Curve to Rhino
description: Demonstrates how to add a NURBS curve to Rhino using RhinoScript.
author: dale@mcneel.com
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/sdksamples/testnurbscurve
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

```vbnet
Sub TestNurbsCurve

  Dim degree : degree = 3
  Dim cv_count : cv_count = 6
  Dim knot_count : knot_count = cv_count + degree - 1

  Dim cvs() : ReDim cvs(cv_count - 1)
  cvs(0) = Array(0.0, 0.0, 0.0)
  cvs(1) = Array(5.0, 10.0, 0.0)
  cvs(2) = Array(10.0, 0.0, 0.0)
  cvs(3) = Array(15.0, 10.0, 0.0)
  cvs(4) = Array(20.0, 0.0, 0.0)
  cvs(5) = Array(25.0, 10.0, 0.0)

  Dim knots() : ReDim knots(knot_count - 1)
  knots(0) = 0.0
  knots(1) = 0.0
  knots(2) = 0.0
  knots(3) = 1.0
  knots(4) = 2.0
  knots(5) = 3.0
  knots(6) = 3.0
  knots(7) = 3.0

  Call Rhino.AddNurbsCurve(cvs, knots, degree)

End Sub
```
