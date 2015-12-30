---
layout: code-sample-rhinocommon
author:
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
title: Tweak Colors
keywords: ['tweak', 'colors']
categories: ['Other']
description:
order: 1
---

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
{: #cs .tab-pane .fade .in .active}


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
{: #vb .tab-pane .fade .in}


```python
# No Python sample available
```
{: #py .tab-pane .fade .in}

