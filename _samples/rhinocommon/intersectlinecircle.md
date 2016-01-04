---
title: Intersecting a Line with a Circle
description:
author:
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
platforms: ['Cross-Platform']
categories: ['Other']
origin: unset
order: 1
keywords: ['intersecting', 'line', 'with', 'circle']
layout: code-sample-rhinocommon
---

```cs
partial class Examples
{
  public static Result IntersectLineCircle(RhinoDoc doc)
  {
    Circle circle;
    var rc = RhinoGet.GetCircle(out circle);
    if (rc != Result.Success)
      return rc;
    doc.Objects.AddCircle(circle);
    doc.Views.Redraw();

    Line line;
    rc = RhinoGet.GetLine(out line);
    if (rc != Result.Success)
      return rc;
    doc.Objects.AddLine(line);
    doc.Views.Redraw();

    double t1, t2;
    Point3d point1, point2;
    var line_circle_intersect = Intersection.LineCircle(line, circle, out t1, out point1, out t2, out point2);
    string msg = "";
    switch (line_circle_intersect) {
      case LineCircleIntersection.None:
        msg = "line does not intersect circle";
        break;
      case LineCircleIntersection.Single:
        msg = string.Format("line intersects circle at point ({0})", point1);
        doc.Objects.AddPoint(point1);
        break;
      case LineCircleIntersection.Multiple:
        msg = string.Format("line intersects circle at points ({0}) and ({1})",
          point1, point2);
        doc.Objects.AddPoint(point1);
        doc.Objects.AddPoint(point2);
        break;
    }
    RhinoApp.WriteLine(msg);
    doc.Views.Redraw();
    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function IntersectLineCircle(ByVal doc As RhinoDoc) As Result
	Dim circle As Circle = Nothing
	Dim rc = RhinoGet.GetCircle(circle)
	If rc IsNot Result.Success Then
	  Return rc
	End If
	doc.Objects.AddCircle(circle)
	doc.Views.Redraw()

	Dim line As Line = Nothing
	rc = RhinoGet.GetLine(line)
	If rc IsNot Result.Success Then
	  Return rc
	End If
	doc.Objects.AddLine(line)
	doc.Views.Redraw()

	Dim t1 As Double = Nothing, t2 As Double = Nothing
	Dim point1 As Point3d = Nothing, point2 As Point3d = Nothing
	Dim line_circle_intersect = Intersection.LineCircle(line, circle, t1, point1, t2, point2)
	Dim msg As String = ""
	Select Case line_circle_intersect
	  Case LineCircleIntersection.None
		msg = "line does not intersect circle"
	  Case LineCircleIntersection.Single
		msg = String.Format("line intersects circle at point ({0})", point1)
		doc.Objects.AddPoint(point1)
	  Case LineCircleIntersection.Multiple
		msg = String.Format("line intersects circle at points ({0}) and ({1})", point1, point2)
		doc.Objects.AddPoint(point1)
		doc.Objects.AddPoint(point2)
	End Select
	RhinoApp.WriteLine(msg)
	doc.Views.Redraw()
	Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
# No Python sample available
```
{: #py .tab-pane .fade .in}

