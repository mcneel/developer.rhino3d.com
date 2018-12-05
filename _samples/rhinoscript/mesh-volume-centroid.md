---
title: Mesh Volume Centroid
description: Demonstrates how to calculate the volume centroid of a mesh.
authors: ['dale_fugier']
sdk: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/scriptsamples/meshvolumecentroid
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

```vbnet
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' MeshVolumeCentroid.rvb -- July 2009
' Mary Fugier, Robert McNeel & Associates
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Option Explicit

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Calculates the volume centroid of a mesh object.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub MeshVolumeCentroid()

  Const RHINO_MESH = 32
  Dim strObject, arrCentroid

  strObject = Rhino.GetObject("Select mesh for volume centroid calculation", RHINO_MESH)
  If Not IsNull(strObject) Then
    arrCentroid = Rhino.MeshVolumeCentroid(strObject)
    If IsArray(arrCentroid) Then
      Call Rhino.AddPoint(arrCentroid)
      Call Rhino.Print("Volume Centroid = " & Rhino.Pt2Str(arrCentroid))
    End If
  End If

End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' If dragged and dropped on Rhino, a "MeshVolumeCentroid" alias
' will be created.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Rhino.AddStartupScript Rhino.LastLoadedScriptFile
Rhino.AddAlias "MeshVolumeCentroid", "_NoEcho _-RunScript (MeshVolumeCentroid)"
```
