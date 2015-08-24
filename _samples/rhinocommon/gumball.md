---
layout: code-sample
author:
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
title: Add Gumball
keywords: ['add', 'gumball']
categories: ['Adding Objects']
description:
order: 1
---

```cs
partial class Examples
{
  public static Rhino.Commands.Result Gumball(RhinoDoc doc)
  {
    // Select objects to scale
    var list = new Rhino.Collections.TransformObjectList();
    var rc = SelectObjects("Select objects to gumball", list);
    if (rc != Rhino.Commands.Result.Success)
      return rc;

    var bbox = list.GetBoundingBox(true, true);
    if (!bbox.IsValid)
      return Rhino.Commands.Result.Failure;

    Rhino.Commands.Result cmdrc;

    var base_gumball = new Rhino.UI.Gumball.GumballObject();
    base_gumball.SetFromBoundingBox(bbox);
    var dc = new Rhino.UI.Gumball.GumballDisplayConduit();
    var appearance = new Rhino.UI.Gumball.GumballAppearanceSettings();

    // turn off some of the scale appearance settings to have a slightly different gumball
    appearance.ScaleXEnabled = false;
    appearance.ScaleYEnabled = false;
    appearance.ScaleZEnabled = false;

    bool bCopy = false;
    while (true)
    {
      dc.SetBaseGumball(base_gumball, appearance);
      dc.Enabled = true;
      doc.Views.Redraw();

      GetGumballXform gp = new GetGumballXform(dc);
      int copy_optindx = gp.AddOption("Copy");
      if (dc.PreTransform == Transform.Identity)
        gp.SetCommandPrompt("Drag gumball");
      else
      {
        gp.AcceptNothing(true);
        gp.SetCommandPrompt("Drag gumball. Press Enter when done");
      }
      gp.AddTransformObjects(list);
      gp.MoveGumball();
      dc.Enabled = false;
      cmdrc = gp.CommandResult();
      if (cmdrc != Rhino.Commands.Result.Success)
        break;

      var getpoint_result = gp.Result();
      if (getpoint_result == Rhino.Input.GetResult.Point)
      {
        if (!dc.InRelocate)
        {
          Transform xform = dc.TotalTransform;
          dc.PreTransform = xform;
        }
        // update location of base gumball
        var gbframe = dc.Gumball.Frame;
        var baseFrame = base_gumball.Frame;
        baseFrame.Plane = gbframe.Plane;
        baseFrame.ScaleGripDistance = gbframe.ScaleGripDistance;
        base_gumball.Frame = baseFrame;
        continue;
      }
      if (getpoint_result == Rhino.Input.GetResult.Option)
      {
        if (gp.OptionIndex() == copy_optindx)
          bCopy = true;
        continue;
      }

      break;
    }

    dc.Enabled = false;
    if (dc.PreTransform != Transform.Identity)
    {
      Transform xform = dc.PreTransform;
      TransformObjects(list, xform, bCopy, bCopy);
    }
    doc.Views.Redraw();
    return cmdrc;
  }
}


class GetGumballXform : Rhino.Input.Custom.GetTransform
{
  readonly Rhino.UI.Gumball.GumballDisplayConduit m_dc;
  public GetGumballXform(Rhino.UI.Gumball.GumballDisplayConduit dc)
  {
    m_dc = dc;
  }

  public override Transform CalculateTransform(Rhino.Display.RhinoViewport viewport, Point3d point)
  {
    if (m_dc.InRelocate)
    {
      // don't move objects while relocating gumball
      return m_dc.PreTransform;
    }

    return m_dc.TotalTransform;
  }

  protected override void OnMouseDown(Rhino.Input.Custom.GetPointMouseEventArgs e)
  {
    if (m_dc.PickResult.Mode != Rhino.UI.Gumball.GumballMode.None)
      return;
    m_dc.PickResult.SetToDefault();

    Rhino.Input.Custom.PickContext pick_context = new Rhino.Input.Custom.PickContext();
    pick_context.View = e.Viewport.ParentView;
    pick_context.PickStyle = Rhino.Input.Custom.PickStyle.PointPick;
    var xform = e.Viewport.GetPickTransform(e.WindowPoint);
    pick_context.SetPickTransform(xform);
    Rhino.Geometry.Line pick_line;
    e.Viewport.GetFrustumLine(e.WindowPoint.X, e.WindowPoint.Y, out pick_line);
    pick_context.PickLine = pick_line;
    pick_context.UpdateClippingPlanes();
    // pick gumball and, if hit, set getpoint dragging constraints.
    m_dc.PickGumball(pick_context, this);
  }

  protected override void OnMouseMove(Rhino.Input.Custom.GetPointMouseEventArgs e)
  {
    if( m_dc.PickResult.Mode == Rhino.UI.Gumball.GumballMode.None )
      return;

    m_dc.CheckShiftAndControlKeys();
    Rhino.Geometry.Line world_line;
    if (!e.Viewport.GetFrustumLine(e.WindowPoint.X, e.WindowPoint.Y, out world_line))
      world_line = Rhino.Geometry.Line.Unset;

    bool rc = m_dc.UpdateGumball(e.Point, world_line);
    if( rc )
      base.OnMouseMove(e);
  }
  
  protected override void OnDynamicDraw(Rhino.Input.Custom.GetPointDrawEventArgs e)
  {
    // Disable default GetTransform drawing by not calling the base class
    // implementation. All aspects of gumball display are handled by 
    // GumballDisplayConduit
    //base.OnDynamicDraw(e);
  }
  
  // lets user drag m_gumball around.
  public Rhino.Input.GetResult MoveGumball()
  {
    // Get point on a MouseUp event
    if( m_dc.PreTransform != Transform.Identity )
    {
      HaveTransform = true;
      Transform = m_dc.PreTransform;
    }
    SetBasePoint(m_dc.BaseGumball.Frame.Plane.Origin, false);

    // V5 uses a display conduit to provide display feedback
    // so shaded objects move
    ObjectList.DisplayFeedbackEnabled = true;
    if( Transform != Transform.Identity )
      ObjectList.UpdateDisplayFeedbackTransform(Transform);

    // Call Get with mouseUp set to true
    var rc = this.Get(true);

    // V5 uses a display conduit to provide display feedback
    // so shaded objects move
    ObjectList.DisplayFeedbackEnabled = false;
    return rc;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function Gumball(ByVal doc As RhinoDoc) As Rhino.Commands.Result
	' Select objects to scale
	Dim list = New Rhino.Collections.TransformObjectList()
	Dim rc = SelectObjects("Select objects to gumball", list)
	If rc IsNot Rhino.Commands.Result.Success Then
	  Return rc
	End If

	Dim bbox = list.GetBoundingBox(True, True)
	If Not bbox.IsValid Then
	  Return Rhino.Commands.Result.Failure
	End If

	Dim cmdrc As Rhino.Commands.Result

	Dim base_gumball = New Rhino.UI.Gumball.GumballObject()
	base_gumball.SetFromBoundingBox(bbox)
	Dim dc = New Rhino.UI.Gumball.GumballDisplayConduit()
	Dim appearance = New Rhino.UI.Gumball.GumballAppearanceSettings()

	' turn off some of the scale appearance settings to have a slightly different gumball
	appearance.ScaleXEnabled = False
	appearance.ScaleYEnabled = False
	appearance.ScaleZEnabled = False

	Dim bCopy As Boolean = False
	Do
	  dc.SetBaseGumball(base_gumball, appearance)
	  dc.Enabled = True
	  doc.Views.Redraw()

	  Dim gp As New GetGumballXform(dc)
	  Dim copy_optindx As Integer = gp.AddOption("Copy")
	  If dc.PreTransform = Transform.Identity Then
		gp.SetCommandPrompt("Drag gumball")
	  Else
		gp.AcceptNothing(True)
		gp.SetCommandPrompt("Drag gumball. Press Enter when done")
	  End If
	  gp.AddTransformObjects(list)
	  gp.MoveGumball()
	  dc.Enabled = False
	  cmdrc = gp.CommandResult()
	  If cmdrc IsNot Rhino.Commands.Result.Success Then
		Exit Do
	  End If

	  Dim getpoint_result = gp.Result()
	  If getpoint_result Is Rhino.Input.GetResult.Point Then
		If Not dc.InRelocate Then
		  Dim xform As Transform = dc.TotalTransform
		  dc.PreTransform = xform
		End If
		' update location of base gumball
		Dim gbframe = dc.Gumball.Frame
		Dim baseFrame = base_gumball.Frame
		baseFrame.Plane = gbframe.Plane
		baseFrame.ScaleGripDistance = gbframe.ScaleGripDistance
		base_gumball.Frame = baseFrame
		Continue Do
	  End If
	  If getpoint_result Is Rhino.Input.GetResult.Option Then
		If gp.OptionIndex() = copy_optindx Then
		  bCopy = True
		End If
		Continue Do
	  End If

	  Exit Do
	Loop

	dc.Enabled = False
	If dc.PreTransform <> Transform.Identity Then
	  Dim xform As Transform = dc.PreTransform
	  TransformObjects(list, xform, bCopy, bCopy)
	End If
	doc.Views.Redraw()
	Return cmdrc
  End Function
End Class


Friend Class GetGumballXform
	Inherits Rhino.Input.Custom.GetTransform

  Private ReadOnly m_dc As Rhino.UI.Gumball.GumballDisplayConduit
  Public Sub New(ByVal dc As Rhino.UI.Gumball.GumballDisplayConduit)
	m_dc = dc
  End Sub

  Public Overrides Function CalculateTransform(ByVal viewport As Rhino.Display.RhinoViewport, ByVal point As Point3d) As Transform
	If m_dc.InRelocate Then
	  ' don't move objects while relocating gumball
	  Return m_dc.PreTransform
	End If

	Return m_dc.TotalTransform
  End Function

  Protected Overrides Sub OnMouseDown(ByVal e As Rhino.Input.Custom.GetPointMouseEventArgs)
	If m_dc.PickResult.Mode <> Rhino.UI.Gumball.GumballMode.None Then
	  Return
	End If
	m_dc.PickResult.SetToDefault()

	Dim pick_context As New Rhino.Input.Custom.PickContext()
	pick_context.View = e.Viewport.ParentView
	pick_context.PickStyle = Rhino.Input.Custom.PickStyle.PointPick
	Dim xform = e.Viewport.GetPickTransform(e.WindowPoint)
	pick_context.SetPickTransform(xform)
	Dim pick_line As Rhino.Geometry.Line = Nothing
	e.Viewport.GetFrustumLine(e.WindowPoint.X, e.WindowPoint.Y, pick_line)
	pick_context.PickLine = pick_line
	pick_context.UpdateClippingPlanes()
	' pick gumball and, if hit, set getpoint dragging constraints.
	m_dc.PickGumball(pick_context, Me)
  End Sub

  Protected Overrides Sub OnMouseMove(ByVal e As Rhino.Input.Custom.GetPointMouseEventArgs)
	If m_dc.PickResult.Mode = Rhino.UI.Gumball.GumballMode.None Then
	  Return
	End If

	m_dc.CheckShiftAndControlKeys()
	Dim world_line As Rhino.Geometry.Line = Nothing
	If Not e.Viewport.GetFrustumLine(e.WindowPoint.X, e.WindowPoint.Y, world_line) Then
	  world_line = Rhino.Geometry.Line.Unset
	End If

	Dim rc As Boolean = m_dc.UpdateGumball(e.Point, world_line)
	If rc Then
	  MyBase.OnMouseMove(e)
	End If
  End Sub

  Protected Overrides Sub OnDynamicDraw(ByVal e As Rhino.Input.Custom.GetPointDrawEventArgs)
	' Disable default GetTransform drawing by not calling the base class
	' implementation. All aspects of gumball display are handled by 
	' GumballDisplayConduit
	'base.OnDynamicDraw(e);
  End Sub

  ' lets user drag m_gumball around.
  Public Function MoveGumball() As Rhino.Input.GetResult
	' Get point on a MouseUp event
	If m_dc.PreTransform <> Transform.Identity Then
	  HaveTransform = True
	  Transform = m_dc.PreTransform
	End If
	SetBasePoint(m_dc.BaseGumball.Frame.Plane.Origin, False)

	' V5 uses a display conduit to provide display feedback
	' so shaded objects move
	ObjectList.DisplayFeedbackEnabled = True
	If Transform <> Transform.Identity Then
	  ObjectList.UpdateDisplayFeedbackTransform(Transform)
	End If

	' Call Get with mouseUp set to true
	Dim rc = Me.Get(True)

	' V5 uses a display conduit to provide display feedback
	' so shaded objects move
	ObjectList.DisplayFeedbackEnabled = False
	Return rc
  End Function
End Class
```
{: #vb .tab-pane .fade .in .active}


```python
```
{: #py .tab-pane .fade .in .active}

