+++
aliases = ["/5/samples/rhinocommon/tweak-colors/", "/6/samples/rhinocommon/tweak-colors/", "/7/samples/rhinocommon/tweak-colors/", "/wip/samples/rhinocommon/tweak-colors/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to set the default paint colors in Rhino."
keywords = [ "tweak", "colors" ]
languages = [ "C#", "VB" ]
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


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function TweakColors(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Rhino.ApplicationSettings.AppearanceSettings.SetPaintColor(Rhino.ApplicationSettings.PaintColor.NormalStart, System.Drawing.Color.AliceBlue)
	Rhino.ApplicationSettings.AppearanceSettings.SetPaintColor(Rhino.ApplicationSettings.PaintColor.NormalEnd, System.Drawing.Color.AliceBlue)
	Rhino.ApplicationSettings.AppearanceSettings.SetPaintColor(Rhino.ApplicationSettings.PaintColor.NormalBorder, System.Drawing.Color.LightBlue)
	Rhino.ApplicationSettings.AppearanceSettings.SetPaintColor(Rhino.ApplicationSettings.PaintColor.HotStart, System.Drawing.Color.LightBlue)
	Rhino.ApplicationSettings.AppearanceSettings.SetPaintColor(Rhino.ApplicationSettings.PaintColor.HotEnd, System.Drawing.Color.LightBlue, True)
	Return Rhino.Commands.Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
# No Python sample available
```

</div>

