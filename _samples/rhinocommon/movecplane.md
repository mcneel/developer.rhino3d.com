---
layout: code-sample
author:
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
title: Move CPlane
keywords: ['move', 'cplane']
categories: ['Other']
description:
order: 1
---

```cs
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
{: #cs .tab-pane .fade .in .active}


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
{: #vb .tab-pane .fade .in}

