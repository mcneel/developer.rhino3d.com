+++
aliases = ["/en/5/samples/rhinocommon/copy-groups/", "/en/6/samples/rhinocommon/copy-groups/", "/en/7/samples/rhinocommon/copy-groups/", "/wip/samples/rhinocommon/copy-groups/"]
authors = [ "steve" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to duplicate objects with grouping."
keywords = [ "duplicating", "objects", "with", "group" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Copy Groups"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/copygroups"
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
  public static Result CopyGroups(RhinoDoc doc)
  {
    var go = new Rhino.Input.Custom.GetObject();
    go.SetCommandPrompt("Select objects to copy in place");
    go.GroupSelect = true;
    go.SubObjectSelect = false;
    go.GetMultiple(1, 0);
    if (go.CommandResult() != Result.Success)
      return go.CommandResult();

    var xform = Transform.Identity;
    var group_map = new Dictionary<int, int>();

    foreach (var obj_ref in go.Objects())
    {
      if (obj_ref != null)
      {
        var obj = obj_ref.Object();
        var duplicate = doc.Objects.Transform(obj_ref.ObjectId, xform, false);
        RhinoUpdateObjectGroups(ref obj, ref group_map);
      }
    }
    doc.Views.Redraw();
    return Result.Success;
  }

  static void RhinoUpdateObjectGroups(ref RhinoObject obj, ref Dictionary<int, int> group_map)
  {
    if (obj == null) return;

    int attrib_group_count = obj.Attributes.GroupCount;
    if (attrib_group_count == 0) return;

    var doc = obj.Document;
    if (doc == null) return;

    var groups = doc.Groups;

    int group_count = groups.Count;
    if (group_count == 0) return;

    if (group_map.Count == 0)
      for (int i = 0; i < group_count; i++)
        group_map.Add(i, -1);

    var attributes = obj.Attributes;
    var group_list = attributes.GetGroupList();
    if (group_list == null) return;
    attrib_group_count = group_list.Length;

    for (int i = 0; i < attrib_group_count; i++)
    {
      int old_group_index = group_list[i];
      int new_group_index = group_map[old_group_index];
      if (new_group_index == -1)
      {
        new_group_index = doc.Groups.Add();
        group_map[old_group_index] = new_group_index;
      }
      group_list[i] = new_group_index;
    }

    attributes.RemoveFromAllGroups();
    for (int i = 0; i < attrib_group_count; i++)
      attributes.AddToGroup(group_list[i]);

    obj.CommitChanges();
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function CopyGroups(ByVal doc As RhinoDoc) As Result
	Dim go = New Rhino.Input.Custom.GetObject()
	go.SetCommandPrompt("Select objects to copy in place")
	go.GroupSelect = True
	go.SubObjectSelect = False
	go.GetMultiple(1, 0)
	If go.CommandResult() <> Result.Success Then
	  Return go.CommandResult()
	End If

	Dim xform = Transform.Identity
	Dim group_map = New Dictionary(Of Integer, Integer)()

	For Each obj_ref In go.Objects()
	  If obj_ref IsNot Nothing Then
		Dim obj = obj_ref.Object()
		Dim duplicate = doc.Objects.Transform(obj_ref.ObjectId, xform, False)
		RhinoUpdateObjectGroups(obj, group_map)
	  End If
	Next obj_ref
	doc.Views.Redraw()
	Return Result.Success
  End Function

  Private Shared Sub RhinoUpdateObjectGroups(ByRef obj As RhinoObject, ByRef group_map As Dictionary(Of Integer, Integer))
	If obj Is Nothing Then
		Return
	End If

	Dim attrib_group_count As Integer = obj.Attributes.GroupCount
	If attrib_group_count = 0 Then
		Return
	End If

	Dim doc = obj.Document
	If doc Is Nothing Then
		Return
	End If

	Dim groups = doc.Groups

	Dim group_count As Integer = groups.Count
	If group_count = 0 Then
		Return
	End If

	If group_map.Count = 0 Then
	  For i As Integer = 0 To group_count - 1
		group_map.Add(i, -1)
	  Next i
	End If

	Dim attributes = obj.Attributes
	Dim group_list = attributes.GetGroupList()
	If group_list Is Nothing Then
		Return
	End If
	attrib_group_count = group_list.Length

	For i As Integer = 0 To attrib_group_count - 1
	  Dim old_group_index As Integer = group_list(i)
	  Dim new_group_index As Integer = group_map(old_group_index)
	  If new_group_index = -1 Then
		new_group_index = doc.Groups.Add()
		group_map(old_group_index) = new_group_index
	  End If
	  group_list(i) = new_group_index
	Next i

	attributes.RemoveFromAllGroups()
	For i As Integer = 0 To attrib_group_count - 1
	  attributes.AddToGroup(group_list(i))
	Next i

	obj.CommitChanges()
  End Sub
End Class
```

</div>


<div class="codetab-content" id="py">

```python
import Rhino
from Rhino.Commands import *
from scriptcontext import doc

def RhinoUpdateObjectGroups(obj, group_map):
    if obj == None: return

    attrib_group_count = obj.Attributes.GroupCount
    if attrib_group_count == 0: return

    doc = obj.Document
    if doc == None: return

    groups = doc.Groups

    group_count = groups.Count
    if group_count == 0: return

    if group_map.Count == 0:
        for i in range(0, group_count):
            group_map.append(-1)

    attributes = obj.Attributes
    group_list = attributes.GetGroupList()
    if group_list == None: return
    attrib_group_count = group_list.Length

    for i in range(0, attrib_group_count):
        old_group_index = group_list[i]
        new_group_index = group_map[old_group_index]
        if new_group_index == -1:
            new_group_index = doc.Groups.Add()
            group_map[old_group_index] = new_group_index
        group_list[i] = new_group_index

    attributes.RemoveFromAllGroups()
    for i in range(0, attrib_group_count):
        attributes.AddToGroup(group_list[i])

    obj.CommitChanges()

def RunCommand():
    go = Rhino.Input.Custom.GetObject()
    go.SetCommandPrompt("Select objects to copy in place")
    go.GroupSelect = True
    go.SubObjectSelect = False
    go.GetMultiple(1, 0)
    if go.CommandResult() != Result.Success:
        return go.CommandResult()

    xform = Rhino.Geometry.Transform.Identity
    group_map = []

    for obj_ref in go.Objects():
        if obj_ref != None:
            obj = obj_ref.Object()
            duplicate = doc.Objects.Transform(obj_ref.ObjectId, xform, False)
            RhinoUpdateObjectGroups(obj, group_map)
    doc.Views.Redraw()
    return Result.Success

if __name__ == "__main__":
    RunCommand()
```

</div>
