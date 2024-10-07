+++
aliases = ["/en/5/samples/rhinocommon/loft-surfaces/", "/en/6/samples/rhinocommon/loft-surfaces/", "/en/7/samples/rhinocommon/loft-surfaces/", "/en/wip/samples/rhinocommon/loft-surfaces/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to create a lofted surface from a set of user-specified curves."
keywords = [ "loft", "surfaces" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Loft Surfaces"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/loft"
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
  public static Result Loft(RhinoDoc doc)
  {
    // select curves to loft
    var gs = new GetObject();
    gs.SetCommandPrompt("select curves to loft");
    gs.GeometryFilter = ObjectType.Curve;
    gs.DisablePreSelect();
    gs.SubObjectSelect = false;
    gs.GetMultiple(2, 0);
    if (gs.CommandResult() != Result.Success)
      return gs.CommandResult();

    var curves = gs.Objects().Select(obj => obj.Curve()).ToList();

    var breps = Brep.CreateFromLoft(curves, Point3d.Unset, Point3d.Unset, LoftType.Tight, false);
    foreach (var brep in breps)
      doc.Objects.AddBrep(brep);

    doc.Views.Redraw();
    return Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function Loft(ByVal doc As RhinoDoc) As Result
	' select curves to loft
	Dim gs = New GetObject()
	gs.SetCommandPrompt("select curves to loft")
	gs.GeometryFilter = ObjectType.Curve
	gs.DisablePreSelect()
	gs.SubObjectSelect = False
	gs.GetMultiple(2, 0)
	If gs.CommandResult() <> Result.Success Then
	  Return gs.CommandResult()
	End If

	Dim curves = gs.Objects().Select(Function(obj) obj.Curve()).ToList()

	Dim breps = Brep.CreateFromLoft(curves, Point3d.Unset, Point3d.Unset, LoftType.Tight, False)
	For Each brep In breps
	  doc.Objects.AddBrep(brep)
	Next brep

	doc.Views.Redraw()
	Return Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
import rhinoscriptsyntax as rs

def RunCommand():
    crvids = rs.GetObjects(message="select curves to loft", filter=rs.filter.curve, minimum_count=2)
    if not crvids: return

    rs.AddLoftSrf(object_ids=crvids, loft_type = 3) #3 = tight

if __name__ == "__main__":
    RunCommand()
```

</div>
