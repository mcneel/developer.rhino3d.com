---
layout: code-sample
title: Create a Surface from Edge Curves
author: 
categories: ['Other'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['create', 'surface', 'edge', 'curves']
order: 72
description:  
---



```cs
public class EdgeSrfCommand : Command
{
  public override string EnglishName { get { return "csEdgeSrf"; } }

  protected override Result RunCommand(RhinoDoc doc, RunMode mode)
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
Public Class EdgeSrfCommand
  Inherits Command
  Public Overrides ReadOnly Property EnglishName() As String
    Get
      Return "vbEdgeSrf"
    End Get
  End Property

  Protected Overrides Function RunCommand(doc As RhinoDoc, mode As RunMode) As Result
    Dim go = New GetObject()
    go.SetCommandPrompt("Select 2, 3, or 4 open curves")
    go.GeometryFilter = ObjectType.Curve
    go.GeometryAttributeFilter = GeometryAttributeFilter.OpenCurve
    go.GetMultiple(2, 4)
    If go.CommandResult() <> Result.Success Then
      Return go.CommandResult()
    End If

    Dim curves = go.Objects().[Select](Function(o) o.Curve())

    Dim brep__1 = Brep.CreateEdgeSurface(curves)

    If brep__1 IsNot Nothing Then
      doc.Objects.AddBrep(brep__1)
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


