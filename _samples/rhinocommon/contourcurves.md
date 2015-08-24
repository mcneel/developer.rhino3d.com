---
layout: code-sample
author:
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
title: Create Contour Curves
keywords: ['create', 'contour', 'curves']
categories: ['Curves']
description:
order: 1
---

```cs
partial class Examples
{
  public static Result ContourCurves(RhinoDoc doc)
  {
    var filter = ObjectType.Surface | ObjectType.PolysrfFilter | ObjectType.Mesh;
    ObjRef[] obj_refs;
    var rc = RhinoGet.GetMultipleObjects("Select objects to contour", false, filter, out obj_refs);
    if (rc != Result.Success)
      return rc;

    var gp = new GetPoint();
    gp.SetCommandPrompt("Contour plane base point");
    gp.Get();
    if (gp.CommandResult() != Result.Success)
      return gp.CommandResult();
    var base_point = gp.Point();

    gp.DrawLineFromPoint(base_point, true);
    gp.SetCommandPrompt("Direction perpendicular to contour planes");
    gp.Get();
    if (gp.CommandResult() != Result.Success)
      return gp.CommandResult();
    var end_point = gp.Point();

    if (base_point.DistanceTo(end_point) < RhinoMath.ZeroTolerance)
      return Result.Nothing;

    double distance = 1.0;
    rc = RhinoGet.GetNumber("Distance between contours", false, ref distance);
    if (rc != Result.Success)
      return rc;

    var interval = Math.Abs(distance);

    Curve[] curves = null;
    foreach (var obj_ref in obj_refs)
    {
      var geometry = obj_ref.Geometry();
      if (geometry == null)
        return Result.Failure;

      if (geometry is Brep)
      {
        curves = Brep.CreateContourCurves(geometry as Brep, base_point, end_point, interval);
      }
      else
      {
        curves = Mesh.CreateContourCurves(geometry as Mesh, base_point, end_point, interval);
      }

      foreach (var curve in curves)
      {
        var curve_object_id = doc.Objects.AddCurve(curve);
        doc.Objects.Select(curve_object_id);
      }
    }

    if (curves != null)
      doc.Views.Redraw();
    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function ContourCurves(ByVal doc As RhinoDoc) As Result
	Dim filter = ObjectType.Surface Or ObjectType.PolysrfFilter Or ObjectType.Mesh
	Dim obj_refs() As ObjRef = Nothing
	Dim rc = RhinoGet.GetMultipleObjects("Select objects to contour", False, filter, obj_refs)
	If rc IsNot Result.Success Then
	  Return rc
	End If

	Dim gp = New GetPoint()
	gp.SetCommandPrompt("Contour plane base point")
	gp.Get()
	If gp.CommandResult() <> Result.Success Then
	  Return gp.CommandResult()
	End If
	Dim base_point = gp.Point()

	gp.DrawLineFromPoint(base_point, True)
	gp.SetCommandPrompt("Direction perpendicular to contour planes")
	gp.Get()
	If gp.CommandResult() <> Result.Success Then
	  Return gp.CommandResult()
	End If
	Dim end_point = gp.Point()

	If base_point.DistanceTo(end_point) < RhinoMath.ZeroTolerance Then
	  Return Result.Nothing
	End If

	Dim distance As Double = 1.0
	rc = RhinoGet.GetNumber("Distance between contours", False, distance)
	If rc IsNot Result.Success Then
	  Return rc
	End If

	Dim interval = Math.Abs(distance)

	Dim curves() As Curve = Nothing
	For Each obj_ref In obj_refs
	  Dim geometry = obj_ref.Geometry()
	  If geometry Is Nothing Then
		Return Result.Failure
	  End If

	  If TypeOf geometry Is Brep Then
		curves = Brep.CreateContourCurves(TryCast(geometry, Brep), base_point, end_point, interval)
	  Else
		curves = Mesh.CreateContourCurves(TryCast(geometry, Mesh), base_point, end_point, interval)
	  End If

	  For Each curve In curves
		Dim curve_object_id = doc.Objects.AddCurve(curve)
		doc.Objects.Select(curve_object_id)
	  Next curve
	Next obj_ref

	If curves IsNot Nothing Then
	  doc.Views.Redraw()
	End If
	Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in .active}

