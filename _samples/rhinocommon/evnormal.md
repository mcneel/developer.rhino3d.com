---
layout: code-sample
title: Determining the Normal Direction of a Brep Face
author: 
categories: ['Other'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['determining', 'normal', 'direction', 'brep', 'face']
order: 75
description:  
---



```cs
public class NormalDirectionOfBrepFaceCommand : Command
{
  public override string EnglishName { get { return "csDetermineNormalDirectionOfBrepFace"; } }

  protected override Result RunCommand(RhinoDoc doc, RunMode mode)
  {
    // select a surface
    var gs = new GetObject();
    gs.SetCommandPrompt("select surface");
    gs.GeometryFilter = ObjectType.Surface;
    gs.DisablePreSelect();
    gs.SubObjectSelect = false;
    gs.Get();
    if (gs.CommandResult() != Result.Success)
      return gs.CommandResult();
    // get the selected face
    var face = gs.Object(0).Face();
    if (face == null)
      return Result.Failure;

    // pick a point on the surface.  Constain
    // picking to the face.
    var gp = new GetPoint();
    gp.SetCommandPrompt("select point on surface");
    gp.Constrain(face, false);
    gp.Get();
    if (gp.CommandResult() != Result.Success)
      return gp.CommandResult();

    // get the parameters of the point on the
    // surface that is clesest to gp.Point()
    double u, v;
    if (face.ClosestPoint(gp.Point(), out u, out v))
    {
      var direction = face.NormalAt(u, v);
      if (face.OrientationIsReversed)
        direction.Reverse();
      RhinoApp.WriteLine(
        string.Format(
          "Surface normal at uv({0:f},{1:f}) = ({2:f},{3:f},{4:f})", 
          u, v, direction.X, direction.Y, direction.Z));
    }
    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Public Class NormalDirectionOfBrepFaceCommand
  Inherits Command
  Public Overrides ReadOnly Property EnglishName() As String
    Get
      Return "vbDetermineNormDirectionOfBrepFace"
    End Get
  End Property

  Protected Overrides Function RunCommand(doc As RhinoDoc, mode As RunMode) As Result
    ' select a surface
    Dim gs = New GetObject()
    gs.SetCommandPrompt("select surface")
    gs.GeometryFilter = ObjectType.Surface
    gs.DisablePreSelect()
    gs.SubObjectSelect = False
    gs.[Get]()
    If gs.CommandResult() <> Result.Success Then
      Return gs.CommandResult()
    End If
    ' get the selected face
    Dim face = gs.[Object](0).Face()
    If face Is Nothing Then
      Return Result.Failure
    End If

    ' pick a point on the surface.  Constain
    ' picking to the face.
    Dim gp = New GetPoint()
    gp.SetCommandPrompt("select point on surface")
    gp.Constrain(face, False)
    gp.[Get]()
    If gp.CommandResult() <> Result.Success Then
      Return gp.CommandResult()
    End If

    ' get the parameters of the point on the
    ' surface that is clesest to gp.Point()
    Dim u As Double, v As Double
    If face.ClosestPoint(gp.Point(), u, v) Then
      Dim direction = face.NormalAt(u, v)
      If face.OrientationIsReversed Then
        direction.Reverse()
      End If
      RhinoApp.WriteLine(String.Format("Surface normal at uv({0:f},{1:f}) = ({2:f},{3:f},{4:f})", u, v, direction.X, direction.Y, direction.Z))
    End If
    Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
import rhinoscriptsyntax as rs
from scriptcontext import *
import Rhino
from Rhino.Commands import Result

def RunCommand():
  # select a surface
  gs = Rhino.Input.Custom.GetObject()
  gs.SetCommandPrompt("select surface")
  gs.GeometryFilter = Rhino.DocObjects.ObjectType.Surface
  gs.DisablePreSelect()
  gs.SubObjectSelect = False
  gs.Get()
  if gs.CommandResult() != Result.Success:
    return gs.CommandResult()

  # get the selected face
  face = gs.Object(0).Face()
  if face == None:
    return

  # pick a point on the surface.  Constain
  # picking to the face.
  gp = Rhino.Input.Custom.GetPoint()
  gp.SetCommandPrompt("select point on surface")
  gp.Constrain(face, False)
  gp.Get()
  if gp.CommandResult() != Result.Success:
    return gp.CommandResult()

  # get the parameters of the point on the
  # surface that is clesest to gp.Point()
  b, u, v = face.ClosestPoint(gp.Point())
  if b:
    dir = face.NormalAt(u, v)
    if face.OrientationIsReversed:
      dir.Reverse()
    print "Surface normal at uv({0:f},{1:f}) = ({2:f},{3:f},{4:f})".format(
        u, v, dir.X, dir.Y, dir.Z)

if __name__ == "__main__":
  RunCommand()
```
{: #py .tab-pane .fade .in}


