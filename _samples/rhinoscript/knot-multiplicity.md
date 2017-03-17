---
title: Knot Multiplicity
description: Demonstrates how to determine curve and surface knot multiplicity using RhinoScript.
authors: ['Dale Fugier']
author_contacts: ['dale']
sdk: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Curves', 'Surfaces']
origin: http://wiki.mcneel.com/developer/scriptsamples/knotmultiplicity
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

```vbnet
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Description:
'   Calculates the multiplicity of a knot.
' Parameters:
'   knots - an array of knot values
'   knot_index - the index of the knot to determine multiplicity
' Returns:
'   The multiplicity if successful
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Function KnotMultiplicity(knots, knot_index)

  Dim knot_count, mult, index, t

  index = knot_index
  knot_count = UBound(knots)

  If (index < 0 Or index > knot_count) Then
    KnotMultiplicity = Null
    Exit Function
  End If

  t = knots(index)
  mult = 1

  Do While (index < knot_count)
    If (knots(index + 1) - t) > 1.0e-12 Then Exit Do
    index = index + 1
    mult = mult + 1
  Loop

  KnotMultiplicity = mult

End Function
```
