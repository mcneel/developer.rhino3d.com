---
layout: code-sample
title: Setting a Viewport's Title
author: 
categories: ['Viewports and Views'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['setting', 'viewports', 'title']
order: 151
description:  
---



```cs
public class SetViewNameCommand : Command
{
  public override string EnglishName { get { return "csSetViewName"; } }

  protected override Result RunCommand(RhinoDoc doc, RunMode mode)
  {
    var view = doc.Views.ActiveView;
    if (view == null)
      return Result.Failure;
   
    view.MainViewport.Name = "Facade";
    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Public Class SetViewNameCommand
  Inherits Command
  Public Overrides ReadOnly Property EnglishName() As String
    Get
      Return "vbSetViewName"
    End Get
  End Property

  Protected Overrides Function RunCommand(doc As RhinoDoc, mode As RunMode) As Result
    Dim view As Rhino.Display.RhinoView = doc.Views.ActiveView
    If view Is Nothing Then
      Return Rhino.Commands.Result.Failure
    End If

    view.MainViewport.Name = "Facade"
    Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
from Rhino.Commands import *
import rhinoscriptsyntax as rs
from scriptcontext import doc

def RunCommand():
  view = doc.Views.ActiveView
  if view == None:
    return Result.Failure
 
  view.MainViewport.Name = "Facade"
  return Result.Success

if __name__ == "__main__":
  RunCommand()
```
{: #py .tab-pane .fade .in}


