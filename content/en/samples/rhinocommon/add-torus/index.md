+++
aliases = ["/en/5/samples/rhinocommon/add-torus/", "/en/6/samples/rhinocommon/add-torus/", "/en/7/samples/rhinocommon/add-torus/", "/wip/samples/rhinocommon/add-torus/"]
authors = [ "steve" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to construct a torus from a set of radii and a plane."
keywords = [ "add", "torus" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Add Torus"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/addtorus"
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
  public static Rhino.Commands.Result AddTorus(Rhino.RhinoDoc doc)
  {
    const double major_radius = 4.0;
    const double minor_radius = 2.0;

    Rhino.Geometry.Plane plane = Rhino.Geometry.Plane.WorldXY;
    Rhino.Geometry.Torus torus = new Rhino.Geometry.Torus(plane, major_radius, minor_radius);
    Rhino.Geometry.RevSurface revsrf = torus.ToRevSurface();
    if (doc.Objects.AddSurface(revsrf) != Guid.Empty)
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
  Public Shared Function AddTorus(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Const major_radius As Double = 4.0
	Const minor_radius As Double = 2.0

	Dim plane As Rhino.Geometry.Plane = Rhino.Geometry.Plane.WorldXY
	Dim torus As New Rhino.Geometry.Torus(plane, major_radius, minor_radius)
	Dim revsrf As Rhino.Geometry.RevSurface = torus.ToRevSurface()
	If doc.Objects.AddSurface(revsrf) <> Guid.Empty Then
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

def AddTorus():
    major_radius = 4.0
    minor_radius = 2.0

    plane = Rhino.Geometry.Plane.WorldXY
    torus = Rhino.Geometry.Torus(plane, major_radius, minor_radius)
    revsrf = torus.ToRevSurface()

    if scriptcontext.doc.Objects.AddSurface(revsrf)!=System.Guid.Empty:
        scriptcontext.doc.Views.Redraw()
        return Rhino.Commands.Result.Success
    return Rhino.Commands.Result.Failure


if __name__=="__main__":
    AddTorus()
```

</div>
