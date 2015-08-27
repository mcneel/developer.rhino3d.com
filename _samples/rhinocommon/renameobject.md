---
layout: code-sample
author:
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
title: Rename Object
keywords: ['rename', 'object']
categories: ['Adding Objects']
description:
order: 1
---

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
{: #cs .tab-pane .fade .in .active}


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
{: #vb .tab-pane .fade .in}

