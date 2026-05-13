+++
aliases = ["/en/5/samples/rhinocommon/orthogonal-mode/", "/en/6/samples/rhinocommon/orthogonal-mode/", "/en/7/samples/rhinocommon/orthogonal-mode/", "/en/wip/samples/rhinocommon/orthogonal-mode/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to enable or disable orthogonal mode and its effects."
keywords = [ "enabling", "orthogonal", "mode" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Orthogonal Mode"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/ortho"
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
  public static Result Ortho(RhinoDoc doc)
  {
    var gp = new GetPoint();
    gp.SetCommandPrompt("Start of line");
    gp.Get();
    if (gp.CommandResult() != Result.Success)
      return gp.CommandResult();
    var start_point = gp.Point();

    var original_ortho = ModelAidSettings.Ortho;
    if (!original_ortho)
      ModelAidSettings.Ortho = true;

    gp.SetCommandPrompt("End of line");
    gp.SetBasePoint(start_point, false);
    gp.DrawLineFromPoint(start_point, true);
    gp.Get();
    if (gp.CommandResult() != Result.Success)
      return gp.CommandResult();
    var end_point = gp.Point();

    if (ModelAidSettings.Ortho != original_ortho)
      ModelAidSettings.Ortho = original_ortho;

    doc.Objects.AddLine(start_point, end_point);
    doc.Views.Redraw();
    return Result.Success;
  }
}
```

</div>

<div class="codetab-content" id="py">

```python
from Rhino import *
from Rhino.ApplicationSettings import *
from Rhino.Commands import *
from Rhino.Input.Custom import *
from scriptcontext import doc

def RunCommand():
    gp = GetPoint()
    gp.SetCommandPrompt("Start of line")
    gp.Get()
    if gp.CommandResult() != Result.Success:
        return gp.CommandResult()
    start_point = gp.Point()

    original_ortho = ModelAidSettings.Ortho
    if not original_ortho:
        ModelAidSettings.Ortho = True

    gp.SetCommandPrompt("End of line")
    gp.SetBasePoint(start_point, False)
    gp.DrawLineFromPoint(start_point, True)
    gp.Get()
    if gp.CommandResult() != Result.Success:
        return gp.CommandResult()
    end_point = gp.Point()

    if ModelAidSettings.Ortho != original_ortho:
        ModelAidSettings.Ortho = original_ortho

    doc.Objects.AddLine(start_point, end_point)
    doc.Views.Redraw()
    return Result.Success

if __name__ == "__main__":
    RunCommand()
```

</div>
