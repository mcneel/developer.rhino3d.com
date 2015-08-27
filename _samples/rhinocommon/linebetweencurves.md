---
layout: code-sample
author:
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
title: Line Between Curves
keywords: ['line', 'between', 'curves']
categories: ['Curves']
description:
order: 1
---

```cs
partial class Examples
{
  public static Rhino.Commands.Result LineBetweenCurves(Rhino.RhinoDoc doc)
  {
    Rhino.Input.Custom.GetObject go = new Rhino.Input.Custom.GetObject();
    go.SetCommandPrompt("Select two curves");
    go.GeometryFilter = Rhino.DocObjects.ObjectType.Curve;
    go.GetMultiple(2, 2);
    if (go.CommandResult() != Rhino.Commands.Result.Success)
      return go.CommandResult();

    Rhino.DocObjects.ObjRef objRef0 = go.Object(0);
    Rhino.DocObjects.ObjRef objRef1 = go.Object(1);

    double t0 = Rhino.RhinoMath.UnsetValue;
    double t1 = Rhino.RhinoMath.UnsetValue;
    Rhino.Geometry.Curve curve0 = objRef0.CurveParameter(out t0);
    Rhino.Geometry.Curve curve1 = objRef1.CurveParameter(out t1);
    if (null == curve0 || !Rhino.RhinoMath.IsValidDouble(t0) ||
        null == curve1 || !Rhino.RhinoMath.IsValidDouble(t1) )
      return Rhino.Commands.Result.Failure;

    Rhino.Geometry.Line line = Rhino.Geometry.Line.Unset;
    bool rc = Rhino.Geometry.Line.TryCreateBetweenCurves(curve0, curve1, ref t0, ref t1, false, false, out line);
    if (rc)
    {
      if (Guid.Empty != doc.Objects.AddLine(line))
      {
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
  Public Shared Function LineBetweenCurves(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim go As New Rhino.Input.Custom.GetObject()
	go.SetCommandPrompt("Select two curves")
	go.GeometryFilter = Rhino.DocObjects.ObjectType.Curve
	go.GetMultiple(2, 2)
	If go.CommandResult() <> Rhino.Commands.Result.Success Then
	  Return go.CommandResult()
	End If

	Dim objRef0 As Rhino.DocObjects.ObjRef = go.Object(0)
	Dim objRef1 As Rhino.DocObjects.ObjRef = go.Object(1)

	Dim t0 As Double = Rhino.RhinoMath.UnsetValue
	Dim t1 As Double = Rhino.RhinoMath.UnsetValue
	Dim curve0 As Rhino.Geometry.Curve = objRef0.CurveParameter(t0)
	Dim curve1 As Rhino.Geometry.Curve = objRef1.CurveParameter(t1)
	If Nothing Is curve0 OrElse Not Rhino.RhinoMath.IsValidDouble(t0) OrElse Nothing Is curve1 OrElse Not Rhino.RhinoMath.IsValidDouble(t1) Then
	  Return Rhino.Commands.Result.Failure
	End If

	Dim line As Rhino.Geometry.Line = Rhino.Geometry.Line.Unset
	Dim rc As Boolean = Rhino.Geometry.Line.TryCreateBetweenCurves(curve0, curve1, t0, t1, False, False, line)
	If rc Then
	  If Guid.Empty <> doc.Objects.AddLine(line) Then
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

