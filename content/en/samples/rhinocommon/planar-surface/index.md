+++
aliases = ["/en/5/samples/rhinocommon/planar-surface/", "/en/6/samples/rhinocommon/planar-surface/", "/en/7/samples/rhinocommon/planar-surface/", "/wip/samples/rhinocommon/planar-surface/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to create a planar surface from a rectangle."
keywords = [ "create", "plane", "surface" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Planar Surface"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/planesurface"
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
  public static Result PlanarSurface(RhinoDoc doc)
  {
    Point3d[] corners;
    var rc = Rhino.Input.RhinoGet.GetRectangle(out corners);
    if (rc != Result.Success)
      return rc;

    var plane = new Plane(corners[0], corners[1], corners[2]);

    var plane_surface = new PlaneSurface(plane,
      new Interval(0, corners[0].DistanceTo(corners[1])),
      new Interval(0, corners[1].DistanceTo(corners[2])));

    doc.Objects.Add(plane_surface);
    doc.Views.Redraw();
    return Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function PlanarSurface(ByVal doc As RhinoDoc) As Result
	Dim corners() As Point3d = Nothing
	Dim rc = Rhino.Input.RhinoGet.GetRectangle(corners)
	If rc IsNot Result.Success Then
	  Return rc
	End If

	Dim plane = New Plane(corners(0), corners(1), corners(2))

	Dim plane_surface = New PlaneSurface(plane, New Interval(0, corners(0).DistanceTo(corners(1))), New Interval(0, corners(1).DistanceTo(corners(2))))

	doc.Objects.Add(plane_surface)
	doc.Views.Redraw()
	Return Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
import Rhino;
import rhinoscriptsyntax as rs

def RunCommand():
    rc, corners = Rhino.Input.RhinoGet.GetRectangle()
    if rc != Rhino.Commands.Result.Success:
        return rc

    plane = Rhino.Geometry.Plane(corners[0], corners[1], corners[2])
    u_dir = rs.Distance(corners[0], corners[1])
    v_dir = rs.Distance(corners[1], corners[2])
    rs.AddPlaneSurface(plane, u_dir, v_dir)

if __name__ == "__main__":
    RunCommand()
```

</div>
