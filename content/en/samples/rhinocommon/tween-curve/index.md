+++
aliases = ["/en/5/samples/rhinocommon/tween-curve/", "/en/6/samples/rhinocommon/tween-curve/", "/en/7/samples/rhinocommon/tween-curve/", "/en/wip/samples/rhinocommon/tween-curve/"]
authors = [ "steve" ]
categories = [ "Curves" ]
description = "Demonstrates how to tween two curves."
keywords = [ "tween", "curve" ]
languages = [ "C#" ]
sdk = [ "RhinoCommon" ]
title = "Tween Curve"
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
  public static Rhino.Commands.Result TweenCurve(Rhino.RhinoDoc doc)
  {
    Rhino.Input.Custom.GetObject go = new Rhino.Input.Custom.GetObject();
    go.SetCommandPrompt("Select two curves");
    go.GeometryFilter = Rhino.DocObjects.ObjectType.Curve;
    go.GetMultiple(2, 2);
    if (go.CommandResult() != Rhino.Commands.Result.Success)
      return go.CommandResult();

    Rhino.Geometry.Curve curve0 = go.Object(0).Curve();
    Rhino.Geometry.Curve curve1 = go.Object(1).Curve();
    if (null != curve0 && null != curve1)
    {
      Rhino.Geometry.Curve[] curves = Rhino.Geometry.Curve.CreateTweenCurves(curve0, curve1, 1);
      if (null != curves)
      {
        for (int i = 0; i < curves.Length; i++)
          doc.Objects.AddCurve(curves[i]);

        doc.Views.Redraw();
        return Rhino.Commands.Result.Success;
      }
    }

    return Rhino.Commands.Result.Failure;
  }
}
```

</div>

<div class="codetab-content" id="py">

```python
# No Python sample available
```

</div>
