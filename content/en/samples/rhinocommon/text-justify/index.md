+++
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to set text justification with a specific font."
keywords = [ "justifying", "text", "entities" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Text Justify"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/textjustify"
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
  public static Result TextJustify(RhinoDoc doc)
  {
    var text_entity = new TextEntity
    {
      Plane = Plane.WorldXY,
      Text = "Hello Rhino!",
      Justification = TextJustification.MiddleCenter,
      FontIndex = doc.Fonts.FindOrCreate("Arial", false, false)
    };

    doc.Objects.AddText(text_entity);
    doc.Views.Redraw();

    return Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function TextJustify(ByVal doc As RhinoDoc) As Result
	Dim text_entity = New TextEntity With {.Plane = Plane.WorldXY, .Text = "Hello Rhino!", .Justification = TextJustification.MiddleCenter, .FontIndex = doc.Fonts.FindOrCreate("Arial", False, False)}

	doc.Objects.AddText(text_entity)
	doc.Views.Redraw()

	Return Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
from scriptcontext import doc
from Rhino.Geometry import *

text_entity = TextEntity()
text_entity.Plane = Plane.WorldXY
text_entity.Text = "Hello Rhino!"
text_entity.Justification = TextJustification.MiddleCenter
text_entity.FontIndex = doc.Fonts.FindOrCreate("Arial", False, False)

doc.Objects.AddText(text_entity)
doc.Views.Redraw()
```

</div>
