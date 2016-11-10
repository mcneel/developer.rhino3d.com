---
title: Create an Icosahedron
description: Demonstrates one way of creating a Icosahedron in RhinoScript.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Adding Objects']
origin: http://wiki.mcneel.com/developer/scriptsamples/icosahedron
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

```vbnet
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Icosahedron.rvb -- September 2009
' If this code works, it was written by Dale Fugier.
' If not, I don't know who wrote it.
' Works with Rhino 4.0.

Option Explicit

' Creates a icosahedron
'   Vertices: 12
'   Edges: 30
'   Faces: 20
'   Edges per face: 3
'   Edges per vertex: 5
'   Sin of angle at edge: 2 / 3
'   Surface area: 5 * sqrt(3) * edgelength^2
'   Volume: 5 * (3 + sqrt(5)) / 12 * edgelength^3
'   Circumscribed radius: sqrt(10 + 2 * sqrt(5)) / 4 * edgelength
'   Inscribed radius: sqrt(42 + 18 * sqrt(5)) / 12 * edgelength
'   Coordinates: a and b, where:
'     a = 1 / 2 and b = 1 / (2 * phi)
'     phi is the golden ratio = (1 + sqrt(5)) / 2
Sub Icosahedron()

  ' Declare local variables
  Dim radius, center
  Dim sqr5, phi, ratio, a, b
  Dim v(11), s(19)

  ' Prompt for center point
  center = Rhino.GetPoint("Center of icosahedral")
  If IsNull(center) Then Exit Sub

  ' Prompt for radius  
  radius = Rhino.GetDistance(center, 1.0, "Radius")
  If IsNull(radius) Then Exit Sub

  ' This will make the script run faster  
  Call Rhino.EnableRedraw(False)

  ' Phi - the square root of 5 plus 1 divided by 2
  sqr5 = Sqr(5.0)
  phi = (1.0 + Sqr5) * 0.5
  ' Golden ratio - the ratio of edgelength to radius
  ratio = Sqr(10.0 + (2.0 * sqr5)) / (4.0 * phi)
  a = (radius / ratio) * 0.5
  b = (radius / ratio) / (2.0 * phi)

  ' Define the icosahedron's 12 vertices
  v(0)  = Rhino.PointAdd(center, Array( 0,  b, -a))
  v(1)  = Rhino.PointAdd(center, Array( b,  a,  0))
  v(2)  = Rhino.PointAdd(center, Array(-b,  a,  0))
  v(3)  = Rhino.PointAdd(center, Array( 0,  b,  a))
  v(4)  = Rhino.PointAdd(center, Array( 0, -b,  a))
  v(5)  = Rhino.PointAdd(center, Array(-a,  0,  b))
  v(6)  = Rhino.PointAdd(center, Array( 0, -b, -a))
  v(7)  = Rhino.PointAdd(center, Array( a,  0, -b))
  v(8)  = Rhino.PointAdd(center, Array( a,  0,  b))
  v(9)  = Rhino.PointAdd(center, Array(-a,  0, -b))
  v(10) = Rhino.PointAdd(center, Array( b, -a,  0))
  v(11) = Rhino.PointAdd(center, Array(-b, -a,  0))

  ' Create the icosahedron's 20 triangular faces
  s(0)  = Rhino.AddSrfPt(Array(v(0), v(1), v(2)))
  s(1)  = Rhino.AddSrfPt(Array(v(3), v(2), v(1)))
  s(2)  = Rhino.AddSrfPt(Array(v(3), v(4), v(5)))
  s(3)  = Rhino.AddSrfPt(Array(v(3), v(8), v(4)))
  s(4)  = Rhino.AddSrfPt(Array(v(0), v(6), v(7)))
  s(5)  = Rhino.AddSrfPt(Array(v(0), v(9), v(6)))
  s(6)  = Rhino.AddSrfPt(Array(v(4), v(10), v(11)))
  s(7)  = Rhino.AddSrfPt(Array(v(6), v(11), v(10)))
  s(8)  = Rhino.AddSrfPt(Array(v(2), v(5), v(9)))
  s(9)  = Rhino.AddSrfPt(Array(v(11), v(9), v(5)))
  s(10) = Rhino.AddSrfPt(Array(v(1), v(7), v(8)))
  s(11) = Rhino.AddSrfPt(Array(v(10), v(8), v(7)))
  s(12) = Rhino.AddSrfPt(Array(v(3), v(5), v(2)))
  s(13) = Rhino.AddSrfPt(Array(v(3), v(1), v(8)))
  s(14) = Rhino.AddSrfPt(Array(v(0), v(2), v(9)))
  s(15) = Rhino.AddSrfPt(Array(v(0), v(7), v(1)))
  s(16) = Rhino.AddSrfPt(Array(v(6), v(9), v(11)))
  s(17) = Rhino.AddSrfPt(Array(v(6), v(10), v(7)))
  s(18) = Rhino.AddSrfPt(Array(v(4), v(11), v(5)))
  s(19) = Rhino.AddSrfPt(Array(v(4), v(8), v(10)))

  ' Join all of the faces
  Rhino.UnselectAllObjects()
  Call Rhino.SelectObjects(s)
  Call Rhino.Command("_Join", False)
  Rhino.UnselectAllObjects()

  ' Don't forget to do this
  Call Rhino.EnableRedraw(True)

End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Rhino.AddStartupScript Rhino.LastLoadedScriptFile
Rhino.AddAlias "Icosahedron", "_NoEcho _-RunScript (Icosahedron)"
```
