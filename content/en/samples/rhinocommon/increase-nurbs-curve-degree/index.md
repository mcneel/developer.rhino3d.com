+++
aliases = ["/en/5/samples/rhinocommon/increase-nurbs-curve-degree/", "/en/6/samples/rhinocommon/increase-nurbs-curve-degree/", "/en/7/samples/rhinocommon/increase-nurbs-curve-degree/", "/en/wip/samples/rhinocommon/increase-nurbs-curve-degree/"]
authors = [ "steve" ]
categories = [ "Curves" ]
description = "Demonstrates how to increase the degree of a NURBS curve."
keywords = [ "increasing", "degree", "nurbs", "curve" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Increase NURBS Curve Degree"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/nurbscurveincreasedegree"
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
  public static Result NurbsCurveIncreaseDegree(RhinoDoc doc)
  {
    ObjRef obj_ref;
    var rc = RhinoGet.GetOneObject(
      "Select curve", false, ObjectType.Curve, out obj_ref);
    if (rc != Result.Success) return rc;
    if (obj_ref == null) return Result.Failure;
    var curve = obj_ref.Curve();
    if (curve == null) return Result.Failure;
    var nurbs_curve = curve.ToNurbsCurve();

    int new_degree = -1;
    rc = RhinoGet.GetInteger(string.Format("New degree <{0}...11>", nurbs_curve.Degree), true, ref new_degree,
      nurbs_curve.Degree, 11);
    if (rc != Result.Success) return rc;

    rc = Result.Failure;
    if (nurbs_curve.IncreaseDegree(new_degree))
      if (doc.Objects.Replace(obj_ref.ObjectId, nurbs_curve))
        rc = Result.Success;

    RhinoApp.WriteLine("Result: {0}", rc.ToString());
    doc.Views.Redraw();
    return rc;
  }
}
```

</div>

<div class="codetab-content" id="py">

```python
from Rhino import *
from Rhino.Commands import *
from Rhino.Input import *
from Rhino.DocObjects import *
from scriptcontext import doc

def RunCommand():
    rc, obj_ref = RhinoGet.GetOneObject("Select curve", False, ObjectType.Curve)
    if rc != Result.Success: return rc
    if obj_ref == None: return Result.Failure
    curve = obj_ref.Curve()
    if curve == None: return Result.Failure
    nurbs_curve = curve.ToNurbsCurve()

    new_degree = -1
    rc, new_degree = RhinoGet.GetInteger("New degree <{0}...11>".format(nurbs_curve.Degree), True, new_degree, nurbs_curve.Degree, 11)
    if rc != Result.Success: return rc

    rc = Result.Failure
    if nurbs_curve.IncreaseDegree(new_degree):
        if doc.Objects.Replace(obj_ref.ObjectId, nurbs_curve):
            rc = Result.Success

    print "Result: {0}".format(rc)
    doc.Views.Redraw()
    return rc

if __name__ == "__main__":
    RunCommand()
```

</div>
