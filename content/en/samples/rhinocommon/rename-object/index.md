+++
aliases = ["/en/5/samples/rhinocommon/rename-object/", "/en/6/samples/rhinocommon/rename-object/", "/en/7/samples/rhinocommon/rename-object/", "/en/wip/samples/rhinocommon/rename-object/"]
authors = [ "steve" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to rename a user-specified object."
keywords = [ "rename", "object" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Rename Object"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/objectname"
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
  public static Result RenameObject(RhinoDoc doc)
  {
    ObjRef obj_ref;
    var rc = RhinoGet.GetOneObject("Select object to change name", true, ObjectType.AnyObject, out obj_ref);
    if (rc != Result.Success)
      return rc;
    var rhino_object = obj_ref.Object();

    var new_object_name = "";
    rc = RhinoGet.GetString("New object name", true, ref new_object_name);
    if (rc != Result.Success)
      return rc;
    if (string.IsNullOrWhiteSpace(new_object_name))
      return Result.Nothing;

    if (rhino_object.Name != new_object_name)
    {
      rhino_object.Attributes.Name = new_object_name;
      rhino_object.CommitChanges();
    }

    return Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function RenameObject(ByVal doc As RhinoDoc) As Result
	Dim obj_ref As ObjRef = Nothing
	Dim rc = RhinoGet.GetOneObject("Select object to change name", True, ObjectType.AnyObject, obj_ref)
	If rc IsNot Result.Success Then
	  Return rc
	End If
	Dim rhino_object = obj_ref.Object()

	Dim new_object_name = ""
	rc = RhinoGet.GetString("New object name", True, new_object_name)
	If rc IsNot Result.Success Then
	  Return rc
	End If
	If String.IsNullOrWhiteSpace(new_object_name) Then
	  Return Result.Nothing
	End If

	If rhino_object.Name <> new_object_name Then
	  rhino_object.Attributes.Name = new_object_name
	  rhino_object.CommitChanges()
	End If

	Return Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
import rhinoscriptsyntax as rs

obj_id = rs.GetObject("Select object to change name")
object_new_name = rs.GetString("New object name")

rs.ObjectName(obj_id, object_new_name)
```

</div>
