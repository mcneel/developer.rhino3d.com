+++
aliases = ["/5/samples/rhinoscript/knot-multiplicity/", "/6/samples/rhinoscript/knot-multiplicity/", "/7/samples/rhinoscript/knot-multiplicity/", "/wip/samples/rhinoscript/knot-multiplicity/"]
authors = [ "dale" ]
categories = [ "Curves", "Surfaces" ]
description = "Demonstrates how to determine curve and surface knot multiplicity using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Knot Multiplicity"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/knotmultiplicity"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

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
