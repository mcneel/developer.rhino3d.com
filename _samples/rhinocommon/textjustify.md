---
layout: code-sample
title: Justifying Text Entities
author: 
categories: ['Other'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['justifying', 'text', 'entities']
order: 161
description:  
---



```cs
public class TextJustifyCommand : Command
{
  public override string EnglishName { get { return "csTextJustify"; } }

  protected override Result RunCommand(RhinoDoc doc, RunMode mode)
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
Public Class TextJustifyCommand
  Inherits Command
  Public Overrides ReadOnly Property EnglishName() As String
    Get
      Return "vbTextJustify"
    End Get
  End Property

  Protected Overrides Function RunCommand(doc As RhinoDoc, mode As RunMode) As Result
    Dim text_entity = New TextEntity()
    text_entity.Plane = Plane.WorldXY
    text_entity.Text = "Hello Rhino!"
    text_entity.Justification = TextJustification.MiddleCenter
    text_entity.FontIndex = doc.Fonts.FindOrCreate("Arial", False, False)

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


