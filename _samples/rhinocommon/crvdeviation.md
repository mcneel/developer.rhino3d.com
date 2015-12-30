---
layout: code-sample-rhinocommon
author:
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
title: Determine the Deviation between two Curves
keywords: ['determine', 'deviation', 'between', 'curves']
categories: ['Curves']
description:
order: 1
---

```cs
class DeviationConduit : Rhino.Display.DisplayConduit
{
  private readonly Curve m_curve_a;
  private readonly Curve m_curve_b;
  private readonly Point3d m_min_dist_point_a ;
  private readonly Point3d m_min_dist_point_b ;
  private readonly Point3d m_max_dist_point_a ;
  private readonly Point3d m_max_dist_point_b ;

  public DeviationConduit(Curve curveA, Curve curveB, Point3d minDistPointA, Point3d minDistPointB, Point3d maxDistPointA, Point3d maxDistPointB)
  {
    m_curve_a = curveA;
    m_curve_b = curveB;
    m_min_dist_point_a = minDistPointA;
    m_min_dist_point_b = minDistPointB;
    m_max_dist_point_a = maxDistPointA;
    m_max_dist_point_b = maxDistPointB;
  }

  protected override void DrawForeground(Rhino.Display.DrawEventArgs e)
  {
    e.Display.DrawCurve(m_curve_a, Color.Red);
    e.Display.DrawCurve(m_curve_b, Color.Red);

    e.Display.DrawPoint(m_min_dist_point_a, Color.LawnGreen);
    e.Display.DrawPoint(m_min_dist_point_b, Color.LawnGreen);
    e.Display.DrawLine(new Line(m_min_dist_point_a, m_min_dist_point_b), Color.LawnGreen);
    e.Display.DrawPoint(m_max_dist_point_a, Color.Red);
    e.Display.DrawPoint(m_max_dist_point_b, Color.Red);
    e.Display.DrawLine(new Line(m_max_dist_point_a, m_max_dist_point_b), Color.Red);
  }
}

partial class Examples
{
  public static Result CrvDeviation(RhinoDoc doc)
  {
    doc.Objects.UnselectAll();

    ObjRef obj_ref1;
    var rc1 = RhinoGet.GetOneObject("first curve", true, ObjectType.Curve, out obj_ref1);
    if (rc1 != Result.Success)
      return rc1;
    Curve curve_a = null;
    if (obj_ref1 != null)
      curve_a = obj_ref1.Curve();
    if (curve_a == null)
      return Result.Failure;

    // Since you already selected a curve if you don't unselect it
    // the next GetOneObject won't stop as it considers that curve 
    // input, i.e., curveA and curveB will point to the same curve.
    // Another option would be to use an instance of Rhino.Input.Custom.GetObject
    // instead of Rhino.Input.RhinoGet as GetObject has a DisablePreSelect() method.
    doc.Objects.UnselectAll();

    ObjRef obj_ref2;
    var rc2 = RhinoGet.GetOneObject("second curve", true, ObjectType.Curve, out obj_ref2);
    if (rc2 != Result.Success)
      return rc2;
    Curve curve_b = null;
    if (obj_ref2 != null)
      curve_b = obj_ref2.Curve();
    if (curve_b == null)
      return Result.Failure;

    var tolerance = doc.ModelAbsoluteTolerance;

    double max_distance;
    double max_distance_parameter_a;
    double max_distance_parameter_b;
    double min_distance;
    double min_distance_parameter_a;
    double min_distance_parameter_b;

    DeviationConduit conduit;
    if (!Curve.GetDistancesBetweenCurves(curve_a, curve_b, tolerance, out max_distance, 
              out max_distance_parameter_a, out max_distance_parameter_b,
              out min_distance, out min_distance_parameter_a, out min_distance_parameter_b))
    {
      RhinoApp.WriteLine("Unable to find overlap intervals.");
      return Result.Success;
    }
    else
    {
      if (min_distance <= RhinoMath.ZeroTolerance)
        min_distance = 0.0;
      var max_dist_pt_a = curve_a.PointAt(max_distance_parameter_a);
      var max_dist_pt_b = curve_b.PointAt(max_distance_parameter_b);
      var min_dist_pt_a = curve_a.PointAt(min_distance_parameter_a);
      var min_dist_pt_b = curve_b.PointAt(min_distance_parameter_b);

      conduit = new DeviationConduit(curve_a, curve_b, min_dist_pt_a, min_dist_pt_b, max_dist_pt_a, max_dist_pt_b) {Enabled = true};
      doc.Views.Redraw();

      RhinoApp.WriteLine("Minimum deviation = {0}   pointA({1}), pointB({2})", min_distance, min_dist_pt_a, min_dist_pt_b);
      RhinoApp.WriteLine("Maximum deviation = {0}   pointA({1}), pointB({2})", max_distance, max_dist_pt_a, max_dist_pt_b);
    }

    var str = "";
    RhinoGet.GetString("Press Enter when done", true, ref str);
    conduit.Enabled = false;

    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function CrvDeviation(ByVal doc As RhinoDoc) As Result
	doc.Objects.UnselectAll()

	Dim obj_ref1 As ObjRef = Nothing
	Dim rc1 = RhinoGet.GetOneObject("first curve", True, ObjectType.Curve, obj_ref1)
	If rc1 IsNot Result.Success Then
	  Return rc1
	End If
	Dim curve_a As Curve = Nothing
	If obj_ref1 IsNot Nothing Then
	  curve_a = obj_ref1.Curve()
	End If
	If curve_a Is Nothing Then
	  Return Result.Failure
	End If

	' Since you already selected a curve if you don't unselect it
	' the next GetOneObject won't stop as it considers that curve 
	' input, i.e., curveA and curveB will point to the same curve.
	' Another option would be to use an instance of Rhino.Input.Custom.GetObject
	' instead of Rhino.Input.RhinoGet as GetObject has a DisablePreSelect() method.
	doc.Objects.UnselectAll()

	Dim obj_ref2 As ObjRef = Nothing
	Dim rc2 = RhinoGet.GetOneObject("second curve", True, ObjectType.Curve, obj_ref2)
	If rc2 IsNot Result.Success Then
	  Return rc2
	End If
	Dim curve_b As Curve = Nothing
	If obj_ref2 IsNot Nothing Then
	  curve_b = obj_ref2.Curve()
	End If
	If curve_b Is Nothing Then
	  Return Result.Failure
	End If

	Dim tolerance = doc.ModelAbsoluteTolerance

	Dim max_distance As Double = Nothing
	Dim max_distance_parameter_a As Double = Nothing
	Dim max_distance_parameter_b As Double = Nothing
	Dim min_distance As Double = Nothing
	Dim min_distance_parameter_a As Double = Nothing
	Dim min_distance_parameter_b As Double = Nothing

	Dim conduit As DeviationConduit
	If Not Curve.GetDistancesBetweenCurves(curve_a, curve_b, tolerance, max_distance, max_distance_parameter_a, max_distance_parameter_b, min_distance, min_distance_parameter_a, min_distance_parameter_b) Then
	  RhinoApp.WriteLine("Unable to find overlap intervals.")
	  Return Result.Success
	Else
	  If min_distance <= RhinoMath.ZeroTolerance Then
		min_distance = 0.0
	  End If
	  Dim max_dist_pt_a = curve_a.PointAt(max_distance_parameter_a)
	  Dim max_dist_pt_b = curve_b.PointAt(max_distance_parameter_b)
	  Dim min_dist_pt_a = curve_a.PointAt(min_distance_parameter_a)
	  Dim min_dist_pt_b = curve_b.PointAt(min_distance_parameter_b)

	  conduit = New DeviationConduit(curve_a, curve_b, min_dist_pt_a, min_dist_pt_b, max_dist_pt_a, max_dist_pt_b) With {.Enabled = True}
	  doc.Views.Redraw()

	  RhinoApp.WriteLine("Minimum deviation = {0}   pointA({1}), pointB({2})", min_distance, min_dist_pt_a, min_dist_pt_b)
	  RhinoApp.WriteLine("Maximum deviation = {0}   pointA({1}), pointB({2})", max_distance, max_dist_pt_a, max_dist_pt_b)
	End If

	Dim str = ""
	RhinoGet.GetString("Press Enter when done", True, str)
	conduit.Enabled = False

	Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
import rhinoscriptsyntax as rs
import scriptcontext
import Rhino

def RunCommand():
  crvA = rs.GetCurveObject("first curve")[0]
  crvA = rs.coercecurve(crvA)
  crvB = rs.GetCurveObject("second curve")[0]
  crvB = rs.coercecurve(crvB)
  if crvA == None or crvB == None:
      return Rhino.Commands.Result.Failure

  maxa, maxb, maxd, mina, minb, mind = rs.CurveDeviation(crvA, crvB)

  if mind <= Rhino.RhinoMath.ZeroTolerance:
      mind = 0.0;
  maxDistPtA = crvA.PointAt(maxa)
  maxDistPtB = crvB.PointAt(maxb)
  minDistPtA = crvA.PointAt(mina)
  minDistPtB = crvB.PointAt(minb)

  print "Minimum deviation = {0}   pointA({1}, {2}, {3}), pointB({4}, {5}, {6})".format(
    mind, minDistPtA.X, minDistPtA.Y, minDistPtA.Z, minDistPtB.X, minDistPtB.Y, minDistPtB.Z)
  print "Maximum deviation = {0}   pointA({1}, {2}, {3}), pointB({4}, {5}, {6})".format(
    maxd, maxDistPtA.X, maxDistPtA.Y, maxDistPtA.Z, maxDistPtB.X, maxDistPtB.Y, maxDistPtB.Z)

if __name__=="__main__":
  RunCommand()
```
{: #py .tab-pane .fade .in}

