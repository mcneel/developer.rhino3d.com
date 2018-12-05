---
title: Exploding Block Instances
description: Demonstrates how to explode an instance of a block using RhinoScript.
authors: ['dale_fugier']
sdk: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Blocks']
origin: http://wiki.mcneel.com/developer/scriptsamples/superexplodeblock
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

```vbnet
Sub SuperExplodeBlock
  Const rhInstanceObject = 4096
  Dim arrBlocks, strBlock
  arrBlocks = Rhino.ObjectsByType(rhInstanceObject)
  If IsArray(arrBlocks) Then
    For Each strBlock In arrBlocks
      If Rhino.IsObjectSelectable(strBlock) Then
        DoInstanceExplosion strBlock
      End If
    Next
  End If
End Sub

Sub DoBlockExplosion(strBlock)
  Dim arrObjects, strObject
  If Rhino.IsBlockInstance(strBlock) Then
    arrObjects = Rhino.ExplodeBlockInstance(strBlock)
    If IsArray(arrObjects) Then
      For Each strObject In arrObjects
        DoBlockExplosion strObject '*RECURSE*
      Next
    End If
  End If
End Sub
```
