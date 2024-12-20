+++
aliases = ["/en/5/samples/rhinocommon/extend-curve/", "/en/6/samples/rhinocommon/extend-curve/", "/en/7/samples/rhinocommon/extend-curve/", "/en/wip/samples/rhinocommon/extend-curve/"]
authors = [ "steve" ]
categories = [ "Curves", "Adding Objects" ]
description = "Demonstrates how to extend a curve object to user-selected boundary objects."
keywords = [ "extend", "curve", "object" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Extend Curve"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/extendcurve"
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
  public static Result ExtendCurve(RhinoDoc doc)
  {
    ObjRef[] boundary_obj_refs;
    var rc = RhinoGet.GetMultipleObjects("Select boundary objects", false, ObjectType.AnyObject, out boundary_obj_refs);
    if (rc != Result.Success)
      return rc;
    if (boundary_obj_refs == null || boundary_obj_refs.Length == 0)
      return Result.Nothing;

    var gc = new GetObject();
    gc.SetCommandPrompt("Select curve to extend");
    gc.GeometryFilter = ObjectType.Curve;
    gc.GeometryAttributeFilter = GeometryAttributeFilter.OpenCurve;
    gc.DisablePreSelect ();
    gc.Get();
    if (gc.CommandResult() != Result.Success)
      return gc.CommandResult();
    var curve_obj_ref = gc.Object(0);

    var curve = curve_obj_ref.Curve();
    if (curve == null) return Result.Failure;
    double t;
    if (!curve.ClosestPoint(curve_obj_ref.SelectionPoint(), out t))
      return Result.Failure;
    var curve_end = t <= curve.Domain.Mid ? CurveEnd.Start : CurveEnd.End;

    var geometry = boundary_obj_refs.Select(obj=> obj.Geometry());
    var extended_curve = curve.Extend(curve_end, CurveExtensionStyle.Line, geometry);
    if (extended_curve != null && extended_curve.IsValid)
    {
      if (!doc.Objects.Replace(curve_obj_ref.ObjectId, extended_curve))
        return Result.Failure;
      doc.Views.Redraw();
    }
    else
    {
      RhinoApp.WriteLine("No boundary object was intersected so curve not extended");
      return Result.Nothing;
    }

    return Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function ExtendCurve(ByVal doc As RhinoDoc) As Result
	Dim boundary_obj_refs() As ObjRef = Nothing
	Dim rc = RhinoGet.GetMultipleObjects("Select boundary objects", False, ObjectType.AnyObject, boundary_obj_refs)
	If rc IsNot Result.Success Then
	  Return rc
	End If
	If boundary_obj_refs Is Nothing OrElse boundary_obj_refs.Length = 0 Then
	  Return Result.Nothing
	End If

	Dim gc = New GetObject()
	gc.SetCommandPrompt("Select curve to extend")
	gc.GeometryFilter = ObjectType.Curve
	gc.GeometryAttributeFilter = GeometryAttributeFilter.OpenCurve
	gc.DisablePreSelect()
	gc.Get()
	If gc.CommandResult() <> Result.Success Then
	  Return gc.CommandResult()
	End If
	Dim curve_obj_ref = gc.Object(0)

	Dim curve = curve_obj_ref.Curve()
	If curve Is Nothing Then
		Return Result.Failure
	End If
	Dim t As Double = Nothing
	If Not curve.ClosestPoint(curve_obj_ref.SelectionPoint(), t) Then
	  Return Result.Failure
	End If
	Dim curve_end = If(t <= curve.Domain.Mid, CurveEnd.Start, CurveEnd.End)

	Dim geometry = boundary_obj_refs.Select(Function(obj) obj.Geometry())
	Dim extended_curve = curve.Extend(curve_end, CurveExtensionStyle.Line, geometry)
	If extended_curve IsNot Nothing AndAlso extended_curve.IsValid Then
	  If Not doc.Objects.Replace(curve_obj_ref.ObjectId, extended_curve) Then
		Return Result.Failure
	  End If
	  doc.Views.Redraw()
	Else
	  RhinoApp.WriteLine("No boundary object was intersected so curve not extended")
	  Return Result.Nothing
	End If

	Return Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
from Rhino import *
from Rhino.Geometry import *
from Rhino.DocObjects import *
from Rhino.Commands import *
from Rhino.Input import *
from Rhino.Input.Custom import *
from scriptcontext import doc

def RunCommand():

    rc, boundary_obj_refs = RhinoGet.GetMultipleObjects("Select boundary objects", False, ObjectType.AnyObject)
    if rc != Result.Success:
        return rc
    if boundary_obj_refs == None or boundary_obj_refs.Length == 0:
        return Result.Nothing

    gc = GetObject()
    gc.SetCommandPrompt("Select curve to extend")
    gc.GeometryFilter = ObjectType.Curve
    gc.GeometryAttributeFilter = GeometryAttributeFilter.OpenCurve
    gc.Get()
    if gc.CommandResult() != Result.Success:
        return gc.CommandResult()
    curve_obj_ref = gc.Object(0)

    curve = curve_obj_ref.Curve()
    if curve == None: return Result.Failure
    b, t = curve.ClosestPoint(curve_obj_ref.SelectionPoint())
    if not b: return Result.Failure
    curve_end = CurveEnd.Start if t <= curve.Domain.Mid else CurveEnd.End

    geometry = [obj.Geometry() for obj in boundary_obj_refs]
    extended_curve = curve.Extend(curve_end, CurveExtensionStyle.Line, geometry)
    if extended_curve != None and extended_curve.IsValid:
        if not doc.Objects.Replace(curve_obj_ref.ObjectId, extended_curve):
            return Result.Failure
        doc.Views.Redraw()
        return Result.Success
    else:
        RhinoApp.WriteLine("No boundary object was intersected so curve not extended")
        return Result.Nothing

if __name__ == "__main__":
    RunCommand()
```

</div>
