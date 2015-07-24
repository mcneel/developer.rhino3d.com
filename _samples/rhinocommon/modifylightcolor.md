---
layout: code-sample
title: Modify a Light's Color
author: 
categories: ['Other'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['modify', 'lights', 'color']
order: 112
description:  
---



```cs
public class ChangeLightColorCommand : Rhino.Commands.Command
{
  public override string EnglishName
  {
    get { return "csLightColor"; }
  }

  protected override Result RunCommand(RhinoDoc doc, RunMode mode)
  {
    ObjRef obj_ref;
    var rc = RhinoGet.GetOneObject("Select light to change color", true,
      ObjectType.Light, out obj_ref);
    if (rc != Result.Success)
      return rc;
    var light = obj_ref.Light();
    if (light == null)
      return Result.Failure;

    var diffuse_color = light.Diffuse;
    if (Dialogs.ShowColorDialog(ref diffuse_color))
    {
      light.Diffuse = diffuse_color;
    }

    doc.Lights.Modify(obj_ref.ObjectId, light);
    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Public Class ChangeLightColorCommand
  Inherits Rhino.Commands.Command
  Public Overrides ReadOnly Property EnglishName() As String
    Get
      Return "vbLightColor"
    End Get
  End Property

  Protected Overrides Function RunCommand(doc As RhinoDoc, mode As RunMode) As Result
    Dim obj_ref As ObjRef = Nothing
    Dim rc = RhinoGet.GetOneObject("Select light to change color", True, ObjectType.Light, obj_ref)
    If rc <> Result.Success Then
      Return rc
    End If
    Dim light = obj_ref.Light()
    If light Is Nothing Then
      Return Result.Failure
    End If

    Dim diffuse_color = light.Diffuse
    If Dialogs.ShowColorDialog(diffuse_color) Then
      light.Diffuse = diffuse_color
    End If

    doc.Lights.Modify(obj_ref.ObjectId, light)
    Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
from Rhino import *
from Rhino.DocObjects import *
from Rhino.Input import *
from Rhino.UI import *
from scriptcontext import doc

def RunCommand():
  rc, obj_ref = RhinoGet.GetOneObject(
    "Select light to change color", 
    True,
    ObjectType.Light)
  if rc != Result.Success:
    return rc
  light = obj_ref.Light()
  if light == None:
    return Result.Failure

  b, color = Dialogs.ShowColorDialog(light.Diffuse)
  if b:
    light.Diffuse = color
    
  doc.Lights.Modify(obj_ref.ObjectId, light)
  return Result.Success

if __name__ == "__main__":
  RunCommand()
```
{: #py .tab-pane .fade .in}


