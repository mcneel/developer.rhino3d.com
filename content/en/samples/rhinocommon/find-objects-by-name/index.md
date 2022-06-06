+++
aliases = ["/5/samples/rhinocommon/find-objects-by-name/", "/6/samples/rhinocommon/find-objects-by-name/", "/7/samples/rhinocommon/find-objects-by-name/", "/wip/samples/rhinocommon/find-objects-by-name/"]
authors = [ "steve" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to find objects by their name or label."
keywords = [ "find", "objects", "name" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Find Objects by Name"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/findobjectsbyname"
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
  public static Rhino.Commands.Result FindObjectsByName(Rhino.RhinoDoc doc)
  {
    const string name = "abc";
    Rhino.DocObjects.ObjectEnumeratorSettings settings = new Rhino.DocObjects.ObjectEnumeratorSettings();
    settings.NameFilter = name;
    System.Collections.Generic.List<Guid> ids = new System.Collections.Generic.List<Guid>();
    foreach (Rhino.DocObjects.RhinoObject rhObj in doc.Objects.GetObjectList(settings))
      ids.Add(rhObj.Id);

    if (ids.Count == 0)
    {
      Rhino.RhinoApp.WriteLine("No objects with the name " + name);
      return Rhino.Commands.Result.Failure;
    }

    Rhino.RhinoApp.WriteLine("Found {0} objects", ids.Count);
    foreach (Guid id in ids)
      Rhino.RhinoApp.WriteLine("  {0}", id);

    return Rhino.Commands.Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function FindObjectsByName(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Const name As String = "abc"
	Dim settings As New Rhino.DocObjects.ObjectEnumeratorSettings()
	settings.NameFilter = name
	Dim ids As New System.Collections.Generic.List(Of Guid)()
	For Each rhObj As Rhino.DocObjects.RhinoObject In doc.Objects.GetObjectList(settings)
	  ids.Add(rhObj.Id)
	Next rhObj

	If ids.Count = 0 Then
	  Rhino.RhinoApp.WriteLine("No objects with the name " & name)
	  Return Rhino.Commands.Result.Failure
	End If

	Rhino.RhinoApp.WriteLine("Found {0} objects", ids.Count)
	For Each id As Guid In ids
	  Rhino.RhinoApp.WriteLine("  {0}", id)
	Next id

	Return Rhino.Commands.Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
import Rhino
import scriptcontext
import System.Guid

def FindObjectsByName():
    name = "abc"
    settings = Rhino.DocObjects.ObjectEnumeratorSettings()
    settings.NameFilter = name
    ids = [rhobj.Id for rhobj in scriptcontext.doc.Objects.GetObjectList(settings)]
    if not ids:
        print "No objects with the name", name
        return Rhino.Commands.Result.Failure
    else:
        print "Found", len(ids), "objects"
        for id in ids: print "  ", id
    return Rhino.Commands.Result.Success

if __name__ == "__main__":
    FindObjectsByName()
```

</div>
