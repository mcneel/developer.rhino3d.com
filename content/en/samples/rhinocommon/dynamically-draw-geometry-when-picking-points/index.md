+++
aliases = ["/en/5/samples/rhinocommon/dynamically-draw-geometry-when-picking-points/", "/en/6/samples/rhinocommon/dynamically-draw-geometry-when-picking-points/", "/en/7/samples/rhinocommon/dynamically-draw-geometry-when-picking-points/", "/wip/samples/rhinocommon/dynamically-draw-geometry-when-picking-points/"]
authors = [ "steve" ]
categories = [ "Draw", "Picking and Selection" ]
description = "Demonstrates how to dynamically draw geometry during point picking."
keywords = [ "dynamically", "draw", "geometry", "when", "picking", "points" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Dynamically Draw Geometry when Picking Points"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/getpointdynamicdraw"
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
  public static Result GetPointDynamicDraw(RhinoDoc doc)
  {
    var gp = new GetPoint();
    gp.SetCommandPrompt("Center point");
    gp.Get();
    if (gp.CommandResult() != Result.Success)
      return gp.CommandResult();
    var center_point = gp.Point();
    if (center_point == Point3d.Unset)
      return Result.Failure;

    var gcp = new GetCircleRadiusPoint(center_point);
    gcp.SetCommandPrompt("Radius");
    gcp.ConstrainToConstructionPlane(false);
    gcp.SetBasePoint(center_point, true);
    gcp.DrawLineFromPoint(center_point, true);
    gcp.Get();
    if (gcp.CommandResult() != Result.Success)
      return gcp.CommandResult();

    var radius = center_point.DistanceTo(gcp.Point());
    var cplane = doc.Views.ActiveView.ActiveViewport.ConstructionPlane();
    doc.Objects.AddCircle(new Circle(cplane, center_point, radius));
    doc.Views.Redraw();
    return Result.Success;
  }
}

public class GetCircleRadiusPoint : GetPoint
{
  private Point3d m_center_point;

  public GetCircleRadiusPoint(Point3d centerPoint)
  {
    m_center_point = centerPoint;
  }

  protected override void OnDynamicDraw(GetPointDrawEventArgs e)
  {
    base.OnDynamicDraw(e);
    var cplane = e.RhinoDoc.Views.ActiveView.ActiveViewport.ConstructionPlane();
    var radius = m_center_point.DistanceTo(e.CurrentPoint);
    var circle = new Circle(cplane, m_center_point, radius);
    e.Display.DrawCircle(circle, System.Drawing.Color.Black);
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function GetPointDynamicDraw(ByVal doc As RhinoDoc) As Result
	Dim gp = New GetPoint()
	gp.SetCommandPrompt("Center point")
	gp.Get()
	If gp.CommandResult() <> Result.Success Then
	  Return gp.CommandResult()
	End If
	Dim center_point = gp.Point()
	If center_point Is Point3d.Unset Then
	  Return Result.Failure
	End If

	Dim gcp = New GetCircleRadiusPoint(center_point)
	gcp.SetCommandPrompt("Radius")
	gcp.ConstrainToConstructionPlane(False)
	gcp.SetBasePoint(center_point, True)
	gcp.DrawLineFromPoint(center_point, True)
	gcp.Get()
	If gcp.CommandResult() <> Result.Success Then
	  Return gcp.CommandResult()
	End If

	Dim radius = center_point.DistanceTo(gcp.Point())
	Dim cplane = doc.Views.ActiveView.ActiveViewport.ConstructionPlane()
	doc.Objects.AddCircle(New Circle(cplane, center_point, radius))
	doc.Views.Redraw()
	Return Result.Success
  End Function
End Class

Public Class GetCircleRadiusPoint
	Inherits GetPoint

  Private m_center_point As Point3d

  Public Sub New(ByVal centerPoint As Point3d)
	m_center_point = centerPoint
  End Sub

  Protected Overrides Sub OnDynamicDraw(ByVal e As GetPointDrawEventArgs)
	MyBase.OnDynamicDraw(e)
	Dim cplane = e.RhinoDoc.Views.ActiveView.ActiveViewport.ConstructionPlane()
	Dim radius = m_center_point.DistanceTo(e.CurrentPoint)
	Dim circle = New Circle(cplane, m_center_point, radius)
	e.Display.DrawCircle(circle, System.Drawing.Color.Black)
  End Sub
End Class
```

</div>


<div class="codetab-content" id="py">

```python
from Rhino import *
from Rhino.Geometry import *
from Rhino.Commands import *
from Rhino.Input.Custom import *
from scriptcontext import doc
from System.Drawing import *

def RunCommand():
    gp = GetPoint()
    gp.SetCommandPrompt("Center point")
    gp.Get()
    if gp.CommandResult() != Result.Success:
        return gp.CommandResult()
    center_point = gp.Point()
    if center_point == Point3d.Unset:
        return Result.Failure

    gcp = GetCircleRadiusPoint(center_point)
    gcp.SetCommandPrompt("Radius")
    gcp.ConstrainToConstructionPlane(False)
    gcp.SetBasePoint(center_point, True)
    gcp.DrawLineFromPoint(center_point, True)
    gcp.Get()
    if gcp.CommandResult() != Result.Success:
        return gcp.CommandResult()

    radius = center_point.DistanceTo(gcp.Point())
    cplane = doc.Views.ActiveView.ActiveViewport.ConstructionPlane()
    doc.Objects.AddCircle(Circle(cplane, center_point, radius))
    doc.Views.Redraw()
    return Result.Success

class GetCircleRadiusPoint (GetPoint):
    def __init__(self, centerPoint):
        self.m_center_point = centerPoint

    def OnDynamicDraw(self, e):
        cplane = e.RhinoDoc.Views.ActiveView.ActiveViewport.ConstructionPlane()
        radius = self.m_center_point.DistanceTo(e.CurrentPoint)
        circle = Circle(cplane, self.m_center_point, radius)
        e.Display.DrawCircle(circle, Color.Black)

if __name__ == "__main__":
    RunCommand()
```

</div>
