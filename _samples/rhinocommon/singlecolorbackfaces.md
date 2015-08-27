---
layout: code-sample
author:
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
title: Single Color Back Faces
keywords: ['single', 'color', 'back', 'faces']
categories: ['Other']
description:
order: 1
---

```cs
partial class Examples
{
  public static Result SingleColorBackfaces(RhinoDoc doc)
  {
    var display_mode_descs = //DisplayModeDescription.GetDisplayModes();
      from dm in DisplayModeDescription.GetDisplayModes()
      where dm.EnglishName == "Shaded"
      select dm;

    foreach (var dmd in display_mode_descs)
    {
      RhinoApp.WriteLine("CurveColor {0}", dmd.DisplayAttributes.CurveColor.ToKnownColor());
      RhinoApp.WriteLine("ObjectColor {0}", dmd.DisplayAttributes.ObjectColor.ToKnownColor());
    }
    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function SingleColorBackfaces(ByVal doc As RhinoDoc) As Result
	Dim display_mode_descs = From dm In DisplayModeDescription.GetDisplayModes()
	                         Where dm.EnglishName = "Shaded"
	                         Select dm 'DisplayModeDescription.GetDisplayModes();

	For Each dmd In display_mode_descs
	  RhinoApp.WriteLine("CurveColor {0}", dmd.DisplayAttributes.CurveColor.ToKnownColor())
	  RhinoApp.WriteLine("ObjectColor {0}", dmd.DisplayAttributes.ObjectColor.ToKnownColor())
	Next dmd
	Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}

