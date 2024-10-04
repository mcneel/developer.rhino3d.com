+++
aliases = ["/en/5/samples/rhinoscript/exploding-meshes/", "/en/6/samples/rhinoscript/exploding-meshes/", "/en/7/samples/rhinoscript/exploding-meshes/", "/wip/samples/rhinoscript/exploding-meshes/"]
authors = [ "dale" ]
categories = [ "Other" ]
description = "Demonstrates how to explode a mesh into individual faces using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Exploding Meshes"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/explodemesh"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
Option Explicit

Sub ExplodeMesh
  Dim mesh
  mesh = Rhino.GetObject("Select mesh to explode", 32)
  If IsNull(mesh) Then Exit Sub

  Dim faces
  faces = Rhino.MeshFaces(mesh, True)
  If Not IsArray(faces) Then Exit Sub

  Rhino.EnableRedraw False
  Dim i, a, b, c, d, bQuad
  i = 0

  While i <= UBound(faces)
    a = faces(i)
    b = faces(i+1)
    c = faces(i+2)
    d = faces(i+3)
    If c(0)=d(0) And c(1)=d(1) And c(2)=d(2) Then
      Rhino.AddMesh Array(a,b,c,d), Array(Array(0,1,2,2))
    Else
      Rhino.AddMesh Array(a,b,c,d), Array(Array(0,1,2,3))
    End If
    i = i + 4
  Wend

  Rhino.DeleteObject mesh
  Rhino.EnableRedraw True

End Sub
```
