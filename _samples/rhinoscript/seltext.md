---
layout: code-sample-rhinoscript
title: Select Text Objects
author: dale@mcneel.com
platforms: ['Windows']
apis: ['RhinoScript']
languages: ['VBScript']
keywords: ['rhinoscript', 'vbscript']
categories: ['Uncategorized']
description: Demonstrates how to use RhinoScript to select all text objects.
TODO: 0
origin: http://wiki.mcneel.com/developer/scriptsamples/seltext
order: 1
---

```vbnet
Sub SelText
  Dim arrObjects, strObject
  arrObjects = Rhino.AllObjects
  If IsArray(arrObjects) Then
    For Each strObject In arrObjects
      If Rhino.IsText(strObject) Then
        Rhino.SelectObject strObject
      End If
    Next
  End If
End Sub
```
