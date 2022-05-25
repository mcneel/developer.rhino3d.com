+++
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to create a surface from a set of corner points."
keywords = [ "surface", "corner", "points" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Surface from Corner Points"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/srfpt"
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
  public static Result SurfaceFromCorners(RhinoDoc doc)
  {
    var surface = NurbsSurface.CreateFromCorners(
      new Point3d(5, 0, 0),
      new Point3d(5, 5, 5),
      new Point3d(0, 5, 0),
      new Point3d(0, 0, 0));

    doc.Objects.AddSurface(surface);
    doc.Views.Redraw();

    return Rhino.Commands.Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function SurfaceFromCorners(ByVal doc As RhinoDoc) As Result
	Dim surface = NurbsSurface.CreateFromCorners(New Point3d(5, 0, 0), New Point3d(5, 5, 5), New Point3d(0, 5, 0), New Point3d(0, 0, 0))

	doc.Objects.AddSurface(surface)
	doc.Views.Redraw()

	Return Rhino.Commands.Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
from Rhino.Geometry import NurbsSurface, Point3d
from scriptcontext import doc

surface = NurbsSurface.CreateFromCorners(
    Point3d(5, 0, 0),
    Point3d(5, 5, 5),
    Point3d(0, 5, 0),
    Point3d(0, 0, 0));

doc.Objects.AddSurface(surface);
doc.Views.Redraw();
```

</div>
