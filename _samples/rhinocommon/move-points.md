---
title: Move Points
description: Demonstrates how to move user-specified points to a new location.
authors: ['steve_baer']
sdk: ['RhinoCommon']
languages: ['C#', 'Python', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/rhinocommonsamples/dotnetmovepointobjects
order: 1
keywords: ['move', 'points']
layout: code-sample-rhinocommon
---

```cs
partial class Examples
{
  public static Result MovePointObjects(RhinoDoc doc)
  {
    ObjRef[] obj_refs;
    var rc = RhinoGet.GetMultipleObjects("Select points to move", false, ObjectType.Point, out obj_refs);
    if (rc != Result.Success || obj_refs == null)
      return rc;

    var gp = new GetPoint();
    gp.SetCommandPrompt("Point to move from");
    gp.Get();
    if (gp.CommandResult() != Result.Success)
      return gp.CommandResult();
    var start_point = gp.Point();

    gp.SetCommandPrompt("Point to move to");
    gp.SetBasePoint(start_point, false);
    gp.DrawLineFromPoint(start_point, true);
    gp.Get();
    if (gp.CommandResult() != Result.Success)
      return gp.CommandResult();
    var end_point = gp.Point();

    var xform = Transform.Translation(end_point - start_point);

    foreach (var obj_ref in obj_refs)
    {
      doc.Objects.Transform(obj_ref, xform, true);
    }

    doc.Views.Redraw();
    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function MovePointObjects(ByVal doc As RhinoDoc) As Result
	Dim obj_refs() As ObjRef = Nothing
	Dim rc = RhinoGet.GetMultipleObjects("Select points to move", False, ObjectType.Point, obj_refs)
	If rc IsNot Result.Success OrElse obj_refs Is Nothing Then
	  Return rc
	End If

	Dim gp = New GetPoint()
	gp.SetCommandPrompt("Point to move from")
	gp.Get()
	If gp.CommandResult() <> Result.Success Then
	  Return gp.CommandResult()
	End If
	Dim start_point = gp.Point()

	gp.SetCommandPrompt("Point to move to")
	gp.SetBasePoint(start_point, False)
	gp.DrawLineFromPoint(start_point, True)
	gp.Get()
	If gp.CommandResult() <> Result.Success Then
	  Return gp.CommandResult()
	End If
	Dim end_point = gp.Point()

	Dim xform = Transform.Translation(end_point - start_point)

	For Each obj_ref In obj_refs
	  doc.Objects.Transform(obj_ref, xform, True)
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
from Rhino.Input.Custom import *
from Rhino.Geometry import *
from scriptcontext import doc

def RunCommand():
  rc, obj_refs = RhinoGet.GetMultipleObjects("Select points to move", False, ObjectType.Point)
  if rc <> Result.Success or obj_refs == None:
    return rc

  gp = GetPoint()
  gp.SetCommandPrompt("Point to move from")
  gp.Get()
  if gp.CommandResult() <> Result.Success:
    return gp.CommandResult()
  start_point = gp.Point()

  gp.SetCommandPrompt("Point to move to")
  gp.SetBasePoint(start_point, False)
  gp.DrawLineFromPoint(start_point, True)
  gp.Get()
  if gp.CommandResult() <> Result.Success:
    return gp.CommandResult()
  end_point = gp.Point()

  xform = Transform.Translation(end_point - start_point)

  for obj_ref in obj_refs:
    doc.Objects.Transform(obj_ref, xform, True)

  doc.Views.Redraw()
  return Result.Success

if __name__ == "__main__":
  RunCommand()
```
{: #py .tab-pane .fade .in}
