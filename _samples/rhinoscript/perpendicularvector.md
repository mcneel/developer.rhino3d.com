---
title: Perpendicular Vectors
description: Demonstrates how to calculate a vector that is perpendicular to another vector using RhinoScript.
author: dale@mcneel.com
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Uncategorized']
origin: http://wiki.mcneel.com/developer/scriptsamples/perpendicularvector
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

```vbnet
' Description:
'   Returns a 3-D vector that is perpendicular to another 3-D vector.
' Parameters:
'   v - the 3-D vector to evaluate.
' Returns:
'   A perpendicular 3-D vector if successful, Null otherwise.
' Remarks:
'   The result is not a unitized 3-D vector.
'       

Function GetPerpendicularVector( v )

  GetPerpendicularVector = Null
  If Not IsArray(v) Or UBound(v) <> 2 Then Exit Function
  If Rhino.IsVectorZero(v) Then Exit Function

  Dim i, j, k
  Dim a, b
  k = 2
  If Abs(v(1)) > Abs(v(0)) Then
    If Abs(v(2)) > Abs(v(1)) Then
      ' |v(2)| > |v(1)| > |v(0)|
      i = 2
      j = 1
      k = 0
      a = v(2)
      b = -v(1)
    ElseIf Abs(v(2)) >= Abs(v(0)) Then
      ' |v(1)| >= |v(2)| >= |v(0)|
      i = 1
      j = 2
      k = 0
      a = v(1)
      b = -v(2)
    Else
      ' |v(1)| > |v(0)| > |v(2)|
      i = 1
      j = 0
      k = 2
      a = v(1)
      b = -v(0)
    End If
  ElseIf Abs(v(2)) > Abs(v(0)) Then
    ' |v(2)| > |v(0)| >= |v(1)|
    i = 2
    j = 0
    k = 1
    a = v(2)
    b = -v(0)
   ElseIf Abs(v(2)) > Abs(v(1)) Then
    ' |v(0)| >= |v(2)| > |v(1)|
    i = 0
    j = 2
    k = 1
    a = v(0)
    b = -v(2)
  Else
    ' |v(0)| >= |v(1)| >= |v(2)|
    i = 0
    j = 1
    k = 2
    a = v(0)
    b = -v(1)
  End If

  Dim rc(2)
  rc(i) = b
  rc(j) = a
  rc(k) = 0.0
  GetPerpendicularVector = rc

End Function
```
