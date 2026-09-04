+++
aliases = ["/en/5/samples/rhinocommon/tweak-colors/", "/en/6/samples/rhinocommon/tweak-colors/", "/en/7/samples/rhinocommon/tweak-colors/", "/en/wip/samples/rhinocommon/tweak-colors/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to set the default paint colors in Rhino."
keywords = [ "tweak", "colors" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Tweak Colors"
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
  public static Rhino.Commands.Result TweakColors(Rhino.RhinoDoc doc)
  {
    Rhino.ApplicationSettings.AppearanceSettings.SetPaintColor(Rhino.ApplicationSettings.PaintColor.NormalStart, System.Drawing.Color.AliceBlue);
    Rhino.ApplicationSettings.AppearanceSettings.SetPaintColor(Rhino.ApplicationSettings.PaintColor.NormalEnd, System.Drawing.Color.AliceBlue);
    Rhino.ApplicationSettings.AppearanceSettings.SetPaintColor(Rhino.ApplicationSettings.PaintColor.NormalBorder, System.Drawing.Color.LightBlue);
    Rhino.ApplicationSettings.AppearanceSettings.SetPaintColor(Rhino.ApplicationSettings.PaintColor.HotStart, System.Drawing.Color.LightBlue);
    Rhino.ApplicationSettings.AppearanceSettings.SetPaintColor(Rhino.ApplicationSettings.PaintColor.HotEnd, System.Drawing.Color.LightBlue, true);
    return Rhino.Commands.Result.Success;
  }
}
```

</div>

<div class="codetab-content" id="py">

```python
#! python 3
import Rhino
import System

def RunCommand():
    Rhino.ApplicationSettings.AppearanceSettings.SetPaintColor(Rhino.ApplicationSettings.PaintColor.NormalStart, System.Drawing.Color.AliceBlue)
    Rhino.ApplicationSettings.AppearanceSettings.SetPaintColor(Rhino.ApplicationSettings.PaintColor.NormalEnd, System.Drawing.Color.AliceBlue)
    Rhino.ApplicationSettings.AppearanceSettings.SetPaintColor(Rhino.ApplicationSettings.PaintColor.NormalBorder, System.Drawing.Color.LightBlue)
    Rhino.ApplicationSettings.AppearanceSettings.SetPaintColor(Rhino.ApplicationSettings.PaintColor.HotStart, System.Drawing.Color.LightBlue)
    Rhino.ApplicationSettings.AppearanceSettings.SetPaintColor(Rhino.ApplicationSettings.PaintColor.HotEnd, System.Drawing.Color.LightBlue, True)
    return Rhino.Commands.Result.Success

if __name__ == "__main__":
    RunCommand()
```

</div>
