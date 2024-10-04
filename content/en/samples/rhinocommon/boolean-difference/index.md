+++
aliases = ["/en/5/samples/rhinocommon/boolean-difference/", "/en/6/samples/rhinocommon/boolean-difference/", "/en/7/samples/rhinocommon/boolean-difference/", "/wip/samples/rhinocommon/boolean-difference/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to perform a boolean difference operation on two selected polysurfaces."
keywords = [ "boolean", "difference" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Boolean Difference"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/booleandifference"
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
  public static Rhino.Commands.Result BooleanDifference(Rhino.RhinoDoc doc)
  {
    Rhino.DocObjects.ObjRef[] objrefs;
    Result rc = Rhino.Input.RhinoGet.GetMultipleObjects("Select first set of polysurfaces",
                                                        false, Rhino.DocObjects.ObjectType.PolysrfFilter, out objrefs);
    if (rc != Rhino.Commands.Result.Success)
      return rc;
    if (objrefs == null || objrefs.Length < 1)
      return Rhino.Commands.Result.Failure;

    List<Rhino.Geometry.Brep> in_breps0 = new List<Rhino.Geometry.Brep>();
    for (int i = 0; i < objrefs.Length; i++)
    {
      Rhino.Geometry.Brep brep = objrefs[i].Brep();
      if (brep != null)
        in_breps0.Add(brep);
    }

    doc.Objects.UnselectAll();
    rc = Rhino.Input.RhinoGet.GetMultipleObjects("Select second set of polysurfaces",
      false, Rhino.DocObjects.ObjectType.PolysrfFilter, out objrefs);
    if (rc != Rhino.Commands.Result.Success)
      return rc;
    if (objrefs == null || objrefs.Length < 1)
      return Rhino.Commands.Result.Failure;

    List<Rhino.Geometry.Brep> in_breps1 = new List<Rhino.Geometry.Brep>();
    for (int i = 0; i < objrefs.Length; i++)
    {
      Rhino.Geometry.Brep brep = objrefs[i].Brep();
      if (brep != null)
        in_breps1.Add(brep);
    }

    double tolerance = doc.ModelAbsoluteTolerance;
    Rhino.Geometry.Brep[] breps = Rhino.Geometry.Brep.CreateBooleanDifference(in_breps0, in_breps1, tolerance);
    if (breps.Length < 1)
      return Rhino.Commands.Result.Nothing;
    for (int i = 0; i < breps.Length; i++)
      doc.Objects.AddBrep(breps[i]);
    doc.Views.Redraw();
    return Rhino.Commands.Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function BooleanDifference(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim objrefs() As Rhino.DocObjects.ObjRef = Nothing
	Dim rc As Result = Rhino.Input.RhinoGet.GetMultipleObjects("Select first set of polysurfaces", False, Rhino.DocObjects.ObjectType.PolysrfFilter, objrefs)
	If rc IsNot Rhino.Commands.Result.Success Then
	  Return rc
	End If
	If objrefs Is Nothing OrElse objrefs.Length < 1 Then
	  Return Rhino.Commands.Result.Failure
	End If

	Dim in_breps0 As New List(Of Rhino.Geometry.Brep)()
	For i As Integer = 0 To objrefs.Length - 1
	  Dim brep As Rhino.Geometry.Brep = objrefs(i).Brep()
	  If brep IsNot Nothing Then
		in_breps0.Add(brep)
	  End If
	Next i

	doc.Objects.UnselectAll()
	rc = Rhino.Input.RhinoGet.GetMultipleObjects("Select second set of polysurfaces", False, Rhino.DocObjects.ObjectType.PolysrfFilter, objrefs)
	If rc IsNot Rhino.Commands.Result.Success Then
	  Return rc
	End If
	If objrefs Is Nothing OrElse objrefs.Length < 1 Then
	  Return Rhino.Commands.Result.Failure
	End If

	Dim in_breps1 As New List(Of Rhino.Geometry.Brep)()
	For i As Integer = 0 To objrefs.Length - 1
	  Dim brep As Rhino.Geometry.Brep = objrefs(i).Brep()
	  If brep IsNot Nothing Then
		in_breps1.Add(brep)
	  End If
	Next i

	Dim tolerance As Double = doc.ModelAbsoluteTolerance
	Dim breps() As Rhino.Geometry.Brep = Rhino.Geometry.Brep.CreateBooleanDifference(in_breps0, in_breps1, tolerance)
	If breps.Length < 1 Then
	  Return Rhino.Commands.Result.Nothing
	End If
	For i As Integer = 0 To breps.Length - 1
	  doc.Objects.AddBrep(breps(i))
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

def BooleanDifference():
    filter = Rhino.DocObjects.ObjectType.PolysrfFilter
    rc, objrefs = Rhino.Input.RhinoGet.GetMultipleObjects("Select first set of polysurfaces", False, filter)
    if rc != Rhino.Commands.Result.Success: return rc
    if not objrefs: return Rhino.Commands.Result.Failure

    in_breps0 = []
    for objref in objrefs:
        brep = objref.Brep()
        if brep: in_breps0.append(brep)

    scriptcontext.doc.Objects.UnselectAll()
    rc, objrefs = Rhino.Input.RhinoGet.GetMultipleObjects("Select second set of polysurfaces", False, filter)
    if rc != Rhino.Commands.Result.Success: return rc
    if not objrefs: return Rhino.Commands.Result.Failure

    in_breps1 = []
    for objref in objrefs:
        brep = objref.Brep()
        if brep: in_breps1.append(brep)

    tolerance = scriptcontext.doc.ModelAbsoluteTolerance
    breps = Rhino.Geometry.Brep.CreateBooleanDifference(in_breps0, in_breps1, tolerance)
    if not breps: return Rhino.Commands.Result.Nothing
    for brep in breps: scriptcontext.doc.Objects.AddBrep(brep)
    scriptcontext.doc.Views.Redraw()
    return Rhino.Commands.Result.Success

if __name__=="__main__":
    BooleanDifference()
```

</div>
