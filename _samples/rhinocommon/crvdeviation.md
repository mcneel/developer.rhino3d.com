---
layout: code-sample
title: Determine the Deviation between two Curves
author: 
categories: ['Curves'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['determine', 'deviation', 'between', 'curves']
order: 46
description:  
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


public class CurveDeviationCommand : Command
{
  public override string EnglishName { get { return "csCurveDeviation"; } }

  protected override Result RunCommand(RhinoDoc doc, RunMode mode)
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
Class DeviationConduit
  Inherits Rhino.Display.DisplayConduit
  Private ReadOnly _curveA As Curve
  Private ReadOnly _curveB As Curve
  Private ReadOnly _minDistPointA As Point3d
  Private ReadOnly _minDistPointB As Point3d
  Private ReadOnly _maxDistPointA As Point3d
  Private ReadOnly _maxDistPointB As Point3d

  Public Sub New(curveA As Curve, curveB As Curve, minDistPointA As Point3d, minDistPointB As Point3d, maxDistPointA As Point3d, maxDistPointB As Point3d)
    _curveA = curveA
    _curveB = curveB
    _minDistPointA = minDistPointA
    _minDistPointB = minDistPointB
    _maxDistPointA = maxDistPointA
    _maxDistPointB = maxDistPointB
  End Sub

  Protected Overrides Sub DrawForeground(e As Rhino.Display.DrawEventArgs)
    e.Display.DrawCurve(_curveA, Color.Red)
    e.Display.DrawCurve(_curveB, Color.Red)

    e.Display.DrawPoint(_minDistPointA, Color.LawnGreen)
    e.Display.DrawPoint(_minDistPointB, Color.LawnGreen)
    e.Display.DrawLine(New Line(_minDistPointA, _minDistPointB), Color.LawnGreen)
    e.Display.DrawPoint(_maxDistPointA, Color.Red)
    e.Display.DrawPoint(_maxDistPointB, Color.Red)
    e.Display.DrawLine(New Line(_maxDistPointA, _maxDistPointB), Color.Red)
  End Sub
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


