+++
aliases = ["/5/samples/rhinocommon/move-cplane/", "/6/samples/rhinocommon/move-cplane/", "/7/samples/rhinocommon/move-cplane/", "/wip/samples/rhinocommon/move-cplane/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to move a CPlane in the active viewport."
keywords = [ "move", "cplane" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Move CPlane"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

+++

<div class="codetab-content" id="cs">

```cs
class MoveCPlanePoint : Rhino.Input.Custom.GetPoint
{
  readonly Rhino.DocObjects.ConstructionPlane m_cplane;
  public MoveCPlanePoint(Rhino.DocObjects.ConstructionPlane cplane)
  {
    m_cplane = cplane;
  }

  protected override void OnMouseMove(Rhino.Input.Custom.GetPointMouseEventArgs e)
  {
    Plane pl = m_cplane.Plane;
    pl.Origin = e.Point;
    m_cplane.Plane = pl;
  }

  protected override void OnDynamicDraw(Rhino.Input.Custom.GetPointDrawEventArgs e)
  {
    e.Display.DrawConstructionPlane(m_cplane);
  }
}

partial class Examples
{
  public static Rhino.Commands.Result MoveCPlane(Rhino.RhinoDoc doc)
  {
    Rhino.Display.RhinoView view = doc.Views.ActiveView;
    if (view == null)
      return Rhino.Commands.Result.Failure;

    Rhino.DocObjects.ConstructionPlane cplane = view.ActiveViewport.GetConstructionPlane();
    Point3d origin = cplane.Plane.Origin;

    MoveCPlanePoint gp = new MoveCPlanePoint(cplane);
    gp.SetCommandPrompt("CPlane origin");
    gp.SetBasePoint(origin, true);
    gp.DrawLineFromPoint(origin, true);
    gp.Get();

    if (gp.CommandResult() != Rhino.Commands.Result.Success)
      return gp.CommandResult();

    Point3d point = gp.Point();
    Vector3d v = origin - point;
    if (v.IsTiny())
      return Rhino.Commands.Result.Nothing;

    Plane pl = cplane.Plane;
    pl.Origin = point;
    cplane.Plane = pl;
    view.ActiveViewport.SetConstructionPlane(cplane);
    view.Redraw();
    return Rhino.Commands.Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function MoveCPlane(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim view As Rhino.Display.RhinoView = doc.Views.ActiveView
	If view Is Nothing Then
	  Return Rhino.Commands.Result.Failure
	End If

	Dim cplane As Rhino.DocObjects.ConstructionPlane = view.ActiveViewport.GetConstructionPlane()
	Dim origin As Point3d = cplane.Plane.Origin

	Dim gp As New MoveCPlanePoint(cplane)
	gp.SetCommandPrompt("CPlane origin")
	gp.SetBasePoint(origin, True)
	gp.DrawLineFromPoint(origin, True)
	gp.Get()

	If gp.CommandResult() <> Rhino.Commands.Result.Success Then
	  Return gp.CommandResult()
	End If

	Dim point As Point3d = gp.Point()
	Dim v As Vector3d = origin - point
	If v.IsTiny() Then
	  Return Rhino.Commands.Result.Nothing
	End If

	Dim pl As Plane = cplane.Plane
	pl.Origin = point
	cplane.Plane = pl
	view.ActiveViewport.SetConstructionPlane(cplane)
	view.Redraw()
	Return Rhino.Commands.Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
import Rhino
import scriptcontext

class MoveCPlanePoint(Rhino.Input.Custom.GetPoint):
    def __init__(self, cplane):
        self.m_cplane = cplane
    def OnMouseMove(self, e):
        pl = self.m_cplane.Plane
        pl.Origin = e.Point
        self.m_cplane.Plane = pl
    def OnDynamicDraw(self, e):
        e.Display.DrawConstructionPlane(self.m_cplane);

def MoveCPlane():
    view = scriptcontext.doc.Views.ActiveView
    if not view: return Rhino.Commands.Result.Failure

    cplane = view.ActiveViewport.GetConstructionPlane()
    origin = cplane.Plane.Origin
    gp = MoveCPlanePoint(cplane)
    gp.SetCommandPrompt("CPlane origin")
    gp.SetBasePoint(origin, True)
    gp.DrawLineFromPoint(origin, True)
    gp.Get()
    if gp.CommandResult()!=Rhino.Commands.Result.Success:
        return gp.CommandResult()

    point = gp.Point()
    v = origin - point
    if v.IsTiny(): return Rhino.Commands.Result.Nothing
    pl = cplane.Plane
    pl.Origin = point
    cplane.Plane = pl
    view.ActiveViewport.SetConstructionPlane(cplane)
    view.Redraw()
    return Rhino.Commands.Result.Success


if __name__=="__main__":
    MoveCPlane()
```

</div>

