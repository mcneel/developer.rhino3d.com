+++
aliases = ["/en/5/samples/rhinocommon/object-iterator/", "/en/6/samples/rhinocommon/object-iterator/", "/en/7/samples/rhinocommon/object-iterator/", "/wip/samples/rhinocommon/object-iterator/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to iterate (or enumerate) through Rhino's geometry table."
keywords = [ "iterate", "through", "rhinos", "geometry", "table" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Object Iterator"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/objectiterator"
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
  public static Result ObjectIterator(RhinoDoc doc)
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

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function ObjectIterator(ByVal doc As RhinoDoc) As Result
	Dim object_enumerator_settings = New ObjectEnumeratorSettings()
	object_enumerator_settings.IncludeLights = True
	object_enumerator_settings.IncludeGrips = False
	Dim rhino_objects = doc.Objects.GetObjectList(object_enumerator_settings)

	Dim count As Integer = 0
	For Each rhino_object In rhino_objects
	  If rhino_object.IsSelectable() AndAlso rhino_object.IsSelected(False) = 0 Then
		rhino_object.Select(True)
		count += 1
	  End If
	Next rhino_object
	If count > 0 Then
	  doc.Views.Redraw()
	  RhinoApp.WriteLine("{0} object{1} selected", count,If(count = 1, "", "s"))
	End If
	Return Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

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
        RhinoApp.WriteLine("{0} object{1} selected", count, "" if count == 1 else "s")

    return Result.Success

if __name__ == "__main__":
    RunCommand()
```

</div>
