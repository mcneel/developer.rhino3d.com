---
title: Add NURBS Curve
description: Demonstrates how to create a NURBS curve from a list of points.
authors: ['Steve Baer']
author_contacts: ['stevebaer']
sdk: ['RhinoCommon']
languages: ['C#', 'Python', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Adding Objects', 'Curves']
origin: http://wiki.mcneel.com/developer/rhinocommonsamples/addnurbscurve
order: 1
keywords: ['add', 'nurbs', 'curve']
layout: code-sample-rhinocommon
---

```cs
partial class Examples
{
  public static Rhino.Commands.Result AddNurbsCurve(Rhino.RhinoDoc doc)
  {
    Rhino.Collections.Point3dList points = new Rhino.Collections.Point3dList(5);
    points.Add(0, 0, 0);
    points.Add(0, 2, 0);
    points.Add(2, 3, 0);
    points.Add(4, 2, 0);
    points.Add(4, 0, 0);
    Rhino.Geometry.NurbsCurve nc = Rhino.Geometry.NurbsCurve.Create(false, 3, points);
    Rhino.Commands.Result rc = Rhino.Commands.Result.Failure;
    if (nc != null && nc.IsValid)
    {
      if (doc.Objects.AddCurve(nc) != Guid.Empty)
      {
        doc.Views.Redraw();
        rc = Rhino.Commands.Result.Success;
      }
    }
    return rc;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function AddNurbsCurve(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim points As New Rhino.Collections.Point3dList(5)
	points.Add(0, 0, 0)
	points.Add(0, 2, 0)
	points.Add(2, 3, 0)
	points.Add(4, 2, 0)
	points.Add(4, 0, 0)
	Dim nc As Rhino.Geometry.NurbsCurve = Rhino.Geometry.NurbsCurve.Create(False, 3, points)
	Dim rc As Rhino.Commands.Result = Rhino.Commands.Result.Failure
	If nc IsNot Nothing AndAlso nc.IsValid Then
	  If doc.Objects.AddCurve(nc) <> Guid.Empty Then
		doc.Views.Redraw()
		rc = Rhino.Commands.Result.Success
	  End If
	End If
	Return rc
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
import Rhino
import scriptcontext
import System.Guid

def AddNurbsCurve():
    points = Rhino.Collections.Point3dList(5)
    points.Add(0, 0, 0)
    points.Add(0, 2, 0)
    points.Add(2, 3, 0)
    points.Add(4, 2, 0)
    points.Add(4, 0, 0)

    nc = Rhino.Geometry.NurbsCurve.Create(False, 3, points)
    rc = Rhino.Commands.Result.Failure
    if nc and nc.IsValid:
        if scriptcontext.doc.Objects.AddCurve(nc)!=System.Guid.Empty:
            scriptcontext.doc.Views.Redraw()
            rc = Rhino.Commands.Result.Success
    return rc

if __name__=="__main__":
    AddNurbsCurve()
```
{: #py .tab-pane .fade .in}
