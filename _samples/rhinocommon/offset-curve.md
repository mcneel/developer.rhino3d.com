---
title: Offset Curve
description: Demonstrates how to offset curves to one side or another by a distance.
authors: ['Steve Baer']
author_contacts: ['stevebaer']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Curves']
origin: http://wiki.mcneel.com/developer/rhinocommonsamples/offsetcurve
order: 1
keywords: ['offset', 'curve']
layout: code-sample-rhinocommon
---

```cs
partial class Examples
{
  public static Result OffsetCurve(RhinoDoc doc)
  {
    ObjRef obj_ref;
    var rs = RhinoGet.GetOneObject(
      "Select Curve", false, ObjectType.Curve, out obj_ref);
    if (rs != Result.Success)
      return rs;
    var curve = obj_ref.Curve();
    if (curve == null)
      return Result.Nothing;

    Point3d point;
    rs = RhinoGet.GetPoint("Select Side", false, out point);
    if (rs != Result.Success)
      return rs;
    if (point == Point3d.Unset)
      return Result.Nothing;

    var curves = curve.Offset(point, Vector3d.ZAxis, 1.0,
      doc.ModelAbsoluteTolerance, CurveOffsetCornerStyle.None);

    foreach (var offset-curve in curves)
      doc.Objects.AddCurve(offset-curve);

    doc.Views.Redraw();
    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function OffsetCurve(ByVal doc As RhinoDoc) As Result
	Dim obj_ref As ObjRef = Nothing
	Dim rs = RhinoGet.GetOneObject("Select Curve", False, ObjectType.Curve, obj_ref)
	If rs IsNot Result.Success Then
	  Return rs
	End If
	Dim curve = obj_ref.Curve()
	If curve Is Nothing Then
	  Return Result.Nothing
	End If

	Dim point As Point3d = Nothing
	rs = RhinoGet.GetPoint("Select Side", False, point)
	If rs IsNot Result.Success Then
	  Return rs
	End If
	If point Is Point3d.Unset Then
	  Return Result.Nothing
	End If

	Dim curves = curve.Offset(point, Vector3d.ZAxis, 1.0, doc.ModelAbsoluteTolerance, CurveOffsetCornerStyle.None)

	For Each offset-curve In curves
	  doc.Objects.AddCurve(offset-curve)
	Next offset-curve

	doc.Views.Redraw()
	Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
from Rhino import *
from Rhino.DocObjects import *
from Rhino.Geometry import *
from Rhino.Input import *
from Rhino.Commands import *
from scriptcontext import doc
import rhinoscriptsyntax as rs

def RunCommand():
  rs, obj_ref = RhinoGet.GetOneObject("Select Curve", False, ObjectType.Curve)
  if rs <> Result.Success:
    return rs
  curve = obj_ref.Curve()
  if curve == None:
    return Result.Nothing

  rs, point = RhinoGet.GetPoint("Select Side", False)
  if rs <> Result.Success:
    return rs
  if point == Point3d.Unset:
    return Result.Nothing

  curves = curve.Offset(point, Vector3d.ZAxis, 1.0,
    doc.ModelAbsoluteTolerance, CurveOffsetCornerStyle.None)

  for offset-curve in curves:
    doc.Objects.AddCurve(offset-curve)

  doc.Views.Redraw()
  return Result.Success

if __name__ == "__main__":
  RunCommand()
```
{: #py .tab-pane .fade .in}
