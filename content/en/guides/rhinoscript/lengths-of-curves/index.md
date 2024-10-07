+++
aliases = ["/en/5/guides/rhinoscript/lengths-of-curves/", "/en/6/guides/rhinoscript/lengths-of-curves/", "/en/7/guides/rhinoscript/lengths-of-curves/", "/en/wip/guides/rhinoscript/lengths-of-curves/"]
authors = [ "dale" ]
categories = [ "Miscellaneous", "Intermediate" ]
description = "This guide demonstrates how to calculate the lengths of curve objects using RhinoScript."
keywords = [ "script", "Rhino", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Lengths of Curves"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/curvelength"
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

Imagine you wish to list of lengths for a selected series of curves.  The Length command gives a composite length and the list command does not give the curve lengths.  You can work around these limitations with a RhinoScript.

## Solution

The following RhinoScript code demonstrates how to do the above...

```vbnet
Option Explicit

Sub CurveLength ()
  Dim arrCurves, dblTotal, dblLength, i
  dblTotal = 0.0
  arrCurves = Rhino.GetObjects("Select curves for length calculation", 4, True, True)
  If IsArray(arrCurves) Then
    For i = 0 To UBound(arrCurves)
      dblLength = Rhino.CurveLength(arrCurves(i))
      Rhino.Print("Curve" & CStr(i) & " = " & CStr(dblLength))
      dblTotal = dblTotal + dblLength
    Next
    Rhino.Print "Total length: " & " = " & CStr(dblTotal)
  End If
End Sub
```
