---
layout: code-sample
title: Curve-Surface Intersection
author: 
categories: ['Curves'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['curve-surface', 'intersection']
order: 51
description:  
---



```cs
public class CurveSurfaceIntersectCommand : Command
{
  public override string EnglishName { get { return "csCurveSurfaceIntersect"; } }

  protected override Result RunCommand(RhinoDoc doc, RunMode mode)
  {
    var gs = new GetObject();
    gs.SetCommandPrompt("select brep");
    gs.GeometryFilter = ObjectType.Brep;
    gs.DisablePreSelect();
    gs.SubObjectSelect = false;
    gs.Get();
    if (gs.CommandResult() != Result.Success)
      return gs.CommandResult();
    var brep = gs.Object(0).Brep();

    var gc = new GetObject();
    gc.SetCommandPrompt("select curve");
    gc.GeometryFilter = ObjectType.Curve;
    gc.DisablePreSelect();
    gc.SubObjectSelect = false;
    gc.Get();
    if (gc.CommandResult() != Result.Success)
      return gc.CommandResult();
    var curve = gc.Object(0).Curve();

    if (brep == null || curve == null)
      return Result.Failure;

    var tolerance = doc.ModelAbsoluteTolerance;

    Point3d[] intersection_points;
    Curve[] overlap_curves;
    if (!Intersection.CurveBrep(curve, brep, tolerance, out overlap_curves, out intersection_points))
    {
      RhinoApp.WriteLine("curve brep intersection failed");
      return Result.Nothing;
    }

    foreach (var overlap_curve in overlap_curves)
      doc.Objects.AddCurve(overlap_curve);
    foreach (var intersection_point in intersection_points)
      doc.Objects.AddPoint(intersection_point);

    RhinoApp.WriteLine("{0} overlap curves, and {1} intersection points", overlap_curves.Length, intersection_points.Length);
    doc.Views.Redraw();

    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Public Class CurveSurfaceIntersectCommand
  Inherits Command
  Public Overrides ReadOnly Property EnglishName() As String
    Get
      Return "vbCurveSurfaceIntersect"
    End Get
  End Property

  Protected Overrides Function RunCommand(doc As RhinoDoc, mode As RunMode) As Result
    Dim gs = New GetObject()
    gs.SetCommandPrompt("select brep")
    gs.GeometryFilter = ObjectType.Brep
    gs.DisablePreSelect()
    gs.SubObjectSelect = False
    gs.Get()
    If gs.CommandResult() <> Result.Success Then
      Return gs.CommandResult()
    End If
    Dim brep = gs.[Object](0).Brep()

    Dim gc = New GetObject()
    gc.SetCommandPrompt("select curve")
    gc.GeometryFilter = ObjectType.Curve
    gc.DisablePreSelect()
    gc.SubObjectSelect = False
    gc.Get()
    If gc.CommandResult() <> Result.Success Then
      Return gc.CommandResult()
    End If
    Dim curve = gc.Object(0).Curve()

    If brep Is Nothing OrElse curve Is Nothing Then
      Return Result.Failure
    End If

    Dim tolerance = doc.ModelAbsoluteTolerance

    Dim intersectionPoints As Point3d() = Nothing
    Dim overlapCurves As Curve() = Nothing
    If Not Intersection.CurveBrep(curve, brep, tolerance, overlapCurves, intersectionPoints) Then
      RhinoApp.WriteLine("curve brep intersection failed")
      Return Result.Nothing
    End If

    For Each overlapCurve As Curve In overlapCurves
      doc.Objects.AddCurve(overlapCurve)
    Next
    For Each intersectionPoint As Point3d In intersectionPoints
      doc.Objects.AddPoint(intersectionPoint)
    Next

    RhinoApp.WriteLine("{0} overlap curves, and {1} intersection points", overlapCurves.Length, intersectionPoints.Length)
    doc.Views.Redraw()

    Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
import rhinoscriptsyntax as rs
from scriptcontext import *
import Rhino
import System.Collections.Generic as scg
import System as s

def RunCommand():
  srfid = rs.GetObject("select surface", rs.filter.surface | rs.filter.polysurface)
  if not srfid: return
 
  crvid = rs.GetObject("select curve", rs.filter.curve)
  if not crvid: return

  result = rs.CurveBrepIntersect(crvid, srfid)
  if result == None:
    print "no intersection"
    return
  
  curves, points = result
  for curve in curves:
    doc.Objects.AddCurve(rs.coercecurve(curve))
  for point in points:
    rs.AddPoint(point)

  doc.Views.Redraw()

if __name__ == "__main__":
  RunCommand()
```
{: #py .tab-pane .fade .in}


