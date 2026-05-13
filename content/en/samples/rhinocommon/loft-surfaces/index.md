+++
aliases = ["/en/5/samples/rhinocommon/loft-surfaces/", "/en/6/samples/rhinocommon/loft-surfaces/", "/en/7/samples/rhinocommon/loft-surfaces/", "/en/wip/samples/rhinocommon/loft-surfaces/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to create a lofted surface from a set of user-specified curves."
keywords = [ "loft", "surfaces" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Loft Surfaces"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/loft"
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
  public static Result Loft(RhinoDoc doc)
  {
    // select curves to loft
    var gs = new GetObject();
    gs.SetCommandPrompt("select curves to loft");
    gs.GeometryFilter = ObjectType.Curve;
    gs.DisablePreSelect();
    gs.SubObjectSelect = false;
    gs.GetMultiple(2, 0);
    if (gs.CommandResult() != Result.Success)
      return gs.CommandResult();

    var curves = gs.Objects().Select(obj => obj.Curve()).ToList();

    var breps = Brep.CreateFromLoft(curves, Point3d.Unset, Point3d.Unset, LoftType.Tight, false);
    foreach (var brep in breps)
      doc.Objects.AddBrep(brep);

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
    crvids = rs.GetObjects(message="select curves to loft", filter=rs.filter.curve, minimum_count=2)
    if not crvids: return

    rs.AddLoftSrf(object_ids=crvids, loft_type = 3) #3 = tight

if __name__ == "__main__":
    RunCommand()
```

</div>
