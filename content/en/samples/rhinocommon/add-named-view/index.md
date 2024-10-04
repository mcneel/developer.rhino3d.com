+++
aliases = ["/en/5/samples/rhinocommon/add-named-view/", "/en/6/samples/rhinocommon/add-named-view/", "/en/7/samples/rhinocommon/add-named-view/", "/wip/samples/rhinocommon/add-named-view/"]
authors = [ "steve" ]
categories = [ "Adding Objects", "Viewports and Views" ]
description = "Demonstrates how to add a named view to a Rhino model from a user-specified view and camera location."
keywords = [ "add", "named", "view" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Add Named View"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/addnamedview"
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
  public static Rhino.Commands.Result AddNamedView(Rhino.RhinoDoc doc)
  {
    Rhino.Display.RhinoView view;
    Rhino.Commands.Result rc = Rhino.Input.RhinoGet.GetView("Select view to adjust", out view);
    if (rc != Rhino.Commands.Result.Success)
      return rc;

    Rhino.Geometry.Point3d location;
    rc = Rhino.Input.RhinoGet.GetPoint("Camera Location", false, out location);
    if (rc != Rhino.Commands.Result.Success)
      return rc;

    Rhino.Input.Custom.GetPoint gp = new Rhino.Input.Custom.GetPoint();
    gp.SetCommandPrompt("Look At Location");
    gp.DrawLineFromPoint(location, false);
    gp.Get();
    if (gp.CommandResult() != Rhino.Commands.Result.Success)
      return gp.CommandResult();
    Rhino.Geometry.Point3d lookat = gp.Point();

    string name = view.ActiveViewport.Name;
    rc = Rhino.Input.RhinoGet.GetString("Name", true, ref name);
    if (rc != Rhino.Commands.Result.Success)
      return rc;

    Rhino.Display.RhinoViewport vp = view.ActiveViewport;
    // save the current viewport projection
    vp.PushViewProjection();
    vp.CameraUp = Rhino.Geometry.Vector3d.ZAxis;
    vp.SetCameraLocation(location, false);
    vp.SetCameraDirection(lookat - location, true);
    vp.Name = name;

    doc.NamedViews.Add(name, vp.Id);
    view.Redraw();
    return Rhino.Commands.Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function AddNamedView(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim view As Rhino.Display.RhinoView = Nothing
	Dim rc As Rhino.Commands.Result = Rhino.Input.RhinoGet.GetView("Select view to adjust", view)
	If rc IsNot Rhino.Commands.Result.Success Then
	  Return rc
	End If

	Dim location As Rhino.Geometry.Point3d = Nothing
	rc = Rhino.Input.RhinoGet.GetPoint("Camera Location", False, location)
	If rc IsNot Rhino.Commands.Result.Success Then
	  Return rc
	End If

	Dim gp As New Rhino.Input.Custom.GetPoint()
	gp.SetCommandPrompt("Look At Location")
	gp.DrawLineFromPoint(location, False)
	gp.Get()
	If gp.CommandResult() <> Rhino.Commands.Result.Success Then
	  Return gp.CommandResult()
	End If
	Dim lookat As Rhino.Geometry.Point3d = gp.Point()

	Dim name As String = view.ActiveViewport.Name
	rc = Rhino.Input.RhinoGet.GetString("Name", True, name)
	If rc IsNot Rhino.Commands.Result.Success Then
	  Return rc
	End If

	Dim vp As Rhino.Display.RhinoViewport = view.ActiveViewport
	' save the current viewport projection
	vp.PushViewProjection()
	vp.CameraUp = Rhino.Geometry.Vector3d.ZAxis
	vp.SetCameraLocation(location, False)
	vp.SetCameraDirection(lookat - location, True)
	vp.Name = name

	doc.NamedViews.Add(name, vp.Id)
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
import System.Guid

def AddNamedView():
    rc, view = Rhino.Input.RhinoGet.GetView("Select view to adjust")
    if rc!=Rhino.Commands.Result.Success: return rc

    rc, location = Rhino.Input.RhinoGet.GetPoint("Camera Location", False)
    if rc!=Rhino.Commands.Result.Success: return rc

    gp = Rhino.Input.Custom.GetPoint()
    gp.SetCommandPrompt("Look At Location")
    gp.DrawLineFromPoint(location, False)
    gp.Get()
    if gp.CommandResult()!=Rhino.Commands.Result.Success:
        return gp.CommandResult()
    lookat = gp.Point()

    name = view.ActiveViewport.Name
    rc, name = Rhino.Input.RhinoGet.GetString("Name", True, name)
    if rc!=Rhino.Commands.Result.Success: return rc

    vp = view.ActiveViewport
    # save the current viewport projection
    vp.PushViewProjection()
    vp.CameraUp = Rhino.Geometry.Vector3d.ZAxis
    vp.SetCameraLocation(location, False)
    vp.SetCameraDirection(lookat - location, True)
    vp.Name = name

    scriptcontext.doc.NamedViews.Add(name, vp.Id)
    view.Redraw()
    return Rhino.Commands.Result.Success

if __name__=="__main__":
    AddNamedView()
```

</div>
