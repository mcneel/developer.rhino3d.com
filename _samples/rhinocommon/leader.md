---
layout: code-sample
title: Creating a Leader
author: 
categories: ['Other'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['creating', 'leader']
order: 104
description:  
---



```cs
public class LeaderCommand : Command
{
  public override string EnglishName { get { return "csLeader"; } }

  protected override Result RunCommand(RhinoDoc doc, RunMode mode)
  {
    var points = new Point3d[]
    {
      new Point3d(1, 1, 0),
      new Point3d(5, 1, 0),
      new Point3d(5, 5, 0),
      new Point3d(9, 5, 0)
    };

    var xy_plane = Plane.WorldXY;

    var points2d = new List<Point2d>();
    foreach (var point3d in points)
    {
      double x, y;
      if (xy_plane.ClosestParameter(point3d, out x, out y))
      {
        var point2d = new Point2d(x, y);
        if (points2d.Count < 1 || point2d.DistanceTo(points2d.Last<Point2d>()) > RhinoMath.SqrtEpsilon)
          points2d.Add(point2d);
      }
    }

    doc.Objects.AddLeader(xy_plane, points2d);
    doc.Views.Redraw();
    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Public Class LeaderCommand
  Inherits Command
  Public Overrides ReadOnly Property EnglishName() As String
    Get
      Return "vbLeader"
    End Get
  End Property

  Protected Overrides Function RunCommand(doc As RhinoDoc, mode As RunMode) As Result
    Dim points = New List(Of Point3d)() From { _
      New Point3d(1, 1, 0), _
      New Point3d(5, 1, 0), _
      New Point3d(5, 5, 0), _
      New Point3d(9, 5, 0) _
    }

    Dim xyPlane = Plane.WorldXY

    Dim points2d = New List(Of Point2d)()
    For Each point3d As Point3d In points
      Dim x As Double, y As Double
      If xyPlane.ClosestParameter(point3d, x, y) Then
        Dim point2d = New Point2d(x, y)
        If points2d.Count < 1 OrElse point2d.DistanceTo(points2d.Last()) > RhinoMath.SqrtEpsilon Then
          points2d.Add(point2d)
        End If
      End If
    Next

    doc.Objects.AddLeader(xyPlane, points2d)
    doc.Views.Redraw()
    Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
import rhinoscriptsyntax as rs

def RunCommand():
  points = [(1,1,0), (5,1,0), (5,5,0), (9,5,0)]
  rs.AddLeader(points)

if __name__ == "__main__":
    RunCommand()
```
{: #py .tab-pane .fade .in}


