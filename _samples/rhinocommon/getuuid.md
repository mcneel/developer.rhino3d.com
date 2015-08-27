---
layout: code-sample
author:
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
title: Get an Object's UUID
keywords: ['objects', 'uuid']
categories: ['Adding Objects']
description:
order: 1
---

```cs
partial class Examples
{
  public static Result GetUUID(RhinoDoc doc)
  {
    ObjRef obj_ref;
    var rc = RhinoGet.GetOneObject("Select object", false, ObjectType.AnyObject, out obj_ref);
    if (rc != Result.Success)
      return rc;
    if (obj_ref == null)
      return Result.Nothing;

    var uuid = obj_ref.ObjectId;
    RhinoApp.WriteLine("The object's unique id is {0}", uuid.ToString());
    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function GetUUID(ByVal doc As RhinoDoc) As Result
	Dim obj_ref As ObjRef = Nothing
	Dim rc = RhinoGet.GetOneObject("Select object", False, ObjectType.AnyObject, obj_ref)
	If rc IsNot Result.Success Then
	  Return rc
	End If
	If obj_ref Is Nothing Then
	  Return Result.Nothing
	End If

	Dim uuid = obj_ref.ObjectId
	RhinoApp.WriteLine("The object's unique id is {0}", uuid.ToString())
	Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
import rhinoscriptsyntax as rs

obj_id = rs.GetObject("Select object")
if obj_id <> None:
  print "The object's unique id is {0}".format(obj_id)
```
{: #py .tab-pane .fade .in}

