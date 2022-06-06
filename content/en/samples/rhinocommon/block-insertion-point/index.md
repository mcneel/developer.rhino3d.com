+++
aliases = ["/5/samples/rhinocommon/block-insertion-point/", "/6/samples/rhinocommon/block-insertion-point/", "/7/samples/rhinocommon/block-insertion-point/", "/wip/samples/rhinocommon/block-insertion-point/"]
authors = [ "steve" ]
categories = [ "Blocks" ]
description = "Demonstrates how to set (or reset) the block insertion point of a block instance."
keywords = [ "obtain", "insertion", "point", "block" ]
languages = [ "C#", "Python", "VB" ]
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


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function BlockInsertionPoint(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim objref As Rhino.DocObjects.ObjRef = Nothing
	Dim rc As Result = Rhino.Input.RhinoGet.GetOneObject("Select instance", True, Rhino.DocObjects.ObjectType.InstanceReference, objref)
	If rc IsNot Rhino.Commands.Result.Success Then
	  Return rc
	End If
	Dim instance As Rhino.DocObjects.InstanceObject = TryCast(objref.Object(), Rhino.DocObjects.InstanceObject)
	If instance IsNot Nothing Then
	  Dim pt As Rhino.Geometry.Point3d = instance.InsertionPoint
	  doc.Objects.AddPoint(pt)
	  doc.Views.Redraw()
	End If
	Return Rhino.Commands.Result.Success
  End Function
End Class
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
