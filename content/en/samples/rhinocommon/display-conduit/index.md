+++
aliases = ["/en/5/samples/rhinocommon/display-conduit/", "/en/6/samples/rhinocommon/display-conduit/", "/en/7/samples/rhinocommon/display-conduit/", "/en/wip/samples/rhinocommon/display-conduit/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates a basic display conduit that draws a custom axis in the Rhino viewport."
keywords = [ "display", "conduit", "introduction", "rhinocommon" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Display Conduit"
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
  static MyConduit m_conduit;
  public static Result DisplayConduit(RhinoDoc doc)
  {
    // The following code lets you toggle the conduit on and off by repeatedly running the command
    if (m_conduit != null)
    {
      m_conduit.Enabled = false;
      m_conduit = null;
    }
    else
    {
      m_conduit = new MyConduit { Enabled = true };
    }
    doc.Views.Redraw();
    return Result.Success;
  }
}

class MyConduit : Rhino.Display.DisplayConduit
{
  protected override void CalculateBoundingBox(CalculateBoundingBoxEventArgs e)
  {
    base.CalculateBoundingBox(e);
    e.BoundingBox.Union(e.Display.Viewport.ConstructionPlane().Origin);
  }

  protected override void PreDrawObjects(DrawEventArgs e)
  {
    base.PreDrawObjects(e);

    var c_plane = e.Display.Viewport.ConstructionPlane();
    var x_color = Rhino.ApplicationSettings.AppearanceSettings.GridXAxisLineColor;
    var y_color = Rhino.ApplicationSettings.AppearanceSettings.GridYAxisLineColor;
    var z_color = Rhino.ApplicationSettings.AppearanceSettings.GridZAxisLineColor;

    e.Display.PushDepthWriting(false);
    e.Display.PushDepthTesting(false);

    e.Display.DrawPoint(c_plane.Origin, System.Drawing.Color.White);
    e.Display.DrawArrow(new Line(c_plane.Origin, new Vector3d(c_plane.XAxis) * 10.0), x_color);
    e.Display.DrawArrow(new Line(c_plane.Origin, new Vector3d(c_plane.YAxis) * 10.0), y_color);
    e.Display.DrawArrow(new Line(c_plane.Origin, new Vector3d(c_plane.ZAxis) * 10.0), z_color);

    e.Display.PopDepthWriting();
    e.Display.PopDepthTesting();
  }
}
```

</div>

<div class="codetab-content" id="py">

```python
#! python 3
import Rhino
import System
import scriptcontext as sc


class MyConduit(Rhino.Display.DisplayConduit):
    def __init__(self):
        super().__init__()

    def CalculateBoundingBox(self, e):
        e.BoundingBox.Union(e.Display.Viewport.ConstructionPlane().Origin)

    def PreDrawObjects(self, e):
        c_plane = e.Display.Viewport.ConstructionPlane()
        x_color = Rhino.ApplicationSettings.AppearanceSettings.GridXAxisLineColor
        y_color = Rhino.ApplicationSettings.AppearanceSettings.GridYAxisLineColor
        z_color = Rhino.ApplicationSettings.AppearanceSettings.GridZAxisLineColor

        e.Display.PushDepthWriting(False)
        e.Display.PushDepthTesting(False)

        e.Display.DrawPoint(c_plane.Origin, System.Drawing.Color.White)
        e.Display.DrawArrow(
            Rhino.Geometry.Line(c_plane.Origin, Rhino.Geometry.Vector3d(c_plane.XAxis) * 10.0),
            x_color,
        )
        e.Display.DrawArrow(
            Rhino.Geometry.Line(c_plane.Origin, Rhino.Geometry.Vector3d(c_plane.YAxis) * 10.0),
            y_color,
        )
        e.Display.DrawArrow(
            Rhino.Geometry.Line(c_plane.Origin, Rhino.Geometry.Vector3d(c_plane.ZAxis) * 10.0),
            z_color,
        )

        e.Display.PopDepthWriting()
        e.Display.PopDepthTesting()


def RunCommand():
    # The following code lets you toggle the conduit on and off by repeatedly running the command
    conduit = sc.sticky.get("my_conduit")
    if conduit is not None:
        conduit.Enabled = False
        sc.sticky["my_conduit"] = None
    else:
        conduit = MyConduit()
        conduit.Enabled = True
        sc.sticky["my_conduit"] = conduit
    sc.doc.Views.Redraw()
    return Rhino.Commands.Result.Success


if __name__ == "__main__":
    RunCommand()
```

</div>
