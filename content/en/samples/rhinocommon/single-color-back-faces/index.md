+++
aliases = ["/en/5/samples/rhinocommon/single-color-back-faces/", "/en/6/samples/rhinocommon/single-color-back-faces/", "/en/7/samples/rhinocommon/single-color-back-faces/", "/en/wip/samples/rhinocommon/single-color-back-faces/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to determine the curve and object colors of back faces."
keywords = [ "single", "color", "back", "faces" ]
languages = [ "C#", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Single Color Back Faces"
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

</div>


<div class="codetab-content" id="vb">

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

</div>


<div class="codetab-content" id="py">

```python
# No Python sample available
```

</div>

