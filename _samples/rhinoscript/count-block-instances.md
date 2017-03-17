---
title: Count Block Instances
description: Demonstrates how to count block instances using RhinoScript.
authors: ['Dale Fugier']
author_contacts: ['dale']
sdk: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Blocks']
origin: http://wiki.mcneel.com/developer/scriptsamples/countblocks
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

```vbnet
Sub CountAllInstancesOfAllBlocks
  arrNames = Rhino.BlockNames(True)
  If IsArray(arrNames) Then
    For Each strName In arrNames
      Rhino.Print strName & " = " & CStr(Rhino.BlockInstanceCount(strName))
    Next
  End If
End Sub
```
