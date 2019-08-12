---
title: Furthest Z on Surface given X Y
description: Demonstrates how to determine the furthest Z on surface given the X Y coordinates.
authors: ['steve_baer']
sdk: ['RhinoCommon']
languages: ['C#', 'Python', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/rhinocommonsamples/elevation
order: 1
keywords: ['determine', 'furthest', 'surface', 'given']
layout: code-sample-rhinocommon
---

```cs
partial class Examples
{
  public static Result FurthestZOnSurfaceGivenXY(RhinoDoc doc)
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

  private static double? MaxZIntersectionMethod(Brep brep, double x, double y, double tolerance)
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
Partial Friend Class Examples
  Public Shared Function FurthestZOnSurfaceGivenXY(ByVal doc As RhinoDoc) As Result
'	#Region "user input"
	' select a surface
	Dim gs = New GetObject()
	gs.SetCommandPrompt("select surface")
	gs.GeometryFilter = ObjectType.Surface
	gs.DisablePreSelect()
	gs.SubObjectSelect = False
	gs.Get()
	If gs.CommandResult() <> Result.Success Then
	  Return gs.CommandResult()
	End If
	' get the brep
	Dim brep = gs.Object(0).Brep()
	If brep Is Nothing Then
	  Return Result.Failure
	End If

	' get X and Y
	Dim x As Double = 0.0, y As Double = 0.0
	Dim rc = RhinoGet.GetNumber("value of X coordinate", True, x)
	If rc IsNot Result.Success Then
	  Return rc
	End If
	rc = RhinoGet.GetNumber("value of Y coordinate", True, y)
	If rc IsNot Result.Success Then
	  Return rc
	End If
'	#End Region

	' an earlier version of this sample used a curve-brep intersection to find Z
	'var maxZ = maxZIntersectionMethod(brep, x, y, doc.ModelAbsoluteTolerance);

	' projecting points is another way to find Z
	Dim max_z = MaxZProjectionMethod(brep, x, y, doc.ModelAbsoluteTolerance)

	If max_z IsNot Nothing Then
	  RhinoApp.WriteLine("Maximum surface Z coordinate at X={0}, Y={1} is {2}", x, y, max_z)
	  doc.Objects.AddPoint(New Point3d(x, y, max_z.Value))
	  doc.Views.Redraw()
	Else
	  RhinoApp.WriteLine("no maximum surface Z coordinate at X={0}, Y={1} found.", x, y)
	End If

	Return Result.Success
  End Function

  Private Shared Function MaxZProjectionMethod(ByVal brep As Brep, ByVal x As Double, ByVal y As Double, ByVal tolerance As Double) As Double?
	Dim max_z? As Double = Nothing
	Dim breps = New List(Of Brep) From {brep}
	Dim points = New List(Of Point3d) From {New Point3d(x, y, 0)}
	' grab all the points projected in Z dir.  Aggregate finds furthest Z from XY plane
	Try
	  max_z = (
	      From pt In Intersection.ProjectPointsToBreps(breps, points, New Vector3d(0, 0, 1), tolerance)
	      Select pt.Z).Aggregate(Function(z1, z2)If(Math.Abs(z1) > Math.Abs(z2), z1, z2))
			  ' Here you might be tempted to use .Max() to get the largest Z value but that doesn't work because
			  ' Z might be negative.  This custom aggregate returns the max Z independant of the sign.  If it had a name
			  ' it could be MaxAbs()
	Catch e1 As InvalidOperationException 'Sequence contains no elements
	End Try
	Return max_z
  End Function

  Private Shared Function MaxZIntersectionMethod(ByVal brep As Brep, ByVal x As Double, ByVal y As Double, ByVal tolerance As Double) As Double?
	Dim max_z? As Double = Nothing

	Dim bbox = brep.GetBoundingBox(True)
	Dim max_dist_from_xy = (
	    From corner In bbox.GetCorners()
	    Select corner.Z).Aggregate(Function(z1, z2)If(Math.Abs(z1) > Math.Abs(z2), z1, z2))
							' furthest Z from XY plane.
							' Here you might be tempted to use .Max() to get the largest Z value but that doesn't work because
							' Z might be negative.  This custom aggregate returns the max Z independant of the sign.  If it had a name
							' it could be MaxAbs()
	' multiply distance by 2 to make sure line intersects completely
	Dim line_curve = New LineCurve(New Point3d(x, y, 0), New Point3d(x, y, max_dist_from_xy*2))

	Dim overlap_curves() As Curve = Nothing
	Dim inter_points() As Point3d = Nothing
	If Intersection.CurveBrep(line_curve, brep, tolerance, overlap_curves, inter_points) Then
	  If overlap_curves.Length > 0 OrElse inter_points.Length > 0 Then
		' grab all the points resulting frem the intersection.
		'    1st set: points from overlapping curves,
		'    2nd set: points when there was no overlap
		'    .Aggregate: furthest Z from XY plane.
		max_z = (
		    From c In overlap_curves
		    Select If(Math.Abs(c.PointAtEnd.Z) > Math.Abs(c.PointAtStart.Z), c.PointAtEnd.Z, c.PointAtStart.Z)).Union(
		    From p In inter_points
		    Select p.Z).Aggregate(Function(z1, z2)If(Math.Abs(z1) > Math.Abs(z2), z1, z2))
				 ' Here you might be tempted to use .Max() to get the largest Z value but that doesn't work because
				 ' Z might be negative.  This custom aggregate returns the max Z independant of the sign.  If it had a name
				 ' it could be MaxAbs()
	  End If
	End If
	Return max_z
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

    pts = [(abs(point.Z), point.Z) for point in Intersect.Intersection.ProjectPointsToBreps([brep], [Point3d(x, y, 0)], Vector3d(0, 0, 1), doc.ModelAbsoluteTolerance)]

    pts.sort(reverse=True)

    if pts == []:
        print "no Z for given X, Y"
    else:
        rs.AddPoint(Point3d(x, y, pts[0][1]))

if __name__ == "__main__":
    RunCommand()
```
{: #py .tab-pane .fade .in}
