+++
aliases = ["/en/5/samples/rhinocommon/constrained-copy/", "/en/6/samples/rhinocommon/constrained-copy/", "/en/7/samples/rhinocommon/constrained-copy/", "/wip/samples/rhinocommon/constrained-copy/"]
authors = [ "steve" ]
categories = [ "Curves" ]
description = "Demonstrates how to use a constrained GetPoint to copy a curve."
keywords = [ "constrained", "getpoint", "copy", "curve" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Constrained Copy"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/constrainedcopy"
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
  public static Rhino.Commands.Result ConstrainedCopy(Rhino.RhinoDoc doc)
  {
    // Get a single planar closed curve
    var go = new Rhino.Input.Custom.GetObject();
    go.SetCommandPrompt("Select curve");
    go.GeometryFilter = Rhino.DocObjects.ObjectType.Curve;
    go.GeometryAttributeFilter = Rhino.Input.Custom.GeometryAttributeFilter.ClosedCurve;
    go.Get();
    if( go.CommandResult() != Rhino.Commands.Result.Success )
      return go.CommandResult();
    var objref = go.Object(0);
    var base_curve = objref.Curve();
    var first_point = objref.SelectionPoint();
    if( base_curve==null || !first_point.IsValid )
      return Rhino.Commands.Result.Cancel;

    Rhino.Geometry.Plane plane;
    if( !base_curve.TryGetPlane(out plane) )
      return Rhino.Commands.Result.Cancel;

    // Get a point constrained to a line passing through the initial selection
    // point and parallel to the plane's normal
    var gp = new Rhino.Input.Custom.GetPoint();
    gp.SetCommandPrompt("Offset point");
    gp.DrawLineFromPoint(first_point, true);
    var line = new Rhino.Geometry.Line(first_point, first_point+plane.Normal);
    gp.Constrain(line);
    gp.Get();
    if( gp.CommandResult() != Rhino.Commands.Result.Success )
      return gp.CommandResult();
    var second_point = gp.Point();
    Rhino.Geometry.Vector3d vec = second_point - first_point;
    if( vec.Length > 0.001 )
    {
      var xf = Rhino.Geometry.Transform.Translation(vec);
      Guid id = doc.Objects.Transform(objref, xf, false);
      if( id!=Guid.Empty )
      {
        doc.Views.Redraw();
        return Rhino.Commands.Result.Success;
      }
    }
    return Rhino.Commands.Result.Cancel;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function ConstrainedCopy(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	' Get a single planar closed curve
	Dim go = New Rhino.Input.Custom.GetObject()
	go.SetCommandPrompt("Select curve")
	go.GeometryFilter = Rhino.DocObjects.ObjectType.Curve
	go.GeometryAttributeFilter = Rhino.Input.Custom.GeometryAttributeFilter.ClosedCurve
	go.Get()
	If go.CommandResult() <> Rhino.Commands.Result.Success Then
	  Return go.CommandResult()
	End If
	Dim objref = go.Object(0)
	Dim base_curve = objref.Curve()
	Dim first_point = objref.SelectionPoint()
	If base_curve Is Nothing OrElse Not first_point.IsValid Then
	  Return Rhino.Commands.Result.Cancel
	End If

	Dim plane As Rhino.Geometry.Plane = Nothing
	If Not base_curve.TryGetPlane(plane) Then
	  Return Rhino.Commands.Result.Cancel
	End If

	' Get a point constrained to a line passing through the initial selection
	' point and parallel to the plane's normal
	Dim gp = New Rhino.Input.Custom.GetPoint()
	gp.SetCommandPrompt("Offset point")
	gp.DrawLineFromPoint(first_point, True)
	Dim line = New Rhino.Geometry.Line(first_point, first_point+plane.Normal)
	gp.Constrain(line)
	gp.Get()
	If gp.CommandResult() <> Rhino.Commands.Result.Success Then
	  Return gp.CommandResult()
	End If
	Dim second_point = gp.Point()
	Dim vec As Rhino.Geometry.Vector3d = second_point - first_point
	If vec.Length > 0.001 Then
	  Dim xf = Rhino.Geometry.Transform.Translation(vec)
	  Dim id As Guid = doc.Objects.Transform(objref, xf, False)
	  If id<>Guid.Empty Then
		doc.Views.Redraw()
		Return Rhino.Commands.Result.Success
	  End If
	End If
	Return Rhino.Commands.Result.Cancel
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
import Rhino
import scriptcontext

def constrainedcopy():
    #get a single closed curve
    go = Rhino.Input.Custom.GetObject()
    go.SetCommandPrompt("Select curve")
    go.GeometryFilter = Rhino.DocObjects.ObjectType.Curve
    go.GeometryAttributeFilter = Rhino.Input.Custom.GeometryAttributeFilter.ClosedCurve
    go.Get()
    if go.CommandResult() != Rhino.Commands.Result.Success: return
    objref = go.Object(0)
    base_curve = objref.Curve()
    first_point = objref.SelectionPoint()
    if not base_curve or not first_point.IsValid:
        return
    isplanar, plane = base_curve.TryGetPlane()
    if not isplanar: return

    gp = Rhino.Input.Custom.GetPoint()
    gp.SetCommandPrompt("Offset point")
    gp.DrawLineFromPoint(first_point, True)
    line = Rhino.Geometry.Line(first_point, first_point + plane.Normal)
    gp.Constrain(line)
    gp.Get()
    if gp.CommandResult() != Rhino.Commands.Result.Success:
        return
    second_point = gp.Point()
    vec = second_point - first_point
    if vec.Length > 0.001:
        xf = Rhino.Geometry.Transform.Translation(vec)
        id = scriptcontext.doc.Objects.Transform(objref, xf, False)
        scriptcontext.doc.Views.Redraw()
        return id

if __name__=="__main__":
    constrainedcopy()
```

</div>
