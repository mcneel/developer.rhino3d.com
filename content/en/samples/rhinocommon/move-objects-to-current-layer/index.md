+++
aliases = ["/en/5/samples/rhinocommon/move-objects-to-current-layer/", "/en/6/samples/rhinocommon/move-objects-to-current-layer/", "/en/7/samples/rhinocommon/move-objects-to-current-layer/", "/en/wip/samples/rhinocommon/move-objects-to-current-layer/"]
authors = [ "steve" ]
categories = [ "Adding Objects", "Layers" ]
description = "Demonstrates how to move object to the currently active layer."
keywords = [ "move", "selected", "objects", "current", "layer" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Move Objects to Current Layer"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/moveobjectstocurrentlayer"
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

</div>


<div class="codetab-content" id="vb">

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

</div>


<div class="codetab-content" id="py">

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

</div>
