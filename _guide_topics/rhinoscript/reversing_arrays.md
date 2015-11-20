---
layout: toc-guide-page
title: Reversing Arrays
author: dale@mcneel.com
categories: ['Miscellaneous', 'Intermediate']
platforms: ['Windows']
apis: ['RhinoScript']
languages: ['VBScript']
keywords: ['script', 'Rhino', 'vbscript']
TODO: 0
origin: http://wiki.mcneel.com/developer/scriptsamples/reversearray
order: 1
---

# Reversing Arrays

This brief guide demonstrates how to reverse an array using RhinoScript.


## Problem

How does one quickly reverse the order of the elements in an array?


## Solution

Consider the following subroutine:

```vbnet
Sub ReverseArray(ByRef arr)

  Dim i, j, last, half, temp
  last = UBound(arr)
  half = Int(last/2)

  For i = 0 To half
    temp = arr(i)
    arr(i) = arr(last-i)
    arr(last-i) = temp
  Next

End Sub
```

...which can be used as follows:

```vbnet
Sub Main()

  Dim arr, i
  arr = Array(1,2,3)

  For i = 0 To UBound(arr)
    Rhino.Print arr(i)
  Next

  Call ReverseArray(arr)

  For i = 0 To UBound(arr)
    Rhino.Print arr(i)
  Next

End Sub
```
