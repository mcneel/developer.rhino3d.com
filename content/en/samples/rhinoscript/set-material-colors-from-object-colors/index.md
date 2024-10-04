+++
aliases = ["/en/5/samples/rhinoscript/set-material-colors-from-object-colors/", "/en/6/samples/rhinoscript/set-material-colors-from-object-colors/", "/en/7/samples/rhinoscript/set-material-colors-from-object-colors/", "/wip/samples/rhinoscript/set-material-colors-from-object-colors/"]
authors = [ "dale" ]
categories = [ "Other" ]
description = "Demonstrates how to modify an object's material color to match its display color using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Set Material Colors from Object Colors"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/setrendercolor"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
Option Explicit

Sub SetMaterialColorsFromObjectColors

 ' Constants
 Const rhColorByLayer = 0
 Const rhColorByObject = 1

 ' Variables
 Dim aObjects, sObject
 Dim nColor, nSource
 Dim sLayer, nMaterial

 ' Get all objects in the document
 aObjects = Rhino.AllObjects
 If Not IsArray(aObjects) Then Exit Sub

 ' Process each object    
 For Each sObject In aObjects

   ' Get the object's color and color source
   nColor = Rhino.ObjectColor(sObject)
   nSource = Rhino.ObjectColorSource(sObject)
   nMaterial = -1

   ' If the object's color source is "by layer"
   ' then get the layer's material index. If the
   ' layer does not have a material, add one.    
   If (nSource = rhColorByLayer) Then
     sLayer = Rhino.ObjectLayer(sObject)
     nMaterial = Rhino.LayerMaterialIndex(sLayer)
     If( nMaterial < 0 ) Then
       nMaterial = Rhino.AddMaterialToLayer(sLayer)
     End If

   ' If the object's color source is "by object"
   ' then get the object's material index. If the
   ' object does not have a material, add one.    
   ElseIf (nSource = rhColorByObject) Then
     nMaterial = Rhino.ObjectMaterialIndex(sObject)
     If( nMaterial < 0 ) Then
       nMaterial = Rhino.AddMaterialToObject(sObject)
     End If

   End If

   ' Set the material color
   If (nMaterial >= 0) Then
     If (nColor <> Rhino.MaterialColor(nMaterial)) Then
       Rhino.MaterialColor nMaterial, nColor
     End If
   End If

 Next

 ' Redraw the document
 Rhino.Redraw

End Sub
```
