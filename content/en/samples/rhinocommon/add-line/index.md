+++
aliases = ["/en/5/samples/rhinocommon/add-line/", "/en/6/samples/rhinocommon/add-line/", "/en/7/samples/rhinocommon/add-line/", "/wip/samples/rhinocommon/add-line/"]
authors = [ "steve" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to construct a line from two points."
keywords = [ "add", "line" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Add Line"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/addline"
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
  public static Rhino.Commands.Result AddLine(Rhino.RhinoDoc doc)
  {
    Rhino.Input.Custom.GetPoint gp = new Rhino.Input.Custom.GetPoint();
    gp.SetCommandPrompt("Start of line");
    gp.Get();
    if (gp.CommandResult() != Rhino.Commands.Result.Success)
      return gp.CommandResult();

    Rhino.Geometry.Point3d pt_start = gp.Point();

    gp.SetCommandPrompt("End of line");
    gp.SetBasePoint(pt_start, false);
    gp.DrawLineFromPoint(pt_start, true);
    gp.Get();
    if (gp.CommandResult() != Rhino.Commands.Result.Success)
      return gp.CommandResult();

    Rhino.Geometry.Point3d pt_end = gp.Point();
    Rhino.Geometry.Vector3d v = pt_end - pt_start;
    if (v.IsTiny(Rhino.RhinoMath.ZeroTolerance))
      return Rhino.Commands.Result.Nothing;

    if (doc.Objects.AddLine(pt_start, pt_end) != Guid.Empty)
    {
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
  Public Shared Function AddLine(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim gp As New Rhino.Input.Custom.GetPoint()
	gp.SetCommandPrompt("Start of line")
	gp.Get()
	If gp.CommandResult() <> Rhino.Commands.Result.Success Then
	  Return gp.CommandResult()
	End If

	Dim pt_start As Rhino.Geometry.Point3d = gp.Point()

	gp.SetCommandPrompt("End of line")
	gp.SetBasePoint(pt_start, False)
	gp.DrawLineFromPoint(pt_start, True)
	gp.Get()
	If gp.CommandResult() <> Rhino.Commands.Result.Success Then
	  Return gp.CommandResult()
	End If

	Dim pt_end As Rhino.Geometry.Point3d = gp.Point()
	Dim v As Rhino.Geometry.Vector3d = pt_end - pt_start
	If v.IsTiny(Rhino.RhinoMath.ZeroTolerance) Then
	  Return Rhino.Commands.Result.Nothing
	End If

	If doc.Objects.AddLine(pt_start, pt_end) <> Guid.Empty Then
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
import Rhino
import scriptcontext
import System.Guid

def AddLine():
    gp = Rhino.Input.Custom.GetPoint()
    gp.SetCommandPrompt("Start of line")
    gp.Get()
    if gp.CommandResult()!=Rhino.Commands.Result.Success:
        return gp.CommandResult()
    pt_start = gp.Point()

    gp.SetCommandPrompt("End of line")
    gp.SetBasePoint(pt_start, False)
    gp.DrawLineFromPoint(pt_start, True)
    gp.Get()
    if gp.CommandResult() != Rhino.Commands.Result.Success:
        return gp.CommandResult()
    pt_end = gp.Point()
    v = pt_end - pt_start
    if v.IsTiny(Rhino.RhinoMath.ZeroTolerance):
        return Rhino.Commands.Result.Nothing

    id = scriptcontext.doc.Objects.AddLine(pt_start, pt_end)
    if id!=System.Guid.Empty:
        scriptcontext.doc.Views.Redraw()
        return Rhino.Commands.Result.Success
    return Rhino.Commands.Result.Failure

if __name__=="__main__":
    AddLine()
```

</div>
