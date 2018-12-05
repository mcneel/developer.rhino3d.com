---
title: Create Surface From Points and Knots
description: Demonstrates how to create a surface from scratch from points and knots.
authors: ['steve_baer']
sdk: ['RhinoCommon']
languages: ['C#', 'Python', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Other']
origin: unset
order: 1
keywords: ['create', 'surface', 'points', 'knots']
layout: code-sample-rhinocommon
---

```cs
partial class Examples
{
  public static Result CreateSurfaceFromPointsAndKnots(RhinoDoc doc)
  {
    const bool is_rational = false;
    const int number_of_dimensions = 3;
    const int u_degree = 2;
    const int v_degree = 3;
    const int u_control_point_count = 3;
    const int v_control_point_count = 5;
   
    // The knot vectors do NOT have the 2 superfluous knots
    // at the start and end of the knot vector.  If you are
    // coming from a system that has the 2 superfluous knots,
    // just ignore them when creating NURBS surfaces.
    var u_knots = new double[u_control_point_count + u_degree - 1];
    var v_knots = new double[v_control_point_count + v_degree - 1];
   
    // make up a quadratic knot vector with no interior knots
    u_knots[0] = u_knots[1] = 0.0;
    u_knots[2] = u_knots[3] = 1.0;
   
    // make up a cubic knot vector with one simple interior knot
    v_knots[0] = v_knots[1] = v_knots[2] = 0.0;
    v_knots[3] = 1.5;
    v_knots[4] = v_knots[5] = v_knots[6] = 2.0;
   
    // Rational control points can be in either homogeneous
    // or euclidean form. Non-rational control points do not
    // need to specify a weight.  
    var control_points = new Point3d[u_control_point_count, v_control_point_count];

    for (int u = 0; u < u_control_point_count; u++)
    {
      for (int v = 0; v < v_control_point_count; v++)
      {
        control_points[u,v] = new Point3d(u, v, u-v);
      }
    }
   
    // creates internal uninitialized arrays for 
    // control points and knots
    var nurbs_surface = NurbsSurface.Create(
      number_of_dimensions,
      is_rational,
      u_degree + 1,
      v_degree + 1,
      u_control_point_count,
      v_control_point_count
      );
   
    // add the knots
    for (int u = 0;  u < nurbs_surface.KnotsU.Count; u++)
      nurbs_surface.KnotsU[u] = u_knots[u];
    for (int v = 0; v < nurbs_surface.KnotsV.Count; v++)
      nurbs_surface.KnotsV[v] = v_knots[v];

    // add the control points
    for (int u = 0; u < nurbs_surface.Points.CountU; u++)
    {
      for (int v = 0; v < nurbs_surface.Points.CountV; v++)
      {
        nurbs_surface.Points.SetControlPoint(u, v, control_points[u, v]);
      }
    }

    if (nurbs_surface.IsValid)
    {
      doc.Objects.AddSurface(nurbs_surface);
      doc.Views.Redraw();
      return Result.Success;
    }
    return Result.Failure;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function CreateSurfaceFromPointsAndKnots(ByVal doc As RhinoDoc) As Result
	Const is_rational As Boolean = False
	Const number_of_dimensions As Integer = 3
	Const u_degree As Integer = 2
	Const v_degree As Integer = 3
	Const u_control_point_count As Integer = 3
	Const v_control_point_count As Integer = 5

	' The knot vectors do NOT have the 2 superfluous knots
	' at the start and end of the knot vector.  If you are
	' coming from a system that has the 2 superfluous knots,
	' just ignore them when creating NURBS surfaces.
	Dim u_knots = New Double(u_control_point_count + u_degree - 2){}
	Dim v_knots = New Double(v_control_point_count + v_degree - 2){}

	' make up a quadratic knot vector with no interior knots
	u_knots(1) = 0.0
	u_knots(0) = u_knots(1)
	u_knots(3) = 1.0
	u_knots(2) = u_knots(3)

	' make up a cubic knot vector with one simple interior knot
	v_knots(2) = 0.0
	v_knots(1) = v_knots(2)
	v_knots(0) = v_knots(1)
	v_knots(3) = 1.5
	v_knots(6) = 2.0
	v_knots(5) = v_knots(6)
	v_knots(4) = v_knots(5)

	' Rational control points can be in either homogeneous
	' or euclidean form. Non-rational control points do not
	' need to specify a weight.  
	Dim control_points = New Point3d(u_control_point_count - 1, v_control_point_count - 1){}

	For u As Integer = 0 To u_control_point_count - 1
	  For v As Integer = 0 To v_control_point_count - 1
		control_points(u,v) = New Point3d(u, v, u-v)
	  Next v
	Next u

	' creates internal uninitialized arrays for 
	' control points and knots
	Dim nurbs_surface = NurbsSurface.Create(number_of_dimensions, is_rational, u_degree + 1, v_degree + 1, u_control_point_count, v_control_point_count)

	' add the knots
	For u As Integer = 0 To nurbs_surface.KnotsU.Count - 1
	  nurbs_surface.KnotsU(u) = u_knots(u)
	Next u
	For v As Integer = 0 To nurbs_surface.KnotsV.Count - 1
	  nurbs_surface.KnotsV(v) = v_knots(v)
	Next v

	' add the control points
	For u As Integer = 0 To nurbs_surface.Points.CountU - 1
	  For v As Integer = 0 To nurbs_surface.Points.CountV - 1
		nurbs_surface.Points.SetControlPoint(u, v, control_points(u, v))
	  Next v
	Next u

	If nurbs_surface.IsValid Then
	  doc.Objects.AddSurface(nurbs_surface)
	  doc.Views.Redraw()
	  Return Result.Success
	End If
	Return Result.Failure
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
from Rhino.Geometry import Point3d, NurbsSurface, ControlPoint
from scriptcontext import doc

def RunCommand():
  bIsRational = False
  dim = 3
  u_degree = 2
  v_degree = 3
  u_cv_count = 3
  v_cv_count = 5

  # make up a quadratic knot vector with no interior knots
  u_knot = [0.0, 0.0, 1.0, 1.0]

  # make up a cubic knot vector with one simple interior knot
  v_knot = [0.0, 0.0, 0.0, 1.5, 2.0, 2.0, 2.0]

  # Rational control points can be in either homogeneous
  # or euclidean form. Non-rational control points do not
  # need to specify a weight.
  CV = dict( ((i,j),None) for i in range(2) for j in range(3) )
  for i in range(0, u_cv_count):
    for j in range(0, v_cv_count):
      CV[i,j] = Point3d(i, j, i-j)

  # creates internal uninitialized arrays for
  # control points and knots
  nurbs_surface = NurbsSurface.Create(
    dim,
    bIsRational,
    u_degree + 1,
    v_degree + 1,
    u_cv_count,
    v_cv_count
    )

  # add the knots
  for i in range(0, nurbs_surface.KnotsU.Count):
    nurbs_surface.KnotsU[i] = u_knot[i]
  for j in range(0, nurbs_surface.KnotsV.Count):
    nurbs_surface.KnotsV[j] = v_knot[j]

  # add the control points
  for i in range(0, nurbs_surface.Points.CountU):
    for j in range(0, nurbs_surface.Points.CountV):
      nurbs_surface.Points.SetControlPoint(i, j, ControlPoint(CV[i, j]))

  if nurbs_surface.IsValid:
    doc.Objects.AddSurface(nurbs_surface)
    doc.Views.Redraw()

if __name__ == "__main__":
  RunCommand()
```
{: #py .tab-pane .fade .in}

