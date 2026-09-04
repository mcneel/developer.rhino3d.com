+++
aliases = ["/en/5/samples/rhinocommon/extract-isocurve/", "/en/6/samples/rhinocommon/extract-isocurve/", "/en/7/samples/rhinocommon/extract-isocurve/", "/en/wip/samples/rhinocommon/extract-isocurve/"]
authors = [ "steve" ]
categories = [ "Curves" ]
description = "Demonstrates how to extract the isoparametric curves from selected surfaces."
keywords = [ "extracting", "isoparametric", "curves", "surfaces" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Extract Isocurve"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/extractisocurve"
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
  public static Result ExtractIsoCurve(RhinoDoc doc)
  {
    ObjRef obj_ref;
    var rc = RhinoGet.GetOneObject("Select surface", false, ObjectType.Surface, out obj_ref);
    if (rc != Result.Success || obj_ref == null)
      return rc;
    var surface = obj_ref.Surface();

    var gp = new GetPoint();
    gp.SetCommandPrompt("Point on surface");
    gp.Constrain(surface, false);
    var option_toggle = new OptionToggle(false, "U", "V");
    gp.AddOptionToggle("Direction", ref option_toggle);
    Point3d point = Point3d.Unset;
    while (true)
    {
      var grc = gp.Get();
      if (grc == GetResult.Option)
        continue;
      else if (grc == GetResult.Point)
      {
        point = gp.Point();
        break;
      }
      else
        return Result.Nothing;
    }
    if (point == Point3d.Unset)
      return Result.Nothing;

    int direction = option_toggle.CurrentValue ? 1 : 0; // V : U
    double u_parameter, v_parameter;
    if (!surface.ClosestPoint(point, out u_parameter, out v_parameter)) return Result.Failure;

    var iso_curve = surface.IsoCurve(direction, direction == 1 ? u_parameter : v_parameter);
    if (iso_curve == null) return Result.Failure;

    doc.Objects.AddCurve(iso_curve);
    doc.Views.Redraw();
    return Result.Success;
  }
}
```

</div>

<div class="codetab-content" id="py">

```python
from Rhino import *
from Rhino.DocObjects import *
from Rhino.Commands import *
from Rhino.Input import *
from Rhino.Input.Custom import *
from Rhino.Geometry import *
from scriptcontext import doc

def RunCommand():
    rc, obj_ref = RhinoGet.GetOneObject("Select surface", False, ObjectType.Surface)
    if rc != Result.Success or obj_ref == None:
        return rc
    surface = obj_ref.Surface()

    gp = GetPoint()
    gp.SetCommandPrompt("Point on surface")
    gp.Constrain(surface, False)
    option_toggle = OptionToggle(False, "U", "V")
    gp.AddOptionToggle("Direction", option_toggle)
    point = Point3d.Unset

    while True:
        grc = gp.Get()
        if grc == GetResult.Option:
            continue
        elif grc == GetResult.Point:
            point = gp.Point()
            break
        else:
            return Result.Nothing

    if point == Point3d.Unset:
        return Result.Nothing

    direction = 1 if option_toggle.CurrentValue else 0
    b, u_parameter, v_parameter = surface.ClosestPoint(point)
    if not b: return Result.Failure

    iso_curve = surface.IsoCurve(direction, u_parameter if direction == 1 else v_parameter)
    if iso_curve == None:
        return Result.Failure

    doc.Objects.AddCurve(iso_curve)
    doc.Views.Redraw()
    return Result.Success

if __name__ == "__main__":
    RunCommand()
```

</div>
