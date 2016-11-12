---
title: Text Justify
description: Demonstrates how to set text justification with a specific font.
authors: ['Steve Baer']
author_contacts: ['stevebaer']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/rhinocommonsamples/textjustify
order: 1
keywords: ['justifying', 'text', 'entities']
layout: code-sample-rhinocommon
---

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
{: #cs .tab-pane .fade .in .active}


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
{: #vb .tab-pane .fade .in}


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
{: #py .tab-pane .fade .in}
