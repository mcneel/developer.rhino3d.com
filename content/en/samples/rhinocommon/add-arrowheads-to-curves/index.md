+++
aliases = ["/en/5/samples/rhinocommon/add-arrowheads-to-curves/", "/en/6/samples/rhinocommon/add-arrowheads-to-curves/", "/en/7/samples/rhinocommon/add-arrowheads-to-curves/", "/en/wip/samples/rhinocommon/add-arrowheads-to-curves/"]
authors = [ "steve" ]
categories = [ "Adding Objects", "Curves" ]
description = "Demonstrates how to decorate curves in a Rhino model with arrowheads."
keywords = [ "adding", "arrowheads", "curves" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Add Arrowheads to Curves"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/objectdecoration"
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
  public static Rhino.Commands.Result ObjectDecoration(Rhino.RhinoDoc doc)
  {
    // Define a line
    var line = new Rhino.Geometry.Line(new Rhino.Geometry.Point3d(0, 0, 0), new Rhino.Geometry.Point3d(10, 0, 0));

    // Make a copy of Rhino's default object attributes
    var attribs = doc.CreateDefaultAttributes();

    // Modify the object decoration style
    attribs.ObjectDecoration = Rhino.DocObjects.ObjectDecoration.BothArrowhead;

    // Create a new curve object with our attributes
    doc.Objects.AddLine(line, attribs);
    doc.Views.Redraw();

    return Rhino.Commands.Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function ObjectDecoration(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	' Define a line
	Dim line = New Rhino.Geometry.Line(New Rhino.Geometry.Point3d(0, 0, 0), New Rhino.Geometry.Point3d(10, 0, 0))

	' Make a copy of Rhino's default object attributes
	Dim attribs = doc.CreateDefaultAttributes()

	' Modify the object decoration style
	attribs.ObjectDecoration = Rhino.DocObjects.ObjectDecoration.BothArrowhead

	' Create a new curve object with our attributes
	doc.Objects.AddLine(line, attribs)
	doc.Views.Redraw()

	Return Rhino.Commands.Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
import Rhino
import scriptcontext

def ObjectDecoration():
    # Define a line
    line = Rhino.Geometry.Line(Rhino.Geometry.Point3d(0, 0, 0), Rhino.Geometry.Point3d(10, 0, 0))

    # Make a copy of Rhino's default object attributes
    attribs = scriptcontext.doc.CreateDefaultAttributes()

    # Modify the object decoration style
    attribs.ObjectDecoration = Rhino.DocObjects.ObjectDecoration.BothArrowhead

    # Create a new curve object with our attributes
    scriptcontext.doc.Objects.AddLine(line, attribs)
    scriptcontext.doc.Views.Redraw()

if __name__ == "__main__":
    ObjectDecoration()
```

</div>
