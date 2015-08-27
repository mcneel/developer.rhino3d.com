---
layout: code-sample
author:
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
title: Get the point at the current cursor position
keywords: ['point', 'current', 'cursor', 'position']
categories: ['Other']
description:
order: 1
---

```cs
partial class Examples
{
  [System.Runtime.InteropServices.DllImport("user32.dll")]
  public static extern bool GetCursorPos(out System.Drawing.Point point);

  [System.Runtime.InteropServices.DllImport("user32.dll")]
  public static extern bool ScreenToClient(IntPtr hWnd, ref System.Drawing.Point point);

  public static Result PointAtCursor(RhinoDoc doc)
  {
    var result = Result.Failure;
    var view = doc.Views.ActiveView;
    if (view == null) return result;

    System.Drawing.Point windows_drawing_point;
    if (!GetCursorPos(out windows_drawing_point) || !ScreenToClient(view.Handle, ref windows_drawing_point))
      return result;

    var xform = view.ActiveViewport.GetTransform(CoordinateSystem.Screen, CoordinateSystem.World);
    var point = new Rhino.Geometry.Point3d(windows_drawing_point.X, windows_drawing_point.Y, 0.0);
    RhinoApp.WriteLine("screen point: ({0})", point);
    point.Transform(xform);
    RhinoApp.WriteLine("world point: ({0})", point);
    result = Result.Success;
    return result;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  <System.Runtime.InteropServices.DllImport("user32.dll")>
  Public Shared Function GetCursorPos(<System.Runtime.InteropServices.Out()> ByRef point As System.Drawing.Point) As Boolean
  End Function

  <System.Runtime.InteropServices.DllImport("user32.dll")>
  Public Shared Function ScreenToClient(ByVal hWnd As IntPtr, ByRef point As System.Drawing.Point) As Boolean
  End Function

  Public Shared Function PointAtCursor(ByVal doc As RhinoDoc) As Result
	Dim result = Result.Failure
	Dim view = doc.Views.ActiveView
	If view Is Nothing Then
		Return result
	End If

	Dim windows_drawing_point As System.Drawing.Point = Nothing
	If Not GetCursorPos(windows_drawing_point) OrElse Not ScreenToClient(view.Handle, windows_drawing_point) Then
	  Return result
	End If

	Dim xform = view.ActiveViewport.GetTransform(CoordinateSystem.Screen, CoordinateSystem.World)
	Dim point = New Rhino.Geometry.Point3d(windows_drawing_point.X, windows_drawing_point.Y, 0.0)
	RhinoApp.WriteLine("screen point: ({0})", point)
	point.Transform(xform)
	RhinoApp.WriteLine("world point: ({0})", point)
	result = Result.Success
	Return result
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
```
{: #py .tab-pane .fade .in}

