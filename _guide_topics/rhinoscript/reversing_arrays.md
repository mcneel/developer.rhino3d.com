---
title: Reversing Arrays
description: This brief guide demonstrates how to reverse an array using RhinoScript.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Miscellaneous', 'Intermediate']
origin: http://wiki.mcneel.com/developer/scriptsamples/reversearray
order: 1
keywords: ['script', 'Rhino', 'vbscript']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

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
