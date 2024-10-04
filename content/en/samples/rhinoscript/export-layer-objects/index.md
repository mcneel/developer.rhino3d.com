+++
aliases = ["/en/5/samples/rhinoscript/export-layer-objects/", "/en/6/samples/rhinoscript/export-layer-objects/", "/en/7/samples/rhinoscript/export-layer-objects/", "/wip/samples/rhinoscript/export-layer-objects/"]
authors = [ "dale" ]
categories = [ "Layers" ]
description = "Demonstrates how to export all objects by layer, with each layer exported to a new file using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Export Layer Objects"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/exportlayerobjects"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
Option Explicit

Sub ExportLayerObjects

  ' Declare local variables
  Dim strPath, strFile
  Dim arrLayers, strLayer
  Dim arrSelected

  ' Get the path to and name of the current document.
  ' Surround with double-quotes in case path includes spaces.
  strPath = Chr(34) & Rhino.DocumentPath & Rhino.DocumentName & Chr(34)

  ' Get names of all layers
  arrLayers = Rhino.LayerNames

  ' Disable redrawing
  Rhino.EnableRedraw False

  ' Process each layer
  For Each strLayer In arrLayers

    ' Unselect all   
    Rhino.Command "_-SelNone", 0

    ' Select all objects on layer. Surround layer name
    ' with double-quotes in case it includes spaces.
    Rhino.Command "_-SelLayer " & Chr(34) & strLayer & Chr(34), 0

    ' Make sure some objects were selected
    arrSelected = Rhino.SelectedObjects
    If IsArray(arrSelected) Then

      ' Generate a modified path string
      ' that includes the layer name
      strFile = strPath
      strFile = Replace(strFile, ".3dm", "_" & strLayer & ".3dm")

      ' Export the selected objects
      Rhino.Command "_-Export " & strFile, 0

    End If
  Next

  ' Unselect all
  Rhino.Command "_-SelNone", 0

  ' Enable redrawing
  Rhino.EnableRedraw True

End Sub
```
