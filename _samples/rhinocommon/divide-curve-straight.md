---
title: Divide Curve Straight
description: Demonstrates how to divide a curve using equi-distance points.
authors: ['Steve Baer']
author_contacts: ['stevebaer']
sdk: ['RhinoCommon']
languages: ['C#', 'Python', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Curves']
origin: http://wiki.mcneel.com/developer/rhinocommonsamples/dividecurvestraight
order: 1
keywords: ['divide', 'curve', 'using', 'equi-distance', 'points']
layout: code-sample-rhinocommon
---

```cs
partial class Examples
{
  private static void NextintersectParamAndPoint(Curve[] overlapCurves, Point3d[] intersectPoints,
    Curve curve, out double intersectParam, out Point3d intersectPoint)
  {
    var intersect_params_and_points = new Dictionary<double, Point3d>();
    foreach (var point in intersectPoints)
    {
      double curve_param;
      curve.ClosestPoint(point, out curve_param);
      intersect_params_and_points[curve_param] = point;
    }
    foreach (var overlap_curve in overlapCurves)
    {
      intersect_params_and_points[overlap_curve.Domain.Min] = overlap_curve.PointAt(overlap_curve.Domain.Min);
      intersect_params_and_points[overlap_curve.Domain.Max] = overlap_curve.PointAt(overlap_curve.Domain.Max);
    }
    var min_t = intersect_params_and_points.Keys.Min();
    intersectParam = min_t;
    intersectPoint = intersect_params_and_points[intersectParam];
  }

  public static Result DivideCurveStraight(RhinoDoc doc)
  {
    // user input
    ObjRef[] obj_refs;
    var rc = RhinoGet.GetMultipleObjects("Select curve to divide", false,
      ObjectType.Curve | ObjectType.EdgeFilter, out obj_refs);
    if (rc != Result.Success || obj_refs == null)
      return rc;

    double distance_between_divisions = 5;
    rc = RhinoGet.GetNumber("Distance between divisions", false,
      ref distance_between_divisions, 1.0, Double.MaxValue);
    if (rc != Result.Success)
      return rc;


    // generate the points
    var points = new List<Point3d>();
    foreach (var obj_ref in obj_refs)
    {
      var curve = obj_ref.Curve();
      if (curve == null) return Result.Failure;

      var t0 = curve.Domain.Min;
      points.Add(curve.PointAt(t0));

      var sphere_center = curve.PointAt(t0);
      var t = t0;
      var rest_of_curve = curve;
      while (true)
      {
        var sphere = new Sphere(sphere_center, distance_between_divisions);
        Curve[] overlap_curves;
        Point3d[] intersect_points;
        var b = Intersection.CurveBrep(rest_of_curve, sphere.ToBrep(), 0.0,
          out overlap_curves, out intersect_points);
        if (!b || (overlap_curves.Length == 0 && intersect_points.Length == 0))
          break;
        double intersect_param;
        Point3d intersect_point;
        NextintersectParamAndPoint(overlap_curves, intersect_points, rest_of_curve,
          out intersect_param, out intersect_point);
        points.Add(intersect_point);
        t = intersect_param;
        sphere_center = intersect_point;
        rest_of_curve = curve.Split(t)[1];
      }
    }

    foreach (var point in points)
      doc.Objects.AddPoint(point);

    doc.Views.Redraw();
    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Private Shared Sub NextintersectParamAndPoint(ByVal overlapCurves() As Curve, ByVal intersectPoints() As Point3d, ByVal curve As Curve, ByRef intersectParam As Double, ByRef intersectPoint As Point3d)
	Dim intersect_params_and_points = New Dictionary(Of Double, Point3d)()
	For Each point In intersectPoints
	  Dim curve_param As Double = Nothing
	  curve.ClosestPoint(point, curve_param)
	  intersect_params_and_points(curve_param) = point
	Next point
	For Each overlap_curve In overlapCurves
	  intersect_params_and_points(overlap_curve.Domain.Min) = overlap_curve.PointAt(overlap_curve.Domain.Min)
	  intersect_params_and_points(overlap_curve.Domain.Max) = overlap_curve.PointAt(overlap_curve.Domain.Max)
	Next overlap_curve
	Dim min_t = intersect_params_and_points.Keys.Min()
	intersectParam = min_t
	intersectPoint = intersect_params_and_points(intersectParam)
  End Sub

  Public Shared Function DivideCurveStraight(ByVal doc As RhinoDoc) As Result
	' user input
	Dim obj_refs() As ObjRef = Nothing
	Dim rc = RhinoGet.GetMultipleObjects("Select curve to divide", False, ObjectType.Curve Or ObjectType.EdgeFilter, obj_refs)
	If rc IsNot Result.Success OrElse obj_refs Is Nothing Then
	  Return rc
	End If

	Dim distance_between_divisions As Double = 5
	rc = RhinoGet.GetNumber("Distance between divisions", False, distance_between_divisions, 1.0, Double.MaxValue)
	If rc IsNot Result.Success Then
	  Return rc
	End If


	' generate the points
	Dim points = New List(Of Point3d)()
	For Each obj_ref In obj_refs
	  Dim curve = obj_ref.Curve()
	  If curve Is Nothing Then
		  Return Result.Failure
	  End If

	  Dim t0 = curve.Domain.Min
	  points.Add(curve.PointAt(t0))

	  Dim sphere_center = curve.PointAt(t0)
	  Dim t = t0
	  Dim rest_of_curve = curve
	  Do
		Dim sphere = New Sphere(sphere_center, distance_between_divisions)
		Dim overlap_curves() As Curve = Nothing
		Dim intersect_points() As Point3d = Nothing
		Dim b = Intersection.CurveBrep(rest_of_curve, sphere.ToBrep(), 0.0, overlap_curves, intersect_points)
		If Not b OrElse (overlap_curves.Length = 0 AndAlso intersect_points.Length = 0) Then
		  Exit Do
		End If
		Dim intersect_param As Double = Nothing
		Dim intersect_point As Point3d = Nothing
		NextintersectParamAndPoint(overlap_curves, intersect_points, rest_of_curve, intersect_param, intersect_point)
		points.Add(intersect_point)
		t = intersect_param
		sphere_center = intersect_point
		rest_of_curve = curve.Split(t)(1)
	  Loop
	Next obj_ref

	For Each point In points
	  doc.Objects.AddPoint(point)
	Next point

	doc.Views.Redraw()
	Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
import rhinoscriptsyntax as rs
import Rhino
from Rhino.Input import *
from Rhino.DocObjects import *
from Rhino.Commands import *
from Rhino.Geometry import *
from Rhino.Geometry.Intersect import *

def nextIntersectParamAndPoint(overlapCurves, intersectPoints, curve):
    intersectParamsAndPoints = [(curve.ClosestPoint(point)[1], point)
                                for point in intersectPoints]
    for overlapCurve in overlapCurves:
        intersectParamsAndPoints.append(
          (overlapCurve.Domain.Min, overlapCurve.PointAt(overlapCurve.Domain.Min)))
        intersectParamsandPoints.append(
          (overlapCurve.Domain.Max, overlapCurve.PointAt(overlapCurve.Domain.max)))
    return min(intersectParamsAndPoints, key =  lambda t: t[0])

def divide_curve():
    # get user input
    res, obj_refs = RhinoGet.GetMultipleObjects("Curves to divide",
        False, ObjectType.EdgeFilter | ObjectType.Curve)
    if res <> Result.Success: return res
    curves = [obj_ref.Curve() for obj_ref in obj_refs]

    distance_between_divisions = rs.GetReal(
      message = "Distance between divisions",
      number = 5.0, minimum = 1.0)
    if distance_between_divisions == None: return

    # generate the points
    points = []
    for curve in curves:
      t0 = curve.Domain.Min
      points.append(curve.PointAt(t0))

      sphere_center = curve.PointAt(t0)
      t = t0
      rest_of_curve = curve
      while True:
        sphere = Sphere(sphere_center, distance_between_divisions)
        b, overlapCurves, intersectPoints = Intersection.CurveBrep(
                               rest_of_curve, sphere.ToBrep(), 0.0)
        if b == False or (overlapCurves.Length == 0 and intersectPoints.Length == 0):
          break
        t, point = nextIntersectParamAndPoint(
          overlapCurves, intersectPoints, rest_of_curve)
        points.append(point)
        sphere_center = point
        rest_of_curve = curve.Split(t)[1]

    rs.AddPoints(points)
    rs.Redraw()

if __name__ == "__main__":
    divide_curve()
```
{: #py .tab-pane .fade .in}
