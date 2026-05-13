+++
aliases = ["/en/5/samples/rhinocommon/is-planar-surface-in-plane/", "/en/6/samples/rhinocommon/is-planar-surface-in-plane/", "/en/7/samples/rhinocommon/is-planar-surface-in-plane/", "/en/wip/samples/rhinocommon/is-planar-surface-in-plane/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to determine if a user-selected surface is in plane."
keywords = [ "planar", "surface", "plane" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Is Planar Surface in Plane"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/issurfaceinplane"
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
  public static Result IsPlanarSurfaceInPlane(RhinoDoc doc)
  {
    ObjRef obj_ref;
    var rc = RhinoGet.GetOneObject("select surface", true, ObjectType.Surface, out obj_ref);
    if (rc != Result.Success)
      return rc;
    var surface = obj_ref.Surface();

    Point3d[] corners;
    rc = RhinoGet.GetRectangle(out corners);
    if (rc != Result.Success)
      return rc;

    var plane = new Plane(corners[0], corners[1], corners[2]);

    var is_or_isnt = " not ";
    if (IsSurfaceInPlane(surface, plane, doc.ModelAbsoluteTolerance))
      is_or_isnt = "";

    RhinoApp.WriteLine("Surface is{0} in plane.", is_or_isnt);
    return Result.Success;
  }

  private static bool IsSurfaceInPlane(Surface surface, Plane plane, double tolerance)
  {
    if (!surface.IsPlanar(tolerance))
      return false;

    var bbox = surface.GetBoundingBox(true);
    return bbox.GetCorners().All(c => System.Math.Abs(plane.DistanceTo(c)) <= tolerance);
  }
}
```

</div>

<div class="codetab-content" id="py">

```python
import Rhino
from Rhino.Geometry import *
import rhinoscriptsyntax as rs
from scriptcontext import doc
import math

def RunCommand():
    surface_id = rs.GetSurfaceObject()[0]
    if surface_id == None:
        return
    surface = rs.coercesurface(surface_id)

    corners = rs.GetRectangle()
    if corners == None:
        return

    plane = Plane(corners[0], corners[1], corners[2])

    is_or_isnt = "" if IsSurfaceInPlane(surface, plane, doc.ModelAbsoluteTolerance) else " not "
    print "Surface is{0} in plane.".format(is_or_isnt)

def IsSurfaceInPlane(surface, plane, tolerance):
    if not surface.IsPlanar(tolerance):
        return False

    bbox = surface.GetBoundingBox(True)
    rc = True
    for corner in bbox.GetCorners():
        if math.fabs(plane.DistanceTo(corner)) > tolerance:
            rc = False
            break

    return rc

if __name__ == "__main__":
    RunCommand()
```

</div>
