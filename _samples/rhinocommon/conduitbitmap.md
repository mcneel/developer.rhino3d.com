---
layout: code-sample
author:
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
title: draw a non-square bitmap in a display conduit
keywords: ['draw', 'non-square', 'bitmap', 'display', 'conduit']
categories: ['Draw']
description:
order: 1
---

```cs
partial class Examples
{
  static readonly DrawBitmapConduit m_conduit = new DrawBitmapConduit();

  public static Result ConduitBitmap(RhinoDoc doc)
  {
    // toggle conduit on/off
    m_conduit.Enabled = !m_conduit.Enabled;
    
    RhinoApp.WriteLine("Custom conduit enabled = {0}", m_conduit.Enabled);
    doc.Views.Redraw();
    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Private Shared ReadOnly m_conduit As New DrawBitmapConduit()

  Public Shared Function ConduitBitmap(ByVal doc As RhinoDoc) As Result
	' toggle conduit on/off
	m_conduit.Enabled = Not m_conduit.Enabled

	RhinoApp.WriteLine("Custom conduit enabled = {0}", m_conduit.Enabled)
	doc.Views.Redraw()
	Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
import Rhino
from Rhino.Geometry import *
import System.Drawing
import Rhino.Display
import scriptcontext
import rhinoscriptsyntax as rs

class CustomConduit(Rhino.Display.DisplayConduit):
    def __init__(self):
      flag = System.Drawing.Bitmap(100,100)
      for x in range(0,100):
        for y in range(0,100):
          flag.SetPixel(x, y, System.Drawing.Color.Red)
      g = System.Drawing.Graphics.FromImage(flag)
      g.FillEllipse(System.Drawing.Brushes.Blue, 25, 25, 50, 50)
      self.display_bitmap = Rhino.Display.DisplayBitmap(flag)

    def DrawForeground(self, e):
      e.Display.DrawBitmap(self.display_bitmap, 50, 50, System.Drawing.Color.Red)

if __name__== "__main__":
    conduit = CustomConduit()
    conduit.Enabled = True
    scriptcontext.doc.Views.Redraw()
    rs.GetString("Pausing for user input")
    conduit.Enabled = False
    scriptcontext.doc.Views.Redraw()
```
{: #py .tab-pane .fade .in}

