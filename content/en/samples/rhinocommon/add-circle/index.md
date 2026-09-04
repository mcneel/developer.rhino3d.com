+++
aliases = ["/en/5/samples/rhinocommon/add-circle/", "/en/6/samples/rhinocommon/add-circle/", "/en/7/samples/rhinocommon/add-circle/", "/en/wip/samples/rhinocommon/add-circle/"]
authors = [ "steve" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to add a circle from a center point and radius."
keywords = [ "add", "circle" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Add Circle"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/addcircle"
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
  public static Rhino.Commands.Result AddCircle(Rhino.RhinoDoc doc)
  {
    Rhino.Geometry.Point3d center = new Rhino.Geometry.Point3d(0, 0, 0);
    const double radius = 10.0;
    Rhino.Geometry.Circle c = new Rhino.Geometry.Circle(center, radius);
    if (doc.Objects.AddCircle(c) != Guid.Empty)
    {
      doc.Views.Redraw();
      return Rhino.Commands.Result.Success;
    }
    return Rhino.Commands.Result.Failure;
  }
}
```

</div>

<div class="codetab-content" id="py">

```python
import Rhino
import scriptcontext
from System import Guid

def AddCircle():
    center = Rhino.Geometry.Point3d(0, 0, 0)
    radius = 10.0
    c = Rhino.Geometry.Circle(center, radius)
    if scriptcontext.doc.Objects.AddCircle(c)!= Guid.Empty:
        scriptcontext.doc.Views.Redraw()
        return Rhino.Commands.Result.Success
    return Rhino.Commands.Result.Failure

if __name__=="__main__":
    AddCircle()
```

</div>
