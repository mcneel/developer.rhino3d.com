---
layout: code-sample
title: Loft Surfaces
author: 
categories: ['Other'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['loft', 'surfaces']
order: 107
description:  
---



```cs
public class LoftCommand : Command
{
  public override string EnglishName { get { return "csLoft"; } }

  protected override Result RunCommand(RhinoDoc doc, RunMode mode)
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
Public Class LoftCommand
  Inherits Command
  Public Overrides ReadOnly Property EnglishName() As String
    Get
      Return "vbLoft"
    End Get
  End Property

  Protected Overrides Function RunCommand(doc As RhinoDoc, mode As Rhino.Commands.RunMode) As Result
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

    Dim curves = New List(Of Curve)()
    For Each obj As ObjRef In gs.Objects()
      curves.Add(obj.Curve())
    Next

    Dim breps = Rhino.Geometry.Brep.CreateFromLoft(curves, Point3d.Unset, Point3d.Unset, LoftType.Tight, False)
    For Each brep As Brep In breps
      doc.Objects.AddBrep(brep)
    Next

    doc.Views.Redraw()
    Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
import rhinoscriptsyntax as rs

def RunCommand():
  crvids = rs.GetObjects(message="select curves to loft", filter=rs.filter.curve, minimum_count=2)
  if not crvids: return

  rs.AddLoftSrf(object_ids=crvids, loft_type = 3) #3 = tight

if __name__ == "__main__":
  RunCommand()
```
{: #py .tab-pane .fade .in}


