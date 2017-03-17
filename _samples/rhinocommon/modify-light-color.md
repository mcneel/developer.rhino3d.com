---
title: Modify Light Color
description: Demonstrates how to change the color of a user-specified light.
authors: ['Steve Baer']
author_contacts: ['stevebaer']
sdk: ['RhinoCommon']
languages: ['C#', 'Python', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/rhinocommonsamples/modifylightcolor
order: 1
keywords: ['modify', 'lights', 'color']
layout: code-sample-rhinocommon
---

```cs
partial class Examples
{
  public static Result ModifyLightColor(RhinoDoc doc)
  {
    ObjRef obj_ref;
    var rc = RhinoGet.GetOneObject("Select light to change color", true,
      ObjectType.Light, out obj_ref);
    if (rc != Result.Success)
      return rc;
    var light = obj_ref.Light();
    if (light == null)
      return Result.Failure;

    var diffuse_color = light.Diffuse;
    if (Dialogs.ShowColorDialog(ref diffuse_color))
    {
      light.Diffuse = diffuse_color;
    }

    doc.Lights.Modify(obj_ref.ObjectId, light);
    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function ModifyLightColor(ByVal doc As RhinoDoc) As Result
	Dim obj_ref As ObjRef = Nothing
	Dim rc = RhinoGet.GetOneObject("Select light to change color", True, ObjectType.Light, obj_ref)
	If rc IsNot Result.Success Then
	  Return rc
	End If
	Dim light = obj_ref.Light()
	If light Is Nothing Then
	  Return Result.Failure
	End If

	Dim diffuse_color = light.Diffuse
	If Dialogs.ShowColorDialog(diffuse_color) Then
	  light.Diffuse = diffuse_color
	End If

	doc.Lights.Modify(obj_ref.ObjectId, light)
	Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
from Rhino import *
from Rhino.DocObjects import *
from Rhino.Input import *
from Rhino.UI import *
from Rhino.Commands import Result
from scriptcontext import doc

def RunCommand():
  rc, obj_ref = RhinoGet.GetOneObject(
    "Select light to change color",
    True,
    ObjectType.Light)
  if rc != Result.Success:
    return rc
  light = obj_ref.Light()
  if light == None:
    return Result.Failure

  b, color = Dialogs.ShowColorDialog(light.Diffuse)
  if b:
    light.Diffuse = color

  doc.Lights.Modify(obj_ref.ObjectId, light)
  return Result.Success

if __name__ == "__main__":
  RunCommand()
```
{: #py .tab-pane .fade .in}
