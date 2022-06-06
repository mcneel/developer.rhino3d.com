+++
aliases = ["/5/samples/rhinocommon/add-brep-box/", "/6/samples/rhinocommon/add-brep-box/", "/7/samples/rhinocommon/add-brep-box/", "/wip/samples/rhinocommon/add-brep-box/"]
authors = [ "steve" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to add a Brep Box to a Rhino model by specifying two points."
keywords = [ "add", "brep" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Add Brep Box"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/addbrepbox"
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
  public static Rhino.Commands.Result AddBrepBox(Rhino.RhinoDoc doc)
  {
    Rhino.Geometry.Point3d pt0 = new Rhino.Geometry.Point3d(0, 0, 0);
    Rhino.Geometry.Point3d pt1 = new Rhino.Geometry.Point3d(10, 10, 10);
    Rhino.Geometry.BoundingBox box = new Rhino.Geometry.BoundingBox(pt0, pt1);
    Rhino.Geometry.Brep brep = box.ToBrep();
    Rhino.Commands.Result rc = Rhino.Commands.Result.Failure;
    if( doc.Objects.AddBrep(brep) != System.Guid.Empty )
    {
      rc = Rhino.Commands.Result.Success;
      doc.Views.Redraw();
    }
    return rc;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function AddBrepBox(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim pt0 As New Rhino.Geometry.Point3d(0, 0, 0)
	Dim pt1 As New Rhino.Geometry.Point3d(10, 10, 10)
	Dim box As New Rhino.Geometry.BoundingBox(pt0, pt1)
	Dim brep As Rhino.Geometry.Brep = box.ToBrep()
	Dim rc As Rhino.Commands.Result = Rhino.Commands.Result.Failure
	If doc.Objects.AddBrep(brep) <> System.Guid.Empty Then
	  rc = Rhino.Commands.Result.Success
	  doc.Views.Redraw()
	End If
	Return rc
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
import Rhino
import scriptcontext
import System.Guid

def AddBrepBox():
    pt0 = Rhino.Geometry.Point3d(0, 0, 0)
    pt1 = Rhino.Geometry.Point3d(10, 10, 10)
    box = Rhino.Geometry.BoundingBox(pt0, pt1)
    brep = box.ToBrep()
    rc = Rhino.Commands.Result.Failure
    if( scriptcontext.doc.Objects.AddBrep(brep) != System.Guid.Empty ):
        rc = Rhino.Commands.Result.Success
        scriptcontext.doc.Views.Redraw()
    return rc

if( __name__ == "__main__" ):
    AddBrepBox()
```

</div>
