---
layout: code-sample
title: Get the point at the current cursor position
author: 
categories: ['Other'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['point', 'current', 'cursor', 'position']
order: 132
description:  
---



```cs
public class PointAtCursorCommand : Command
{
  public override string EnglishName { get { return "csPointAtCursor"; } }

  [System.Runtime.InteropServices.DllImport("user32.dll")]
  public static extern bool GetCursorPos(out System.Drawing.Point point);
 
  [System.Runtime.InteropServices.DllImport("user32.dll")]
  public static extern bool ScreenToClient(IntPtr hWnd, ref System.Drawing.Point point);

  protected override Result RunCommand(RhinoDoc doc, RunMode mode)
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
Public Class PointAtCursorCommand
  Inherits Command
  Public Overrides ReadOnly Property EnglishName() As String
    Get
      Return "vbPointAtCursor"
    End Get
  End Property

  <System.Runtime.InteropServices.DllImport("user32.dll")> _
  Public Shared Function GetCursorPos(ByRef point As System.Drawing.Point) As Boolean
  End Function

  <System.Runtime.InteropServices.DllImport("user32.dll")> _
  Public Shared Function ScreenToClient(hWnd As IntPtr, ByRef point As System.Drawing.Point) As Boolean
  End Function

  Protected Overrides Function RunCommand(doc As RhinoDoc, mode As RunMode) As Result
    Dim result__1 = Result.Failure
    Dim view = doc.Views.ActiveView
    If view Is Nothing Then
      Return result__1
    End If

    Dim windowsDrawingPoint As System.Drawing.Point
    If Not GetCursorPos(windowsDrawingPoint) OrElse Not ScreenToClient(view.Handle, windowsDrawingPoint) Then
      Return result__1
    End If

    Dim xform = view.ActiveViewport.GetTransform(CoordinateSystem.Screen, CoordinateSystem.World)
    Dim point = New Rhino.Geometry.Point3d(windowsDrawingPoint.X, windowsDrawingPoint.Y, 0.0)
    RhinoApp.WriteLine([String].Format("screen point: ({0}, {1}, {2})", point.X, point.Y, point.Z))
    point.Transform(xform)
    RhinoApp.WriteLine([String].Format("world point: ({0}, {1}, {2})", point.X, point.Y, point.Z))
    result__1 = Result.Success
    Return result__1
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
no python code sample available
```
{: #py .tab-pane .fade .in}


