+++
aliases = ["/en/5/samples/rhinocommon/fillet-curves/", "/en/6/samples/rhinocommon/fillet-curves/", "/en/7/samples/rhinocommon/fillet-curves/", "/en/wip/samples/rhinocommon/fillet-curves/"]
authors = [ "steve" ]
categories = [ "Curves" ]
description = "Demonstrates how to fillet two curves by a specified radius."
keywords = [ "fillet", "curves" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Fillet Curves"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/filletcurves"
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
  public static Result FilletCurves(RhinoDoc doc)
  {
    var gc1 = new GetObject();
    gc1.DisablePreSelect();
    gc1.SetCommandPrompt("Select first curve to fillet (close to the end you want to fillet)");
    gc1.GeometryFilter = ObjectType.Curve;
    gc1.GeometryAttributeFilter = GeometryAttributeFilter.OpenCurve;
    gc1.Get();
    if (gc1.CommandResult() != Result.Success)
      return gc1.CommandResult();
    var curve1_obj_ref = gc1.Object(0);
    var curve1 = curve1_obj_ref.Curve();
    if (curve1 == null) return Result.Failure;
    var curve1_point_near_end = curve1_obj_ref.SelectionPoint();
    if (curve1_point_near_end == Point3d.Unset)
      return Result.Failure;

    var gc2 = new GetObject();
    gc2.DisablePreSelect();
    gc2.SetCommandPrompt("Select second curve to fillet (close to the end you want to fillet)");
    gc2.GeometryFilter = ObjectType.Curve;
    gc2.GeometryAttributeFilter = GeometryAttributeFilter.OpenCurve;
    gc2.Get();
    if (gc2.CommandResult() != Result.Success)
      return gc2.CommandResult();
    var curve2_obj_ref = gc2.Object(0);
    var curve2 = curve2_obj_ref.Curve();
    if (curve2 == null) return Result.Failure;
    var curve2_point_near_end = curve2_obj_ref.SelectionPoint();
    if (curve2_point_near_end == Point3d.Unset)
      return Result.Failure;

    double radius = 0;
    var rc = RhinoGet.GetNumber("fillet radius", false, ref radius);
    if (rc != Result.Success) return rc;

    var join = false;
    var trim = true;
    var arc_extension = true;
    var fillet-curves = Curve.CreateFilletCurves(curve1, curve1_point_near_end, curve2, curve2_point_near_end, radius,
      join, trim, arc_extension, doc.ModelAbsoluteTolerance, doc.ModelAngleToleranceDegrees);
    if (fillet-curves == null /*|| fillet-curves.Length != 3*/)
      return Result.Failure;

    foreach(var fillet-curve in fillet-curves)
      doc.Objects.AddCurve(fillet-curve);
    doc.Views.Redraw();
    return rc;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function FilletCurves(ByVal doc As RhinoDoc) As Result
	Dim gc1 = New GetObject()
	gc1.DisablePreSelect()
	gc1.SetCommandPrompt("Select first curve to fillet (close to the end you want to fillet)")
	gc1.GeometryFilter = ObjectType.Curve
	gc1.GeometryAttributeFilter = GeometryAttributeFilter.OpenCurve
	gc1.Get()
	If gc1.CommandResult() <> Result.Success Then
	  Return gc1.CommandResult()
	End If
	Dim curve1_obj_ref = gc1.Object(0)
	Dim curve1 = curve1_obj_ref.Curve()
	If curve1 Is Nothing Then
		Return Result.Failure
	End If
	Dim curve1_point_near_end = curve1_obj_ref.SelectionPoint()
	If curve1_point_near_end Is Point3d.Unset Then
	  Return Result.Failure
	End If

	Dim gc2 = New GetObject()
	gc2.DisablePreSelect()
	gc2.SetCommandPrompt("Select second curve to fillet (close to the end you want to fillet)")
	gc2.GeometryFilter = ObjectType.Curve
	gc2.GeometryAttributeFilter = GeometryAttributeFilter.OpenCurve
	gc2.Get()
	If gc2.CommandResult() <> Result.Success Then
	  Return gc2.CommandResult()
	End If
	Dim curve2_obj_ref = gc2.Object(0)
	Dim curve2 = curve2_obj_ref.Curve()
	If curve2 Is Nothing Then
		Return Result.Failure
	End If
	Dim curve2_point_near_end = curve2_obj_ref.SelectionPoint()
	If curve2_point_near_end Is Point3d.Unset Then
	  Return Result.Failure
	End If

	Dim radius As Double = 0
	Dim rc = RhinoGet.GetNumber("fillet radius", False, radius)
	If rc IsNot Result.Success Then
		Return rc
	End If

	Dim join = False
	Dim trim = True
	Dim arc_extension = True
	Dim fillet-curves = Curve.CreateFilletCurves(curve1, curve1_point_near_end, curve2, curve2_point_near_end, radius, join, trim, arc_extension, doc.ModelAbsoluteTolerance, doc.ModelAngleToleranceDegrees)
	If fillet-curves Is Nothing Then '|| fillet-curves.Length != 3
	  Return Result.Failure
	End If

	For Each fillet-curve In fillet-curves
	  doc.Objects.AddCurve(fillet-curve)
	Next fillet-curve
	doc.Views.Redraw()
	Return rc
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
from Rhino import *
from Rhino.Commands import *
from Rhino.Geometry import *
from Rhino.Input import *
from Rhino.DocObjects import *
from Rhino.Input.Custom import *
from scriptcontext import doc

def RunCommand():
    gc1 = GetObject()
    gc1.DisablePreSelect()
    gc1.SetCommandPrompt("Select first curve to fillet (close to the end you want to fillet)")
    gc1.GeometryFilter = ObjectType.Curve
    gc1.GeometryAttributeFilter = GeometryAttributeFilter.OpenCurve
    gc1.Get()
    if gc1.CommandResult() != Result.Success:
        return gc1.CommandResult()
    curve1_obj_ref = gc1.Object(0)
    curve1 = curve1_obj_ref.Curve()
    if curve1 == None: return Result.Failure
    curve1_point_near_end = curve1_obj_ref.SelectionPoint()
    if curve1_point_near_end == Point3d.Unset:
        return Result.Failure

    gc2 = GetObject()
    gc2.DisablePreSelect()
    gc2.SetCommandPrompt("Select second curve to fillet (close to the end you want to fillet)")
    gc2.GeometryFilter = ObjectType.Curve
    gc2.GeometryAttributeFilter = GeometryAttributeFilter.OpenCurve
    gc2.Get()
    if gc2.CommandResult() != Result.Success:
        return gc2.CommandResult()
    curve2_obj_ref = gc2.Object(0)
    curve2 = curve2_obj_ref.Curve()
    if curve2 == None: return Result.Failure
    curve2_point_near_end = curve2_obj_ref.SelectionPoint()
    if curve2_point_near_end == Point3d.Unset:
        return Result.Failure

    radius = 0.0
    rc, radius = RhinoGet.GetNumber("fillet radius", False, radius)
    if rc != Result.Success: return rc

    fillet-curve = Curve.CreateFilletCurves(curve1, curve1_point_near_end, curve2, curve2_point_near_end, radius, True, True, True, doc.ModelAbsoluteTolerance, doc.ModelAngleToleranceDegrees)
    if fillet-curve == None or fillet-curve.Length != 1:
        return Result.Failure

    doc.Objects.AddCurve(fillet-curve[0])
    doc.Views.Redraw()
    return rc

if __name__ == "__main__":
    RunCommand()
```

</div>
