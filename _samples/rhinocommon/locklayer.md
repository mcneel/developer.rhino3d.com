---
layout: code-sample
title: Lock a Layer
author: 
categories: ['Other'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['lock', 'layer']
order: 106
description:  
---



```cs
public class LockLayerCommand : Command
{
  public override string EnglishName { get { return "csLockLayer"; } }

  protected override Result RunCommand(RhinoDoc doc, RunMode mode)
  {
    string layer_name = "";
    var rc = RhinoGet.GetString("Name of layer to lock", true, ref layer_name);
    if (rc != Result.Success)
      return rc;
    if (String.IsNullOrWhiteSpace(layer_name))
      return Result.Nothing;
   
    // because of sublayers it's possible that mone than one layer has the same name
    // so simply calling doc.Layers.Find(layerName) isn't good enough.  If "layerName" returns
    // more than one layer then present them to the user and let him decide.
    var matching_layers = (from layer in doc.Layers
                           where layer.Name == layer_name
                           select layer).ToList<Rhino.DocObjects.Layer>();

    Rhino.DocObjects.Layer layer_to_lock = null;
    if (matching_layers.Count == 0)
    {
      RhinoApp.WriteLine("Layer \"{0}\" does not exist.", layer_name);
      return Result.Nothing;
    }
    else if (matching_layers.Count == 1)
    {
      layer_to_lock = matching_layers[0];
    }
    else if (matching_layers.Count > 1)
    {
      for (int i = 0; i < matching_layers.Count; i++)
      {
        RhinoApp.WriteLine("({0}) {1}", i+1, matching_layers[i].FullPath.Replace("::", "->"));
      }
      int selected_layer = -1;
      rc = RhinoGet.GetInteger("which layer?", true, ref selected_layer);
      if (rc != Result.Success)
        return rc;
      if (selected_layer > 0 && selected_layer <= matching_layers.Count)
        layer_to_lock = matching_layers[selected_layer - 1];
      else return Result.Nothing;
    }

    if (layer_to_lock == null)
      return Result.Nothing;

    if (!layer_to_lock.IsLocked)
    {
      layer_to_lock.IsLocked = true;
      layer_to_lock.CommitChanges();
      return Result.Success;
    }
    else
    {
      RhinoApp.WriteLine("layer {0} is already locked.", layer_to_lock.FullPath);
      return Result.Nothing;
    } 
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Public Class LockLayerCommand
  Inherits Command
  Public Overrides ReadOnly Property EnglishName() As String
    Get
      Return "vbLockLayer"
    End Get
  End Property

  Protected Overrides Function RunCommand(doc As RhinoDoc, mode As RunMode) As Result
    Dim layerName As String = ""
    Dim rc = Rhino.Input.RhinoGet.GetString("Name of layer to lock", True, layerName)
    If rc <> Result.Success Then
      Return rc
    End If
    If [String].IsNullOrWhiteSpace(layerName) Then
      Return Result.[Nothing]
    End If

    ' because of sublayers it's possible that mone than one layer has the same name
    ' so simply calling doc.Layers.Find(layerName) isn't good enough.  If "layerName" returns
    ' more than one layer then present them to the user and let him decide.
    Dim matchingLayers = (From layer In doc.Layers Where layer.Name = layerName Select layer).ToList()

    Dim layerToLock As Rhino.DocObjects.Layer = Nothing
    If matchingLayers.Count = 0 Then
      RhinoApp.WriteLine([String].Format("Layer ""{0}"" does not exist.", layerName))
      Return Result.[Nothing]
    ElseIf matchingLayers.Count = 1 Then
      layerToLock = matchingLayers(0)
    ElseIf matchingLayers.Count > 1 Then
      For i As Integer = 0 To matchingLayers.Count - 1
        RhinoApp.WriteLine([String].Format("({0}) {1}", i + 1, matchingLayers(i).FullPath.Replace("::", "->")))
      Next
      Dim selectedLayer As Integer = -1
      rc = Rhino.Input.RhinoGet.GetInteger("which layer?", True, selectedLayer)
      If rc <> Result.Success Then
        Return rc
      End If
      If selectedLayer > 0 AndAlso selectedLayer <= matchingLayers.Count Then
        layerToLock = matchingLayers(selectedLayer - 1)
      Else
        Return Result.[Nothing]
      End If
    End If

    If layerToLock Is Nothing Then
      Return Result.Nothing
    End If

    If Not layerToLock.IsLocked Then
      layerToLock.IsLocked = True
      layerToLock.CommitChanges()
      Return Result.Success
    Else
      RhinoApp.WriteLine([String].Format("layer {0} is already locked.", layerToLock.FullPath))
      Return Result.[Nothing]
    End If
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
import rhinoscriptsyntax as rs
from scriptcontext import doc

def lock():
    layerName = rs.GetString("Name of layer to lock")
    
    matchingLayers = [layer for layer in doc.Layers if layer.Name == layerName]
    
    layerToLock = None
    if len(matchingLayers) == 0:
        print "Layer \"{0}\" does not exist.".format(layerName)
    elif len(matchingLayers) == 1:
        layerToLock = matchingLayers[0]
    elif len(matchingLayers) > 1:
        i = 0;
        for layer in matchingLayers:
            print "({0}) {1}".format(i+1, matchingLayers[i].FullPath.replace("::", "->"))
            i += 1
            
        selectedLayer = rs.GetInteger("which layer?", -1, 1, len(matchingLayers))
        if selectedLayer == None:
            return
        layerToLock = matchingLayers[selectedLayer - 1]
        
    if layerToLock.IsLocked:
        print "layer {0} is already locked.".format(layerToLock.FullPath)
    else:
        layerToLock.IsLocked = True
        layerToLock.CommitChanges()
          
if __name__ == "__main__":
    lock()
        
```
{: #py .tab-pane .fade .in}


