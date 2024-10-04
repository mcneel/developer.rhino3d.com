+++
aliases = ["/en/5/samples/rhinocommon/add-sphere/", "/en/6/samples/rhinocommon/add-sphere/", "/en/7/samples/rhinocommon/add-sphere/", "/wip/samples/rhinocommon/add-sphere/"]
authors = [ "steve" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to create a sphere from a center point and radius."
keywords = [ "add", "sphere" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Add Sphere"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/addsphere"
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
  public static Rhino.Commands.Result AddSphere(Rhino.RhinoDoc doc)
  {
    Rhino.Geometry.Point3d center = new Rhino.Geometry.Point3d(0, 0, 0);
    const double radius = 5.0;
    Rhino.Geometry.Sphere sphere = new Rhino.Geometry.Sphere(center, radius);
    if( doc.Objects.AddSphere(sphere) != Guid.Empty )
    {
      doc.Views.Redraw();
      return Rhino.Commands.Result.Success;
    }
    return Rhino.Commands.Result.Failure;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function AddSphere(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim center As New Rhino.Geometry.Point3d(0, 0, 0)
	Const radius As Double = 5.0
	Dim sphere As New Rhino.Geometry.Sphere(center, radius)
	If doc.Objects.AddSphere(sphere) <> Guid.Empty Then
	  doc.Views.Redraw()
	  Return Rhino.Commands.Result.Success
	End If
	Return Rhino.Commands.Result.Failure
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
import Rhino
import scriptcontext
import System.Guid

def AddSphere():
    center = Rhino.Geometry.Point3d(0, 0, 0)
    radius = 5.0
    sphere = Rhino.Geometry.Sphere(center, radius)
    if scriptcontext.doc.Objects.AddSphere(sphere)!=System.Guid.Empty:
        scriptcontext.doc.Views.Redraw()
        return Rhino.Commands.Result.Success
    return Rhino.Commands.Result.Failure


if __name__ == "__main__":
    AddSphere()
```

</div>
