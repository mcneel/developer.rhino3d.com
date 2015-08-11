---
layout: code-sample
title: Print Active Viewport Resolution
author: 
categories: ['Viewports and Views'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['print', 'active', 'viewport', 'resolution']
order: 169
description:  
---



```cs
public class ViewportResolutionCommand : Command
{
  public override string EnglishName { get { return "csViewportResolution"; } }

  protected override Result RunCommand(RhinoDoc doc, RunMode mode)
  {
    var active_viewport = doc.Views.ActiveView.ActiveViewport;
    RhinoApp.WriteLine("Name = {0}: Width = {1}, Height = {2}", 
      active_viewport.Name, active_viewport.Size.Width, active_viewport.Size.Height);
    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Public Class ViewportResolutionCommand
  Inherits Command
  Public Overrides ReadOnly Property EnglishName() As String
    Get
      Return "vbViewportResolution"
    End Get
  End Property

  Protected Overrides Function RunCommand(doc As RhinoDoc, mode As RunMode) As Result
    Dim activeViewport = doc.Views.ActiveView.ActiveViewport
    RhinoApp.WriteLine([String].Format("Name = {0}: Width = {1}, Height = {2}", activeViewport.Name, activeViewport.Size.Width, activeViewport.Size.Height))
    Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
from scriptcontext import doc

activeViewport = doc.Views.ActiveView.ActiveViewport
print "Name = {0}: Width = {1}, Height = {2}".format(
    activeViewport.Name, activeViewport.Size.Width, activeViewport.Size.Height)
```
{: #py .tab-pane .fade .in}


