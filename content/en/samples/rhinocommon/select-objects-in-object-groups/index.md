+++
aliases = ["/en/5/samples/rhinocommon/select-objects-in-object-groups/", "/en/6/samples/rhinocommon/select-objects-in-object-groups/", "/en/7/samples/rhinocommon/select-objects-in-object-groups/", "/wip/samples/rhinocommon/select-objects-in-object-groups/"]
authors = [ "steve" ]
categories = [ "Picking and Selection", "Adding Objects" ]
description = "Demonstrates how to select objects that are an object group."
keywords = [ "select", "objects", "groups" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Select Objects in Object Groups"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/selectgroupobject"
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
  public static Result SelectObjectsInObjectGroups(RhinoDoc doc)
  {
    ObjRef obj_ref;
    var rs = RhinoGet.GetOneObject(
      "Select object", false, ObjectType.AnyObject, out obj_ref);
    if (rs != Result.Success)
      return rs;
    var rhino_object = obj_ref.Object();
    if (rhino_object == null)
      return Result.Failure;

    var rhino_object_groups = rhino_object.Attributes.GetGroupList().DefaultIfEmpty(-1);

    var selectable_objects= from obj in doc.Objects.GetObjectList(ObjectType.AnyObject)
                            where obj.IsSelectable(true, false, false, false)
                            select obj;

    foreach (var selectable_object in selectable_objects)
    {
      foreach (var group in selectable_object.Attributes.GetGroupList())
      {
        if (rhino_object_groups.Contains(group))
        {
            selectable_object.Select(true);
            continue;
        }
      }
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
  Public Shared Function SelectObjectsInObjectGroups(ByVal doc As RhinoDoc) As Result
	Dim obj_ref As ObjRef = Nothing
	Dim rs = RhinoGet.GetOneObject("Select object", False, ObjectType.AnyObject, obj_ref)
	If rs IsNot Result.Success Then
	  Return rs
	End If
	Dim rhino_object = obj_ref.Object()
	If rhino_object Is Nothing Then
	  Return Result.Failure
	End If

	Dim rhino_object_groups = rhino_object.Attributes.GetGroupList().DefaultIfEmpty(-1)

	Dim selectable_objects = From obj In doc.Objects.GetObjectList(ObjectType.AnyObject)
	                         Where obj.IsSelectable(True, False, False, False)
	                         Select obj

	For Each selectable_object In selectable_objects
	  For Each group In selectable_object.Attributes.GetGroupList()
		If rhino_object_groups.Contains(group) Then
			selectable_object.Select(True)
			Continue For
		End If
	  Next group
	Next selectable_object
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
from Rhino.Input import *
from scriptcontext import doc

def RunCommand():
    rs, obj_ref = RhinoGet.GetOneObject("Select object", False, ObjectType.AnyObject)
    if rs != Result.Success:
        return rs
    rhino_object = obj_ref.Object()
    if rhino_object == None:
        return Result.Failure

    rhino_object_groups = [group for group in rhino_object.Attributes.GetGroupList()]

    selectable_objects= [
        obj for obj in doc.Objects.GetObjectList(ObjectType.AnyObject)
        if obj.IsSelectable(True, False, False, False)]

    for selectable_object in selectable_objects:
        for group in selectable_object.Attributes.GetGroupList():
            if rhino_object_groups.Contains(group):
                selectable_object.Select(True)
                continue

    doc.Views.Redraw()
    return Result.Success

if __name__ == "__main__":
    RunCommand()
```

</div>
