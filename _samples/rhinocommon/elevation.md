---
layout: code-sample
title: Furthest Z value on Surface for Given X,Y
author: 
categories: ['Other'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['furthest', 'value', 'surface', 'given']
order: 74
description:  
---



```cs
public class FurthestZOnSurfaceCommand : Command
{
  public override string EnglishName { get { return "csFurthestZOnSurfaceGivenXY"; } }

  protected override Result RunCommand(RhinoDoc doc, RunMode mode)
  {
    #region user input
    // select a surface
    var gs = new GetObject();
    gs.SetCommandPrompt("select surface");
    gs.GeometryFilter = ObjectType.Surface;
    gs.DisablePreSelect();
    gs.SubObjectSelect = false;
    gs.Get();
    if (gs.CommandResult() != Result.Success)
      return gs.CommandResult();
    // get the brep
    var brep = gs.Object(0).Brep();
    if (brep == null)
      return Result.Failure;

    // get X and Y
    double x = 0.0, y = 0.0;
    var rc = RhinoGet.GetNumber("value of X coordinate", true, ref x);
    if (rc != Result.Success)
      return rc;
    rc = RhinoGet.GetNumber("value of Y coordinate", true, ref y);
    if (rc != Result.Success)
      return rc;
    #endregion
    
    // an earlier version of this sample used a curve-brep intersection to find Z
    //var maxZ = maxZIntersectionMethod(brep, x, y, doc.ModelAbsoluteTolerance);

    // projecting points is another way to find Z
    var max_z = MaxZProjectionMethod(brep, x, y, doc.ModelAbsoluteTolerance);

    if (max_z != null)
    {
      RhinoApp.WriteLine("Maximum surface Z coordinate at X={0}, Y={1} is {2}", x, y, max_z);
      doc.Objects.AddPoint(new Point3d(x, y, max_z.Value));
      doc.Views.Redraw();
    }
    else
      RhinoApp.WriteLine("no maximum surface Z coordinate at X={0}, Y={1} found.", x, y);

    return Result.Success;
  }

  private static double? MaxZProjectionMethod(Brep brep, double x, double y, double tolerance)
  {
    double? max_z = null;
    var breps = new List<Brep> {brep};
    var points = new List<Point3d> {new Point3d(x, y, 0)};
    // grab all the points projected in Z dir.  Aggregate finds furthest Z from XY plane
    try {
      max_z = (from pt in Intersection.ProjectPointsToBreps(breps, points, new Vector3d(0, 0, 1), tolerance) select pt.Z)
              // Here you might be tempted to use .Max() to get the largest Z value but that doesn't work because
              // Z might be negative.  This custom aggregate returns the max Z independant of the sign.  If it had a name
              // it could be MaxAbs()
              .Aggregate((z1, z2) => Math.Abs(z1) > Math.Abs(z2) ? z1 : z2);
    } catch (InvalidOperationException) {/*Sequence contains no elements*/}
    return max_z;
  }

  private double? MaxZIntersectionMethod(Brep brep, double x, double y, double tolerance)
  {
    double? max_z = null;

    var bbox = brep.GetBoundingBox(true);
    var max_dist_from_xy = (from corner in bbox.GetCorners() select corner.Z)
                            // furthest Z from XY plane.
                            // Here you might be tempted to use .Max() to get the largest Z value but that doesn't work because
                            // Z might be negative.  This custom aggregate returns the max Z independant of the sign.  If it had a name
                            // it could be MaxAbs()
                            .Aggregate((z1, z2) => Math.Abs(z1) > Math.Abs(z2) ? z1 : z2);
    // multiply distance by 2 to make sure line intersects completely
    var line_curve = new LineCurve(new Point3d(x, y, 0), new Point3d(x, y, max_dist_from_xy*2));

    Curve[] overlap_curves;
    Point3d[] inter_points;
    if (Intersection.CurveBrep(line_curve, brep, tolerance, out overlap_curves, out inter_points))
    {
      if (overlap_curves.Length > 0 || inter_points.Length > 0)
      {
        // grab all the points resulting frem the intersection. 
        //    1st set: points from overlapping curves, 
        //    2nd set: points when there was no overlap
        //    .Aggregate: furthest Z from XY plane.
        max_z = (from c in overlap_curves select Math.Abs(c.PointAtEnd.Z) > Math.Abs(c.PointAtStart.Z) ? c.PointAtEnd.Z : c.PointAtStart.Z)
                .Union
                (from p in inter_points select p.Z)
                 // Here you might be tempted to use .Max() to get the largest Z value but that doesn't work because
                 // Z might be negative.  This custom aggregate returns the max Z independant of the sign.  If it had a name
                 // it could be MaxAbs()
                .Aggregate((z1, z2) => Math.Abs(z1) > Math.Abs(z2) ? z1 : z2);
      }
    }
    return max_z;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Public Class FurthestZOnSurfaceCommand
  Inherits Command
  Public Overrides ReadOnly Property EnglishName() As String
    Get
      Return "vbFurthestZOnSurfaceGivenXY"
    End Get
  End Property

  Protected Overrides Function RunCommand(doc As RhinoDoc, mode As RunMode) As Result
    '#Region "user input"
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
    ' get the brep
    Dim brep = gs.[Object](0).Brep()
    If brep Is Nothing Then
      Return Result.Failure
    End If

    ' get X and Y
    Dim x As Double = 0.0, y As Double = 0.0
    Dim rc = RhinoGet.GetNumber("value of X coordinate", True, x)
    If rc <> Result.Success Then
      Return rc
    End If
    rc = RhinoGet.GetNumber("value of Y coordinate", True, y)
    If rc <> Result.Success Then
      Return rc
    End If
    '#End Region

    ' an earlier version of this sample used a curve-brep intersection to find Z
    'var maxZ = MaxZIntersectionMethod(brep, x, y, doc.ModelAbsoluteTolerance);

    ' projecting points is another way to find Z
    Dim maxZ = MaxZProjectionMethod(brep, x, y, doc.ModelAbsoluteTolerance)

    If maxZ IsNot Nothing Then
      RhinoApp.WriteLine("Maximum surface Z coordinate at X={0}, Y={1} is {2}", x, y, maxZ)
      doc.Objects.AddPoint(New Point3d(x, y, maxZ.Value))
      doc.Views.Redraw()
    Else
      RhinoApp.WriteLine("no maximum surface Z coordinate at X={0}, Y={1} found.", x, y)
    End If

    Return Result.Success
  End Function

  Private Function MaxZProjectionMethod(brep As Brep, x As Double, y As Double, tolerance As Double) As System.Nullable(Of Double)
    Dim maxZ As System.Nullable(Of Double) = Nothing
    Dim breps = New List(Of Brep)() From { _
      brep _
    }
    Dim points = New List(Of Point3d)() From { _
      New Point3d(x, y, 0) _
    }
    ' grab all the points projected in Z dir.  Aggregate finds furthest Z from XY plane
    Try
      maxZ = (From pt In Intersection.ProjectPointsToBreps(breps, points, New Vector3d(0, 0, 1), tolerance) Select pt.Z).Aggregate(Function(z1, z2) If(Math.Abs(z1) > Math.Abs(z2), z1, z2))
      'Sequence contains no elements
    Catch generatedExceptionName As InvalidOperationException
    End Try
    Return maxZ
  End Function

  Private Function MaxZIntersectionMethod(brep As Brep, x As Double, y As Double, tolerance As Double) As System.Nullable(Of Double)
    Dim maxZ As System.Nullable(Of Double) = Nothing

    Dim bbox = brep.GetBoundingBox(True)
    ' furthest Z from XY plane.  Max() doesn't work because of possible negative Z values
    Dim maxDistFromXY = (From corner In bbox.GetCorners() Select corner.Z).Aggregate(Function(z1, z2) If(Math.Abs(z1) > Math.Abs(z2), z1, z2))
    ' multiply distance by 2 to make sure line intersects completely
    Dim lineCurve = New LineCurve(New Point3d(x, y, 0), New Point3d(x, y, maxDistFromXY * 2))

    Dim overlapCurves As Curve() = Nothing
    Dim interPoints As Point3d() = Nothing
    If Intersection.CurveBrep(lineCurve, brep, tolerance, overlapCurves, interPoints) Then
      If overlapCurves.Length > 0 OrElse interPoints.Length > 0 Then
        ' grab all the points resulting frem the intersection. 
        '    1st set: points from overlapping curves, 
        '    2nd set: points when there was no overlap
        '    .Aggregate: furthest Z from XY plane.
        Dim overlapCrvsZs As IEnumerable(Of Double) = (From c In overlapCurves Select DirectCast(IIf(Math.Abs(c.PointAtEnd.Z) > Math.Abs(c.PointAtStart.Z), c.PointAtEnd.Z, c.PointAtStart.Z), Double))
        Dim intersectPtsZs As IEnumerable(Of Double) = (From p In interPoints Select p.Z)
        Dim allZs = overlapCrvsZs.Union(intersectPtsZs).ToArray()
        maxZ = allZs.Aggregate(Function(runZ, nextZ) DirectCast(IIf(Math.Abs(runZ) > Math.Abs(nextZ), runZ, nextZ), Double))
      End If
    End If
    Return maxZ
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
import rhinoscriptsyntax as rs
from Rhino.Geometry import Intersect, Point3d, Vector3d
from scriptcontext import doc

def RunCommand():
  # select a surface
  srfid = rs.GetObject("select serface", rs.filter.surface | rs.filter.polysurface)
  if not srfid: return
  # get the brep
  brep = rs.coercebrep(srfid)
  if not brep: return

  x = rs.GetReal("value of x", 0)
  y = rs.GetReal("value of y", 0)

  pts = [(abs(point.Z), point.Z) for point in Intersect.Intersection.ProjectPointsToBreps(
           [brep], [Point3d(x, y, 0)], Vector3d(0, 0, 1), doc.ModelAbsoluteTolerance)]
           
  pts.sort(reverse=True)
  
  if pts == []:
    print "no Z for given X, Y"
  else:
    rs.AddPoint(Point3d(x, y, pts[0][1]))

if __name__ == "__main__":
  RunCommand()
```
{: #py .tab-pane .fade .in}


