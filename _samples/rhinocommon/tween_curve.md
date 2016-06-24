---
title: Tween Curve
description: Demonstrates how to tween two curves.
author: steve@mcneel.com
apis: ['RhinoCommon']
languages: ['C#', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Curves']
origin: unset
order: 1
keywords: ['tween', 'curve']
layout: code-sample-rhinocommon
---

```cs
partial class Examples
{
  public static Rhino.Commands.Result TweenCurve(Rhino.RhinoDoc doc)
  {
    Rhino.Input.Custom.GetObject go = new Rhino.Input.Custom.GetObject();
    go.SetCommandPrompt("Select two curves");
    go.GeometryFilter = Rhino.DocObjects.ObjectType.Curve;
    go.GetMultiple(2, 2);
    if (go.CommandResult() != Rhino.Commands.Result.Success)
      return go.CommandResult();

    Rhino.Geometry.Curve curve0 = go.Object(0).Curve();
    Rhino.Geometry.Curve curve1 = go.Object(1).Curve();
    if (null != curve0 && null != curve1)
    {
      Rhino.Geometry.Curve[] curves = Rhino.Geometry.Curve.CreateTweenCurves(curve0, curve1, 1);
      if (null != curves)
      {
        for (int i = 0; i < curves.Length; i++)
          doc.Objects.AddCurve(curves[i]);

        doc.Views.Redraw();
        return Rhino.Commands.Result.Success;
      }
    }

    return Rhino.Commands.Result.Failure;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function TweenCurve(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim go As New Rhino.Input.Custom.GetObject()
	go.SetCommandPrompt("Select two curves")
	go.GeometryFilter = Rhino.DocObjects.ObjectType.Curve
	go.GetMultiple(2, 2)
	If go.CommandResult() <> Rhino.Commands.Result.Success Then
	  Return go.CommandResult()
	End If

	Dim curve0 As Rhino.Geometry.Curve = go.Object(0).Curve()
	Dim curve1 As Rhino.Geometry.Curve = go.Object(1).Curve()
	If Nothing IsNot curve0 AndAlso Nothing IsNot curve1 Then
	  Dim curves() As Rhino.Geometry.Curve = Rhino.Geometry.Curve.CreateTweenCurves(curve0, curve1, 1)
	  If Nothing IsNot curves Then
		For i As Integer = 0 To curves.Length - 1
		  doc.Objects.AddCurve(curves(i))
		Next i

		doc.Views.Redraw()
		Return Rhino.Commands.Result.Success
	  End If
	End If

	Return Rhino.Commands.Result.Failure
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
# No Python sample available
```
{: #py .tab-pane .fade .in}

