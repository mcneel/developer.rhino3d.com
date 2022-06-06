+++
aliases = ["/5/samples/rhinoscript/is-dynamic-array-dimensioned/", "/6/samples/rhinoscript/is-dynamic-array-dimensioned/", "/7/samples/rhinoscript/is-dynamic-array-dimensioned/", "/wip/samples/rhinoscript/is-dynamic-array-dimensioned/"]
authors = [ "dale" ]
categories = [ "Other" ]
description = "Demonstrates how to determine of a dynamic array has been dimensioned."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Is Dynamic Array Dimensioned"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/isupperbound"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

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
