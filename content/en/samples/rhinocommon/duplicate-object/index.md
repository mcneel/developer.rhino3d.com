+++
aliases = ["/en/5/samples/rhinocommon/duplicate-object/", "/en/6/samples/rhinocommon/duplicate-object/", "/en/7/samples/rhinocommon/duplicate-object/", "/en/wip/samples/rhinocommon/duplicate-object/"]
authors = [ "steve" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to clone (or copy, or duplicate) a Rhino object."
keywords = [ "clone", "copy", "duplicate", "rhino", "object" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Duplicate Object"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/duplicateobject"
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
  public static Result DuplicateObject(RhinoDoc doc)
  {
    ObjRef obj_ref;
    var rc = RhinoGet.GetOneObject("Select object to duplicate", false, ObjectType.AnyObject, out obj_ref);
    if (rc != Result.Success)
      return rc;
    var rhino_object = obj_ref.Object();

    var geometry_base = rhino_object.DuplicateGeometry();
    if (geometry_base != null)
      if (doc.Objects.Add(geometry_base) != Guid.Empty)
        doc.Views.Redraw();

    return Result.Success;
  }
}
```

</div>

<div class="codetab-content" id="py">

```python
from System import *
from Rhino import *
from Rhino.Commands import *
from Rhino.DocObjects import *
from Rhino.Input import *
from scriptcontext import doc

def RunCommand():

    rc, obj_ref = RhinoGet.GetOneObject("Select object to duplicate", False, ObjectType.AnyObject)
    if rc != Result.Success:
        return rc
    rhino_object = obj_ref.Object()

    geometry_base = rhino_object.DuplicateGeometry()
    if geometry_base != None:
        if doc.Objects.Add(geometry_base) != Guid.Empty:
            doc.Views.Redraw()

    return Result.Success

if __name__ == "__main__":
    RunCommand()
```

</div>
