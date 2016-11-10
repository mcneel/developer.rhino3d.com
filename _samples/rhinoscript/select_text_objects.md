---
title: Select Text Objects
description: Demonstrates how to use RhinoScript to select all text objects.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Picking and Selection']
origin: http://wiki.mcneel.com/developer/scriptsamples/seltext
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
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
