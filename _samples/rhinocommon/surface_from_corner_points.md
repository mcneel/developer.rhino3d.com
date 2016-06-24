---
title: Surface from Corner Points
description: Demonstrates how to create a surface from a set of corner points.
author: steve@mcneel.com
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/rhinocommonsamples/srfpt
order: 1
keywords: ['surface', 'corner', 'points']
layout: code-sample-rhinocommon
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
{: #vb .tab-pane .fade .in}


```python
from Rhino.Geometry import NurbsSurface, Point3d
from scriptcontext import doc

surface = NurbsSurface.CreateFromCorners(
  Point3d(5, 0, 0),
  Point3d(5, 5, 5),
  Point3d(0, 5, 0),
  Point3d(0, 0, 0));

doc.Objects.AddSurface(surface);
doc.Views.Redraw();
```
{: #py .tab-pane .fade .in}
