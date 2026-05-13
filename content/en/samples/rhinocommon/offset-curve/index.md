+++
aliases = ["/en/5/samples/rhinocommon/offset-curve/", "/en/6/samples/rhinocommon/offset-curve/", "/en/7/samples/rhinocommon/offset-curve/", "/en/wip/samples/rhinocommon/offset-curve/"]
authors = [ "steve" ]
categories = [ "Curves" ]
description = "Demonstrates how to offset curves to one side or another by a distance."
keywords = [ "offset", "curve" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Offset Curve"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/offsetcurve"
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
  public static Result OffsetCurve(RhinoDoc doc)
  {
    ObjRef obj_ref;
    var rs = RhinoGet.GetOneObject(
      "Select Curve", false, ObjectType.Curve, out obj_ref);
    if (rs != Result.Success)
      return rs;
    var curve = obj_ref.Curve();
    if (curve == null)
      return Result.Nothing;

    Point3d point;
    rs = RhinoGet.GetPoint("Select Side", false, out point);
    if (rs != Result.Success)
      return rs;
    if (point == Point3d.Unset)
      return Result.Nothing;

    var curves = curve.Offset(point, Vector3d.ZAxis, 1.0,
      doc.ModelAbsoluteTolerance, CurveOffsetCornerStyle.None);

    foreach (var offset-curve in curves)
      doc.Objects.AddCurve(offset-curve);

    doc.Views.Redraw();
    return Result.Success;
  }
}
```

</div>

<div class="codetab-content" id="py">

```python
from Rhino.DocObjects import ObjectType
from Rhino.Geometry import Point3d, Vector3d, CurveOffsetCornerStyle
from Rhino.Input import RhinoGet
from Rhino.Commands import Result
from scriptcontext import doc
import rhinoscriptsyntax as rs
import System

def RunCommand():
    rc, obj_ref = RhinoGet.GetOneObject("Select Curve", False, ObjectType.Curve)
    if rc != Result.Success:
        return rc
    curve = obj_ref.Curve()
    if curve == None:
        return Result.Nothing

    rc, point = RhinoGet.GetPoint("Select Side", False)
    if rc != Result.Success:
        return rc
    if point == Point3d.Unset:
        return Result.Nothing

    curves = curve.Offset(point, Vector3d.ZAxis, 1.0, doc.ModelAbsoluteTolerance, System.Enum.Parse(CurveOffsetCornerStyle, "None"))

    for offset_curve in curves:
        doc.Objects.AddCurve(offset_curve)

    doc.Views.Redraw()
    return Result.Success

if __name__ == "__main__":
    RunCommand()
```

</div>
