---
layout: code-sample
title: Select objects on layer
author: 
categories: ['Picking and Selection'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['select', 'objects', 'layer']
order: 149
description:  
---



```cs
public static Rhino.Commands.Result SelLayer(Rhino.RhinoDoc doc)
{
  // Prompt for a layer name
  string layername = doc.Layers.CurrentLayer.Name;
  Result rc = Rhino.Input.RhinoGet.GetString("Name of layer to select objects", true, ref layername);
  if (rc != Rhino.Commands.Result.Success)
    return rc;

  // Get all of the objects on the layer. If layername is bogus, you will
  // just get an empty list back
  Rhino.DocObjects.RhinoObject[] rhobjs = doc.Objects.FindByLayer(layername);
  if (rhobjs == null || rhobjs.Length < 1)
    return Rhino.Commands.Result.Cancel;

  for (int i = 0; i < rhobjs.Length; i++)
    rhobjs[i].Select(true);
  doc.Views.Redraw();
  return Rhino.Commands.Result.Success;
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Public Shared Function SelLayer(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
  Dim rc As Rhino.Commands.Result
  ' Prompt for a layer name
  Dim layername As String = doc.Layers.CurrentLayer.Name
  rc = Rhino.Input.RhinoGet.GetString("Name of layer to select objects", True, layername)
  If rc <> Rhino.Commands.Result.Success Then Return rc

  ' Get all of the objects on the layer. If layername is bogus, you will
  ' just get an empty list back
  Dim rhobjs As Rhino.DocObjects.RhinoObject() = doc.Objects.FindByLayer(layername)
  If rhobjs Is Nothing OrElse rhobjs.Length < 1 Then
    Return Rhino.Commands.Result.Cancel
  End If

  For i As Integer = 0 To rhobjs.Length - 1
    rhobjs(i).Select(True)
  Next
  doc.Views.Redraw()
  Return Rhino.Commands.Result.Success
End Function
```
{: #vb .tab-pane .fade .in}


```python
import Rhino
import scriptcontext
import System.Guid, System.Drawing.Color

def SelLayer():
    # Prompt for a layer name
    layername = scriptcontext.doc.Layers.CurrentLayer.Name
    rc, layername = Rhino.Input.RhinoGet.GetString("Name of layer to select objects", True, layername)
    if rc!=Rhino.Commands.Result.Success: return rc
    
    # Get all of the objects on the layer. If layername is bogus, you will
    # just get an empty list back
    rhobjs = scriptcontext.doc.Objects.FindByLayer(layername)
    if not rhobjs: Rhino.Commands.Result.Cancel
    
    for obj in rhobjs: obj.Select(True)
    scriptcontext.doc.Views.Redraw()
    return Rhino.Commands.Result.Success

if __name__=="__main__":
    SelLayer()
```
{: #py .tab-pane .fade .in}


