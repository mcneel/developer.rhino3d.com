+++
aliases = ["/en/5/samples/rhinocommon/curve-surface-intersection/", "/en/6/samples/rhinocommon/curve-surface-intersection/", "/en/7/samples/rhinocommon/curve-surface-intersection/", "/wip/samples/rhinocommon/curve-surface-intersection/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to calculate the intersection points of a user-specified Brep and a curve."
keywords = [ "curve-surface", "intersection" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Curve Surface Intersection"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/curvesurfaceintersect"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

+++

<div class="codetab-content" id="cs">

```cs
partial class Examples
{
  public static Result CurveSurfaceIntersect(RhinoDoc doc)
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

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function CurveSurfaceIntersect(ByVal doc As RhinoDoc) As Result
	Dim gs = New GetObject()
	gs.SetCommandPrompt("select brep")
	gs.GeometryFilter = ObjectType.Brep
	gs.DisablePreSelect()
	gs.SubObjectSelect = False
	gs.Get()
	If gs.CommandResult() <> Result.Success Then
	  Return gs.CommandResult()
	End If
	Dim brep = gs.Object(0).Brep()

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

	Dim intersection_points() As Point3d = Nothing
	Dim overlap_curves() As Curve = Nothing
	If Not Intersection.CurveBrep(curve, brep, tolerance, overlap_curves, intersection_points) Then
	  RhinoApp.WriteLine("curve brep intersection failed")
	  Return Result.Nothing
	End If

	For Each overlap_curve In overlap_curves
	  doc.Objects.AddCurve(overlap_curve)
	Next overlap_curve
	For Each intersection_point In intersection_points
	  doc.Objects.AddPoint(intersection_point)
	Next intersection_point

	RhinoApp.WriteLine("{0} overlap curves, and {1} intersection points", overlap_curves.Length, intersection_points.Length)
	doc.Views.Redraw()

	Return Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

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

</div>
