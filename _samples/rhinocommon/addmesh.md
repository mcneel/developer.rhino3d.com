---
layout: code-sample
title: Add Mesh
author: 
categories: ['Adding Objects'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['mesh']
order: 15
description:  
---



```cs
public static Rhino.Commands.Result AddMesh(Rhino.RhinoDoc doc)
{
  Rhino.Geometry.Mesh mesh = new Rhino.Geometry.Mesh();
  mesh.Vertices.Add(0.0, 0.0, 1.0); //0
  mesh.Vertices.Add(1.0, 0.0, 1.0); //1
  mesh.Vertices.Add(2.0, 0.0, 1.0); //2
  mesh.Vertices.Add(3.0, 0.0, 0.0); //3
  mesh.Vertices.Add(0.0, 1.0, 1.0); //4
  mesh.Vertices.Add(1.0, 1.0, 2.0); //5
  mesh.Vertices.Add(2.0, 1.0, 1.0); //6
  mesh.Vertices.Add(3.0, 1.0, 0.0); //7
  mesh.Vertices.Add(0.0, 2.0, 1.0); //8
  mesh.Vertices.Add(1.0, 2.0, 1.0); //9
  mesh.Vertices.Add(2.0, 2.0, 1.0); //10
  mesh.Vertices.Add(3.0, 2.0, 1.0); //11

  mesh.Faces.AddFace(0, 1, 5, 4);
  mesh.Faces.AddFace(1, 2, 6, 5);
  mesh.Faces.AddFace(2, 3, 7, 6);
  mesh.Faces.AddFace(4, 5, 9, 8);
  mesh.Faces.AddFace(5, 6, 10, 9);
  mesh.Faces.AddFace(6, 7, 11, 10);
  mesh.Normals.ComputeNormals();
  mesh.Compact();
  if (doc.Objects.AddMesh(mesh) != Guid.Empty)
  {
    doc.Views.Redraw();
    return Rhino.Commands.Result.Success;
  }
  return Rhino.Commands.Result.Failure;
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Public Shared Function AddMesh(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
  Dim mesh As New Rhino.Geometry.Mesh()
  mesh.Vertices.Add(0.0, 0.0, 1.0) '0
  mesh.Vertices.Add(1.0, 0.0, 1.0) '1
  mesh.Vertices.Add(2.0, 0.0, 1.0) '2
  mesh.Vertices.Add(3.0, 0.0, 0.0) '3
  mesh.Vertices.Add(0.0, 1.0, 1.0) '4
  mesh.Vertices.Add(1.0, 1.0, 2.0) '5
  mesh.Vertices.Add(2.0, 1.0, 1.0) '6
  mesh.Vertices.Add(3.0, 1.0, 0.0) '7
  mesh.Vertices.Add(0.0, 2.0, 1.0) '8
  mesh.Vertices.Add(1.0, 2.0, 1.0) '9
  mesh.Vertices.Add(2.0, 2.0, 1.0) '10
  mesh.Vertices.Add(3.0, 2.0, 1.0) '11
  mesh.Faces.AddFace(0, 1, 5, 4)
  mesh.Faces.AddFace(1, 2, 6, 5)
  mesh.Faces.AddFace(2, 3, 7, 6)
  mesh.Faces.AddFace(4, 5, 9, 8)
  mesh.Faces.AddFace(5, 6, 10, 9)
  mesh.Faces.AddFace(6, 7, 11, 10)
  mesh.Normals.ComputeNormals()
  mesh.Compact()
  If doc.Objects.AddMesh(mesh) <> Guid.Empty Then
    doc.Views.Redraw()
    Return Rhino.Commands.Result.Success
  End If
  Return Rhino.Commands.Result.Failure
End Function
```
{: #vb .tab-pane .fade .in}


```python
import Rhino
import scriptcontext
import System.Guid

def AddMesh():
    mesh = Rhino.Geometry.Mesh()
    mesh.Vertices.Add(0.0, 0.0, 1.0) #0
    mesh.Vertices.Add(1.0, 0.0, 1.0) #1
    mesh.Vertices.Add(2.0, 0.0, 1.0) #2
    mesh.Vertices.Add(3.0, 0.0, 0.0) #3
    mesh.Vertices.Add(0.0, 1.0, 1.0) #4
    mesh.Vertices.Add(1.0, 1.0, 2.0) #5
    mesh.Vertices.Add(2.0, 1.0, 1.0) #6
    mesh.Vertices.Add(3.0, 1.0, 0.0) #7
    mesh.Vertices.Add(0.0, 2.0, 1.0) #8
    mesh.Vertices.Add(1.0, 2.0, 1.0) #9
    mesh.Vertices.Add(2.0, 2.0, 1.0) #10
    mesh.Vertices.Add(3.0, 2.0, 1.0) #11
    
    mesh.Faces.AddFace(0, 1, 5, 4)
    mesh.Faces.AddFace(1, 2, 6, 5)
    mesh.Faces.AddFace(2, 3, 7, 6)
    mesh.Faces.AddFace(4, 5, 9, 8)
    mesh.Faces.AddFace(5, 6, 10, 9)
    mesh.Faces.AddFace(6, 7, 11, 10)
    mesh.Normals.ComputeNormals()
    mesh.Compact()
    if scriptcontext.doc.Objects.AddMesh(mesh)!=System.Guid.Empty:
        scriptcontext.doc.Views.Redraw()
        return Rhino.Commands.Result.Success
    return Rhino.Commands.Result.Failure


if __name__=="__main__":
    AddMesh()
```
{: #py .tab-pane .fade .in}


