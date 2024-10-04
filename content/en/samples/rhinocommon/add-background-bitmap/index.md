+++
aliases = ["/en/5/samples/rhinocommon/add-background-bitmap/", "/en/6/samples/rhinocommon/add-background-bitmap/", "/en/7/samples/rhinocommon/add-background-bitmap/", "/wip/samples/rhinocommon/add-background-bitmap/"]
authors = [ "steve" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to add a background bitmap to a Rhino model at a user-specified location."
keywords = [ "add", "background", "bitmap" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Add Background Bitmap"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/addbackgroundbitmap"
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
  public static Rhino.Commands.Result AddBackgroundBitmap(Rhino.RhinoDoc doc)
  {
    Rhino.RhinoApp.WriteLine ("hey");
    // Allow the user to select a bitmap file
    Rhino.UI.OpenFileDialog fd = new Rhino.UI.OpenFileDialog();
    fd.Filter = "Image Files (*.bmp;*.png;*.jpg)|*.bmp;*.png;*.jpg";
    if (!fd.ShowDialog())
      return Rhino.Commands.Result.Cancel;

    // Verify the file that was selected
    System.Drawing.Image image;
    try
    {
      image = System.Drawing.Image.FromFile(fd.FileName);
    }
    catch (Exception)
    {
      return Rhino.Commands.Result.Failure;
    }

    // Allow the user to pick the bitmap origin
    Rhino.Input.Custom.GetPoint gp = new Rhino.Input.Custom.GetPoint();
    gp.SetCommandPrompt("Bitmap Origin");
    gp.ConstrainToConstructionPlane(true);
    gp.Get();
    if (gp.CommandResult() != Rhino.Commands.Result.Success)
      return gp.CommandResult();

    // Get the view that the point was picked in.
    // This will be the view that the bitmap appears in.
    Rhino.Display.RhinoView view = gp.View();
    if (view == null)
    {
      view = doc.Views.ActiveView;
      if (view == null)
        return Rhino.Commands.Result.Failure;
    }

    // Allow the user to specify the bitmap with in model units
    Rhino.Input.Custom.GetNumber gn = new Rhino.Input.Custom.GetNumber();
    gn.SetCommandPrompt("Bitmap width");
    gn.SetLowerLimit(1.0, false);
    gn.Get();
    if (gn.CommandResult() != Rhino.Commands.Result.Success)
      return gn.CommandResult();

    // Cook up some scale factors
    double w = gn.Number();
    double image_width = image.Width;
    double image_height = image.Height;
    double h = w * (image_height / image_width);

    Rhino.Geometry.Plane plane = view.ActiveViewport.ConstructionPlane();
    plane.Origin = gp.Point();
    view.ActiveViewport.SetTraceImage(fd.FileName, plane, w, h, false, false);
    view.Redraw();
    return Rhino.Commands.Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function AddBackgroundBitmap(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Rhino.RhinoApp.WriteLine("hey")
	' Allow the user to select a bitmap file
	Dim fd As New Rhino.UI.OpenFileDialog()
	fd.Filter = "Image Files (*.bmp;*.png;*.jpg)|*.bmp;*.png;*.jpg"
	If Not fd.ShowDialog() Then
	  Return Rhino.Commands.Result.Cancel
	End If

	' Verify the file that was selected
	Dim image As System.Drawing.Image
	Try
	  image = System.Drawing.Image.FromFile(fd.FileName)
	Catch e1 As Exception
	  Return Rhino.Commands.Result.Failure
	End Try

	' Allow the user to pick the bitmap origin
	Dim gp As New Rhino.Input.Custom.GetPoint()
	gp.SetCommandPrompt("Bitmap Origin")
	gp.ConstrainToConstructionPlane(True)
	gp.Get()
	If gp.CommandResult() <> Rhino.Commands.Result.Success Then
	  Return gp.CommandResult()
	End If

	' Get the view that the point was picked in.
	' This will be the view that the bitmap appears in.
	Dim view As Rhino.Display.RhinoView = gp.View()
	If view Is Nothing Then
	  view = doc.Views.ActiveView
	  If view Is Nothing Then
		Return Rhino.Commands.Result.Failure
	  End If
	End If

	' Allow the user to specify the bitmap with in model units
	Dim gn As New Rhino.Input.Custom.GetNumber()
	gn.SetCommandPrompt("Bitmap width")
	gn.SetLowerLimit(1.0, False)
	gn.Get()
	If gn.CommandResult() <> Rhino.Commands.Result.Success Then
	  Return gn.CommandResult()
	End If

	' Cook up some scale factors
	Dim w As Double = gn.Number()
	Dim image_width As Double = image.Width
	Dim image_height As Double = image.Height
	Dim h As Double = w * (image_height / image_width)

	Dim plane As Rhino.Geometry.Plane = view.ActiveViewport.ConstructionPlane()
	plane.Origin = gp.Point()
	view.ActiveViewport.SetTraceImage(fd.FileName, plane, w, h, False, False)
	view.Redraw()
	Return Rhino.Commands.Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
import Rhino
import scriptcontext
import System.Windows.Forms.DialogResult
import System.Drawing.Image

def AddBackgroundBitmap():
    # Allow the user to select a bitmap file
    fd = Rhino.UI.OpenFileDialog()
    fd.Filter = "Image Files (*.bmp;*.png;*.jpg)|*.bmp;*.png;*.jpg"
    if not fd.ShowDialog():
        return Rhino.Commands.Result.Cancel

    # Verify the file that was selected
    image = None
    try:
        image = System.Drawing.Image.FromFile(fd.FileName)
    except:
        return Rhino.Commands.Result.Failure

    # Allow the user to pick the bitmap origin
    gp = Rhino.Input.Custom.GetPoint()
    gp.SetCommandPrompt("Bitmap Origin")
    gp.ConstrainToConstructionPlane(True)
    gp.Get()
    if gp.CommandResult()!=Rhino.Commands.Result.Success:
        return gp.CommandResult()

    # Get the view that the point was picked in.
    # This will be the view that the bitmap appears in.
    view = gp.View()
    if view is None:
        view = scriptcontext.doc.Views.ActiveView
        if view is None: return Rhino.Commands.Result.Failure

    # Allow the user to specify the bitmap with in model units
    gn = Rhino.Input.Custom.GetNumber()
    gn.SetCommandPrompt("Bitmap width")
    gn.SetLowerLimit(1.0, False)
    gn.Get()
    if gn.CommandResult()!=Rhino.Commands.Result.Success:
        return gn.CommandResult()

    # Cook up some scale factors
    w = gn.Number()
    h = w * (image.Width / image.Height)

    plane = view.ActiveViewport.ConstructionPlane()
    plane.Origin = gp.Point()
    view.ActiveViewport.SetTraceImage(fd.FileName, plane, w, h, False, False)
    view.Redraw()
    return Rhino.Commands.Result.Success

if __name__=="__main__":
    AddBackgroundBitmap()
```

</div>
