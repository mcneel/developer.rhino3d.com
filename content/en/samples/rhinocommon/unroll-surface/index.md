+++
aliases = ["/en/5/samples/rhinocommon/unroll-surface/", "/en/6/samples/rhinocommon/unroll-surface/", "/en/7/samples/rhinocommon/unroll-surface/", "/wip/samples/rhinocommon/unroll-surface/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Unrolling a developable surface"
keywords = [ "unrolling", "developable", "surface" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Unroll Surface"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/unrollsurface"
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
  public static Rhino.Commands.Result UnrollSurface(Rhino.RhinoDoc doc)
  {
    const ObjectType filter = Rhino.DocObjects.ObjectType.Brep | Rhino.DocObjects.ObjectType.Surface;
    Rhino.DocObjects.ObjRef objref;
    Result rc = Rhino.Input.RhinoGet.GetOneObject("Select surface or brep to unroll", false, filter, out objref);
    if (rc != Rhino.Commands.Result.Success)
      return rc;
    Rhino.Geometry.Unroller unroll=null;
    Rhino.Geometry.Brep brep = objref.Brep();
    if (brep != null)
      unroll = new Rhino.Geometry.Unroller(brep);
    else
    {
      Rhino.Geometry.Surface srf = objref.Surface();
      if (srf != null)
        unroll = new Rhino.Geometry.Unroller(srf);
    }
    if (unroll == null)
      return Rhino.Commands.Result.Cancel;

    unroll.AbsoluteTolerance = 0.01;
    unroll.RelativeTolerance = 0.01;

    Rhino.Input.Custom.GetObject go = new Rhino.Input.Custom.GetObject();
    go.SetCommandPrompt("Select points, curves, and dots to unroll with surface");
    go.GeometryFilter = Rhino.DocObjects.ObjectType.Point | Rhino.DocObjects.ObjectType.Curve | Rhino.DocObjects.ObjectType.TextDot;
    go.AcceptNothing(true);
    go.GetMultiple(0, 0);
    if (go.CommandResult() != Rhino.Commands.Result.Success)
      return go.CommandResult();
    for (int i = 0; i < go.ObjectCount; i++)
    {
      objref = go.Object(i);
      Rhino.Geometry.GeometryBase g = objref.Geometry();
      Rhino.Geometry.Point pt = g as Rhino.Geometry.Point;
      Rhino.Geometry.Curve crv = g as Rhino.Geometry.Curve;
      Rhino.Geometry.TextDot dot = g as Rhino.Geometry.TextDot;
      if (pt != null)
        unroll.AddFollowingGeometry(pt.Location);
      else if (crv != null)
        unroll.AddFollowingGeometry(crv);
      else if (dot != null)
        unroll.AddFollowingGeometry(dot);
    }

    unroll.ExplodeOutput = false;
    Rhino.Geometry.Curve[] curves;
    Rhino.Geometry.Point3d[] points;
    Rhino.Geometry.TextDot[] dots;
    Rhino.Geometry.Brep[] breps = unroll.PerformUnroll(out curves, out points, out dots);
    if (breps == null || breps.Length < 1)
      return Rhino.Commands.Result.Failure;

    for (int i = 0; i < breps.Length; i++)
      doc.Objects.AddBrep(breps[i]);
    for (int i = 0; i < curves.Length; i++)
      doc.Objects.AddCurve(curves[i]);
    doc.Objects.AddPoints(points);
    for (int i = 0; i < dots.Length; i++)
      doc.Objects.AddTextDot(dots[i]);
    doc.Views.Redraw();
    return Rhino.Commands.Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function UnrollSurface(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Const filter As ObjectType = Rhino.DocObjects.ObjectType.Brep Or Rhino.DocObjects.ObjectType.Surface
	Dim objref As Rhino.DocObjects.ObjRef = Nothing
	Dim rc As Result = Rhino.Input.RhinoGet.GetOneObject("Select surface or brep to unroll", False, filter, objref)
	If rc IsNot Rhino.Commands.Result.Success Then
	  Return rc
	End If
	Dim unroll As Rhino.Geometry.Unroller=Nothing
	Dim brep As Rhino.Geometry.Brep = objref.Brep()
	If brep IsNot Nothing Then
	  unroll = New Rhino.Geometry.Unroller(brep)
	Else
	  Dim srf As Rhino.Geometry.Surface = objref.Surface()
	  If srf IsNot Nothing Then
		unroll = New Rhino.Geometry.Unroller(srf)
	  End If
	End If
	If unroll Is Nothing Then
	  Return Rhino.Commands.Result.Cancel
	End If

	unroll.AbsoluteTolerance = 0.01
	unroll.RelativeTolerance = 0.01

	Dim go As New Rhino.Input.Custom.GetObject()
	go.SetCommandPrompt("Select points, curves, and dots to unroll with surface")
	go.GeometryFilter = Rhino.DocObjects.ObjectType.Point Or Rhino.DocObjects.ObjectType.Curve Or Rhino.DocObjects.ObjectType.TextDot
	go.AcceptNothing(True)
	go.GetMultiple(0, 0)
	If go.CommandResult() <> Rhino.Commands.Result.Success Then
	  Return go.CommandResult()
	End If
	For i As Integer = 0 To go.ObjectCount - 1
	  objref = go.Object(i)
	  Dim g As Rhino.Geometry.GeometryBase = objref.Geometry()
	  Dim pt As Rhino.Geometry.Point = TryCast(g, Rhino.Geometry.Point)
	  Dim crv As Rhino.Geometry.Curve = TryCast(g, Rhino.Geometry.Curve)
	  Dim dot As Rhino.Geometry.TextDot = TryCast(g, Rhino.Geometry.TextDot)
	  If pt IsNot Nothing Then
		unroll.AddFollowingGeometry(pt.Location)
	  ElseIf crv IsNot Nothing Then
		unroll.AddFollowingGeometry(crv)
	  ElseIf dot IsNot Nothing Then
		unroll.AddFollowingGeometry(dot)
	  End If
	Next i

	unroll.ExplodeOutput = False
	Dim curves() As Rhino.Geometry.Curve = Nothing
	Dim points() As Rhino.Geometry.Point3d = Nothing
	Dim dots() As Rhino.Geometry.TextDot = Nothing
	Dim breps() As Rhino.Geometry.Brep = unroll.PerformUnroll(curves, points, dots)
	If breps Is Nothing OrElse breps.Length < 1 Then
	  Return Rhino.Commands.Result.Failure
	End If

	For i As Integer = 0 To breps.Length - 1
	  doc.Objects.AddBrep(breps(i))
	Next i
	For i As Integer = 0 To curves.Length - 1
	  doc.Objects.AddCurve(curves(i))
	Next i
	doc.Objects.AddPoints(points)
	For i As Integer = 0 To dots.Length - 1
	  doc.Objects.AddTextDot(dots(i))
	Next i
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

def UnrollSurface():
    filter = Rhino.DocObjects.ObjectType.Brep | Rhino.DocObjects.ObjectType.Surface
    rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select surface or brep to unroll", False, filter)
    if rc!=Rhino.Commands.Result.Success: return rc;

    unroll = Rhino.Geometry.Unroller(objref.Geometry())
    go = Rhino.Input.Custom.GetObject()
    go.SetCommandPrompt("Select points, curves, and dots to unroll with surface")
    go.GeometryFilter = Rhino.DocObjects.ObjectType.Point | Rhino.DocObjects.ObjectType.Curve | Rhino.DocObjects.ObjectType.TextDot
    go.AcceptNothing(True)
    go.GetMultiple(0, 0)
    if go.CommandResult()!=Rhino.Commands.Result.Success:
        return go.CommandResult()

    for i in range(go.ObjectCount):
        objref = go.Object(i);
        g = objref.Geometry();
        unroll.AddFollowingGeometry(g)

    unroll.ExplodeOutput = False
    breps, curves, points, dots = unroll.PerformUnroll()
    if not breps: return Rhino.Commands.Result.Failure
    for brep in breps: scriptcontext.doc.Objects.AddBrep(brep)
    for curve in curves: scriptcontext.doc.Objects.AddCurve(curve)
    for point in points: scriptcontext.doc.Objects.AddPoint(point)
    for dot in dots: scriptcontext.doc.Objects.AddTextDot(dot)
    scriptcontext.doc.Views.Redraw()
    return Rhino.Commands.Result.Success

if __name__=="__main__":
    UnrollSurface()
```

</div>
