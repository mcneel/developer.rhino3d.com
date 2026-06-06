+++
aliases = ["/en/5/samples/rhinocommon/create-spiral/", "/en/6/samples/rhinocommon/create-spiral/", "/en/7/samples/rhinocommon/create-spiral/", "/en/wip/samples/rhinocommon/create-spiral/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to create a spiral object from an axis and a radius point."
keywords = [ "create", "spiral" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Create Spiral"
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
  public static Rhino.Commands.Result CreateSpiral(Rhino.RhinoDoc doc)
  {
    var axisStart = new Rhino.Geometry.Point3d(0, 0, 0);
    var axisDir = new Rhino.Geometry.Vector3d(1, 0, 0);
    var radiusPoint = new Rhino.Geometry.Point3d(0, 1, 0);

    Rhino.Geometry.NurbsCurve curve0 = GetSpirial0();
    if (null != curve0)
      doc.Objects.AddCurve(curve0);

    Rhino.Geometry.NurbsCurve curve1 = GetSpirial1();
    if (null != curve1)
      doc.Objects.AddCurve(curve1);

    doc.Views.Redraw();

    return Rhino.Commands.Result.Success;
  }

  private static Rhino.Geometry.NurbsCurve GetSpirial0()
  {
    var axisStart = new Rhino.Geometry.Point3d(0, 0, 0);
    var axisDir = new Rhino.Geometry.Vector3d(1, 0, 0);
    var radiusPoint = new Rhino.Geometry.Point3d(0, 1, 0);

    return Rhino.Geometry.NurbsCurve.CreateSpiral(axisStart, axisDir, radiusPoint, 1, 10, 1.0, 1.0);
  }

  private static Rhino.Geometry.NurbsCurve GetSpirial1()
  {
    var railStart = new Rhino.Geometry.Point3d(0, 0, 0);
    var railEnd = new Rhino.Geometry.Point3d(0, 0, 10);
    var railCurve = new Rhino.Geometry.LineCurve(railStart, railEnd);

    double t0 = railCurve.Domain.Min;
    double t1 = railCurve.Domain.Max;

    var radiusPoint = new Rhino.Geometry.Point3d(1, 0, 0);

    return Rhino.Geometry.NurbsCurve.CreateSpiral(railCurve, t0, t1, radiusPoint, 1, 10, 1.0, 1.0, 12);
  }
}
```

</div>

<div class="codetab-content" id="py">

```python
#! python 3
import Rhino
import scriptcontext as sc

def GetSpirial0():
    axisStart = Rhino.Geometry.Point3d(0, 0, 0)
    axisDir = Rhino.Geometry.Vector3d(1, 0, 0)
    radiusPoint = Rhino.Geometry.Point3d(0, 1, 0)

    return Rhino.Geometry.NurbsCurve.CreateSpiral(axisStart, axisDir, radiusPoint, 1, 10, 1.0, 1.0)

def GetSpirial1():
    railStart = Rhino.Geometry.Point3d(0, 0, 0)
    railEnd = Rhino.Geometry.Point3d(0, 0, 10)
    railCurve = Rhino.Geometry.LineCurve(railStart, railEnd)

    t0 = railCurve.Domain.Min
    t1 = railCurve.Domain.Max

    radiusPoint = Rhino.Geometry.Point3d(1, 0, 0)

    return Rhino.Geometry.NurbsCurve.CreateSpiral(railCurve, t0, t1, radiusPoint, 1, 10, 1.0, 1.0, 12)

def RunCommand():
    axisStart = Rhino.Geometry.Point3d(0, 0, 0)
    axisDir = Rhino.Geometry.Vector3d(1, 0, 0)
    radiusPoint = Rhino.Geometry.Point3d(0, 1, 0)

    curve0 = GetSpirial0()
    if curve0 is not None:
        sc.doc.Objects.AddCurve(curve0)

    curve1 = GetSpirial1()
    if curve1 is not None:
        sc.doc.Objects.AddCurve(curve1)

    sc.doc.Views.Redraw()

    return Rhino.Commands.Result.Success

if __name__ == "__main__":
    RunCommand()
```

</div>
