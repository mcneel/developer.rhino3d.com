+++
authors = [ "steve" ]
categories = [ "Draw" ]
description = "Demonstrates how to use a display conduit to draw overlay text."
keywords = [ "display", "conduit", "draw", "overlay", "text" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Overlay Text Display Conduit"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/drawoverlay"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

+++

<div class="codetab-content" id="cs">

```cs
class CustomConduit : Rhino.Display.DisplayConduit
{
  protected override void DrawForeground(Rhino.Display.DrawEventArgs e)
  {
    var bounds = e.Viewport.Bounds;
    var pt = new Rhino.Geometry.Point2d(bounds.Right - 100, bounds.Bottom - 30);
    e.Display.Draw2dText("Hello", System.Drawing.Color.Red, pt, false);
  }
}

partial class Examples
{
  readonly static CustomConduit m_customconduit = new CustomConduit();
  public static Rhino.Commands.Result DrawOverlay(RhinoDoc doc)
  {
    // toggle conduit on/off
    m_customconduit.Enabled = !m_conduit.Enabled;

    RhinoApp.WriteLine("Custom conduit enabled = {0}", m_customconduit.Enabled);
    doc.Views.Redraw();
    return Rhino.Commands.Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Private ReadOnly Shared m_customconduit As New CustomConduit()
  Public Shared Function DrawOverlay(ByVal doc As RhinoDoc) As Rhino.Commands.Result
	' toggle conduit on/off
	m_customconduit.Enabled = Not m_conduit.Enabled

	RhinoApp.WriteLine("Custom conduit enabled = {0}", m_customconduit.Enabled)
	doc.Views.Redraw()
	Return Rhino.Commands.Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
import Rhino
import System.Drawing
import scriptcontext
import rhinoscriptsyntax as rs

# DisplayConduit subclass that overrides the DrawForeground function
# e is an instance of Rhino.Display.DrawEventArgs
class CustomConduit(Rhino.Display.DisplayConduit):
    def DrawForeground(self, e):
        color = System.Drawing.Color.Red
        bounds = e.Viewport.Bounds
        pt = Rhino.Geometry.Point2d(bounds.Right - 100, bounds.Bottom - 30)
        e.Display.Draw2dText("Hello", color, pt, False)


def showafterscript():
    # Create a custom conduit that can continue to draw after the
    # script has completed. The conduit is kept in the sticky
    # dictionary so we can get at it and turn it off in the future
    #
    # check to see if the conduit has been created and is in sticky
    conduit = None
    if scriptcontext.sticky.has_key("myconduit"):
        conduit = scriptcontext.sticky["myconduit"]
    else:
        # create a conduit and place it in sticky
        conduit = CustomConduit()
        scriptcontext.sticky["myconduit"] = conduit

    # Toggle enabled state for conduit. Every time this script is
    # run, it will turn the conduit on and off
    conduit.Enabled = not conduit.Enabled
    if conduit.Enabled: print "conduit enabled"
    else: print "conduit disabled"
    scriptcontext.doc.Views.Redraw()


def showinscript():
    # create a custom conduit that only displays during the execution
    # of this script. Once the script has completed, the conduit is turned
    # off and display goes back to normal
    conduit = CustomConduit()
    conduit.Enabled = True
    scriptcontext.doc.Views.Redraw()
    rs.GetString("Pausing for user input")
    conduit.Enabled = False
    scriptcontext.doc.Views.Redraw()

if __name__=="__main__":
    showinscript()
    #showafterscript()
```

</div>
