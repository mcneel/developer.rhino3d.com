+++
authors = [ "steve" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to get the UUID (sometimes called GUID) of a Rhino object."
keywords = [ "objects", "uuid" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Get Object UUID"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/getuuid"
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

</div>


<div class="codetab-content" id="vb">

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

</div>


<div class="codetab-content" id="py">

```python
import rhinoscriptsyntax as rs

obj_id = rs.GetObject("Select object")
if obj_id != None:
    print "The object's unique id is {0}".format(obj_id)
```

</div>
