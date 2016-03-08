---
title: Isolate the Layers of Selected Objects
description: Demonstrates how to isolate the layers of selected objects using RhinoScript.
author: dale@mcneel.com
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/scriptsamples/isolatelayers
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

```vbnet
Option Explicit

Sub IsolateLayers()

  ' Select objects
  Dim objects
  objects = Rhino.GetObjects("Select objects on layers to isolate", , True, True)
  If Not IsArray(objects) Then Exit Sub

  ' Determine the number of selected objects
  Dim bound
  bound = UBound(objects)

  ' Create an array to the object layer names
  Dim object_layers()
  ReDim object_layers( bound + 1 )

  ' Fill the array
  Dim i
  For i = 0 To bound
    object_layers(i) = Rhino.ObjectLayer(objects(i))
  Next

  ' Don't forget to include current layer      
  object_layers(bound + 1) = Rhino.CurrentLayer

  ' Cull any duplicate layer names
  Dim culled_layers
  culled_layers = Rhino.CullDuplicateStrings(object_layers)

  ' Create an array containing all of the layer names
  Dim all_layers
  all_layers = Rhino.LayerNames

  ' For each layer name, search the list of culled layer names.
  ' If the layer name is not found, then turn it off.
  Dim layer
  For Each layer In all_layers
    If UBound(Filter(culled_layers, layer)) < 0 Then
      Rhino.LayerMode layer, 1
    End If
  Next

End Sub
```
