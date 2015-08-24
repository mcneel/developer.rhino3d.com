---
layout: code-sample
author:
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
title: Surface from Corner Points
keywords: ['surface', 'corner', 'points']
categories: ['Other']
description:
order: 1
---

```cs
partial class Examples
{
  public static Result SurfaceFromCorners(RhinoDoc doc)
  {
    var surface = NurbsSurface.CreateFromCorners(
      new Point3d(5, 0, 0),
      new Point3d(5, 5, 5),
      new Point3d(0, 5, 0),
      new Point3d(0, 0, 0));

    doc.Objects.AddSurface(surface);
    doc.Views.Redraw();

    return Rhino.Commands.Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function SurfaceFromCorners(ByVal doc As RhinoDoc) As Result
	Dim surface = NurbsSurface.CreateFromCorners(New Point3d(5, 0, 0), New Point3d(5, 5, 5), New Point3d(0, 5, 0), New Point3d(0, 0, 0))

	doc.Objects.AddSurface(surface)
	doc.Views.Redraw()

	Return Rhino.Commands.Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in .active}

