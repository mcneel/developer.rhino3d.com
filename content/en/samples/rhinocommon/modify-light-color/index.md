+++
aliases = ["/en/5/samples/rhinocommon/modify-light-color/", "/en/6/samples/rhinocommon/modify-light-color/", "/en/7/samples/rhinocommon/modify-light-color/", "/en/wip/samples/rhinocommon/modify-light-color/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to change the color of a user-specified light."
keywords = [ "modify", "lights", "color" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Modify Light Color"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/modifylightcolor"
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
  public static Result ModifyLightColor(RhinoDoc doc)
  {
    ObjRef obj_ref;
    var rc = RhinoGet.GetOneObject("Select light to change color", true,
      ObjectType.Light, out obj_ref);
    if (rc != Result.Success)
      return rc;
    var light = obj_ref.Light();
    if (light == null)
      return Result.Failure;

    var diffuse_color = light.Diffuse;
    if (Dialogs.ShowColorDialog(ref diffuse_color))
    {
      light.Diffuse = diffuse_color;
    }

    doc.Lights.Modify(obj_ref.ObjectId, light);
    return Result.Success;
  }
}
```

</div>

<div class="codetab-content" id="py">

```python
from Rhino import *
from Rhino.DocObjects import *
from Rhino.Input import *
from Rhino.UI import *
from Rhino.Commands import Result
from scriptcontext import doc

def RunCommand():
    rc, obj_ref = RhinoGet.GetOneObject("Select light to change color", True, ObjectType.Light)
    if rc != Result.Success:
        return rc
    light = obj_ref.Light()
    if light == None:
        return Result.Failure

    b, color = Dialogs.ShowColorDialog(light.Diffuse)
    if b:
        light.Diffuse = color

    doc.Lights.Modify(obj_ref.ObjectId, light)
    return Result.Success

if __name__ == "__main__":
    RunCommand()
```

</div>
