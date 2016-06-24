---
title: Move Points Non Uniform
description: Demonstrates how to move points in a non-uniform manner.
author: steve@mcneel.com
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/rhinocommonsamples/dotnetmovepointobjectsnonuniform
order: 1
keywords: ['move', 'points', 'uniform']
layout: code-sample-rhinocommon
---

```cs
partial class Examples
{
  public static Result MovePointObjectsNonUniform(RhinoDoc doc)
  {
    ObjRef[] obj_refs;
    var rc = RhinoGet.GetMultipleObjects("Select points to move", false, ObjectType.Point, out obj_refs);
    if (rc != Result.Success || obj_refs == null)
      return rc;

    foreach (var obj_ref in obj_refs)
    {
      var point3d = obj_ref.Point().Location;
      // modify the point coordinates in some way ...
      point3d.X++;
      point3d.Y++;
      point3d.Z++;

      doc.Objects.Replace(obj_ref, point3d);
    }

    doc.Views.Redraw();
    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function MovePointObjectsNonUniform(ByVal doc As RhinoDoc) As Result
	Dim obj_refs() As ObjRef = Nothing
	Dim rc = RhinoGet.GetMultipleObjects("Select points to move", False, ObjectType.Point, obj_refs)
	If rc IsNot Result.Success OrElse obj_refs Is Nothing Then
	  Return rc
	End If

	For Each obj_ref In obj_refs
	  Dim point3d = obj_ref.Point().Location
	  ' modify the point coordinates in some way ...
	  point3d.X += 1
	  point3d.Y += 1
	  point3d.Z += 1

	  doc.Objects.Replace(obj_ref, point3d)
	Next obj_ref

	doc.Views.Redraw()
	Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
from Rhino import *
from Rhino.DocObjects import *
from Rhino.Commands import *
from Rhino.Input import *
from scriptcontext import doc

def RunCommand():
  rc, obj_refs = RhinoGet.GetMultipleObjects("Select points to move", False, ObjectType.Point)
  if rc <> Result.Success or obj_refs == None:
    return rc

  for obj_ref in obj_refs:
    point3d = obj_ref.Point().Location
    point3d.X += 1
    point3d.Y += 1
    point3d.Z += 1
    doc.Objects.Replace(obj_ref, point3d)

  doc.Views.Redraw()
  return Result.Success

if __name__ == "__main__":
  RunCommand()
```
{: #py .tab-pane .fade .in}
