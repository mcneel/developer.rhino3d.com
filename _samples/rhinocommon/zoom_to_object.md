---
title: Zoom to Object
description: Zoom to a Selected Object
author: ['Steve Baer', '@stevebaer']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Adding Objects']
origin: http://wiki.mcneel.com/developer/rhinocommonsamples/zoomtoobject
order: 1
keywords: ['zoom', 'selected', 'object']
layout: code-sample-rhinocommon
---

```cs
partial class Examples
{
  public static Rhino.Commands.Result ZoomToObject(Rhino.RhinoDoc doc)
  {
    Rhino.DocObjects.ObjRef rhObject;
    var rc = Rhino.Input.RhinoGet.GetOneObject("Select object to zoom", false, Rhino.DocObjects.ObjectType.None, out rhObject);
    if (rc != Rhino.Commands.Result.Success)
      return rc;

    var obj = rhObject.Object();
    var view = doc.Views.ActiveView;
    if (obj == null || view == null)
      return Rhino.Commands.Result.Failure;

    var bbox = obj.Geometry.GetBoundingBox(true);

    const double pad = 0.05;    // A little padding...
    double dx = (bbox.Max.X - bbox.Min.X) * pad;
    double dy = (bbox.Max.Y - bbox.Min.Y) * pad;
    double dz = (bbox.Max.Z - bbox.Min.Z) * pad;
    bbox.Inflate(dx, dy, dz);
    view.ActiveViewport.ZoomBoundingBox(bbox);
    view.Redraw();
    return Rhino.Commands.Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function ZoomToObject(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	Dim rhObject As Rhino.DocObjects.ObjRef = Nothing
	Dim rc = Rhino.Input.RhinoGet.GetOneObject("Select object to zoom", False, Rhino.DocObjects.ObjectType.None, rhObject)
	If rc IsNot Rhino.Commands.Result.Success Then
	  Return rc
	End If

	Dim obj = rhObject.Object()
	Dim view = doc.Views.ActiveView
	If obj Is Nothing OrElse view Is Nothing Then
	  Return Rhino.Commands.Result.Failure
	End If

	Dim bbox = obj.Geometry.GetBoundingBox(True)

	Const pad As Double = 0.05 ' A little padding...
	Dim dx As Double = (bbox.Max.X - bbox.Min.X) * pad
	Dim dy As Double = (bbox.Max.Y - bbox.Min.Y) * pad
	Dim dz As Double = (bbox.Max.Z - bbox.Min.Z) * pad
	bbox.Inflate(dx, dy, dz)
	view.ActiveViewport.ZoomBoundingBox(bbox)
	view.Redraw()
	Return Rhino.Commands.Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
import Rhino
import scriptcontext

def ZoomToObject():
    rc, rhobject = Rhino.Input.RhinoGet.GetOneObject("Select object to zoom", False, Rhino.DocObjects.ObjectType.None)
    if rc != Rhino.Commands.Result.Success: return

    obj = rhobject.Object()
    view = scriptcontext.doc.Views.ActiveView
    if not obj or not view: return

    bbox = obj.Geometry.GetBoundingBox(True)

    pad = 0.05  #A little padding...
    dx = (bbox.Max.X - bbox.Min.X) * pad
    dy = (bbox.Max.Y - bbox.Min.Y) * pad
    dz = (bbox.Max.Z - bbox.Min.Z) * pad
    bbox.Inflate(dx, dy, dz);
    view.ActiveViewport.ZoomBoundingBox(bbox)
    view.Redraw()

if __name__=="__main__":
    ZoomToObject()
```
{: #py .tab-pane .fade .in}
