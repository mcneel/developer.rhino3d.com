+++
aliases = ["/en/5/samples/rhinocommon/duplicate-surface-border/", "/en/6/samples/rhinocommon/duplicate-surface-border/", "/en/7/samples/rhinocommon/duplicate-surface-border/", "/wip/samples/rhinocommon/duplicate-surface-border/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to duplicate the borders of a user-specified surface or polysurface."
keywords = [ "duplicate", "borders", "surface" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Duplicate Surface Border"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/dupborder"
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
  public static Rhino.Commands.Result DupBorder(Rhino.RhinoDoc doc)
  {
    const ObjectType filter = Rhino.DocObjects.ObjectType.Surface | Rhino.DocObjects.ObjectType.PolysrfFilter;
    Rhino.DocObjects.ObjRef objref;
    Rhino.Commands.Result rc = Rhino.Input.RhinoGet.GetOneObject("Select surface or polysurface", false, filter, out objref);
    if (rc != Rhino.Commands.Result.Success || objref == null)
      return rc;

    Rhino.DocObjects.RhinoObject rhobj = objref.Object();
    Rhino.Geometry.Brep brep = objref.Brep();
    if (rhobj == null || brep == null)
      return Rhino.Commands.Result.Failure;

    rhobj.Select(false);
    Rhino.Geometry.Curve[] curves = brep.DuplicateEdgeCurves(true);
    double tol = doc.ModelAbsoluteTolerance * 2.1;
    curves = Rhino.Geometry.Curve.JoinCurves(curves, tol);
    for (int i = 0; i < curves.Length; i++)
    {
      Guid id = doc.Objects.AddCurve(curves[i]);
      doc.Objects.Select(id);
    }
    doc.Views.Redraw();
    return Rhino.Commands.Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function DupBorder(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Const filter As ObjectType = Rhino.DocObjects.ObjectType.Surface Or Rhino.DocObjects.ObjectType.PolysrfFilter
	Dim objref As Rhino.DocObjects.ObjRef = Nothing
	Dim rc As Rhino.Commands.Result = Rhino.Input.RhinoGet.GetOneObject("Select surface or polysurface", False, filter, objref)
	If rc IsNot Rhino.Commands.Result.Success OrElse objref Is Nothing Then
	  Return rc
	End If

	Dim rhobj As Rhino.DocObjects.RhinoObject = objref.Object()
	Dim brep As Rhino.Geometry.Brep = objref.Brep()
	If rhobj Is Nothing OrElse brep Is Nothing Then
	  Return Rhino.Commands.Result.Failure
	End If

	rhobj.Select(False)
	Dim curves() As Rhino.Geometry.Curve = brep.DuplicateEdgeCurves(True)
	Dim tol As Double = doc.ModelAbsoluteTolerance * 2.1
	curves = Rhino.Geometry.Curve.JoinCurves(curves, tol)
	For i As Integer = 0 To curves.Length - 1
	  Dim id As Guid = doc.Objects.AddCurve(curves(i))
	  doc.Objects.Select(id)
	Next i
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

def DupBorder():
    filter = Rhino.DocObjects.ObjectType.Surface | Rhino.DocObjects.ObjectType.PolysrfFilter
    rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select surface or polysurface", False, filter)
    if rc != Rhino.Commands.Result.Success: return rc

    rhobj = objref.Object()
    brep = objref.Brep()
    if not rhobj or not brep: return Rhino.Commands.Result.Failure
    rhobj.Select(False)
    curves = brep.DuplicateEdgeCurves(True)
    tol = scriptcontext.doc.ModelAbsoluteTolerance * 2.1
    curves = Rhino.Geometry.Curve.JoinCurves(curves, tol)
    for curve in curves:
        id = scriptcontext.doc.Objects.AddCurve(curve)
        scriptcontext.doc.Objects.Select(id)
    scriptcontext.doc.Views.Redraw()
    return Rhino.Commands.Result.Success

if __name__=="__main__":
    DupBorder()
```

</div>
