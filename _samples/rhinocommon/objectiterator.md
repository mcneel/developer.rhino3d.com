---
layout: code-sample
title: Iterate through Rhino's Geometry Table
author: 
categories: ['Other'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['iterate', 'through', 'rhinos', 'geometry', 'table']
order: 123
description:  
---



```cs
public class ObjectEnumeratorCommand : Command
{
  public override string EnglishName
  {
    get { return "csObjectEnumerator"; }
  }

  protected override Result RunCommand(RhinoDoc doc, RunMode mode)
  {
    var object_enumerator_settings = new ObjectEnumeratorSettings();
    object_enumerator_settings.IncludeLights = true;
    object_enumerator_settings.IncludeGrips = false;
    var rhino_objects = doc.Objects.GetObjectList(object_enumerator_settings);

    int count = 0;
    foreach (var rhino_object in rhino_objects)
    {
      if (rhino_object.IsSelectable() && rhino_object.IsSelected(false) == 0)
      {
        rhino_object.Select(true);
        count++;
      }
    }
    if (count > 0)
    {
      doc.Views.Redraw();
      RhinoApp.WriteLine("{0} object{1} selected", count,
        count == 1 ? "" : "s");
    }
    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Public Class ObjectEnumeratorCommand
  Inherits Command
  Public Overrides ReadOnly Property EnglishName() As String
    Get
      Return "vbObjectEnumerator"
    End Get
  End Property

  Protected Overrides Function RunCommand(doc As RhinoDoc, mode As RunMode) As Result
    Dim object_enumerator_settings = New ObjectEnumeratorSettings()
    object_enumerator_settings.IncludeLights = True
    object_enumerator_settings.IncludeGrips = False
    Dim rhino_objects = doc.Objects.GetObjectList(object_enumerator_settings)

    Dim count As Integer = 0
    For Each rhino_object As RhinoObject In rhino_objects
      If rhino_object.IsSelectable() AndAlso rhino_object.IsSelected(False) = 0 Then
        rhino_object.[Select](True)
        count += 1
      End If
    Next
    If count > 0 Then
      doc.Views.Redraw()
      RhinoApp.WriteLine("{0} object{1} selected", count, If(count = 1, "", "s"))
    End If
    Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
from Rhino import *
from Rhino.DocObjects import *
from Rhino.Commands import *
from scriptcontext import doc

def RunCommand():
  object_enumerator_settings = ObjectEnumeratorSettings()
  object_enumerator_settings.IncludeLights = True
  object_enumerator_settings.IncludeGrips = False
  rhino_objects = doc.Objects.GetObjectList(object_enumerator_settings)

  count = 0
  for rhino_object in rhino_objects:
    if rhino_object.IsSelectable() and rhino_object.IsSelected(False) == 0:
      rhino_object.Select(True)
      count += 1;

  if count > 0:
    doc.Views.Redraw()
    RhinoApp.WriteLine("{0} object{1} selected", count,
      "" if count == 1 else "s")

  return Result.Success

if __name__ == "__main__":
  RunCommand()
```
{: #py .tab-pane .fade .in}


