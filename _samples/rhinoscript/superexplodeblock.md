---
layout: code-sample-rhinoscript
title: Exploding Block Instances
author: dale@mcneel.com
platforms: ['Windows']
apis: ['RhinoScript']
languages: ['VBScript']
keywords: ['rhinoscript', 'vbscript']
categories: ['Uncategorized']
description: Demonstrates how to explode an instance of a block using RhinoScript.
origin: http://wiki.mcneel.com/developer/scriptsamples/superexplodeblock
order: 1
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
