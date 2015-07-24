---
layout: code-sample
title: Maximize a View
author: 
categories: ['Other'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['maximize', 'view']
order: 109
description:  
---



```cs
public class MaximizeViewCommand : Command
{
  [DllImport("user32.dll", ExactSpelling = true, CharSet = CharSet.Auto)]
  public static extern IntPtr GetParent(IntPtr hWnd);
 
  [DllImport("user32.dll")]
  static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);

  public override string EnglishName { get { return "csMaximizeView"; } }

  protected override Result RunCommand(RhinoDoc doc, RunMode mode)
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
Public Class MaximizeViewCommand
  Inherits Command
  <DllImport("user32.dll", ExactSpelling:=True, CharSet:=CharSet.Auto)> _
  Public Shared Function GetParent(hWnd As IntPtr) As IntPtr
  End Function

  <DllImport("user32.dll")> _
  Private Shared Function ShowWindow(hWnd As IntPtr, nCmdShow As Integer) As Boolean
  End Function

  Public Overrides ReadOnly Property EnglishName() As String
    Get
      Return "vbMaximizeView"
    End Get
  End Property

  Protected Overrides Function RunCommand(doc As RhinoDoc, mode As RunMode) As Result
    Dim parent_handle As IntPtr = GetParent(doc.Views.ActiveView.Handle)
    If parent_handle <> IntPtr.Zero Then
      ShowWindow(parent_handle, 3)
    End If
    Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
no python code sample available
```
{: #py .tab-pane .fade .in}


