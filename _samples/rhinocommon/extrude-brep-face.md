---
title: Extrude Brep Face
description: Demonstrates how to extrude the Brep face from a user-specified surface.
authors: ['steve_baer']
author_contacts: ['stevebaer']
sdk: ['RhinoCommon']
languages: ['C#', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Other']
origin: unset
order: 1
keywords: ['extrude', 'brep', 'face']
layout: code-sample-rhinocommon
---

```cs
partial class Examples
{
  public static Rhino.Commands.Result ExtrudeBrepFace(Rhino.RhinoDoc doc)
  {
    Rhino.Input.Custom.GetObject go0 = new Rhino.Input.Custom.GetObject();
    go0.SetCommandPrompt("Select surface to extrude");
    go0.GeometryFilter = Rhino.DocObjects.ObjectType.Surface;
    go0.SubObjectSelect = true;
    go0.Get();
    if (go0.CommandResult() != Rhino.Commands.Result.Success)
      return go0.CommandResult();

    Rhino.Geometry.BrepFace face = go0.Object(0).Face();
    if (null == face)
      return Rhino.Commands.Result.Failure;

    Rhino.Input.Custom.GetObject go1 = new Rhino.Input.Custom.GetObject();
    go1.SetCommandPrompt("Select path curve");
    go1.GeometryFilter = Rhino.DocObjects.ObjectType.Curve;
    go1.SubObjectSelect = true;
    go1.DeselectAllBeforePostSelect = false;
    go1.Get();
    if (go1.CommandResult() != Rhino.Commands.Result.Success)
      return go1.CommandResult();

    Rhino.Geometry.Curve curve = go1.Object(0).Curve();
    if (null == curve)
      return Rhino.Commands.Result.Failure;

    Rhino.Geometry.Brep brep = face.CreateExtrusion(curve, true);
    if (null != brep)
    {
      doc.Objects.Add(brep);
      doc.Views.Redraw();
    }

    return Rhino.Commands.Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function ExtrudeBrepFace(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim go0 As New Rhino.Input.Custom.GetObject()
	go0.SetCommandPrompt("Select surface to extrude")
	go0.GeometryFilter = Rhino.DocObjects.ObjectType.Surface
	go0.SubObjectSelect = True
	go0.Get()
	If go0.CommandResult() <> Rhino.Commands.Result.Success Then
	  Return go0.CommandResult()
	End If

	Dim face As Rhino.Geometry.BrepFace = go0.Object(0).Face()
	If Nothing Is face Then
	  Return Rhino.Commands.Result.Failure
	End If

	Dim go1 As New Rhino.Input.Custom.GetObject()
	go1.SetCommandPrompt("Select path curve")
	go1.GeometryFilter = Rhino.DocObjects.ObjectType.Curve
	go1.SubObjectSelect = True
	go1.DeselectAllBeforePostSelect = False
	go1.Get()
	If go1.CommandResult() <> Rhino.Commands.Result.Success Then
	  Return go1.CommandResult()
	End If

	Dim curve As Rhino.Geometry.Curve = go1.Object(0).Curve()
	If Nothing Is curve Then
	  Return Rhino.Commands.Result.Failure
	End If

	Dim brep As Rhino.Geometry.Brep = face.CreateExtrusion(curve, True)
	If Nothing IsNot brep Then
	  doc.Objects.Add(brep)
	  doc.Views.Redraw()
	End If

	Return Rhino.Commands.Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
# No Python sample available
```
{: #py .tab-pane .fade .in}
