---
title: Display Conduit Arrowheads
description: Drawing Arrowheads in a Display Conduit
author:
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
platforms: ['Cross-Platform']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/rhinocommonsamples/conduitarrowheads
order: 1
keywords: ['drawing', 'arrowheads', 'display', 'conduit']
layout: code-sample-rhinocommon
---

```cs
class DrawArrowHeadsConduit : Rhino.Display.DisplayConduit
{
  private readonly Line m_line;
  private readonly int m_screen_size;
  private readonly double m_world_size;

  public DrawArrowHeadsConduit(Line line, int screenSize, double worldSize)
  {
    m_line = line;
    m_screen_size = screenSize;
    m_world_size = worldSize;
  }

  protected override void DrawForeground(Rhino.Display.DrawEventArgs e)
  {
    e.Display.DrawArrow(m_line, System.Drawing.Color.Black, m_screen_size, m_world_size);
  }
}

partial class Examples
{
  static DrawArrowHeadsConduit m_draw_conduit;

  public static Result ConduitArrowHeads(RhinoDoc doc)
  {
    if (m_draw_conduit != null)
    {
      RhinoApp.WriteLine("Turn off existing arrowhead conduit");
      m_draw_conduit.Enabled = false;
      m_draw_conduit = null;
    }
    else
    {
      // get arrow head size
      var go = new GetOption();
      go.SetCommandPrompt("ArrowHead length in screen size (pixels) or world size (percentage of arrow length)?");
      go.AddOption("screen");
      go.AddOption("world");
      go.Get();
      if (go.CommandResult() != Result.Success)
        return go.CommandResult();

      int screen_size = 0;
      double world_size = 0.0;
      if (go.Option().EnglishName == "screen")
      {
        var gi = new GetInteger();
        gi.SetLowerLimit(0, true);
        gi.SetCommandPrompt("Length of arrow head in pixels");
        gi.Get();
        if (gi.CommandResult() != Result.Success)
          return gi.CommandResult();
        screen_size = gi.Number();
      }
      else
      {
        var gi = new GetInteger();
        gi.SetLowerLimit(0, true);
        gi.SetUpperLimit(100, false);
        gi.SetCommandPrompt("Length of arrow head in percentage of total arrow length");
        gi.Get();
        if (gi.CommandResult() != Result.Success)
          return gi.CommandResult();
        world_size = gi.Number() / 100.0;
      }


      // get arrow start and end points
      var gp = new GetPoint();
      gp.SetCommandPrompt("Start of line");
      gp.Get();
      if (gp.CommandResult() != Result.Success)
        return gp.CommandResult();
      var start_point = gp.Point();

      gp.SetCommandPrompt("End of line");
      gp.SetBasePoint(start_point, false);
      gp.DrawLineFromPoint(start_point, true);
      gp.Get();
      if (gp.CommandResult() != Result.Success)
        return gp.CommandResult();
      var end_point = gp.Point();

      var v = end_point - start_point;
      if (v.IsTiny(Rhino.RhinoMath.ZeroTolerance))
        return Result.Nothing;

      var line = new Line(start_point, end_point);

      m_draw_conduit = new DrawArrowHeadsConduit(line, screen_size, world_size);
      // toggle conduit on/off
      m_draw_conduit.Enabled = true;
      RhinoApp.WriteLine("Draw arrowheads conduit enabled.");
    }
    doc.Views.Redraw();
    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Private Shared m_draw_conduit As DrawArrowHeadsConduit

  Public Shared Function ConduitArrowHeads(ByVal doc As RhinoDoc) As Result
	If m_draw_conduit IsNot Nothing Then
	  RhinoApp.WriteLine("Turn off existing arrowhead conduit")
	  m_draw_conduit.Enabled = False
	  m_draw_conduit = Nothing
	Else
	  ' get arrow head size
	  Dim go = New GetOption()
	  go.SetCommandPrompt("ArrowHead length in screen size (pixels) or world size (percentage of arrow length)?")
	  go.AddOption("screen")
	  go.AddOption("world")
	  go.Get()
	  If go.CommandResult() <> Result.Success Then
		Return go.CommandResult()
	  End If

	  Dim screen_size As Integer = 0
	  Dim world_size As Double = 0.0
	  If go.Option().EnglishName = "screen" Then
		Dim gi = New GetInteger()
		gi.SetLowerLimit(0, True)
		gi.SetCommandPrompt("Length of arrow head in pixels")
		gi.Get()
		If gi.CommandResult() <> Result.Success Then
		  Return gi.CommandResult()
		End If
		screen_size = gi.Number()
	  Else
		Dim gi = New GetInteger()
		gi.SetLowerLimit(0, True)
		gi.SetUpperLimit(100, False)
		gi.SetCommandPrompt("Length of arrow head in percentage of total arrow length")
		gi.Get()
		If gi.CommandResult() <> Result.Success Then
		  Return gi.CommandResult()
		End If
'INSTANT VB WARNING: Instant VB cannot determine whether both operands of this division are integer types - if they are then you should use the VB integer division operator:
		world_size = gi.Number() / 100.0
	  End If


	  ' get arrow start and end points
	  Dim gp = New GetPoint()
	  gp.SetCommandPrompt("Start of line")
	  gp.Get()
	  If gp.CommandResult() <> Result.Success Then
		Return gp.CommandResult()
	  End If
	  Dim start_point = gp.Point()

	  gp.SetCommandPrompt("End of line")
	  gp.SetBasePoint(start_point, False)
	  gp.DrawLineFromPoint(start_point, True)
	  gp.Get()
	  If gp.CommandResult() <> Result.Success Then
		Return gp.CommandResult()
	  End If
	  Dim end_point = gp.Point()

	  Dim v = end_point - start_point
	  If v.IsTiny(Rhino.RhinoMath.ZeroTolerance) Then
		Return Result.Nothing
	  End If

	  Dim line = New Line(start_point, end_point)

	  m_draw_conduit = New DrawArrowHeadsConduit(line, screen_size, world_size)
	  ' toggle conduit on/off
	  m_draw_conduit.Enabled = True
	  RhinoApp.WriteLine("Draw arrowheads conduit enabled.")
	End If
	doc.Views.Redraw()
	Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
import Rhino
import System.Drawing
import scriptcontext
import rhinoscriptsyntax as rs

class DrawArrowHeadsConduit(Rhino.Display.DisplayConduit):
  def __init__(self, line, screenSize, worldSize):
    self.line = line
    self.screenSize = screenSize
    self.worldSize = worldSize

  def DrawForeground(self, e):
    e.Display.DrawArrow(self.line, System.Drawing.Color.Black, self.screenSize, self.worldSize)

def RunCommand():
  # get arrow head size
  go = Rhino.Input.Custom.GetOption()
  go.SetCommandPrompt("ArrowHead length in screen size (pixles) or world size (percentage of arrow lenght)?")
  go.AddOption("screen")
  go.AddOption("world")
  go.Get()
  if (go.CommandResult() != Rhino.Commands.Result.Success):
    return go.CommandResult()

  screenSize = 0
  worldSize = 0.0
  if (go.Option().EnglishName == "screen"):
    gi = Rhino.Input.Custom.GetInteger()
    gi.SetLowerLimit(0,True)
    gi.SetCommandPrompt("Length of arrow head in pixels")
    gi.Get()
    if (gi.CommandResult() != Rhino.Commands.Result.Success):
      return gi.CommandResult()
    screenSize = gi.Number()
  else:
    gi = Rhino.Input.Custom.GetInteger()
    gi.SetLowerLimit(0, True)
    gi.SetUpperLimit(100, False)
    gi.SetCommandPrompt("Lenght of arrow head in percentage of total arrow lenght")
    gi.Get()
    if (gi.CommandResult() != Rhino.Commands.Result.Success):
      return gi.CommandResult()
    worldSize = gi.Number()/100.0


  # get arrow start and end points
  gp = Rhino.Input.Custom.GetPoint()
  gp.SetCommandPrompt("Start of line")
  gp.Get()
  if (gp.CommandResult() != Rhino.Commands.Result.Success):
    return gp.CommandResult()
  ptStart = gp.Point()

  gp.SetCommandPrompt("End of line")
  gp.SetBasePoint(ptStart, False)
  gp.DrawLineFromPoint(ptStart, True)
  gp.Get()
  if (gp.CommandResult() != Rhino.Commands.Result.Success):
    return gp.CommandResult()
  ptEnd = gp.Point()


  v = ptEnd - ptStart
  if (v.IsTiny(Rhino.RhinoMath.ZeroTolerance)):
    return Rhino.Commands.Result.Nothing

  line = Rhino.Geometry.Line(ptStart, ptEnd)

  conduit = DrawArrowHeadsConduit(line, screenSize, worldSize)
  conduit.Enabled = True
  scriptcontext.doc.Views.Redraw()
  rs.GetString("Pausing for user input")
  conduit.Enabled = False
  scriptcontext.doc.Views.Redraw()

  return Rhino.Commands.Result.Success

if __name__=="__main__":
  RunCommand()
```
{: #py .tab-pane .fade .in}
