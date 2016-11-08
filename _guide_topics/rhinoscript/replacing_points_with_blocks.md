---
title: Replacing Points with Blocks
description: This guide demonstrates how to replace point objects with block objects using RhinoScript.
author: ['Dale Fugier', '@dale']
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Miscellaneous', 'Advanced']
origin: http://wiki.mcneel.com/developer/scriptsamples/replacepointswithblocks
order: 1
keywords: ['script', 'Rhino', 'vbscript']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## Problem

Imagine you have a number of point objects in your model and you would like to replace them with a block so they appear as markers.  How can this be done without running the Insert command a bunch of times?

## Solution

The following sample code demonstrates how to replace point objects with block objects using RhinoScript...

```vbnet
' Replaces points with blocks
Sub ReplacePointsWithBlocks

  ' Select points to replace with a block
  Dim arrObjects
  arrObjects = Rhino.GetObjects("Select points to replace with a block", 1, True, True)
  If Not IsArray(arrObjects) Then Exit Sub

  ' Get the names of all block definitions in the document    
  Dim arrBlocks
  arrBlocks = Rhino.BlockNames(True)
  If Not IsArray(arrBlocks) Then
    Rhino.Print "No block definitions found in the document."
    Exit Sub
  End If

  ' Select a block name from a list
  Dim strBlock
  strBlock = Rhino.ListBox(arrBlocks, "Select block", "Replace Points")
  If IsNull(strBlock) Then Exit Sub

  ' Turn off redrawing (faster)
  Rhino.EnableRedraw True      

  ' Process each selected point object
  Dim strObject, arrPoint
  For Each strObject In arrObjects
    ' Get the point object's coordinates
    arrPoint = Rhino.PointCoordinates(strObject)
    ' Insert the block at that location
    Rhino.InsertBlock strBlock, arrPoint
  Next

  ' Delete all of the point objects
  Rhino.DeleteObjects arrObjects   

  ' Turn redrawing back on     
  Rhino.EnableRedraw True      

End Sub
```

## Inverse

The following script will do just the opposite - it will replace block objects with point objects...

```vbnet
' Replaces blocks with points
Sub ReplaceBlocksWithPoints

  ' Select blocks to replace with points
  Dim arrObjects
  arrObjects = Rhino.GetObjects("Select blocks to replace with points", 4096, True, True)
  If Not IsArray(arrObjects) Then Exit Sub

  ' Turn off redrawing (faster)
  Rhino.EnableRedraw True      

  ' Process each selected block object
  Dim strObject, arrPoint
  For Each strObject In arrObjects
    ' Get the block's insertion point
    arrPoint = Rhino.BlockInstanceInsertPoint(strObject)
    ' Add a point object at that location
    Rhino.AddPoint arrPoint
  Next

  ' Delete all of the block objects
  Rhino.DeleteObjects arrObjects   

  ' Turn redrawing back on     
  Rhino.EnableRedraw True      

End Sub
```
