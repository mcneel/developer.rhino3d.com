---
layout: code-sample
author:
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
title: Maximize a View
keywords: ['maximize', 'view']
categories: ['Viewports and Views']
description:
order: 1
---

```cs
partial class Examples
{
  [DllImport("user32.dll", ExactSpelling = true, CharSet = CharSet.Auto)]
  public static extern IntPtr GetParent(IntPtr hWnd);

  [DllImport("user32.dll")]
  static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);

  public static Result MaximizeView(RhinoDoc doc)
  {
    IntPtr parent_handle = GetParent(doc.Views.ActiveView.Handle);
    if (parent_handle != IntPtr.Zero)
      ShowWindow(parent_handle, 3);
    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  <DllImport("user32.dll", ExactSpelling := True, CharSet := CharSet.Auto)>
  Public Shared Function GetParent(ByVal hWnd As IntPtr) As IntPtr
  End Function

  <DllImport("user32.dll")>
  Shared Function ShowWindow(ByVal hWnd As IntPtr, ByVal nCmdShow As Integer) As Boolean
  End Function

  Public Shared Function MaximizeView(ByVal doc As RhinoDoc) As Result
	Dim parent_handle As IntPtr = GetParent(doc.Views.ActiveView.Handle)
	If parent_handle <> IntPtr.Zero Then
	  ShowWindow(parent_handle, 3)
	End If
	Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in .active}


```python
```
{: #py .tab-pane .fade .in .active}

