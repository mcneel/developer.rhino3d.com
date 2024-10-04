+++
aliases = ["/en/5/samples/rhinocommon/intersect-lines/", "/en/6/samples/rhinocommon/intersect-lines/", "/en/7/samples/rhinocommon/intersect-lines/", "/wip/samples/rhinocommon/intersect-lines/"]
authors = [ "steve" ]
categories = [ "Curves" ]
description = "Demonstrates how to find the intersection point of two (non-parallel) lines."
keywords = [ "intersecting", "line", "curves" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Intersect Lines"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/intersectlines"
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
  public static Rhino.Commands.Result IntersectLines(Rhino.RhinoDoc doc)
  {
    Rhino.Input.Custom.GetObject go = new Rhino.Input.Custom.GetObject();
    go.SetCommandPrompt( "Select lines" );
    go.GeometryFilter = Rhino.DocObjects.ObjectType.Curve;
    go.GetMultiple( 2, 2);
    if( go.CommandResult() != Rhino.Commands.Result.Success )
      return go.CommandResult();
    if( go.ObjectCount != 2 )
      return Rhino.Commands.Result.Failure;

    LineCurve crv0 = go.Object(0).Geometry() as LineCurve;
    LineCurve crv1 = go.Object(1).Geometry() as LineCurve;
    if( crv0==null || crv1==null )
      return Rhino.Commands.Result.Failure;

    Line line0 = crv0.Line;
    Line line1 = crv1.Line;
    Vector3d v0 = line0.Direction;
    v0.Unitize();
    Vector3d v1 = line1.Direction;
    v1.Unitize();

    if( v0.IsParallelTo(v1) != 0 )
    {
      Rhino.RhinoApp.WriteLine("Selected lines are parallel.");
      return Rhino.Commands.Result.Nothing;
    }

    double a, b;
    if( !Rhino.Geometry.Intersect.Intersection.LineLine(line0, line1, out a, out b))
    {
      Rhino.RhinoApp.WriteLine("No intersection found.");
      return Rhino.Commands.Result.Nothing;
    }

    Point3d pt0 = line0.PointAt(a);
    doc.Objects.AddPoint( pt0 );
    doc.Views.Redraw();
    return Rhino.Commands.Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function IntersectLines(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim go As New Rhino.Input.Custom.GetObject()
	go.SetCommandPrompt("Select lines")
	go.GeometryFilter = Rhino.DocObjects.ObjectType.Curve
	go.GetMultiple(2, 2)
	If go.CommandResult() <> Rhino.Commands.Result.Success Then
	  Return go.CommandResult()
	End If
	If go.ObjectCount <> 2 Then
	  Return Rhino.Commands.Result.Failure
	End If

	Dim crv0 As LineCurve = TryCast(go.Object(0).Geometry(), LineCurve)
	Dim crv1 As LineCurve = TryCast(go.Object(1).Geometry(), LineCurve)
	If crv0 Is Nothing OrElse crv1 Is Nothing Then
	  Return Rhino.Commands.Result.Failure
	End If

	Dim line0 As Line = crv0.Line
	Dim line1 As Line = crv1.Line
	Dim v0 As Vector3d = line0.Direction
	v0.Unitize()
	Dim v1 As Vector3d = line1.Direction
	v1.Unitize()

	If v0.IsParallelTo(v1) <> 0 Then
	  Rhino.RhinoApp.WriteLine("Selected lines are parallel.")
	  Return Rhino.Commands.Result.Nothing
	End If

	Dim a As Double = Nothing, b As Double = Nothing
	If Not Rhino.Geometry.Intersect.Intersection.LineLine(line0, line1, a, b) Then
	  Rhino.RhinoApp.WriteLine("No intersection found.")
	  Return Rhino.Commands.Result.Nothing
	End If

	Dim pt0 As Point3d = line0.PointAt(a)
	doc.Objects.AddPoint(pt0)
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

def IntersectLines():
    go = Rhino.Input.Custom.GetObject()
    go.SetCommandPrompt( "Select lines" )
    go.GeometryFilter = Rhino.DocObjects.ObjectType.Curve
    go.GetMultiple( 2, 2)
    if go.CommandResult()!=Rhino.Commands.Result.Success:
        return go.CommandResult()
    if go.ObjectCount!=2: return Rhino.Commands.Result.Failure

    crv0 = go.Object(0).Geometry()
    crv1 = go.Object(1).Geometry()
    if not crv0 or not crv1: return Rhino.Commands.Result.Failure

    line0 = crv0.Line
    line1 = crv1.Line
    v0 = line0.Direction
    v0.Unitize()
    v1 = line1.Direction
    v1.Unitize()

    if v0.IsParallelTo(v1)!=0:
        print "Selected lines are parallel."
        return Rhino.Commands.Result.Nothing

    rc, a, b = Rhino.Geometry.Intersect.Intersection.LineLine(line0, line1)
    if not rc:
        print "No intersection found."
        return Rhino.Commands.Result.Nothing

    pt0 = line0.PointAt(a)
    pt1 = line1.PointAt(b)
    # pt0 and pt1 should be equal, so we will only add pt0 to the document
    scriptcontext.doc.Objects.AddPoint(pt0)
    scriptcontext.doc.Views.Redraw()
    return Rhino.Commands.Result.Success

if __name__=="__main__":
    IntersectLines()
```

</div>
