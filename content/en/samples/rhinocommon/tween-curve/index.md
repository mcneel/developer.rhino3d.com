+++
authors = [ "steve" ]
categories = [ "Curves" ]
description = "Demonstrates how to tween two curves."
keywords = [ "tween", "curve" ]
languages = [ "C#", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Tween Curve"
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

</div>


<div class="codetab-content" id="vb">

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

</div>


<div class="codetab-content" id="py">

```python
# No Python sample available
```

</div>

