+++
aliases = ["/en/5/samples/rhinocommon/add-truncated-cone/", "/en/6/samples/rhinocommon/add-truncated-cone/", "/en/7/samples/rhinocommon/add-truncated-cone/", "/wip/samples/rhinocommon/add-truncated-cone/"]
authors = [ "steve" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to construct a truncated cone (TCone) from two circles."
keywords = [ "add", "truncated", "cone" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Add Truncated Cone"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/addtruncatedcone"
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
  public static Rhino.Commands.Result AddTruncatedCone(Rhino.RhinoDoc doc)
  {
    Point3d bottom_pt = new Point3d(0,0,0);
    const double bottom_radius = 2;
    Circle bottom_circle = new Circle(bottom_pt, bottom_radius);

    Point3d top_pt = new Point3d(0,0,10);
    const double top_radius = 6;
    Circle top_circle = new Circle(top_pt, top_radius);

    LineCurve shapeCurve = new LineCurve(bottom_circle.PointAt(0), top_circle.PointAt(0));
    Line axis = new Line(bottom_circle.Center, top_circle.Center);
    RevSurface revsrf = RevSurface.Create(shapeCurve, axis);
    Brep tcone_brep = Brep.CreateFromRevSurface(revsrf, true, true);
    if( doc.Objects.AddBrep(tcone_brep) != Guid.Empty )
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
  Public Shared Function AddTruncatedCone(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim bottom_pt As New Point3d(0,0,0)
	Const bottom_radius As Double = 2
	Dim bottom_circle As New Circle(bottom_pt, bottom_radius)

	Dim top_pt As New Point3d(0,0,10)
	Const top_radius As Double = 6
	Dim top_circle As New Circle(top_pt, top_radius)

	Dim shapeCurve As New LineCurve(bottom_circle.PointAt(0), top_circle.PointAt(0))
	Dim axis As New Line(bottom_circle.Center, top_circle.Center)
	Dim revsrf As RevSurface = RevSurface.Create(shapeCurve, axis)
	Dim tcone_brep As Brep = Brep.CreateFromRevSurface(revsrf, True, True)
	If doc.Objects.AddBrep(tcone_brep) <> Guid.Empty Then
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

def AddTruncatedCone():
    bottom_pt = Rhino.Geometry.Point3d(0,0,0)
    bottom_radius = 2
    bottom_circle = Rhino.Geometry.Circle(bottom_pt, bottom_radius)

    top_pt = Rhino.Geometry.Point3d(0,0,10)
    top_radius = 6
    top_circle = Rhino.Geometry.Circle(top_pt, top_radius)

    shapeCurve = Rhino.Geometry.LineCurve(bottom_circle.PointAt(0), top_circle.PointAt(0))
    axis = Rhino.Geometry.Line(bottom_circle.Center, top_circle.Center)
    revsrf = Rhino.Geometry.RevSurface.Create(shapeCurve, axis)
    tcone_brep = Rhino.Geometry.Brep.CreateFromRevSurface(revsrf, True, True)

    if scriptcontext.doc.Objects.AddBrep(tcone_brep)!=System.Guid.Empty:
        scriptcontext.doc.Views.Redraw()
        return Rhino.Commands.Result.Success
    return Rhino.Commands.Result.Failure


if __name__=="__main__":
    AddTruncatedCone()
```

</div>
