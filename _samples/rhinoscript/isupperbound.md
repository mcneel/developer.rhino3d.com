---
layout: code-sample-rhinoscript
title: Determine if a Dynamic Array has been Dimensioned
author: dale@mcneel.com
platforms: ['Windows']
apis: ['RhinoScript']
languages: ['VBScript']
keywords: ['rhinoscript', 'vbscript']
categories: ['Uncategorized']
description: Demonstrates how to determine of a dynamic array has been dimensioned.
origin: http://wiki.mcneel.com/developer/scriptsamples/isupperbound
order: 1
---

```vbnet
' Returns a Boolean value indicating whether an
' array has been dimensioned - determine
' whether or not the array has an upper bound.
'
Function IsUpperBound(ByVal arr)
  IsUpperBound = False
  If IsArray(arr) Then
    On Error Resume Next
    UBound arr
    If Err.Number = 0 Then IsUpperBound = True
  End If
End Function
```
