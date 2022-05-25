+++
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to insert a knot into a user-selected NURBS curve."
keywords = [ "insert", "knot" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Insert Knot"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/intertknot"
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
  public static Rhino.Commands.Result InsertKnot(Rhino.RhinoDoc doc)
  {
    const ObjectType filter = Rhino.DocObjects.ObjectType.Curve;
    Rhino.DocObjects.ObjRef objref;
    Result rc = Rhino.Input.RhinoGet.GetOneObject("Select curve for knot insertion", false, filter, out objref);
    if (rc != Rhino.Commands.Result.Success)
      return rc;
    Rhino.Geometry.Curve curve = objref.Curve();
    if (null == curve)
      return Rhino.Commands.Result.Failure;
    Rhino.Geometry.NurbsCurve nurb = curve.ToNurbsCurve();
    if (null == nurb)
      return Rhino.Commands.Result.Failure;

    Rhino.Input.Custom.GetPoint gp = new Rhino.Input.Custom.GetPoint();
    gp.SetCommandPrompt("Point on curve to add knot");
    gp.Constrain(nurb, false);
    gp.Get();
    if (gp.CommandResult() == Rhino.Commands.Result.Success)
    {
      double t;
      Rhino.Geometry.Curve crv = gp.PointOnCurve(out t);
      if( crv!=null && nurb.Knots.InsertKnot(t) )
      {
        doc.Objects.Replace(objref, nurb);
        doc.Views.Redraw();
      }
    }
    return Rhino.Commands.Result.Success;  
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function InsertKnot(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Const filter As ObjectType = Rhino.DocObjects.ObjectType.Curve
	Dim objref As Rhino.DocObjects.ObjRef = Nothing
	Dim rc As Result = Rhino.Input.RhinoGet.GetOneObject("Select curve for knot insertion", False, filter, objref)
	If rc IsNot Rhino.Commands.Result.Success Then
	  Return rc
	End If
	Dim curve As Rhino.Geometry.Curve = objref.Curve()
	If Nothing Is curve Then
	  Return Rhino.Commands.Result.Failure
	End If
	Dim nurb As Rhino.Geometry.NurbsCurve = curve.ToNurbsCurve()
	If Nothing Is nurb Then
	  Return Rhino.Commands.Result.Failure
	End If

	Dim gp As New Rhino.Input.Custom.GetPoint()
	gp.SetCommandPrompt("Point on curve to add knot")
	gp.Constrain(nurb, False)
	gp.Get()
	If gp.CommandResult() = Rhino.Commands.Result.Success Then
	  Dim t As Double = Nothing
	  Dim crv As Rhino.Geometry.Curve = gp.PointOnCurve(t)
	  If crv IsNot Nothing AndAlso nurb.Knots.InsertKnot(t) Then
		doc.Objects.Replace(objref, nurb)
		doc.Views.Redraw()
	  End If
	End If
	Return Rhino.Commands.Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
import Rhino
import scriptcontext

def InsertKnot():
    filter = Rhino.DocObjects.ObjectType.Curve
    rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select curve for knot insertion", False, filter)
    if rc != Rhino.Commands.Result.Success: return rc

    curve = objref.Curve()
    if not curve: return Rhino.Commands.Result.Failure
    nurb = curve.ToNurbsCurve()
    if not nurb: return Rhino.Commands.Result.Failure

    gp = Rhino.Input.Custom.GetPoint()
    gp.SetCommandPrompt("Point on curve to add knot")
    gp.Constrain(nurb, False)
    gp.Get()
    if gp.CommandResult() == Rhino.Commands.Result.Success:
        crv, t = gp.PointOnCurve()
        if crv and nurb.Knots.InsertKnot(t):
            scriptcontext.doc.Objects.Replace(objref, nurb)
            scriptcontext.doc.Views.Redraw()
    return Rhino.Commands.Result.Success

if __name__=="__main__":
    InsertKnot()
```

</div>
