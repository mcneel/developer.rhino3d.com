+++
aliases = ["/5/samples/rhinocommon/dynamically-drawing-text-strings/", "/6/samples/rhinocommon/dynamically-drawing-text-strings/", "/7/samples/rhinocommon/dynamically-drawing-text-strings/", "/wip/samples/rhinocommon/dynamically-drawing-text-strings/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to dynamically draw text strings relative to a given screen to world transform."
keywords = [ "dynamically", "drawing", "text", "strings" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Dynamically Drawing Text Strings"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/drawstring"
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
  public static Result DrawString(RhinoDoc doc)
  {
    var gp = new GetDrawStringPoint();
    gp.SetCommandPrompt("Point");
    gp.Get();
    return gp.CommandResult();
  }
}

public class GetDrawStringPoint : GetPoint
{
  protected override void OnDynamicDraw(GetPointDrawEventArgs e)
  {
    base.OnDynamicDraw(e);
    var xform = e.Viewport.GetTransform(CoordinateSystem.World, CoordinateSystem.Screen);
    var current_point = e.CurrentPoint;
    current_point.Transform(xform);
    var screen_point = new Point2d(current_point.X, current_point.Y);
    var msg = string.Format("screen {0:F}, {1:F}", current_point.X, current_point.Y);
    e.Display.Draw2dText(msg, System.Drawing.Color.Blue, screen_point, false);
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function DrawString(ByVal doc As RhinoDoc) As Result
	Dim gp = New GetDrawStringPoint()
	gp.SetCommandPrompt("Point")
	gp.Get()
	Return gp.CommandResult()
  End Function
End Class

Public Class GetDrawStringPoint
	Inherits GetPoint

  Protected Overrides Sub OnDynamicDraw(ByVal e As GetPointDrawEventArgs)
	MyBase.OnDynamicDraw(e)
	Dim xform = e.Viewport.GetTransform(CoordinateSystem.World, CoordinateSystem.Screen)
	Dim current_point = e.CurrentPoint
	current_point.Transform(xform)
	Dim screen_point = New Point2d(current_point.X, current_point.Y)
	Dim msg = String.Format("screen {0:F}, {1:F}", current_point.X, current_point.Y)
	e.Display.Draw2dText(msg, System.Drawing.Color.Blue, screen_point, False)
  End Sub
End Class
```

</div>


<div class="codetab-content" id="py">

```python
from Rhino import *
from Rhino.DocObjects import *
from Rhino.Geometry import *
from Rhino.Commands import *
from Rhino.Input.Custom import *
from System.Drawing import Color

def RunCommand():
    gp = GetDrawStringPoint()
    gp.SetCommandPrompt("Point")
    gp.Get()
    return gp.CommandResult()

class GetDrawStringPoint(GetPoint):
    def OnDynamicDraw(self, e):
        xform = e.Viewport.GetTransform(CoordinateSystem.World, CoordinateSystem.Screen)

        current_point = e.CurrentPoint
        current_point.Transform(xform)
        screen_point = Point2d(current_point.X, current_point.Y)

        msg = "screen {0}, {1}".format(screen_point.X, screen_point.Y)
        e.Display.Draw2dText(msg, Color.Blue, screen_point, False)

if __name__ == "__main__":
    RunCommand()
```

</div>
