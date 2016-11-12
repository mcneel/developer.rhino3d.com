---
title: Convert Dots to Text
description: Illustrates RhinoScript code that converts annotation dots to text object.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Adding Objects']
origin: http://wiki.mcneel.com/developer/scriptsamples/convertdotstotext
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
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
