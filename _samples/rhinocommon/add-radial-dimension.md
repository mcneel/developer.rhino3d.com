---
title: Add Radial Dimension
description: Demonstrates how to add radial dimensions to a selected curve.
authors: ['steve_baer']
author_contacts: ['stevebaer']
sdk: ['RhinoCommon']
languages: ['C#', 'Python', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/rhinocommonsamples/addradialdimension
order: 1
keywords: ['create', 'radial', 'dimensions']
layout: code-sample-rhinocommon
---

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
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function AddRadialDimension(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim obj_ref As ObjRef = Nothing
	Dim rc = RhinoGet.GetOneObject("Select curve for radius dimension", True, ObjectType.Curve, obj_ref)
	If rc IsNot Result.Success Then
	  Return rc
	End If
	Dim curve_parameter As Double = Nothing
	Dim curve = obj_ref.CurveParameter(curve_parameter)
	If curve Is Nothing Then
	  Return Result.Failure
	End If

	If curve.IsLinear() OrElse curve.IsPolyline() Then
	  RhinoApp.WriteLine("Curve must be non-linear.")
	  Return Result.Nothing
	End If

	' in this example just deal with planar curves
	If Not curve.IsPlanar() Then
	  RhinoApp.WriteLine("Curve must be planar.")
	  Return Result.Nothing
	End If

	Dim point_on_curve = curve.PointAt(curve_parameter)
	Dim curvature_vector = curve.CurvatureAt(curve_parameter)
	Dim len = curvature_vector.Length
	If len < RhinoMath.SqrtEpsilon Then
	  RhinoApp.WriteLine("Curve is almost linear and therefore has no curvature.")
	  Return Result.Nothing
	End If

	Dim center = point_on_curve + (curvature_vector/(len*len))
	Dim plane As Plane = Nothing
	curve.TryGetPlane(plane)
	Dim radial_dimension = New RadialDimension(center, point_on_curve, plane.XAxis, plane.Normal, 5.0)
	doc.Objects.AddRadialDimension(radial_dimension)
	doc.Views.Redraw()
	Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
from Rhino import *
from Rhino.DocObjects import *
from Rhino.Commands import *
from Rhino.Geometry import *
from Rhino.Input import *
from scriptcontext import doc

def RunCommand():
  rc, obj_ref = RhinoGet.GetOneObject("Select curve for radius dimension",
    True, ObjectType.Curve)
  if rc != Result.Success:
    return rc
  curve, curve_parameter = obj_ref.CurveParameter()
  if curve == None:
    return Result.Failure

  if curve.IsLinear() or curve.IsPolyline():
    print "Curve must be non-linear."
    return Result.Nothing

  # in this example just deal with planar curves
  if not curve.IsPlanar():
    print "Curve must be planar."
    return Result.Nothing

  point_on_curve = curve.PointAt(curve_parameter)
  curvature_vector = curve.CurvatureAt(curve_parameter)
  len = curvature_vector.Length
  if len < RhinoMath.SqrtEpsilon:
    print "Curve is almost linear and therefore has no curvature."
    return Result.Nothing

  center = point_on_curve + (curvature_vector/(len*len))
  _, plane = curve.TryGetPlane()
  radial_dimension = \
    RadialDimension(center, point_on_curve, plane.XAxis, plane.Normal, 5.0)
  doc.Objects.AddRadialDimension(radial_dimension)
  doc.Views.Redraw()
  return Result.Success

if __name__=="__main__":
  RunCommand()
```
{: #py .tab-pane .fade .in}
