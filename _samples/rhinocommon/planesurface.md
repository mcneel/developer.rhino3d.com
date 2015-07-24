---
layout: code-sample
title: Create a Plane Surface
author: 
categories: ['Other'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['create', 'plane', 'surface']
order: 131
description:  
---



```cs
public class PlaneSurfaceCommand : Command
{
  public override string EnglishName { get { return "csPlaneSurface"; } }

  protected override Result RunCommand(RhinoDoc doc, RunMode mode)
  {
    Point3d[] corners;
    var rc = Rhino.Input.RhinoGet.GetRectangle(out corners);
    if (rc != Result.Success)
      return rc;

    var plane = new Plane(corners[0], corners[1], corners[2]);

    var plane_surface = new PlaneSurface(plane, 
      new Interval(0, corners[0].DistanceTo(corners[1])), 
      new Interval(0, corners[1].DistanceTo(corners[2])));

    doc.Objects.Add(plane_surface);
    doc.Views.Redraw();
    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Public Class PlaneSurfaceCommand
  Inherits Command
  Public Overrides ReadOnly Property EnglishName() As String
    Get
      Return "vbPlaneSurface"
    End Get
  End Property

  Protected Overrides Function RunCommand(doc As RhinoDoc, mode As RunMode) As Result
    Dim corners As Point3d() = Nothing
    Dim rc = Input.RhinoGet.GetRectangle(corners)
    If rc <> Result.Success Then
      Return rc
    End If

    Dim plane = New Plane(corners(0), corners(1), corners(2))
    Dim plane_surface = New PlaneSurface(plane, New Interval(0, corners(0).DistanceTo(corners(1))), New Interval(0, corners(1).DistanceTo(corners(2))))
    doc.Objects.Add(plane_surface)
    doc.Views.Redraw()
    Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
import Rhino;
import rhinoscriptsyntax as rs

def RunCommand():
  rc, corners = Rhino.Input.RhinoGet.GetRectangle()
  if rc <> Rhino.Commands.Result.Success:
      return rc

  plane = Rhino.Geometry.Plane(corners[0], corners[1], corners[2])
  u_dir = rs.Distance(corners[0], corners[1])
  v_dir = rs.Distance(corners[1], corners[2])
  rs.AddPlaneSurface(plane, u_dir, v_dir)

if __name__ == "__main__":
    RunCommand()
```
{: #py .tab-pane .fade .in}


