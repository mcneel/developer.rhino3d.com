+++
aliases = ["/en/5/samples/rhinocommon/add-objects-to-group/", "/en/6/samples/rhinocommon/add-objects-to-group/", "/en/7/samples/rhinocommon/add-objects-to-group/", "/wip/samples/rhinocommon/add-objects-to-group/"]
authors = [ "steve" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to group objects from a user-specified selection set of objects."
keywords = [ "add", "objects", "group" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Add Objects to Group"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/addobjectstogroup"
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
  public static Rhino.Commands.Result AddObjectsToGroup(Rhino.RhinoDoc doc)
  {
    Rhino.Input.Custom.GetObject go = new Rhino.Input.Custom.GetObject();
    go.SetCommandPrompt("Select objects to group");
    go.GroupSelect = true;
    go.GetMultiple(1, 0);
    if (go.CommandResult() != Rhino.Commands.Result.Success)
      return go.CommandResult();

    List<Guid> ids = new List<Guid>();
    for (int i = 0; i < go.ObjectCount; i++)
    {
      ids.Add(go.Object(i).ObjectId);
    }
    int index = doc.Groups.Add(ids);
    doc.Views.Redraw();
    if (index >= 0)
      return Rhino.Commands.Result.Success;
    return Rhino.Commands.Result.Failure;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function AddObjectsToGroup(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim go As New Rhino.Input.Custom.GetObject()
	go.SetCommandPrompt("Select objects to group")
	go.GroupSelect = True
	go.GetMultiple(1, 0)
	If go.CommandResult() <> Rhino.Commands.Result.Success Then
	  Return go.CommandResult()
	End If

	Dim ids As New List(Of Guid)()
	For i As Integer = 0 To go.ObjectCount - 1
	  ids.Add(go.Object(i).ObjectId)
	Next i
	Dim index As Integer = doc.Groups.Add(ids)
	doc.Views.Redraw()
	If index >= 0 Then
	  Return Rhino.Commands.Result.Success
	End If
	Return Rhino.Commands.Result.Failure
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
import Rhino
import scriptcontext

def AddObjectsToGroup():
    go = Rhino.Input.Custom.GetObject()
    go.SetCommandPrompt("Select objects to group")
    go.GroupSelect = True
    go.GetMultiple(1, 0)
    if go.CommandResult()!=Rhino.Commands.Result.Success:
        return go.CommandResult()

    ids = [go.Object(i).ObjectId for i in range(go.ObjectCount)]
    index = scriptcontext.doc.Groups.Add(ids)
    scriptcontext.doc.Views.Redraw()
    if index>=0: return Rhino.Commands.Result.Success
    return Rhino.Commands.Result.Failure


if __name__ == "__main__":
    AddObjectsToGroup()
```

</div>
