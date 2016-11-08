---
title: Surface from Edge Curves
description: Create a Surface from Edge Curves
author: ['Steve Baer', '@stevebaer']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Curves']
origin: http://wiki.mcneel.com/developer/rhinocommonsamples/edgesrf
order: 1
keywords: ['create', 'surface', 'edge', 'curves']
layout: code-sample-rhinocommon
---

```cs
partial class Examples
{
  public static Result EdgeSrf(RhinoDoc doc)
  {
    var go = new GetObject();
    go.SetCommandPrompt("Select 2, 3, or 4 open curves");
    go.GeometryFilter = ObjectType.Curve;
    go.GeometryAttributeFilter = GeometryAttributeFilter.OpenCurve;
    go.GetMultiple(2, 4);
    if (go.CommandResult() != Result.Success)
      return go.CommandResult();

    var curves = go.Objects().Select(o => o.Curve());

    var brep = Brep.CreateEdgeSurface(curves);

    if (brep != null)
    {
      doc.Objects.AddBrep(brep);
      doc.Views.Redraw();
    }

    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function EdgeSrf(ByVal doc As RhinoDoc) As Result
	Dim go = New GetObject()
	go.SetCommandPrompt("Select 2, 3, or 4 open curves")
	go.GeometryFilter = ObjectType.Curve
	go.GeometryAttributeFilter = GeometryAttributeFilter.OpenCurve
	go.GetMultiple(2, 4)
	If go.CommandResult() <> Result.Success Then
	  Return go.CommandResult()
	End If

	Dim curves = go.Objects().Select(Function(o) o.Curve())

	Dim brep = Brep.CreateEdgeSurface(curves)

	If brep IsNot Nothing Then
	  doc.Objects.AddBrep(brep)
	  doc.Views.Redraw()
	End If

	Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
from Rhino import *
from Rhino.Commands import *
from Rhino.DocObjects import *
from Rhino.Geometry import *
from Rhino.Input.Custom import *
from scriptcontext import doc

def RunCommand():
  go = GetObject()
  go.SetCommandPrompt("Select 2, 3, or 4 open curves")
  go.GeometryFilter = ObjectType.Curve
  go.GeometryAttributeFilter = GeometryAttributeFilter.OpenCurve
  go.GetMultiple(2, 4)
  if go.CommandResult() <> Result.Success:
    return go.CommandResult()

  curves = [o.Curve() for o in go.Objects()]

  brep = Brep.CreateEdgeSurface(curves)

  if brep <> None:
    doc.Objects.AddBrep(brep)
    doc.Views.Redraw()

  return Result.Success

if __name__ == "__main__":
  RunCommand()
```
{: #py .tab-pane .fade .in}
