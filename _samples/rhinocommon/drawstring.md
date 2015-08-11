---
layout: code-sample
title: Dynamically Drawing Text Strings
author: 
categories: ['Draw'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['dynamically', 'drawing', 'text', 'strings']
order: 68
description:  
---



```cs
public class DrawStringCommand : Command
{
  public override string EnglishName { get { return "csDrawString"; } }

  protected override Result RunCommand(RhinoDoc doc, RunMode mode)
  {
    var gp = new GetDrawStringPoint();
    gp.SetCommandPrompt("Point");
    gp.Get();
    return gp.CommandResult();
  }
}

public class GetDrawStringPoint : GetPoint
{
  protected override void OnDynamicDraw(GetPointDrawEventArgs e)
  {
    base.OnDynamicDraw(e);
    var xform = e.Viewport.GetTransform(CoordinateSystem.World, CoordinateSystem.Screen);
    var current_point = e.CurrentPoint;
    current_point.Transform(xform);
    var screen_point = new Point2d(current_point.X, current_point.Y);
    var msg = string.Format("screen {0:F}, {1:F}", current_point.X, current_point.Y);
    e.Display.Draw2dText(msg, System.Drawing.Color.Blue, screen_point, false);
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Public Class DrawStringCommand
  Inherits Command
  Public Overrides ReadOnly Property EnglishName() As String
    Get
      Return "vbDrawString"
    End Get
  End Property

  Protected Overrides Function RunCommand(doc As RhinoDoc, mode As RunMode) As Result
    Dim gp = New GetDrawStringPoint()
    gp.SetCommandPrompt("Point")
    gp.[Get]()
    Return gp.CommandResult()
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
from Rhino import *
from Rhino.DocObjects import *
from Rhino.Geometry import *
from Rhino.Commands import *
from Rhino.Input.Custom import *
from System.Drawing import Color

def RunCommand():
  gp = GetDrawStringPoint()
  gp.SetCommandPrompt("Point")
  gp.Get()
  return gp.CommandResult()

class GetDrawStringPoint(GetPoint):
  def OnDynamicDraw(self, e):
    xform = e.Viewport.GetTransform(
      CoordinateSystem.World, CoordinateSystem.Screen)    

    current_point = e.CurrentPoint
    current_point.Transform(xform)
    screen_point = Point2d(current_point.X, current_point.Y)

    msg = "screen {0}, {1}".format(screen_point.X, screen_point.Y)
    e.Display.Draw2dText(msg, Color.Blue, screen_point, False)

if __name__ == "__main__":
  RunCommand()
```
{: #py .tab-pane .fade .in}


