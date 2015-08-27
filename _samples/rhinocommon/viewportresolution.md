---
layout: code-sample
author:
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
title: Print Active Viewport Resolution
keywords: ['print', 'active', 'viewport', 'resolution']
categories: ['Viewports and Views']
description:
order: 1
---

```cs
partial class Examples
{
  public static Result ViewportResolution(RhinoDoc doc)
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
Partial Friend Class Examples
  Public Shared Function ViewportResolution(ByVal doc As RhinoDoc) As Result
	Dim active_viewport = doc.Views.ActiveView.ActiveViewport
	RhinoApp.WriteLine("Name = {0}: Width = {1}, Height = {2}", active_viewport.Name, active_viewport.Size.Width, active_viewport.Size.Height)
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

