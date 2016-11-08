---
title: Modify Object Color
description: Demonstrates how to modify the color of a user-specified object.
author: ['Steve Baer', '@stevebaer']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Adding Objects']
origin: http://wiki.mcneel.com/developer/rhinocommonsamples/modifyobjectcolor
order: 1
keywords: ['modify', 'objects', 'color']
layout: code-sample-rhinocommon
---

```cs
partial class Examples
{
  public static Result ModifyObjectColor(RhinoDoc doc)
  {
    ObjRef obj_ref;
    var rc = RhinoGet.GetOneObject("Select object", false, ObjectType.AnyObject, out obj_ref);
    if (rc != Result.Success)
      return rc;
    var rhino_object = obj_ref.Object();
    var color = rhino_object.Attributes.ObjectColor;
    bool b = Rhino.UI.Dialogs.ShowColorDialog(ref color);
    if (!b) return Result.Cancel;

    rhino_object.Attributes.ObjectColor = color;
    rhino_object.Attributes.ColorSource = ObjectColorSource.ColorFromObject;
    rhino_object.CommitChanges();

    // an object's color attributes can also be specified
    // when the object is added to Rhino
    var sphere = new Sphere(Point3d.Origin, 5.0);
    var attributes = new ObjectAttributes();
    attributes.ObjectColor = Color.CadetBlue;
    attributes.ColorSource = ObjectColorSource.ColorFromObject;
    doc.Objects.AddSphere(sphere, attributes);

    doc.Views.Redraw();
    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function ModifyObjectColor(ByVal doc As RhinoDoc) As Result
	Dim obj_ref As ObjRef = Nothing
	Dim rc = RhinoGet.GetOneObject("Select object", False, ObjectType.AnyObject, obj_ref)
	If rc IsNot Result.Success Then
	  Return rc
	End If
	Dim rhino_object = obj_ref.Object()
	Dim color = rhino_object.Attributes.ObjectColor
	Dim b As Boolean = Rhino.UI.Dialogs.ShowColorDialog(color)
	If Not b Then
		Return Result.Cancel
	End If

	rhino_object.Attributes.ObjectColor = color
	rhino_object.Attributes.ColorSource = ObjectColorSource.ColorFromObject
	rhino_object.CommitChanges()

	' an object's color attributes can also be specified
	' when the object is added to Rhino
	Dim sphere = New Sphere(Point3d.Origin, 5.0)
	Dim attributes = New ObjectAttributes()
	attributes.ObjectColor = System.Drawing.Color.CadetBlue
	attributes.ColorSource = ObjectColorSource.ColorFromObject
	doc.Objects.AddSphere(sphere, attributes)

	doc.Views.Redraw()
	Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
from System.Drawing import *
from Rhino import *
from Rhino.DocObjects import *
from Rhino.Geometry import *
from Rhino.Input import *
from Rhino.Commands import *
from Rhino.UI.Dialogs import ShowColorDialog
from scriptcontext import doc

def RunCommand():
  rc, obj_ref = RhinoGet.GetOneObject("Select object", False, ObjectType.AnyObject)
  if rc <> Result.Success:
    return rc
  rhino_object = obj_ref.Object()
  color = rhino_object.Attributes.ObjectColor
  b, color = ShowColorDialog(color)
  if not b: return Result.Cancel

  rhino_object.Attributes.ObjectColor = color
  rhino_object.Attributes.ColorSource = ObjectColorSource.ColorFromObject
  rhino_object.CommitChanges()

  # an object's color attributes can also be specified
  # when the object is added to Rhino
  sphere = Sphere(Point3d.Origin, 5.0)
  attributes = ObjectAttributes()
  attributes.ObjectColor = Color.CadetBlue
  attributes.ColorSource = ObjectColorSource.ColorFromObject
  doc.Objects.AddSphere(sphere, attributes)

  doc.Views.Redraw()
  return Result.Success

if __name__ == "__main__":
  RunCommand()
```
{: #py .tab-pane .fade .in}
