---
layout: code-sample
author:
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
title: Loft Surfaces
keywords: ['loft', 'surfaces']
categories: ['Other']
description:
order: 1
---

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
{: #cs .tab-pane .fade .in .active}


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
{: #vb .tab-pane .fade .in .active}


```python
import rhinoscriptsyntax as rs

def RunCommand():
  crvids = rs.GetObjects(message="select curves to loft", filter=rs.filter.curve, minimum_count=2)
  if not crvids: return

  rs.AddLoftSrf(object_ids=crvids, loft_type = 3) #3 = tight

if __name__ == "__main__":
  RunCommand()
```
{: #py .tab-pane .fade .in .active}

