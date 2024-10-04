+++
aliases = ["/en/5/guides/rhinoscript/replacing-points-with-blocks/", "/en/6/guides/rhinoscript/replacing-points-with-blocks/", "/en/7/guides/rhinoscript/replacing-points-with-blocks/", "/wip/guides/rhinoscript/replacing-points-with-blocks/"]
authors = [ "dale" ]
categories = [ "Miscellaneous", "Advanced" ]
description = "This guide demonstrates how to replace point objects with block objects using RhinoScript."
keywords = [ "script", "Rhino", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Replacing Points with Blocks"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/replacepointswithblocks"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

 
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
