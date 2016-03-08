---
title: Selecting Planar Meshes
description: Demonstrates how to select mesh objects that are planar using RhinoScript.
author: dale@mcneel.com
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Picking and Selection']
origin: http://wiki.mcneel.com/developer/scriptsamples/selplanarmesh
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

```vbnet
Sub SelPlanarMeshes
  Const rhMesh = 32
  Dim arrMeshes, arrVertices, i
  arrMeshes = Rhino.ObjectsByType(rhMesh)
  If IsArray(arrMeshes) Then
    Rhino.EnableRedraw vbFalse
    For i = 0 To UBound(arrMeshes)
      arrVertices = Rhino.MeshVertices(arrMeshes(i))
      If Rhino.PointsAreCoplanar(arrVertices) Then
        Rhino.SelectObject arrMeshes(i)
      End If
    Next
    Rhino.EnableRedraw vbTrue
  End If
End Sub
```
