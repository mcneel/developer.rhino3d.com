+++
aliases = ["/en/5/samples/rhinocommon/intersect-line-and-circle/", "/en/6/samples/rhinocommon/intersect-line-and-circle/", "/en/7/samples/rhinocommon/intersect-line-and-circle/", "/en/wip/samples/rhinocommon/intersect-line-and-circle/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to find the intersection point(s) of a circle and a line."
keywords = [ "intersecting", "line", "with", "circle" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Intersecting Line and Circle"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/intersectlinecircle"
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
  public static Result IntersectLineCircle(RhinoDoc doc)
  {
    Circle circle;
    var rc = RhinoGet.GetCircle(out circle);
    if (rc != Result.Success)
      return rc;
    doc.Objects.AddCircle(circle);
    doc.Views.Redraw();

    Line line;
    rc = RhinoGet.GetLine(out line);
    if (rc != Result.Success)
      return rc;
    doc.Objects.AddLine(line);
    doc.Views.Redraw();

    double t1, t2;
    Point3d point1, point2;
    var line_circle_intersect = Intersection.LineCircle(line, circle, out t1, out point1, out t2, out point2);
    string msg = "";
    switch (line_circle_intersect) {
      case LineCircleIntersection.None:
        msg = "line does not intersect circle";
        break;
      case LineCircleIntersection.Single:
        msg = string.Format("line intersects circle at point ({0})", point1);
        doc.Objects.AddPoint(point1);
        break;
      case LineCircleIntersection.Multiple:
        msg = string.Format("line intersects circle at points ({0}) and ({1})",
          point1, point2);
        doc.Objects.AddPoint(point1);
        doc.Objects.AddPoint(point2);
        break;
    }
    RhinoApp.WriteLine(msg);
    doc.Views.Redraw();
    return Result.Success;
  }
}
```

</div>

<div class="codetab-content" id="py">

```python
#! python 3
import Rhino
import scriptcontext as sc

def RunCommand():
    rc, circle = Rhino.Input.RhinoGet.GetCircle()
    if rc != Rhino.Commands.Result.Success:
        return rc
    sc.doc.Objects.AddCircle(circle)
    sc.doc.Views.Redraw()

    rc, line = Rhino.Input.RhinoGet.GetLine()
    if rc != Rhino.Commands.Result.Success:
        return rc
    sc.doc.Objects.AddLine(line)
    sc.doc.Views.Redraw()

    line_circle_intersect, t1, point1, t2, point2 = Rhino.Geometry.Intersect.Intersection.LineCircle(line, circle)
    msg = ""
    if line_circle_intersect == getattr(Rhino.Geometry.Intersect.LineCircleIntersection, "None"):
        msg = "line does not intersect circle"
    elif line_circle_intersect == Rhino.Geometry.Intersect.LineCircleIntersection.Single:
        msg = "line intersects circle at point ({0})".format(point1)
        sc.doc.Objects.AddPoint(point1)
    elif line_circle_intersect == Rhino.Geometry.Intersect.LineCircleIntersection.Multiple:
        msg = "line intersects circle at points ({0}) and ({1})".format(point1, point2)
        sc.doc.Objects.AddPoint(point1)
        sc.doc.Objects.AddPoint(point2)
    Rhino.RhinoApp.WriteLine(msg)
    sc.doc.Views.Redraw()
    return Rhino.Commands.Result.Success

if __name__ == "__main__":
    RunCommand()
```

</div>
