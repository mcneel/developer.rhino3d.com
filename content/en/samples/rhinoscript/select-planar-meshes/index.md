+++
aliases = ["/5/samples/rhinoscript/select-planar-meshes/", "/6/samples/rhinoscript/select-planar-meshes/", "/7/samples/rhinoscript/select-planar-meshes/", "/wip/samples/rhinoscript/select-planar-meshes/"]
authors = [ "dale" ]
categories = [ "Picking and Selection" ]
description = "Demonstrates how to select mesh objects that are planar using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Select Planar Meshes"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/selplanarmesh"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

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
