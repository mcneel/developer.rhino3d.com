+++
aliases = ["/en/5/samples/rhinoscript/set-hierarchical-layer-names/", "/en/6/samples/rhinoscript/set-hierarchical-layer-names/", "/en/7/samples/rhinoscript/set-hierarchical-layer-names/", "/wip/samples/rhinoscript/set-hierarchical-layer-names/"]
authors = [ "dale" ]
categories = [ "Layers" ]
description = "Demonstrates how to rename layers in a hierarchical manner using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Set Hierarchical Layer Names"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/hierarchiallayers"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
Option Explicit

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' SetHierarchicalLayerNames
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub SetHierarchicalLayerNames()

  ' String that separates layer names
  Const separator = "-"

  ' Get all of the layer names.
  Dim all_layer
  all_layer = Rhino.LayerNames

  ' If only one layer, just bail.
  If UBound(all_layer) = 0 Then Exit Sub

  ' Build an array of layers who have no parent
  ' and that are from a reference file.
  Dim root_layers(), layer_count
  layer_count = 0  
  Dim layer_name, parent_layer
  For Each layer_name In all_layer
    parent_layer = Rhino.ParentLayer(layer_name)
    If IsNull(parent_layer) And Rhino.IsLayerReference(layer_name) = vbFalse Then
      ReDim Preserve root_layers(layer_count)
      root_layers(layer_count) = layer_name
      layer_count = layer_count + 1
    End If
  Next

  ' If the lists are the same size, then there are not
  ' child layers. So, just bail.
  If UBound(all_layer) = UBound(root_layers) Then Exit Sub

  ' Process the list of parentless layers    
  ProcessLayerList root_layers, separator

End Sub

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' ProcessLayerList
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub ProcessLayerList(layer_list, separator)
  ' Process each layer in the array. Note,
  ' this is a recursive function.
  Dim layer_name, layer_children
  For Each layer_name In layer_list
    ProcessLayer layer_name, separator
  Next
End Sub

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' ProcessLayer
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub ProcessLayer(layer_name, separator)

  ' Get the layer's parent
  Dim parent_layer, renamed_layer, layer_children
  parent_layer = Rhino.ParentLayer(layer_name)

  ' If the layer has a parent, then modify its name
  ' to include its parent name.
  If IsNull(parent_layer) Then
    renamed_layer = layer_name
  Else
    renamed_layer = parent_layer & separator & layer_name
    Rhino.RenameLayer layer_name, renamed_layer
  End If

  ' Get the layer's immediate children
  layer_children = Rhino.LayerChildren(renamed_layer)
  If IsArray(layer_children) Then
    ' Process these layers too    
    ProcessLayerList layer_children, separator
  End If  

End Sub
```
