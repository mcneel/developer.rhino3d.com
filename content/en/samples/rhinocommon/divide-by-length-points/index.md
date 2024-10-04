+++
aliases = ["/en/5/samples/rhinocommon/divide-by-length-points/", "/en/6/samples/rhinocommon/divide-by-length-points/", "/en/7/samples/rhinocommon/divide-by-length-points/", "/wip/samples/rhinocommon/divide-by-length-points/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to divide a user-selected curve into a set of spaced points along the curve."
keywords = [ "divide", "length", "points" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Divide by Length Points"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/dividebylength"
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
  public static Rhino.Commands.Result DivideByLengthPoints(Rhino.RhinoDoc doc)
  {
    const ObjectType filter = Rhino.DocObjects.ObjectType.Curve;
    Rhino.DocObjects.ObjRef objref;
    Rhino.Commands.Result rc = Rhino.Input.RhinoGet.GetOneObject("Select curve to divide", false, filter, out objref);
    if (rc != Rhino.Commands.Result.Success || objref == null)
      return rc;

    Rhino.Geometry.Curve crv = objref.Curve();
    if (crv == null || crv.IsShort(Rhino.RhinoMath.ZeroTolerance))
      return Rhino.Commands.Result.Failure;

    double crv_length = crv.GetLength();
    string s = string.Format("Curve length is {0:f3}. Segment length", crv_length);

    double seg_length = crv_length / 2.0;
    rc = Rhino.Input.RhinoGet.GetNumber(s, false, ref seg_length, 0, crv_length);
    if (rc != Rhino.Commands.Result.Success)
      return rc;

    Rhino.Geometry.Point3d[] points;
    crv.DivideByLength(seg_length, true, out points);
    if (points == null)
      return Rhino.Commands.Result.Failure;

    foreach (Rhino.Geometry.Point3d point in points)
      doc.Objects.AddPoint(point);

    doc.Views.Redraw();
    return Rhino.Commands.Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function DivideByLengthPoints(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Const filter As ObjectType = Rhino.DocObjects.ObjectType.Curve
	Dim objref As Rhino.DocObjects.ObjRef = Nothing
	Dim rc As Rhino.Commands.Result = Rhino.Input.RhinoGet.GetOneObject("Select curve to divide", False, filter, objref)
	If rc IsNot Rhino.Commands.Result.Success OrElse objref Is Nothing Then
	  Return rc
	End If

	Dim crv As Rhino.Geometry.Curve = objref.Curve()
	If crv Is Nothing OrElse crv.IsShort(Rhino.RhinoMath.ZeroTolerance) Then
	  Return Rhino.Commands.Result.Failure
	End If

	Dim crv_length As Double = crv.GetLength()
	Dim s As String = String.Format("Curve length is {0:f3}. Segment length", crv_length)

	Dim seg_length As Double = crv_length / 2.0
	rc = Rhino.Input.RhinoGet.GetNumber(s, False, seg_length, 0, crv_length)
	If rc IsNot Rhino.Commands.Result.Success Then
	  Return rc
	End If

	Dim points() As Rhino.Geometry.Point3d = Nothing
	crv.DivideByLength(seg_length, True, points)
	If points Is Nothing Then
	  Return Rhino.Commands.Result.Failure
	End If

	For Each point As Rhino.Geometry.Point3d In points
	  doc.Objects.AddPoint(point)
	Next point

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

def DivideByLengthPoints():
    filter = Rhino.DocObjects.ObjectType.Curve
    rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select curve to divide", False, filter)
    if not objref or rc!=Rhino.Commands.Result.Success: return rc

    crv = objref.Curve()
    if not crv or crv.IsShort(Rhino.RhinoMath.ZeroTolerance):
        return Rhino.Commands.Result.Failure

    crv_length = crv.GetLength()
    s = "Curve length is {0:.3f}. Segment length".format(crv_length)
    seg_length = crv_length / 2.0
    rc, length = Rhino.Input.RhinoGet.GetNumber(s, False, seg_length, 0, crv_length)
    if rc!=Rhino.Commands.Result.Success: return rc
    t_vals = crv.DivideByLength(length, True)
    if not t_vals:
        return Rhino.Commands.Result.Failure

    [scriptcontext.doc.Objects.AddPoint(crv.PointAt(t)) for t in t_vals]
    scriptcontext.doc.Views.Redraw()
    return Rhino.Commands.Result.Success

if __name__=="__main__":
    DivideByLengthPoints()
```

</div>
