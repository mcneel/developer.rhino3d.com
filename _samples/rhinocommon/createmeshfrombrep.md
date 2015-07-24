---
layout: code-sample
title: Create Meshes from Brep
author: 
categories: ['Other'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['create', 'meshes', 'brep']
order: 43
description:  
---



```cs
public class CreateMeshFromBrepCommand : Command
{
  public override string EnglishName { get { return "csCreateMeshFromBrep"; } }

  protected override Result RunCommand(RhinoDoc doc, RunMode mode)
  {
    ObjRef obj_ref;
    var rc = RhinoGet.GetOneObject("Select surface or polysurface to mesh", true, ObjectType.Surface | ObjectType.PolysrfFilter, out obj_ref);
    if (rc != Result.Success)
      return rc;
    var brep = obj_ref.Brep();
    if (null == brep)
      return Result.Failure;

    // you could choose anyone of these for example
    var jagged_and_faster = MeshingParameters.Coarse;
    var smooth_and_slower = MeshingParameters.Smooth;
    var default_mesh_params = MeshingParameters.Default;
    var minimal = MeshingParameters.Minimal;

    var meshes = Mesh.CreateFromBrep(brep, smooth_and_slower);
    if (meshes == null || meshes.Length == 0)
      return Result.Failure;

    var brep_mesh = new Mesh();
    foreach (var mesh in meshes)
      brep_mesh.Append(mesh);
    doc.Objects.AddMesh(brep_mesh);
    doc.Views.Redraw();

    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Public Class CreateMeshFromBrepCommand
  Inherits Command
  Public Overrides ReadOnly Property EnglishName() As String
    Get
      Return "vbCreateMeshFromBrep"
    End Get
  End Property

  Protected Overrides Function RunCommand(doc As RhinoDoc, mode As RunMode) As Result
    Dim objRef As ObjRef = Nothing
    Dim rc = Rhino.Input.RhinoGet.GetOneObject("Select surface or polysurface to mesh", True, ObjectType.Surface Or ObjectType.PolysrfFilter, objRef)
    If rc <> Result.Success Then
      Return rc
    End If
    Dim brep = objRef.Brep()
    If brep Is Nothing Then
      Return Result.Failure
    End If

    ' you could choose any one of these for example
    Dim jaggedAndFaster = MeshingParameters.Coarse
    Dim smoothAndSlower = MeshingParameters.Smooth
    Dim defaultMeshParams = MeshingParameters.Default
    Dim minimal = MeshingParameters.Minimal

    Dim meshes = Mesh.CreateFromBrep(brep, smoothAndSlower)
    If meshes Is Nothing OrElse meshes.Length = 0 Then
      Return Result.Failure
    End If

    Dim brepmesh = New Mesh()
    For Each facemesh As Mesh In meshes
      brepmesh.Append(facemesh)
    Next

    doc.Objects.AddMesh(brepmesh)
    doc.Views.Redraw()
    Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
import Rhino
from Rhino.Geometry import *
from Rhino.Input import RhinoGet
from Rhino.Commands import Result
from Rhino.DocObjects import ObjectType
import rhinoscriptsyntax as rs
from scriptcontext import doc

def RunCommand():
  rc, objRef = RhinoGet.GetOneObject("Select surface or polysurface to mesh", True, 
                                     ObjectType.Surface | ObjectType.PolysrfFilter)
  if rc <> Result.Success:
    return rc
  brep = objRef.Brep()
  if None == brep:
    return Result.Failure

  jaggedAndFaster = MeshingParameters.Coarse
  smoothAndSlower = MeshingParameters.Smooth
  defaultMeshParams = MeshingParameters.Default
  minimal = MeshingParameters.Minimal

  meshes = Mesh.CreateFromBrep(brep, smoothAndSlower)
  if meshes == None or meshes.Length == 0:
    return Result.Failure

  brepMesh = Mesh()
  for mesh in meshes:
    brepMesh.Append(mesh)
  doc.Objects.AddMesh(brepMesh)
  doc.Views.Redraw()

if __name__ == "__main__":
  RunCommand()
```
{: #py .tab-pane .fade .in}


