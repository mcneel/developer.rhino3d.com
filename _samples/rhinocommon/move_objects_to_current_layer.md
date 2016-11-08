---
title: Move Objects to Current Layer
description: Demonstrates how to move object to the currently active layer.
author: ['Steve Baer', '@stevebaer']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Adding Objects', 'Layers']
origin: http://wiki.mcneel.com/developer/rhinocommonsamples/moveobjectstocurrentlayer
order: 1
keywords: ['move', 'selected', 'objects', 'current', 'layer']
layout: code-sample-rhinocommon
---

```cs
partial class Examples
{
  public static Result MoveObjectsToCurrentLayer(RhinoDoc doc)
  {
    // all non-light objects that are selected
    var object_enumerator_settings = new ObjectEnumeratorSettings();
    object_enumerator_settings.IncludeLights = false;
    object_enumerator_settings.IncludeGrips = true;
    object_enumerator_settings.NormalObjects = true;
    object_enumerator_settings.LockedObjects = true;
    object_enumerator_settings.HiddenObjects = true;
    object_enumerator_settings.ReferenceObjects = true;
    object_enumerator_settings.SelectedObjectsFilter = true;
    var selected_objects = doc.Objects.GetObjectList(object_enumerator_settings);

    var current_layer_index = doc.Layers.CurrentLayerIndex;
    foreach (var selected_object in selected_objects)
    {
      selected_object.Attributes.LayerIndex = current_layer_index;
      selected_object.CommitChanges();
    }
    doc.Views.Redraw();
    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function MoveObjectsToCurrentLayer(ByVal doc As RhinoDoc) As Result
	' all non-light objects that are selected
	Dim object_enumerator_settings = New ObjectEnumeratorSettings()
	object_enumerator_settings.IncludeLights = False
	object_enumerator_settings.IncludeGrips = True
	object_enumerator_settings.NormalObjects = True
	object_enumerator_settings.LockedObjects = True
	object_enumerator_settings.HiddenObjects = True
	object_enumerator_settings.ReferenceObjects = True
	object_enumerator_settings.SelectedObjectsFilter = True
	Dim selected_objects = doc.Objects.GetObjectList(object_enumerator_settings)

	Dim current_layer_index = doc.Layers.CurrentLayerIndex
	For Each selected_object In selected_objects
	  selected_object.Attributes.LayerIndex = current_layer_index
	  selected_object.CommitChanges()
	Next selected_object
	doc.Views.Redraw()
	Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
from Rhino import *
from Rhino.Commands import *
from Rhino.DocObjects import *
from scriptcontext import doc

def RunCommand():
  # all non-light objects that are selected
  object_enumerator_settings = ObjectEnumeratorSettings()
  object_enumerator_settings.IncludeLights = False
  object_enumerator_settings.IncludeGrips = True
  object_enumerator_settings.NormalObjects = True
  object_enumerator_settings.LockedObjects = True
  object_enumerator_settings.HiddenObjects = True
  object_enumerator_settings.ReferenceObjects = True
  object_enumerator_settings.SelectedObjectsFilter = True
  selected_objects = doc.Objects.GetObjectList(object_enumerator_settings)

  current_layer_index = doc.Layers.CurrentLayerIndex
  for selected_object in selected_objects:
    selected_object.Attributes.LayerIndex = current_layer_index
    selected_object.CommitChanges()

  doc.Views.Redraw()
  return Result.Success

if __name__ == "__main__":
  RunCommand()
```
{: #py .tab-pane .fade .in}
