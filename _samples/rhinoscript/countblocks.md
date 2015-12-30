---
layout: code-sample-rhinoscript
title: Count Block Instances
author: dale@mcneel.com
platforms: ['Windows']
apis: ['RhinoScript']
languages: ['VBScript']
keywords: ['rhinoscript', 'vbscript']
categories: ['Uncategorized']
description: Demonstrates how to count block instances using RhinoScript.
origin: http://wiki.mcneel.com/developer/scriptsamples/countblocks
order: 1
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
