+++
authors = [ "dale" ]
categories = [ "Miscellaneous", "Intermediate" ]
description = "This brief guide demonstrates how to reverse an array using RhinoScript."
keywords = [ "script", "Rhino", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Reversing Arrays"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/reversearray"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

 
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
