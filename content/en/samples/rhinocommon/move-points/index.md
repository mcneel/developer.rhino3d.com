+++
aliases = ["/en/5/samples/rhinocommon/move-points/", "/en/6/samples/rhinocommon/move-points/", "/en/7/samples/rhinocommon/move-points/", "/en/wip/samples/rhinocommon/move-points/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to move user-specified points to a new location."
keywords = [ "move", "points" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Move Points"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/dotnetmovepointobjects"
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
  public static Result MovePointObjects(RhinoDoc doc)
  {
    ObjRef[] obj_refs;
    var rc = RhinoGet.GetMultipleObjects("Select points to move", false, ObjectType.Point, out obj_refs);
    if (rc != Result.Success || obj_refs == null)
      return rc;

    var gp = new GetPoint();
    gp.SetCommandPrompt("Point to move from");
    gp.Get();
    if (gp.CommandResult() != Result.Success)
      return gp.CommandResult();
    var start_point = gp.Point();

    gp.SetCommandPrompt("Point to move to");
    gp.SetBasePoint(start_point, false);
    gp.DrawLineFromPoint(start_point, true);
    gp.Get();
    if (gp.CommandResult() != Result.Success)
      return gp.CommandResult();
    var end_point = gp.Point();

    var xform = Transform.Translation(end_point - start_point);

    foreach (var obj_ref in obj_refs)
    {
      doc.Objects.Transform(obj_ref, xform, true);
    }

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
    rc, obj_refs = RhinoGet.GetMultipleObjects("Select points to move", False, ObjectType.Point)
    if rc != Result.Success or obj_refs == None:
        return rc

    gp = GetPoint()
    gp.SetCommandPrompt("Point to move from")
    gp.Get()
    if gp.CommandResult() != Result.Success:
        return gp.CommandResult()
    start_point = gp.Point()

    gp.SetCommandPrompt("Point to move to")
    gp.SetBasePoint(start_point, False)
    gp.DrawLineFromPoint(start_point, True)
    gp.Get()
    if gp.CommandResult() != Result.Success:
        return gp.CommandResult()
    end_point = gp.Point()

    xform = Transform.Translation(end_point - start_point)

    for obj_ref in obj_refs:
        doc.Objects.Transform(obj_ref, xform, True)

    doc.Views.Redraw()
    return Result.Success

if __name__ == "__main__":
    RunCommand()
```

</div>
