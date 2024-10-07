+++
aliases = ["/en/5/samples/rhinocommon/add-linear-dimension2/", "/en/6/samples/rhinocommon/add-linear-dimension2/", "/en/7/samples/rhinocommon/add-linear-dimension2/", "/en/wip/samples/rhinocommon/add-linear-dimension2/"]
authors = [ "steve" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to add a linear dimension from two points given an offset point."
keywords = [ "add", "linear", "dimension2" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Add Linear Dimension2"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/addlineardimension2"
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
  public static Rhino.Commands.Result AddLinearDimension2(Rhino.RhinoDoc doc)
  {
    Point3d origin = new Point3d(1,1,0);
    Point3d offset = new Point3d(11,1,0);
    Point3d pt = new Point3d((offset.X-origin.X)/2,3,0);

    Plane plane = Plane.WorldXY;
    plane.Origin = origin;

    double u,v;
    plane.ClosestParameter(origin, out u, out v);
    Point2d ext1 = new Point2d(u, v);

    plane.ClosestParameter(offset, out u, out v);
    Point2d ext2 = new Point2d(u, v);

    plane.ClosestParameter(pt, out u, out v);
    Point2d linePt = new Point2d(u, v);

    LinearDimension dimension = new LinearDimension(plane, ext1, ext2, linePt);
    if (doc.Objects.AddLinearDimension(dimension) != Guid.Empty)
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
  Public Shared Function AddLinearDimension2(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim origin As New Point3d(1,1,0)
	Dim offset As New Point3d(11,1,0)
'INSTANT VB WARNING: Instant VB cannot determine whether both operands of this division are integer types - if they are then you should use the VB integer division operator:
	Dim pt As New Point3d((offset.X-origin.X)/2,3,0)

	Dim plane As Plane = Plane.WorldXY
	plane.Origin = origin

	Dim u As Double = Nothing, v As Double = Nothing
	plane.ClosestParameter(origin, u, v)
	Dim ext1 As New Point2d(u, v)

	plane.ClosestParameter(offset, u, v)
	Dim ext2 As New Point2d(u, v)

	plane.ClosestParameter(pt, u, v)
	Dim linePt As New Point2d(u, v)

	Dim dimension As New LinearDimension(plane, ext1, ext2, linePt)
	If doc.Objects.AddLinearDimension(dimension) <> Guid.Empty Then
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

def AddLinearDimension2():
    origin = Rhino.Geometry.Point3d(1,1,0)
    offset = Rhino.Geometry.Point3d(11,1,0)
    pt = Rhino.Geometry.Point3d((offset.X-origin.X)/2.0,3,0)
    plane = Rhino.Geometry.Plane.WorldXY
    plane.Origin = origin

    rc, u, v = plane.ClosestParameter(origin)
    ext1 = Rhino.Geometry.Point2d(u,v)
    rc, u, v = plane.ClosestParameter(offset)
    ext2 = Rhino.Geometry.Point2d(u,v)
    rc, u, v = plane.ClosestParameter(pt)
    linePt = Rhino.Geometry.Point2d(u,v)

    dimension = Rhino.Geometry.LinearDimension(plane, ext1, ext2, linePt)
    if scriptcontext.doc.Objects.AddLinearDimension(dimension)!=System.Guid.Empty:
        scriptcontext.doc.Views.Redraw()
        return Rhino.Commands.Result.Success
    return Rhino.Commands.Result.Failure

if __name__=="__main__":
    AddLinearDimension2()
```

</div>
