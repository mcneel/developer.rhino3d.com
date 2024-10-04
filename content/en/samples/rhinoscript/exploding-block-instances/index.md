+++
aliases = ["/en/5/samples/rhinoscript/exploding-block-instances/", "/en/6/samples/rhinoscript/exploding-block-instances/", "/en/7/samples/rhinoscript/exploding-block-instances/", "/wip/samples/rhinoscript/exploding-block-instances/"]
authors = [ "dale" ]
categories = [ "Blocks" ]
description = "Demonstrates how to explode an instance of a block using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Exploding Block Instances"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/superexplodeblock"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

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
