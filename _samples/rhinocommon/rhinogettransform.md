---
layout: code-sample
title: Showing Dynamic Object Transformations
author: 
categories: ['Other'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['showing', 'dynamic', 'object', 'transformations']
order: 144
description:  
---



```cs
public class GetTranslation : GetTransform
{
  public override Transform CalculateTransform(RhinoViewport viewport, Point3d point)
  {
    var xform = Transform.Identity;
    Point3d base_point;
    if (TryGetBasePoint(out base_point))
    {
      var v = point - base_point;
      if (!v.IsZero)
      {
        xform = Transform.Translation(v);
        if (!xform.IsValid)
          xform = Transform.Identity;
      }
    }
    return xform;
  }
}

public class RhinoGetTransformCommand : TransformCommand
{
  public RhinoGetTransformCommand()
  {
    // simple example of handling the BeforeTransformObjects event
    RhinoDoc.BeforeTransformObjects += RhinoDocOnBeforeTransformObjects;
  }

  private void RhinoDocOnBeforeTransformObjects(object sender, RhinoTransformObjectsEventArgs ea)
  {
    RhinoApp.WriteLine("Transform Objects Count: {0}", ea.ObjectCount);
  }

  public override string EnglishName { get { return "csGetTranslation"; } }

  protected override Result RunCommand(RhinoDoc doc, RunMode mode)
  {
    var list = new Rhino.Collections.TransformObjectList();
    var rc = SelectObjects("Select objects to move", list);
    if (rc != Rhino.Commands.Result.Success)
      return rc;

    var gp = new GetPoint();
    gp.SetCommandPrompt("Point to move from");
    gp.Get();
    if (gp.CommandResult() != Result.Success)
      return gp.CommandResult();


    var gt = new GetTranslation();
    gt.SetCommandPrompt("Point to move to");
    gt.SetBasePoint(gp.Point(), true);
    gt.DrawLineFromPoint(gp.Point(), true);
    gt.AddTransformObjects(list);
    gt.GetXform();
    if (gt.CommandResult() != Result.Success)
      return gt.CommandResult();

    var xform = gt.CalculateTransform(gt.View().ActiveViewport, gt.Point());
    TransformObjects(list, xform, false, false);
    doc.Views.Redraw();
    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Public Class GetTranslation
  Inherits GetTransform
  Public Overrides Function CalculateTransform(viewport As RhinoViewport, point As Point3d) As Transform
    Dim xform = Transform.Identity
    Dim base_point As Point3d
    If TryGetBasePoint(base_point) Then
      Dim v = point - base_point
      If Not v.IsZero Then
        xform = Transform.Translation(v)
        If Not xform.IsValid Then
          xform = Transform.Identity
        End If
      End If
    End If
    Return xform
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
import Rhino
from Rhino.Geometry import *
from Rhino.Input.Custom import *
from Rhino.Commands import *
from scriptcontext import doc
import rhinoscriptsyntax as rs

class GetTranslation(GetTransform):
  def CalculateTransform(self, viewport, point):
    xform = Transform.Identity
    b, base_point = self.TryGetBasePoint()
    if (b):
      v = point - base_point
      if (not v.IsZero):
        xform = Transform.Translation(v)
        if (not xform.IsValid):
          xform = Transform.Identity
    return xform

def RunCommand():
  objectIds = rs.GetObjects("Select objects to move")
  if objectIds is None: return

  gp = GetPoint()
  gp.SetCommandPrompt("Point to move from")
  gp.Get()
  if gp.CommandResult() != Result.Success:
    return gp.CommandResult()

  gt = GetTranslation()
  gt.SetCommandPrompt("Point to move to")
  gt.SetBasePoint(gp.Point(), True)
  gt.DrawLineFromPoint(gp.Point(), True)
  gt.GetXform()
  if gt.CommandResult() != Result.Success:
    return gt.CommandResult()

  list = Rhino.Collections.TransformObjectList()
  for id in objectIds:
      rhobj = rs.coercerhinoobject(id, True, True)
      list.Add(rhobj)
  gt.AddTransformObjects(list)

  xform = gt.CalculateTransform(gt.View().ActiveViewport, gt.Point())
  TransformObjects(list, xform, False, False)
  doc.Views.Redraw()
  return Result.Success

if __name__ == "__main__":
  RunCommand()
```
{: #py .tab-pane .fade .in}


