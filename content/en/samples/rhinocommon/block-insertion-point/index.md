+++
aliases = ["/en/5/samples/rhinocommon/block-insertion-point/", "/en/6/samples/rhinocommon/block-insertion-point/", "/en/7/samples/rhinocommon/block-insertion-point/", "/en/wip/samples/rhinocommon/block-insertion-point/"]
authors = [ "steve" ]
categories = [ "Blocks" ]
description = "Demonstrates how to set (or reset) the block insertion point of a block instance."
keywords = [ "obtain", "insertion", "point", "block" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Block Insertion Point"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/blockinsertionpoint"
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
  public static Rhino.Commands.Result BlockInsertionPoint(Rhino.RhinoDoc doc)
  {
    Rhino.DocObjects.ObjRef objref;
    Result rc = Rhino.Input.RhinoGet.GetOneObject("Select instance", true, Rhino.DocObjects.ObjectType.InstanceReference, out objref);
    if (rc != Rhino.Commands.Result.Success)
      return rc;
    Rhino.DocObjects.InstanceObject instance = objref.Object() as Rhino.DocObjects.InstanceObject;
    if (instance != null)
    {
      Rhino.Geometry.Point3d pt = instance.InsertionPoint;
      doc.Objects.AddPoint(pt);
      doc.Views.Redraw();
    }
    return Rhino.Commands.Result.Success;
  }
}
```

</div>

<div class="codetab-content" id="py">

```python
import Rhino
import scriptcontext

def BlockInsertionPoint():
    rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select instance", True, Rhino.DocObjects.ObjectType.InstanceReference)
    if rc!=Rhino.Commands.Result.Success: return rc;
    instance = objref.Object()
    if instance:
        pt = instance.InsertionPoint
        scriptcontext.doc.Objects.AddPoint(pt)
        scriptcontext.doc.Views.Redraw()
        return Rhino.Commands.Result.Success
    return Rhino.Commands.Result.Failure

if __name__=="__main__":
    BlockInsertionPoint()
```

</div>
