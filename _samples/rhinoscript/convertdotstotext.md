---
layout: code-sample-rhinoscript
title: Convert Annotation Dots to Text
author: dale@mcneel.com
platforms: ['Windows']
apis: ['RhinoScript']
languages: ['VBScript']
keywords: ['rhinoscript', 'vbscript']
categories: ['Uncategorized']
description: Illustrates RhinoScript code that converts annotation dots to text object.
origin: http://wiki.mcneel.com/developer/scriptsamples/convertdotstotext
order: 1
---

```vbnet
Sub ConvertDotsToText
  Dim arrDots, strDot
  arrDots = Rhino.GetObjects("Select dots", 0, True, True )
  If Not IsArray(arrDots) Then Exit Sub

  Dim arrPt, strText
  For Each strDot In arrDots
    If Rhino.IsTextDot(strDot) Then
      strText = Rhino.TextDotText(strDot)
      arrPt = Rhino.TextDotPoint(strDot)
      Rhino.AddText strText, arrPt
      Rhino.DeleteObject strDot
    End If
  Next
End Sub
```
