---
layout: code-sample
title: Bounding Polyline from Naked Edges of Open Mesh
author: 
categories: ['Other'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['bounding', 'polyline', 'naked', 'edges', 'open', 'mesh']
order: 71
description:  
---



```cs
public class DupMeshBoundaryCommand : Command
{
  public override string EnglishName { get { return "csDupMeshBoundary"; } }

  protected override Result RunCommand(RhinoDoc doc, RunMode mode)
  {
    var gm = new GetObject();
    gm.SetCommandPrompt("Select open mesh");
    gm.GeometryFilter = ObjectType.Mesh;
    gm.GeometryAttributeFilter = GeometryAttributeFilter.OpenMesh;
    gm.Get();
    if (gm.CommandResult() != Result.Success)
      return gm.CommandResult();
    var mesh = gm.Object(0).Mesh();
    if (mesh == null)
      return Result.Failure;

    var polylines = mesh.GetNakedEdges();
    foreach (var polyline in polylines)
    {
      doc.Objects.AddPolyline(polyline);
    }

    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Public Class DupMeshBoundaryCommand
  Inherits Command
  Public Overrides ReadOnly Property EnglishName() As String
    Get
      Return "vbDupMeshBoundary"
    End Get
  End Property

  Protected Overrides Function RunCommand(doc As RhinoDoc, mode As RunMode) As Result
    Dim gm = New GetObject()
    gm.SetCommandPrompt("Select open mesh")
    gm.GeometryFilter = ObjectType.Mesh
    gm.GeometryAttributeFilter = GeometryAttributeFilter.OpenMesh
    gm.[Get]()
    If gm.CommandResult() <> Result.Success Then
      Return gm.CommandResult()
    End If
    Dim mesh = gm.[Object](0).Mesh()
    If mesh Is Nothing Then
      Return Result.Failure
    End If

    Dim polylines = mesh.GetNakedEdges()
    For Each polyline As Polyline In polylines
      doc.Objects.AddPolyline(polyline)
    Next

    Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
from Rhino.Commands import *
from Rhino.Input.Custom import *
from Rhino.DocObjects import *
from scriptcontext import doc

def RunCommand():
  gm = GetObject()
  gm.SetCommandPrompt("Select open mesh")
  gm.GeometryFilter = ObjectType.Mesh
  gm.GeometryAttributeFilter = GeometryAttributeFilter.OpenMesh
  gm.Get()
  if gm.CommandResult() != Result.Success:
    return gm.CommandResult()
  mesh = gm.Object(0).Mesh()
  if mesh == None:
    return Result.Failure

  polylines = mesh.GetNakedEdges()
  for polyline in polylines:
    doc.Objects.AddPolyline(polyline)
  doc.Views.Redraw()
  return Result.Success

if __name__ == "__main__":
    RunCommand()
```
{: #py .tab-pane .fade .in}


