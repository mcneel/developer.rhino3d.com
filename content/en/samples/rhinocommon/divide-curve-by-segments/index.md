+++
authors = [ "steve" ]
categories = [ "Curves" ]
description = "Demonstrates how to divide a user-selected curve into length segments."
keywords = [ "divide", "curve", "segments" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Divide Curve by Segments"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/dividecurvesegments"
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
  public static Result DivideCurveBySegments(RhinoDoc doc)
  {
    const ObjectType filter = ObjectType.Curve;
    ObjRef objref;
    var rc = RhinoGet.GetOneObject("Select curve to divide", false, filter, out objref);
    if (rc != Result.Success || objref == null)
      return rc;

    var curve = objref.Curve();
    if (curve == null || curve.IsShort(RhinoMath.ZeroTolerance))
      return Result.Failure;

    var segment_count = 2;
    rc = RhinoGet.GetInteger("Divide curve into how many segments?", false, ref segment_count);
    if (rc != Result.Success)
      return rc;

    Point3d[] points;
    curve.DivideByCount(segment_count, true, out points);
    if (points == null)
      return Result.Failure;

    foreach (var point in points)
      doc.Objects.AddPoint(point);

    doc.Views.Redraw();
    return Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function DivideCurveBySegments(ByVal doc As RhinoDoc) As Result
	Const filter As ObjectType = ObjectType.Curve
	Dim objref As ObjRef = Nothing
	Dim rc = RhinoGet.GetOneObject("Select curve to divide", False, filter, objref)
	If rc IsNot Result.Success OrElse objref Is Nothing Then
	  Return rc
	End If

	Dim curve = objref.Curve()
	If curve Is Nothing OrElse curve.IsShort(RhinoMath.ZeroTolerance) Then
	  Return Result.Failure
	End If

	Dim segment_count = 2
	rc = RhinoGet.GetInteger("Divide curve into how many segments?", False, segment_count)
	If rc IsNot Result.Success Then
	  Return rc
	End If

	Dim points() As Point3d = Nothing
	curve.DivideByCount(segment_count, True, points)
	If points Is Nothing Then
	  Return Result.Failure
	End If

	For Each point In points
	  doc.Objects.AddPoint(point)
	Next point

	doc.Views.Redraw()
	Return Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
from Rhino.DocObjects import *
from Rhino.Input import *
from Rhino.Commands import *
from Rhino.Geometry import *
from Rhino import *
from scriptcontext import doc

def RunCommand():
    rc, objref = RhinoGet.GetOneObject("Select curve to divide", False, ObjectType.Curve)
    if rc != Result.Success or objref == None:
        return rc

    curve = objref.Curve()
    if curve == None or curve.IsShort(RhinoMath.ZeroTolerance):
        return Result.Failure

    segment_count = 2
    rc, segment_count = RhinoGet.GetInteger("Divide curve into how many segments?", False, segment_count)
    if rc != Result.Success:
        return rc

    curve_params = curve.DivideByCount(segment_count, True)
    if curve_params == None:
        return Result.Failure

    points = [curve.PointAt(t) for t in curve_params]
    for point in points:
        doc.Objects.AddPoint(point)

    doc.Views.Redraw()
    return Result.Success

if __name__ == "__main__":
    RunCommand()
```

</div>
