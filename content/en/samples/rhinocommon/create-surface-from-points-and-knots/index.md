+++
aliases = ["/en/5/samples/rhinocommon/create-surface-from-points-and-knots/", "/en/6/samples/rhinocommon/create-surface-from-points-and-knots/", "/en/7/samples/rhinocommon/create-surface-from-points-and-knots/", "/en/wip/samples/rhinocommon/create-surface-from-points-and-knots/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to create a surface from scratch from points and knots."
keywords = [ "create", "surface", "points", "knots" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Create Surface From Points and Knots"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = ""
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

</div>

<div class="codetab-content" id="py">

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
    nurbs_surface = NurbsSurface.Create(dim, bIsRational, u_degree + 1, v_degree + 1, u_cv_count, v_cv_count)

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

</div>
