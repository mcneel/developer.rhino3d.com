---
layout: code-sample
title: Pick Objects
author: 
categories: ['Picking and Selection'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['pick', 'objects']
order: 129
description:  
---



```cs
public class PickPointsOnConduitCommand : Rhino.Commands.Command
{
  private readonly List<ConduitPoint> m_conduit_points = new List<ConduitPoint>();

  public override string EnglishName { get { return "csPickPoints"; } }

  protected override Rhino.Commands.Result RunCommand(RhinoDoc doc, Rhino.Commands.RunMode mode)
  {
    var conduit = new PointsConduit(m_conduit_points);
    conduit.Enabled = true;

    var gp = new Rhino.Input.Custom.GetPoint();
    while (true)
    {
      gp.SetCommandPrompt("click location to create point. (<ESC> exit)");
      gp.AcceptNothing(true);
      gp.Get();
      if (gp.CommandResult() != Rhino.Commands.Result.Success)
        break;
      m_conduit_points.Add(new ConduitPoint(gp.Point()));
      doc.Views.Redraw();
    }

    var gcp = new GetConduitPoint(m_conduit_points);
    while (true)
    {
      gcp.SetCommandPrompt("select conduit point. (<ESC> to exit)");
      gcp.AcceptNothing(true);
      gcp.Get(true);
      doc.Views.Redraw();
      if (gcp.CommandResult() != Rhino.Commands.Result.Success)
        break;
    }

    return Rhino.Commands.Result.Success;
  }
}

public class ConduitPoint
{
  public ConduitPoint(Point3d point)
  {
    Color = System.Drawing.Color.White;
    Point = point;
  }
  public System.Drawing.Color Color { get; set; }
  public Point3d Point { get; set; }
}

public class GetConduitPoint : GetPoint
{
  private readonly List<ConduitPoint> m_conduit_points;
 
  public GetConduitPoint(List<ConduitPoint> conduitPoints )
  {
    m_conduit_points = conduitPoints;
  }

  protected override void OnMouseDown(GetPointMouseEventArgs e)
  {
    base.OnMouseDown(e);
    var picker = new PickContext();
    picker.View = e.Viewport.ParentView;

    picker.PickStyle = PickStyle.PointPick;

    var xform = e.Viewport.GetPickTransform(e.WindowPoint);
    picker.SetPickTransform(xform);

    foreach (var cp in m_conduit_points)
    {
      double depth;
      double distance;
      if (picker.PickFrustumTest(cp.Point, out depth, out distance))
        cp.Color = System.Drawing.Color.Red;
      else
        cp.Color = System.Drawing.Color.White;
    }
  }
}

class PointsConduit : Rhino.Display.DisplayConduit
{
  private readonly List<ConduitPoint> m_conduit_points;
 
  public PointsConduit(List<ConduitPoint> conduitPoints )
  {
    m_conduit_points = conduitPoints;
  }

  protected override void DrawForeground(Rhino.Display.DrawEventArgs e)
  {
    if (m_conduit_points != null)
      foreach (var cp in m_conduit_points) 
      e.Display.DrawPoint(cp.Point, PointStyle.Simple, 3, cp.Color);
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Public Class PickPointsOnConduitCommand
  Inherits Rhino.Commands.Command
  Private conduitPoints As New List(Of ConduitPoint)()

  Public Overrides ReadOnly Property EnglishName() As String
    Get
      Return "vbPickPoints"
    End Get
  End Property

  Protected Overrides Function RunCommand(doc As RhinoDoc, mode As Rhino.Commands.RunMode) As Rhino.Commands.Result
    Dim conduit = New PointsConduit(conduitPoints)
    conduit.Enabled = True

    Dim gp = New Rhino.Input.Custom.GetPoint()
    While True
      gp.SetCommandPrompt("click location to create point. (<ESC> exit)")
      gp.AcceptNothing(True)
      gp.[Get]()
      If gp.CommandResult() <> Rhino.Commands.Result.Success Then
        Exit While
      End If
      conduitPoints.Add(New ConduitPoint(gp.Point()))
      doc.Views.Redraw()
    End While

    Dim gcp = New GetConduitPoint(conduitPoints)
    While True
      gcp.SetCommandPrompt("select conduit point. (<ESC> to exit)")
      gcp.AcceptNothing(True)
      gcp.[Get](True)
      doc.Views.Redraw()
      If gcp.CommandResult() <> Rhino.Commands.Result.Success Then
        Exit While
      End If
    End While

    Return Rhino.Commands.Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
import System.Drawing
import Rhino.Input.Custom
from scriptcontext import doc

def RunCommand():
  conduitPoints = []
  conduit = PointsConduit(conduitPoints)
  conduit.Enabled = True

  gp = Rhino.Input.Custom.GetPoint()
  result = Rhino.Commands.Result.Success

  while True:
    gp.SetCommandPrompt("click location to create point. (<ESC> exit)")
    gp.AcceptNothing(True)
    gp.Get()
    result = gp.CommandResult()
    if result != Rhino.Commands.Result.Success:
      break
    conduitPoints.append(ConduitPoint(gp.Point()))
    doc.Views.Redraw()
    
  gcp = GetConduitPoint(conduitPoints)
  result = Rhino.Commands.Result.Success
  
  while True:
    gcp.SetCommandPrompt("select conduit point. (<ESC> to exit)")
    gcp.AcceptNothing(True)
    gcp.Get(True)
    doc.Views.Redraw()
    if gcp.CommandResult() != Rhino.Commands.Result.Success:
      break
    
  return Rhino.Commands.Result.Success

class ConduitPoint():
  def __init__(self, point):
    self.Color = System.Drawing.Color.White
    self.Point = point

class GetConduitPoint(Rhino.Input.Custom.GetPoint):
  def __init__(self, conduitPoints):
    self.conduitPoints = conduitPoints

  def OnMouseDown(self, getPointMouseEventArgs):
    picker = PickContext()
    picker.View = getPointMouseEventArgs.Viewport.ParentView

    picker.PickStyle = PickStyle.PointPick

    xform = getPointMouseEventArgs.Viewport.GetPickTransform(getPointMouseEventArgs.WindowPoint)
    picker.SetPickTransform(xform)

    for cp in conduitPoints:
      b, depth, distance = picker.PickFrustumTest(cp.Point)
      if b:
        cp.Color = System.Drawing.Color.Red
      else:
        cp.Color = System.Drawing.Color.White

class PointsConduit(Rhino.Display.DisplayConduit):
  def __init__(self, conduitPoints ):
    self.conduitPoints = conduitPoints

  def DrawForeground(self, drawEventArgs):
    for cp in conduitPoints:
      drawEventArgs.Display.DrawPoint(cp.Point, PointStyle.Simple, 3, cp.Color)

if __name__ == "__main__":
  RunCommand()
```
{: #py .tab-pane .fade .in}


