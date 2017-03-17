---
title: Pick Points
description: Demonstrates how to pick and select point objects.
authors: ['Steve Baer']
author_contacts: ['stevebaer']
sdk: ['RhinoCommon']
languages: ['C#', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Picking and Selection']
origin: http://wiki.mcneel.com/developer/rhinocommonsamples/pickpoint
order: 1
keywords: ['pick', 'points']
layout: code-sample-rhinocommon
---

```cs
partial class Examples
{
  private static readonly List<ConduitPoint> m_conduit_points = new List<ConduitPoint>();

  public static Rhino.Commands.Result PickPoints(RhinoDoc doc)
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
Partial Friend Class Examples
  Private Shared ReadOnly m_conduit_points As New List(Of ConduitPoint)()

  Public Shared Function PickPoints(ByVal doc As RhinoDoc) As Rhino.Commands.Result
	Dim conduit = New PointsConduit(m_conduit_points)
	conduit.Enabled = True

	Dim gp = New Rhino.Input.Custom.GetPoint()
	Do
	  gp.SetCommandPrompt("click location to create point. (<ESC> exit)")
	  gp.AcceptNothing(True)
	  gp.Get()
	  If gp.CommandResult() <> Rhino.Commands.Result.Success Then
		Exit Do
	  End If
	  m_conduit_points.Add(New ConduitPoint(gp.Point()))
	  doc.Views.Redraw()
	Loop

	Dim gcp = New GetConduitPoint(m_conduit_points)
	Do
	  gcp.SetCommandPrompt("select conduit point. (<ESC> to exit)")
	  gcp.AcceptNothing(True)
	  gcp.Get(True)
	  doc.Views.Redraw()
	  If gcp.CommandResult() <> Rhino.Commands.Result.Success Then
		Exit Do
	  End If
	Loop

	Return Rhino.Commands.Result.Success
  End Function
End Class

Public Class ConduitPoint
  Public Sub New(ByVal point As Point3d)
	Color = System.Drawing.Color.White
	Me.Point = point
  End Sub
  Public Property Color() As System.Drawing.Color
  Public Property Point() As Point3d
End Class

Public Class GetConduitPoint
	Inherits GetPoint

  Private ReadOnly m_conduit_points As List(Of ConduitPoint)

  Public Sub New(ByVal conduitPoints As List(Of ConduitPoint))
	m_conduit_points = conduitPoints
  End Sub

  Protected Overrides Sub OnMouseDown(ByVal e As GetPointMouseEventArgs)
	MyBase.OnMouseDown(e)
	Dim picker = New PickContext()
	picker.View = e.Viewport.ParentView

	picker.PickStyle = PickStyle.PointPick

	Dim xform = e.Viewport.GetPickTransform(e.WindowPoint)
	picker.SetPickTransform(xform)

	For Each cp In m_conduit_points
	  Dim depth As Double = Nothing
	  Dim distance As Double = Nothing
	  If picker.PickFrustumTest(cp.Point, depth, distance) Then
		cp.Color = System.Drawing.Color.Red
	  Else
		cp.Color = System.Drawing.Color.White
	  End If
	Next cp
  End Sub
End Class

Friend Class PointsConduit
	Inherits Rhino.Display.DisplayConduit

  Private ReadOnly m_conduit_points As List(Of ConduitPoint)

  Public Sub New(ByVal conduitPoints As List(Of ConduitPoint))
	m_conduit_points = conduitPoints
  End Sub

  Protected Overrides Sub DrawForeground(ByVal e As Rhino.Display.DrawEventArgs)
	If m_conduit_points IsNot Nothing Then
	  For Each cp In m_conduit_points
	  e.Display.DrawPoint(cp.Point, PointStyle.Simple, 3, cp.Color)
	  Next cp
	End If
  End Sub
End Class
```
{: #vb .tab-pane .fade .in}


```python
# No Python sample available
```
{: #py .tab-pane .fade .in}
