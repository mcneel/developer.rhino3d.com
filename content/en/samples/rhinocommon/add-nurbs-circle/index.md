+++
aliases = ["/en/5/samples/rhinocommon/add-nurbs-circle/", "/en/6/samples/rhinocommon/add-nurbs-circle/", "/en/7/samples/rhinocommon/add-nurbs-circle/", "/wip/samples/rhinocommon/add-nurbs-circle/"]
authors = [ "steve" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to create a NURBS circle from scratch using points and knots."
keywords = [ "add", "nurbs", "circle" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Add NURBS Circle"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/addnurbscircle"
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
  public static Rhino.Commands.Result AddNurbsCircle(Rhino.RhinoDoc doc)
  {
    // The easy way to get a NURBS curve from a circle is with
    // the following two lines of code.
    //
    // Rhino.Geometry.Circle c = new Rhino.Geometry.Circle(20);
    // Rhino.Geometry.NurbsCurve nc = c.ToNurbsCurve();
    //
    // This sample demonstrates creating a NURBS curve from scratch.
    const int dimension = 3;
    const bool isRational = true;
    const int order = 3;
    const int cv_count = 9;
    Rhino.Geometry.NurbsCurve nc = new Rhino.Geometry.NurbsCurve(dimension, isRational, order, cv_count);
    nc.Points.SetPoint(0, 1.0, 0.0, 0.0, 1.0);
    nc.Points.SetPoint(1, 0.707107, 0.707107, 0.0, 0.707107);
    nc.Points.SetPoint(2, 0.0, 1.0, 0.0, 1.0);
    nc.Points.SetPoint(3, -0.707107, 0.707107, 0.0, 0.707107);
    nc.Points.SetPoint(4, -1.0, 0.0, 0.0, 1.0);
    nc.Points.SetPoint(5, -0.707107, -0.707107, 0.0, 0.707107);
    nc.Points.SetPoint(6, 0.0, -1.0, 0.0, 1.0);
    nc.Points.SetPoint(7, 0.707107, -0.707107, 0.0, 0.707107);
    nc.Points.SetPoint(8, 1.0, 0.0, 0.0, 1.0);
    nc.Knots[0] = 0.0;
    nc.Knots[1] = 0.0;
    nc.Knots[2] = 0.5 * Math.PI;
    nc.Knots[3] = 0.5 * Math.PI;
    nc.Knots[4] = Math.PI;
    nc.Knots[5] = Math.PI;
    nc.Knots[6] = 1.5 * Math.PI;
    nc.Knots[7] = 1.5 * Math.PI;
    nc.Knots[8] = 2.0 * Math.PI;
    nc.Knots[9] = 2.0 * Math.PI;
    if (nc.IsValid)
    {
      doc.Objects.AddCurve(nc);
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
  Public Shared Function AddNurbsCircle(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	' The easy way to get a NURBS curve from a circle is with
	' the following two lines of code.
	'
	' Rhino.Geometry.Circle c = new Rhino.Geometry.Circle(20);
	' Rhino.Geometry.NurbsCurve nc = c.ToNurbsCurve();
	'
	' This sample demonstrates creating a NURBS curve from scratch.
	Const dimension As Integer = 3
	Const isRational As Boolean = True
	Const order As Integer = 3
	Const cv_count As Integer = 9
	Dim nc As New Rhino.Geometry.NurbsCurve(dimension, isRational, order, cv_count)
	nc.Points.SetPoint(0, 1.0, 0.0, 0.0, 1.0)
	nc.Points.SetPoint(1, 0.707107, 0.707107, 0.0, 0.707107)
	nc.Points.SetPoint(2, 0.0, 1.0, 0.0, 1.0)
	nc.Points.SetPoint(3, -0.707107, 0.707107, 0.0, 0.707107)
	nc.Points.SetPoint(4, -1.0, 0.0, 0.0, 1.0)
	nc.Points.SetPoint(5, -0.707107, -0.707107, 0.0, 0.707107)
	nc.Points.SetPoint(6, 0.0, -1.0, 0.0, 1.0)
	nc.Points.SetPoint(7, 0.707107, -0.707107, 0.0, 0.707107)
	nc.Points.SetPoint(8, 1.0, 0.0, 0.0, 1.0)
	nc.Knots(0) = 0.0
	nc.Knots(1) = 0.0
	nc.Knots(2) = 0.5 * Math.PI
	nc.Knots(3) = 0.5 * Math.PI
	nc.Knots(4) = Math.PI
	nc.Knots(5) = Math.PI
	nc.Knots(6) = 1.5 * Math.PI
	nc.Knots(7) = 1.5 * Math.PI
	nc.Knots(8) = 2.0 * Math.PI
	nc.Knots(9) = 2.0 * Math.PI
	If nc.IsValid Then
	  doc.Objects.AddCurve(nc)
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
import System
from Rhino.Geometry import NurbsCurve
from Rhino.Commands import Result
from scriptcontext import doc

def AddNurbsCircle():
    # The easy way to get a NURBS curve from a circle is with
    # the following two lines of code.
    #
    # Circle c = new Circle(20)
    # NurbsCurve nc = c.ToNurbsCurve()
    #
    # This sample demonstrates creating a NURBS curve from scratch.
    dimension = 3
    isRational = True
    order = 3
    cv_count = 9
    nc = NurbsCurve(dimension, isRational, order, cv_count)
    nc.Points.SetPoint(0, 1.0, 0.0, 0.0, 1.0)
    nc.Points.SetPoint(1, 1.0, 1.0, 0.0, 0.707107)
    nc.Points.SetPoint(2, 0.0, 1.0, 0.0, 1.0)
    nc.Points.SetPoint(3, -1.0, 1.0, 0.0, 0.707107)
    nc.Points.SetPoint(4, -1.0, 0.0, 0.0, 1.0)
    nc.Points.SetPoint(5, -1.0, -1.0, 0.0, 0.707107)
    nc.Points.SetPoint(6, 0.0, -1.0, 0.0, 1.0)
    nc.Points.SetPoint(7, 1.0, -1.0, 0.0, 0.707107)
    nc.Points.SetPoint(8, 1.0, 0.0, 0.0, 1.0)
    nc.Knots[0] = 0.0
    nc.Knots[1] = 0.0
    nc.Knots[2] = 0.5 * System.Math.PI
    nc.Knots[3] = 0.5 * System.Math.PI
    nc.Knots[4] = System.Math.PI
    nc.Knots[5] = System.Math.PI
    nc.Knots[6] = 1.5 * System.Math.PI
    nc.Knots[7] = 1.5 * System.Math.PI
    nc.Knots[8] = 2.0 * System.Math.PI
    nc.Knots[9] = 2.0 * System.Math.PI
    if nc.IsValid:
        doc.Objects.AddCurve(nc)
        doc.Views.Redraw()
        return Result.Success
    return Result.Failure

if __name__=="__main__":
    AddNurbsCircle()
```

</div>
