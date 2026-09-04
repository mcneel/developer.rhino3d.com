+++
aliases = ["/en/5/samples/rhinocommon/project-points-to-mesh/", "/en/6/samples/rhinocommon/project-points-to-mesh/", "/en/7/samples/rhinocommon/project-points-to-mesh/", "/en/wip/samples/rhinocommon/project-points-to-mesh/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to project points to a mesh."
keywords = [ "project", "points", "mesh" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Project Points to Mesh"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/projectpointstomeshes"
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
  public static Result ProjectPointsToMeshesEx(RhinoDoc doc)
  {
    ObjRef obj_ref;
    var rc = RhinoGet.GetOneObject("mesh", false, ObjectType.Mesh, out obj_ref);
    if (rc != Result.Success) return rc;
    var mesh = obj_ref.Mesh();

    ObjRef[] obj_ref_pts;
    rc = RhinoGet.GetMultipleObjects("points", false, ObjectType.Point, out obj_ref_pts);
    if (rc != Result.Success) return rc;
    var points = new List<Point3d>();
    foreach (var obj_ref_pt in obj_ref_pts)
    {
      var pt = obj_ref_pt.Point().Location;
      points.Add(pt);
    }

    int[] indices;
    var prj_points = Intersection.ProjectPointsToMeshesEx(new[] {mesh}, points, new Vector3d(0, 1, 0), 0, out indices);
    foreach (var prj_pt in prj_points) doc.Objects.AddPoint(prj_pt);
    doc.Views.Redraw();
    return Result.Success;
  }
}
```

</div>

<div class="codetab-content" id="py">

```python
from System.Collections.Generic import *
from Rhino import *
from Rhino.Commands import *
from Rhino.Geometry import *
from Rhino.Geometry.Intersect import *
from Rhino.Input import *
from Rhino.DocObjects import *
from scriptcontext import doc

def RunCommand():
    rc, obj_ref = RhinoGet.GetOneObject("mesh", False, ObjectType.Mesh)
    if rc != Result.Success: return rc
    mesh = obj_ref.Mesh()

    rc, obj_ref_pts = RhinoGet.GetMultipleObjects("points", False, ObjectType.Point)
    if rc != Result.Success: return rc
    points = []
    for obj_ref_pt in obj_ref_pts:
        pt = obj_ref_pt.Point().Location
        points.append(pt)

    prj_points, indices = Intersection.ProjectPointsToMeshesEx({mesh}, points, Vector3d(0, 1, 0), 0)
    for prj_pt in prj_points:
        doc.Objects.AddPoint(prj_pt)
    doc.Views.Redraw()
    return Result.Success

if __name__ == "__main__":
    RunCommand()
```

</div>
