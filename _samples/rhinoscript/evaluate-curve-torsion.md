---
title: Evaluate Curve Torsion
description: Demonstrates how to evaluate the torsion of a curve in RhinoScript.
authors: ['dale_fugier']
author_contacts: ['dale']
sdk: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Curves']
origin: http://wiki.mcneel.com/developer/scriptsamples/torsion
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

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
