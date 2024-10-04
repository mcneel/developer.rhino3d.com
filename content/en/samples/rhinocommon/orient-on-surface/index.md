+++
aliases = ["/en/5/samples/rhinocommon/orient-on-surface/", "/en/6/samples/rhinocommon/orient-on-surface/", "/en/7/samples/rhinocommon/orient-on-surface/", "/wip/samples/rhinocommon/orient-on-surface/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to orient objects on a surface."
keywords = [ "orient", "surface" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Orient On Surface"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/orientonsrf"
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
  public static Rhino.Commands.Result OrientOnSrf(Rhino.RhinoDoc doc)
  {
    // Select objects to orient
    Rhino.Input.Custom.GetObject go = new Rhino.Input.Custom.GetObject();
    go.SetCommandPrompt("Select objects to orient");
    go.SubObjectSelect = false;
    go.GroupSelect = true;
    go.GetMultiple(1, 0);
    if (go.CommandResult() != Rhino.Commands.Result.Success)
      return go.CommandResult();

    // Point to orient from
    Rhino.Input.Custom.GetPoint gp = new Rhino.Input.Custom.GetPoint();
    gp.SetCommandPrompt("Point to orient from");
    gp.Get();
    if (gp.CommandResult() != Rhino.Commands.Result.Success)
      return gp.CommandResult();

    // Define source plane
    Rhino.Display.RhinoView view = gp.View();
    if (view == null)
    {
      view = doc.Views.ActiveView;
      if (view == null)
        return Rhino.Commands.Result.Failure;
    }
    Rhino.Geometry.Plane source_plane = view.ActiveViewport.ConstructionPlane();
    source_plane.Origin = gp.Point();

    // Surface to orient on
    Rhino.Input.Custom.GetObject gs = new Rhino.Input.Custom.GetObject();
    gs.SetCommandPrompt("Surface to orient on");
    gs.GeometryFilter = Rhino.DocObjects.ObjectType.Surface;
    gs.SubObjectSelect = true;
    gs.DeselectAllBeforePostSelect = false;
    gs.OneByOnePostSelect = true;
    gs.Get();
    if (gs.CommandResult() != Rhino.Commands.Result.Success)
      return gs.CommandResult();

    Rhino.DocObjects.ObjRef objref = gs.Object(0);
    // get selected surface object
    Rhino.DocObjects.RhinoObject obj = objref.Object();
    if (obj == null)
      return Rhino.Commands.Result.Failure;
    // get selected surface (face)
    Rhino.Geometry.Surface surface = objref.Surface();
    if (surface == null)
      return Rhino.Commands.Result.Failure;
    // Unselect surface
    obj.Select(false);

    // Point on surface to orient to
    gp.SetCommandPrompt("Point on surface to orient to");
    gp.Constrain(surface, false);
    gp.Get();
    if (gp.CommandResult() != Rhino.Commands.Result.Success)
      return gp.CommandResult();

    // Do transformation
    Rhino.Commands.Result rc = Rhino.Commands.Result.Failure;
    double u, v;
    if (surface.ClosestPoint(gp.Point(), out u, out v))
    {
      Rhino.Geometry.Plane target_plane;
      if (surface.FrameAt(u, v, out target_plane))
      {
        // Build transformation
        Rhino.Geometry.Transform xform = Rhino.Geometry.Transform.PlaneToPlane(source_plane, target_plane);

        // Do the transformation. In this example, we will copy the original objects
        const bool delete_original = false;
        for (int i = 0; i < go.ObjectCount; i++)
          doc.Objects.Transform(go.Object(i), xform, delete_original);

        doc.Views.Redraw();
        rc = Rhino.Commands.Result.Success;
      }
    }
    return rc;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function OrientOnSrf(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	' Select objects to orient
	Dim go As New Rhino.Input.Custom.GetObject()
	go.SetCommandPrompt("Select objects to orient")
	go.SubObjectSelect = False
	go.GroupSelect = True
	go.GetMultiple(1, 0)
	If go.CommandResult() <> Rhino.Commands.Result.Success Then
	  Return go.CommandResult()
	End If

	' Point to orient from
	Dim gp As New Rhino.Input.Custom.GetPoint()
	gp.SetCommandPrompt("Point to orient from")
	gp.Get()
	If gp.CommandResult() <> Rhino.Commands.Result.Success Then
	  Return gp.CommandResult()
	End If

	' Define source plane
	Dim view As Rhino.Display.RhinoView = gp.View()
	If view Is Nothing Then
	  view = doc.Views.ActiveView
	  If view Is Nothing Then
		Return Rhino.Commands.Result.Failure
	  End If
	End If
	Dim source_plane As Rhino.Geometry.Plane = view.ActiveViewport.ConstructionPlane()
	source_plane.Origin = gp.Point()

	' Surface to orient on
	Dim gs As New Rhino.Input.Custom.GetObject()
	gs.SetCommandPrompt("Surface to orient on")
	gs.GeometryFilter = Rhino.DocObjects.ObjectType.Surface
	gs.SubObjectSelect = True
	gs.DeselectAllBeforePostSelect = False
	gs.OneByOnePostSelect = True
	gs.Get()
	If gs.CommandResult() <> Rhino.Commands.Result.Success Then
	  Return gs.CommandResult()
	End If

	Dim objref As Rhino.DocObjects.ObjRef = gs.Object(0)
	' get selected surface object
	Dim obj As Rhino.DocObjects.RhinoObject = objref.Object()
	If obj Is Nothing Then
	  Return Rhino.Commands.Result.Failure
	End If
	' get selected surface (face)
	Dim surface As Rhino.Geometry.Surface = objref.Surface()
	If surface Is Nothing Then
	  Return Rhino.Commands.Result.Failure
	End If
	' Unselect surface
	obj.Select(False)

	' Point on surface to orient to
	gp.SetCommandPrompt("Point on surface to orient to")
	gp.Constrain(surface, False)
	gp.Get()
	If gp.CommandResult() <> Rhino.Commands.Result.Success Then
	  Return gp.CommandResult()
	End If

	' Do transformation
	Dim rc As Rhino.Commands.Result = Rhino.Commands.Result.Failure
	Dim u As Double = Nothing, v As Double = Nothing
	If surface.ClosestPoint(gp.Point(), u, v) Then
	  Dim target_plane As Rhino.Geometry.Plane = Nothing
	  If surface.FrameAt(u, v, target_plane) Then
		' Build transformation
		Dim xform As Rhino.Geometry.Transform = Rhino.Geometry.Transform.PlaneToPlane(source_plane, target_plane)

		' Do the transformation. In this example, we will copy the original objects
		Const delete_original As Boolean = False
		For i As Integer = 0 To go.ObjectCount - 1
		  doc.Objects.Transform(go.Object(i), xform, delete_original)
		Next i

		doc.Views.Redraw()
		rc = Rhino.Commands.Result.Success
	  End If
	End If
	Return rc
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
import Rhino
import scriptcontext
import System.Guid

def OrientOnSrf():
    # Select objects to orient
    go = Rhino.Input.Custom.GetObject()
    go.SetCommandPrompt("Select objects to orient")
    go.SubObjectSelect = False
    go.GroupSelect = True
    go.GetMultiple(1, 0)
    if go.CommandResult()!=Rhino.Commands.Result.Success:
        return go.CommandResult()

    # Point to orient from
    gp = Rhino.Input.Custom.GetPoint()
    gp.SetCommandPrompt("Point to orient from")
    gp.Get()
    if gp.CommandResult()!=Rhino.Commands.Result.Success:
        return gp.CommandResult()

    # Define source plane
    view = gp.View()
    if not view:
        view = doc.Views.ActiveView
        if not view: return Rhino.Commands.Result.Failure

    source_plane = view.ActiveViewport.ConstructionPlane()
    source_plane.Origin = gp.Point()

    # Surface to orient on
    gs = Rhino.Input.Custom.GetObject()
    gs.SetCommandPrompt("Surface to orient on")
    gs.GeometryFilter = Rhino.DocObjects.ObjectType.Surface
    gs.SubObjectSelect = True
    gs.DeselectAllBeforePostSelect = False
    gs.OneByOnePostSelect = True
    gs.Get()
    if gs.CommandResult()!=Rhino.Commands.Result.Success:
        return gs.CommandResult()

    objref = gs.Object(0)
    # get selected surface object
    obj = objref.Object()
    if not obj: return Rhino.Commands.Result.Failure
    # get selected surface (face)
    surface = objref.Surface()
    if not surface: return Rhino.Commands.Result.Failure
    # Unselect surface
    obj.Select(False)

    # Point on surface to orient to
    gp.SetCommandPrompt("Point on surface to orient to")
    gp.Constrain(surface, False)
    gp.Get()
    if gp.CommandResult()!=Rhino.Commands.Result.Success:
        return gp.CommandResult()

    # Do transformation
    rc = Rhino.Commands.Result.Failure
    getrc, u, v = surface.ClosestPoint(gp.Point())
    if getrc:
        getrc, target_plane = surface.FrameAt(u,v)
        if getrc:
            # Build transformation
            xform = Rhino.Geometry.Transform.PlaneToPlane(source_plane, target_plane)
            # Do the transformation. In this example, we will copy the original objects
            delete_original = False
            for i in range(go.ObjectCount):
                rhobj = go.Object(i)
                scriptcontext.doc.Objects.Transform(rhobj, xform, delete_original)
            scriptcontext.doc.Views.Redraw()
            rc = Rhino.Commands.Result.Success
    return rc


if __name__=="__main__":
    OrientOnSrf()
```

</div>
