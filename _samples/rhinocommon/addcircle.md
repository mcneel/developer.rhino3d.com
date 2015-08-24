---
layout: code-sample
author:
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
title: Add Circle
keywords: ['add', 'circle']
categories: ['Adding Objects']
description:
order: 1
---

```cs
partial class Examples
{
  public static Rhino.Commands.Result AddCircle(Rhino.RhinoDoc doc)
  {
    Rhino.Geometry.Point3d center = new Rhino.Geometry.Point3d(0, 0, 0);
    const double radius = 10.0;
    Rhino.Geometry.Circle c = new Rhino.Geometry.Circle(center, radius);
    if (doc.Objects.AddCircle(c) != Guid.Empty)
    {
      doc.Views.Redraw();
      return Rhino.Commands.Result.Success;
    }
    return Rhino.Commands.Result.Failure;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function AddCircle(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim center As New Rhino.Geometry.Point3d(0, 0, 0)
	Const radius As Double = 10.0
	Dim c As New Rhino.Geometry.Circle(center, radius)
	If doc.Objects.AddCircle(c) <> Guid.Empty Then
	  doc.Views.Redraw()
	  Return Rhino.Commands.Result.Success
	End If
	Return Rhino.Commands.Result.Failure
  End Function
End Class
```
{: #vb .tab-pane .fade .in .active}


```python
```
{: #py .tab-pane .fade .in .active}

