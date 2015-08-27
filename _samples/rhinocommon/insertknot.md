---
layout: code-sample
author:
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
title: Insert Knot
keywords: ['insert', 'knot']
categories: ['Other']
description:
order: 1
---

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
{: #cs .tab-pane .fade .in .active}


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
{: #vb .tab-pane .fade .in}

