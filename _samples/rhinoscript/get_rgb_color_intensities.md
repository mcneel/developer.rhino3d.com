---
title: Get RGB Color Intensities
description: Demonstrates retrieve red, green, and blue color intensities using VBScript.
author: dale@mcneel.com
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/scriptsamples/color
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

```vbnet
''' ---------------------------------------------------------------------------
''' Function:   GetRValue
''' Purpose:    Returns the Red value from an RGB color value
''' Arguments:  vbLong - An RGB color value
''' Returns:    vbLong - A Red color value, -1 on error
''' ---------------------------------------------------------------------------
Function GetRValue(val)
  If val > -1 And val < 16777216 Then
    GetRValue = val \ 256 ^ 0 And 255
  Else
    GetRValue = -1
  End If
End Function

''' ---------------------------------------------------------------------------
''' Function:   GetGValue
''' Purpose:    Returns the Green value from an RGB color value
''' Arguments:  vbLong - an RGB color value
''' Returns:    vbLong - a Green color value, -1 on error
''' ---------------------------------------------------------------------------
Function GetGValue(val)
  If val > -1 And val < 16777216 Then
    GetGValue = val \ 256 ^ 1 And 255
  Else
    GetGValue = -1
  End If
End Function

''' ---------------------------------------------------------------------------
''' Function:   GetBValue
''' Purpose:    Returns the Blue value from an RGB color value
''' Arguments:  vbLong - an RGB color value
''' Returns:    vbLong - a Blue color value, -1 on error
''' ---------------------------------------------------------------------------
Function GetBValue(val)
  If val > -1 And val < 16777216 Then
    GetBValue = val \ 256 ^ 2 And 255
  Else
    GetBValue = -1
  End If
End Function
```
