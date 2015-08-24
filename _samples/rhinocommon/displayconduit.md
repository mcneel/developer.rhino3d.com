---
layout: code-sample
author:
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
title: Display Conduit Introduction for RhinoCommon
keywords: ['display', 'conduit', 'introduction', 'rhinocommon']
categories: ['Other']
description:
order: 1
---

```cs
partial class Examples
{
  static MyConduit m_conduit;
  public static Result DisplayConduit(RhinoDoc doc)
  {
    // The following code lets you toggle the conduit on and off by repeatedly running the command
    if (m_conduit != null)
    {
      m_conduit.Enabled = false;
      m_conduit = null;
    }
    else
    {
      m_conduit = new MyConduit { Enabled = true };
    }
    doc.Views.Redraw();
    return Result.Success;
  }
}

class MyConduit : Rhino.Display.DisplayConduit
{
  protected override void CalculateBoundingBox(CalculateBoundingBoxEventArgs e)
  {
    base.CalculateBoundingBox(e);
    e.BoundingBox.Union(e.Display.Viewport.ConstructionPlane().Origin);
  }

  protected override void PreDrawObjects(DrawEventArgs e)
  {
    base.PreDrawObjects(e);

    var c_plane = e.Display.Viewport.ConstructionPlane();
    var x_color = Rhino.ApplicationSettings.AppearanceSettings.GridXAxisLineColor;
    var y_color = Rhino.ApplicationSettings.AppearanceSettings.GridYAxisLineColor;
    var z_color = Rhino.ApplicationSettings.AppearanceSettings.GridZAxisLineColor;

    e.Display.PushDepthWriting(false);
    e.Display.PushDepthTesting(false);

    e.Display.DrawPoint(c_plane.Origin, System.Drawing.Color.White);
    e.Display.DrawArrow(new Line(c_plane.Origin, new Vector3d(c_plane.XAxis) * 10.0), x_color);
    e.Display.DrawArrow(new Line(c_plane.Origin, new Vector3d(c_plane.YAxis) * 10.0), y_color);
    e.Display.DrawArrow(new Line(c_plane.Origin, new Vector3d(c_plane.ZAxis) * 10.0), z_color);

    e.Display.PopDepthWriting();
    e.Display.PopDepthTesting();
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Private Shared m_conduit As MyConduit
  Public Shared Function DisplayConduit(ByVal doc As RhinoDoc) As Result
	' The following code lets you toggle the conduit on and off by repeatedly running the command
	If m_conduit IsNot Nothing Then
	  m_conduit.Enabled = False
	  m_conduit = Nothing
	Else
	  m_conduit = New MyConduit With {.Enabled = True}
	End If
	doc.Views.Redraw()
	Return Result.Success
  End Function
End Class

Friend Class MyConduit
	Inherits Rhino.Display.DisplayConduit

  Protected Overrides Sub CalculateBoundingBox(ByVal e As CalculateBoundingBoxEventArgs)
	MyBase.CalculateBoundingBox(e)
	e.BoundingBox.Union(e.Display.Viewport.ConstructionPlane().Origin)
  End Sub

  Protected Overrides Sub PreDrawObjects(ByVal e As DrawEventArgs)
	MyBase.PreDrawObjects(e)

	Dim c_plane = e.Display.Viewport.ConstructionPlane()
	Dim x_color = Rhino.ApplicationSettings.AppearanceSettings.GridXAxisLineColor
	Dim y_color = Rhino.ApplicationSettings.AppearanceSettings.GridYAxisLineColor
	Dim z_color = Rhino.ApplicationSettings.AppearanceSettings.GridZAxisLineColor

	e.Display.PushDepthWriting(False)
	e.Display.PushDepthTesting(False)

	e.Display.DrawPoint(c_plane.Origin, System.Drawing.Color.White)
	e.Display.DrawArrow(New Line(c_plane.Origin, New Vector3d(c_plane.XAxis) * 10.0), x_color)
	e.Display.DrawArrow(New Line(c_plane.Origin, New Vector3d(c_plane.YAxis) * 10.0), y_color)
	e.Display.DrawArrow(New Line(c_plane.Origin, New Vector3d(c_plane.ZAxis) * 10.0), z_color)

	e.Display.PopDepthWriting()
	e.Display.PopDepthTesting()
  End Sub
End Class
```
{: #vb .tab-pane .fade .in .active}


```python
```
{: #py .tab-pane .fade .in .active}

