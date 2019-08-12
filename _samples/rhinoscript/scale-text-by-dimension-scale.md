---
title: Scale Text by Dimension Scale
description: Demonstrates how to properly scale text objects by the document's dimension scale in RhinoScript.
authors: ['dale_fugier']
sdk: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/scriptsamples/dimscaletext
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

```vbnet
Option Explicit

' Scales all text objects by the document's dimension scale
Sub DimScaleText

  ' Dim local variables
  Dim arrObjects, strObject, arrPlane, dblScale

  ' Get document's dimension scale  
  dblScale = Rhino.DimScale
  If dblScale = 1.0 Then
    Rhino.Print "Dimension scale set to 1.0."
    Exit Sub
  End If

  ' Get ids of all annotation objects    
  arrObjects = Rhino.ObjectsByType(512)
  If Not IsArray(arrObjects) Then
    Rhino.Print "No text objects to scale."
    Exit Sub
  End If

  ' Turn off viewport redrawing (faster)    
  Rhino.EnableRedraw False

  ' Save current view's construction plane
  arrPlane = Rhino.ViewCPlane(Rhino.CurrentView)

  ' Process each object
  For Each strObject In arrObjects

    ' Verify object is a text object
    If Rhino.IsText(strObject) And Rhino.IsObjectSelectable(strObject) Then

      ' Set the current view's construction plane to plane
      ' that defines the position and orientatio of the text
      Rhino.ViewCPlane Rhino.CurrentView, Rhino.TextObjectPlane(strObject)

      ' Select the object
      Rhino.SelectObject strObject

      ' Scale the object by the dimension scale
      Rhino.Command "_-Scale 0,0,0 " & CStr(dblScale), False

      ' Unselect the object
      Rhino.UnselectObject strObject

    End If
  Next

  ' Restore current view's construction plane
  Rhino.ViewCPlane Rhino.CurrentView, arrPlane

  ' Turn on viewport drawing
  Rhino.EnableRedraw True

End Sub
```
