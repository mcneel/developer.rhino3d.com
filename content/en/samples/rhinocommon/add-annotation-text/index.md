+++
authors = [ "steve" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to add annotation text to a Rhino model at a specific location."
keywords = [ "add", "annotation", "text" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Add Annotation Text"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = ""
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
  public static Rhino.Commands.Result AddAnnotationText(Rhino.RhinoDoc doc)
  {
    Rhino.Geometry.Point3d pt = new Rhino.Geometry.Point3d(10, 0, 0);
    const string text = "Hello RhinoCommon";
    const double height = 2.0;
    const string font = "Arial";
    Rhino.Geometry.Plane plane = doc.Views.ActiveView.ActiveViewport.ConstructionPlane();
    plane.Origin = pt;
    Guid id = doc.Objects.AddText(text, plane, height, font, false, false);
    if( id != Guid.Empty )
    {
      doc.Views.Redraw();
      return Rhino.Commands.Result.Success;
    }
    return Rhino.Commands.Result.Failure;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function AddAnnotationText(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim pt As New Rhino.Geometry.Point3d(10, 0, 0)
	Const text As String = "Hello RhinoCommon"
	Const height As Double = 2.0
	Const font As String = "Arial"
	Dim plane As Rhino.Geometry.Plane = doc.Views.ActiveView.ActiveViewport.ConstructionPlane()
	plane.Origin = pt
	Dim id As Guid = doc.Objects.AddText(text, plane, height, font, False, False)
	If id <> Guid.Empty Then
	  doc.Views.Redraw()
	  Return Rhino.Commands.Result.Success
	End If
	Return Rhino.Commands.Result.Failure
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
import Rhino
import scriptcontext
import System.Guid

def AddAnnotationText():
    pt = Rhino.Geometry.Point3d(10, 0, 0)
    text = "Hello RhinoCommon"
    height = 2.0
    font = "Arial"
    plane = scriptcontext.doc.Views.ActiveView.ActiveViewport.ConstructionPlane()
    plane.Origin = pt
    id = scriptcontext.doc.Objects.AddText(text, plane, height, font, False, False)
    if id!=System.Guid.Empty:
        scriptcontext.doc.Views.Redraw()
        return Rhino.Commands.Result.Success
    return Rhino.Commands.Result.Failure


if __name__=="__main__":
    AddAnnotationText()
```

</div>
