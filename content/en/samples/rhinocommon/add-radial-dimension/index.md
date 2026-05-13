+++
aliases = ["/en/5/samples/rhinocommon/add-radial-dimension/", "/en/6/samples/rhinocommon/add-radial-dimension/", "/en/7/samples/rhinocommon/add-radial-dimension/", "/en/wip/samples/rhinocommon/add-radial-dimension/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to add radial dimensions to a selected curve."
keywords = [ "create", "radial", "dimensions" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Add Radial Dimension"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/addradialdimension"
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
  public static Rhino.Commands.Result AddRadialDimension(Rhino.RhinoDoc doc)
  {
    ObjRef obj_ref;
    var rc = RhinoGet.GetOneObject("Select curve for radius dimension",
      true, ObjectType.Curve, out obj_ref);
    if (rc != Result.Success)
      return rc;
    double curve_parameter;
    var curve = obj_ref.CurveParameter(out curve_parameter);
    if (curve == null)
      return Result.Failure;

    if (curve.IsLinear() || curve.IsPolyline())
    {
      RhinoApp.WriteLine("Curve must be non-linear.");
      return Result.Nothing;
    }

    // in this example just deal with planar curves
    if (!curve.IsPlanar())
    {
      RhinoApp.WriteLine("Curve must be planar.");
      return Result.Nothing;
    }

    var point_on_curve = curve.PointAt(curve_parameter);
    var curvature_vector = curve.CurvatureAt(curve_parameter);
    var len = curvature_vector.Length;
    if (len < RhinoMath.SqrtEpsilon)
    {
      RhinoApp.WriteLine("Curve is almost linear and therefore has no curvature.");
      return Result.Nothing;
    }

    var center = point_on_curve + (curvature_vector/(len*len));
    Plane plane;
    curve.TryGetPlane(out plane);
    var radial_dimension =
      new RadialDimension(center, point_on_curve, plane.XAxis, plane.Normal, 5.0);
    doc.Objects.AddRadialDimension(radial_dimension);
    doc.Views.Redraw();
    return Result.Success;
  }
}
```

</div>

<div class="codetab-content" id="py">

```python
from Rhino import RhinoMath
from Rhino.DocObjects import ObjectType
from Rhino.Commands import Result
from Rhino.Geometry import RadialDimension, AnnotationType
from Rhino.Input import RhinoGet
from scriptcontext import doc

def RunCommand():
    rc, obj_ref = RhinoGet.GetOneObject("Select curve for radius dimension", True, ObjectType.Curve)
    if rc != Result.Success:
        return rc
    curve, curve_parameter = obj_ref.CurveParameter()
    if curve == None:
        return Result.Failure

    if curve.IsLinear() or curve.IsPolyline():
        print("Curve must be non-linear.")
        return Result.Nothing

    # in this example just deal with planar curves
    if not curve.IsPlanar():
        print("Curve must be planar.")
        return Result.Nothing

    point_on_curve = curve.PointAt(curve_parameter)
    curvature_vector = curve.CurvatureAt(curve_parameter)
    len = curvature_vector.Length
    if len < RhinoMath.SqrtEpsilon:
        print("Curve is almost linear and therefore has no curvature.")
        return Result.Nothing

    center = point_on_curve + (curvature_vector/(len*len))
    _, plane = curve.TryGetPlane()
    indicator_point = point_on_curve + (point_on_curve - center) * 0.5
    radial_dimension = RadialDimension(AnnotationType.Radius, plane, center, point_on_curve, indicator_point)
    doc.Objects.AddRadialDimension(radial_dimension)
    doc.Views.Redraw()
    return Result.Success

if __name__=="__main__":
    RunCommand()
```

</div>
