+++
aliases = ["/en/5/samples/rhinocommon/get-object-uuid/", "/en/6/samples/rhinocommon/get-object-uuid/", "/en/7/samples/rhinocommon/get-object-uuid/", "/en/wip/samples/rhinocommon/get-object-uuid/"]
authors = [ "steve" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to get the UUID (sometimes called GUID) of a Rhino object."
keywords = [ "objects", "uuid" ]
languages = [ "C#", "Python" ]
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

<div class="codetab-content" id="py">

```python
import rhinoscriptsyntax as rs

obj_id = rs.GetObject("Select object")
if obj_id != None:
    print("The object's unique id is {0}".format(obj_id))

```

</div>
