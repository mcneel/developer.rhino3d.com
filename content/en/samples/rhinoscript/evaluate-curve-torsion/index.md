+++
aliases = ["/en/5/samples/rhinoscript/evaluate-curve-torsion/", "/en/6/samples/rhinoscript/evaluate-curve-torsion/", "/en/7/samples/rhinoscript/evaluate-curve-torsion/", "/en/wip/samples/rhinoscript/evaluate-curve-torsion/"]
authors = [ "dale" ]
categories = [ "Curves" ]
description = "Demonstrates how to evaluate the torsion of a curve in RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Evaluate Curve Torsion"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/torsion"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0
+++

```vbnet
'''
''' Description
'''   Evaluate the torsion of a curve.
''' Parameters
'''   crv - a string that identifies the curve to evaluate
'''   t   - a parameter of the curve within its domain
''' Returns
'''   The torsion if successful.
'''   Null if the torsion is undefined at the parameter.
'''
Function EvaluateTorsion(crv, t)

  ' Local variables
  Dim data, d1xd2, numer, denom

  ' Default return value
  EvaluateTorsion = Null

  ' Calculate the torsion
  data = Rhino.CurveEvaluate(crv, t, 3)
  If IsArray(data) And UBound(data) = 3 Then
    d1xd2 = Rhino.VectorCrossProduct(data(1), data(2))
    numer = Rhino.VectorDotProduct(d1xd2, data(3))
    denom = Rhino.VectorDotProduct(d1xd2, d1xd2)
    If denom > 0 Then
      EvaluateTorsion = numer / denom
    End If
  End If

End Function
```
