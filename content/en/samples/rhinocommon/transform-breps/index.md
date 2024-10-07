+++
aliases = ["/en/5/samples/rhinocommon/transform-breps/", "/en/6/samples/rhinocommon/transform-breps/", "/en/7/samples/rhinocommon/transform-breps/", "/en/wip/samples/rhinocommon/transform-breps/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to move (or transform) a user-specified Brep object."
keywords = [ "transform", "brep" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Transform Breps"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/transformbrep"
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
  public static Rhino.Commands.Result TransformBrep(Rhino.RhinoDoc doc)
  {
    Rhino.DocObjects.ObjRef rhobj;
    var rc = RhinoGet.GetOneObject("Select brep", true, Rhino.DocObjects.ObjectType.Brep, out rhobj);
    if(rc!= Rhino.Commands.Result.Success)
      return rc;

    // Simple translation transformation
    var xform = Rhino.Geometry.Transform.Translation(18,-18,25);
    doc.Objects.Transform(rhobj, xform, true);
    doc.Views.Redraw();
    return Rhino.Commands.Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function TransformBrep(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim rhobj As Rhino.DocObjects.ObjRef = Nothing
	Dim rc = RhinoGet.GetOneObject("Select brep", True, Rhino.DocObjects.ObjectType.Brep, rhobj)
	If rc IsNot Rhino.Commands.Result.Success Then
	  Return rc
	End If

	' Simple translation transformation
	Dim xform = Rhino.Geometry.Transform.Translation(18,-18,25)
	doc.Objects.Transform(rhobj, xform, True)
	doc.Views.Redraw()
	Return Rhino.Commands.Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
import Rhino
import scriptcontext

def TransformBrep():
    rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select brep", True, Rhino.DocObjects.ObjectType.Brep)
    if rc!=Rhino.Commands.Result.Success: return

    # Simple translation transformation
    xform = Rhino.Geometry.Transform.Translation(18,-18,25)
    scriptcontext.doc.Objects.Transform(objref, xform, True)
    scriptcontext.doc.Views.Redraw()

if __name__=="__main__":
    TransformBrep()
```

</div>
