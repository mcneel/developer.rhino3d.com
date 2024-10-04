+++
aliases = ["/en/5/samples/rhinocommon/extend-surface/", "/en/6/samples/rhinocommon/extend-surface/", "/en/7/samples/rhinocommon/extend-surface/", "/wip/samples/rhinocommon/extend-surface/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to extend a user-specified edge of a surface."
keywords = [ "extend", "surface" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Extend Surface"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/extendsurface"
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
  public static Result ExtendSurface(RhinoDoc doc)
  {
    var go = new Rhino.Input.Custom.GetObject();
    go.SetCommandPrompt("Select edge of surface to extend");
    go.GeometryFilter = ObjectType.EdgeFilter;
    go.GeometryAttributeFilter = GeometryAttributeFilter.EdgeCurve;
    go.Get();
    if (go.CommandResult() != Result.Success)
      return go.CommandResult();
    var obj_ref = go.Object(0);

    var surface = obj_ref.Surface();
    if (surface == null)
    {
      RhinoApp.WriteLine("Unable to extend polysurfaces.");
      return Result.Failure;
    }

    var brep = obj_ref.Brep();
    var face = obj_ref.Face();
    if (brep == null || face == null)
      return Result.Failure;
    if (face.FaceIndex < 0)
      return Result.Failure;

    if( !brep.IsSurface)
    {
      RhinoApp.WriteLine("Unable to extend trimmed surfaces.");
      return Result.Nothing;
    }

    var curve = obj_ref.Curve();

    var trim = obj_ref.Trim();
    if (trim == null)
      return Result.Failure;

    if (trim.TrimType == BrepTrimType.Seam)
    {
      RhinoApp.WriteLine("Unable to extend surface at seam.");
      return Result.Nothing;
    }

    var extended_surface = surface.Extend(trim.IsoStatus, 5.0, true);
    if (extended_surface != null)
    {
      var mybrep = Brep.CreateFromSurface(extended_surface);
      doc.Objects.Replace(obj_ref.ObjectId, mybrep);
      doc.Views.Redraw();
    }
    return Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function ExtendSurface(ByVal doc As RhinoDoc) As Result
	Dim go = New Rhino.Input.Custom.GetObject()
	go.SetCommandPrompt("Select edge of surface to extend")
	go.GeometryFilter = ObjectType.EdgeFilter
	go.GeometryAttributeFilter = GeometryAttributeFilter.EdgeCurve
	go.Get()
	If go.CommandResult() <> Result.Success Then
	  Return go.CommandResult()
	End If
	Dim obj_ref = go.Object(0)

	Dim surface = obj_ref.Surface()
	If surface Is Nothing Then
	  RhinoApp.WriteLine("Unable to extend polysurfaces.")
	  Return Result.Failure
	End If

	Dim brep = obj_ref.Brep()
	Dim face = obj_ref.Face()
	If brep Is Nothing OrElse face Is Nothing Then
	  Return Result.Failure
	End If
	If face.FaceIndex < 0 Then
	  Return Result.Failure
	End If

	If Not brep.IsSurface Then
	  RhinoApp.WriteLine("Unable to extend trimmed surfaces.")
	  Return Result.Nothing
	End If

	Dim curve = obj_ref.Curve()

	Dim trim = obj_ref.Trim()
	If trim Is Nothing Then
	  Return Result.Failure
	End If

	If trim.TrimType = BrepTrimType.Seam Then
	  RhinoApp.WriteLine("Unable to extend surface at seam.")
	  Return Result.Nothing
	End If

	Dim extended_surface = surface.Extend(trim.IsoStatus, 5.0, True)
	If extended_surface IsNot Nothing Then
	  Dim mybrep = Brep.CreateFromSurface(extended_surface)
	  doc.Objects.Replace(obj_ref.ObjectId, mybrep)
	  doc.Views.Redraw()
	End If
	Return Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
import Rhino
from Rhino.Input.Custom import *
from Rhino.DocObjects import *
from Rhino.Commands import *
from Rhino.Geometry import *
from scriptcontext import doc

def RunCommand():
    go = Rhino.Input.Custom.GetObject()
    go.SetCommandPrompt("Select edge of surface to extend")
    go.GeometryFilter = ObjectType.EdgeFilter
    go.GeometryAttributeFilter = GeometryAttributeFilter.EdgeCurve
    go.Get()
    if go.CommandResult() != Result.Success:
        return go.CommandResult()
    obj_ref = go.Object(0)

    surface = obj_ref.Surface()
    if surface == None:
        print "Unable to extend polysurfaces."
        return Result.Failure

    brep = obj_ref.Brep()
    face = obj_ref.Face()
    if brep == None or face == None:
        return Result.Failure
    if face.FaceIndex < 0:
        return Result.Failure

    if not brep.IsSurface:
        print "Unable to extend trimmed surfaces."
        return Result.Nothing

    curve = obj_ref.Curve()

    trim = obj_ref.Trim()
    if trim == None:
        return Result.Failure

    if trim.TrimType == BrepTrimType.Seam:
        print "Unable to extend surface at seam."
        return Result.Nothing

    extended_surface = surface.Extend(trim.IsoStatus, 5.0, True)
    if extended_surface != None:
        mybrep = Brep.CreateFromSurface(extended_surface)
        doc.Objects.Replace(obj_ref.ObjectId, mybrep)
        doc.Views.Redraw()
    return Result.Success

if __name__ == "__main__":
    RunCommand()
```

</div>
