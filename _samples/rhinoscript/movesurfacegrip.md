---
layout: code-sample-rhinoscript
title: Move Surface Grips
author: dale@mcneel.com
platforms: ['Windows']
apis: ['RhinoScript']
languages: ['VBScript']
keywords: ['rhinoscript', 'vbscript']
categories: ['Uncategorized']
description: Demonstrates how to move a surface's grip objects using RhinoScript.
origin: http://wiki.mcneel.com/developer/scriptsamples/movesurfacegrip
order: 1
---

```vbnet
Option Explicit

' Moves a surface grip
Sub MoveSurfaceGrip

  ' The name of the surface we are going to manipulate
  Dim object_name
  object_name = "Hull"

  ' The distance to move the control point(s)  
  Dim distance
  distance = 0.5

  ' Find the object by object_name
  Dim object_list
  object_list = Rhino.ObjectsByName(object_name)
  If Not IsArray(object_list) Then
    Rhino.Print "Object not found."
    Exit Sub
  End If

  ' In case more than one were found,
  ' use the first on in the array
  Dim object_id
  object_id = object_list(0)

  ' Make sure is really is a surface
  If Not Rhino.IsSurface(object_id) Then
    Rhino.Print "Object is not a surface."
    Exit Sub
  End If

  ' Get all of the selected grips      
  Dim grip_list
  grip_list = Rhino.SelectedObjectGrips(object_id)
  If Not IsArray(grip_list) Then
    Rhino.Print "No grips selected."
    Exit Sub
  End If

  ' Process each grip    
  Dim grip_idx, grip_pt, new_pt, uv
  Dim normal_pts, normal, normal_scaled

  For Each grip_idx In grip_list
    ' Get the grip's location
    grip_pt = Rhino.ObjectGripLocation(object_id, grip_idx)
    ' Find the parameter on the surface closest to the location
    uv = Rhino.SurfaceClosestPoint(object_id, grip_pt)
    ' Find the normal to the parameter
    normal_pts = Rhino.SurfaceNormal(object_id, uv)
    ' Create a vector from the results
    normal = VectorCreate( normal_pts(0), normal_pts(1) )
    ' Scale the vector based on the specified distance
    normal_scaled = VectorScale( normal, distance )
    ' Modify the point location
    new_pt = PointAddVector( grip_pt, normal_scaled )
    ' Update the grip location
    Rhino.ObjectGripLocation object_id, grip_idx, new_pt
  Next

End Sub

' NOTE, V4 contains a number of vector related
' functions. Thus, the following would not be
' necessary if we were scripting in V4.

' Creates a 3D vector from 2- 3D points  
Function VectorCreate(p1, p2)
  VectorCreate = Null
  If Not IsArray(p1) Or (UBound(p1) <> 2) Then Exit Function
  If Not IsArray(p2) Or (UBound(p2) <> 2) Then Exit Function
  VectorCreate =  Array(p2(0) - p1(0), p2(1) - p1(1), p2(2) - p1(2))
End Function

' Scale a 3D vector
Function VectorScale(v, d)
  VectorScale = Null
  If Not IsArray(v) Or (UBound(v) <> 2) Then Exit Function
  If Not IsNumeric(d) Then Exit Function
  VectorScale = Array(v(0) * d, v(1) * d, v(2) * d)
End Function

' Adds a 3D vector to a 3D point
Function PointAddVector(p, v)
  PointAddVector = Null
  If Not IsArray(p) Or (UBound(p) <> 2) Then Exit Function
  If Not IsArray(v) Or (UBound(v) <> 2) Then Exit Function
  PointAddVector = Array(p(0) + v(0), p(1) + v(1), p(2) + v(2))
End Function
```
