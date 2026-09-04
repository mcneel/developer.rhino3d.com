+++
aliases = ["/en/5/samples/rhinocommon/add-leader/", "/en/6/samples/rhinocommon/add-leader/", "/en/7/samples/rhinocommon/add-leader/", "/en/wip/samples/rhinocommon/add-leader/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to add a leaders to your Rhino model from an array of points."
keywords = [ "creating", "leader" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Add Leader"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/leader"
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
  public static Result Leader(RhinoDoc doc)
  {
    var points = new Point3d[]
    {
      new Point3d(1, 1, 0),
      new Point3d(5, 1, 0),
      new Point3d(5, 5, 0),
      new Point3d(9, 5, 0)
    };

    var xy_plane = Plane.WorldXY;

    var points2d = new List<Point2d>();
    foreach (var point3d in points)
    {
      double x, y;
      if (xy_plane.ClosestParameter(point3d, out x, out y))
      {
        var point2d = new Point2d(x, y);
        if (points2d.Count < 1 || point2d.DistanceTo(points2d.Last<Point2d>()) > RhinoMath.SqrtEpsilon)
          points2d.Add(point2d);
      }
    }

    doc.Objects.AddLeader(xy_plane, points2d);
    doc.Views.Redraw();
    return Result.Success;
  }
}
```

</div>

<div class="codetab-content" id="py">

```python
import rhinoscriptsyntax as rs

def RunCommand():
    points = [(1,1,0), (5,1,0), (5,5,0), (9,5,0)]
    rs.AddLeader(points)

if __name__ == "__main__":
    RunCommand()
```

</div>
