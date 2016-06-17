---
title: Count Objects
description: Demonstrates how to count all the different object types using RhinoScript.
author: dale@mcneel.com
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/scriptsamples/countobjects
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

```vbnet
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' RhinoCountObjects.rvb -- December 2007
' If this code works, it was written by Dale Fugier.
' If not, I don't know who wrote it.
' Works with Rhino 4.0.

Option Explicit

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Counts all objects
Sub CountAllObjects
  Dim objects, obj
  objects = Rhino.AllObjects(False,True)
  If IsArray(objects) Then
    Call DoCounting(objects, True)
  Else
    Rhino.Print "No objects to count."
  End If
End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Counts selected objects
Sub CountSelectedObjects
  Dim objects
  objects = Rhino.GetObjects("Select objects to count", 0, True, True)
  If IsArray(objects) Then
    Call DoCounting(objects, False)
  End If
End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Do the counting
Sub DoCounting(objects, bTotal)

  If Not IsArray(objects) Then Exit Sub

  ' Declare constants
  Const rhPoint      = 1
  Const rhPointCloud = 2
  Const rhCurve      = 4
  Const rhSurface    = 8
  Const rhPolysrf    = 16
  Const rhMesh       = 32
  Const rhLight      = 256
  Const rhAnnotation = 512
  Const rhBlock      = 4096
  Const rhTextDot    = 8192
  Const rhGrip       = 16384
  Const rhDetail     = 32768
  Const rhHatch      = 65536
  Const rhMorph      = 131072
  Const rhCage       = 134217728
  Const rhPhantom    = 268435456
  Const rhClip       = 536870912

  ' Declare variables
  Dim points      : points      = 0
  Dim pointclouds : pointclouds = 0
  Dim curves      : curves      = 0
  Dim surfaces    : surfaces    = 0
  Dim polysrfs    : polysrfs    = 0
  Dim meshes      : meshes      = 0
  Dim lights      : lights      = 0
  Dim annotations : annotations = 0
  Dim blocks      : blocks      = 0
  Dim textdots    : textdots    = 0
  Dim grips       : grips       = 0
  Dim details     : details     = 0
  Dim hatches     : hatches     = 0
  Dim morphs      : morphs      = 0
  Dim cages       : cages       = 0
  Dim phantoms    : phantoms    = 0
  Dim clips       : clips       = 0

  Dim obj

  ' Count them
  For Each obj In objects
    If Not Rhino.IsObjectReference(obj) Then
      Select Case Rhino.ObjectType(obj)
        Case rhPoint      points      = points      + 1
        Case rhPointCloud pointclouds = pointclouds + 1
        Case rhCurve      curves      = curves      + 1
        Case rhSurface    surfaces    = surfaces    + 1
        Case rhPolysrf    polysrfs    = polysrfs    + 1
        Case rhMesh       meshes      = meshes      + 1
        Case rhLight      lights      = lights      + 1
        Case rhAnnotation annotations = annotations + 1
        Case rhBlock      blocks      = blocks      + 1
        Case rhTextDot    textdots    = textdots    + 1
        Case rhGrip       grips       = grips       + 1
        Case rhDetail     details     = details     + 1
        Case rhHatch      hatches     = hatches     + 1
        Case rhMorph      morphs      = morphs      + 1
        Case rhCage       cages       = cages       + 1
        Case rhPhantom    phantoms    = phantoms    + 1
        Case rhClip       clips       = clips       + 1
      End Select
    End If
  Next

  ' Report them
  If (bTotal = True) Then
    Rhino.Print "Total object count = " & CStr(UBound(objects) + 1)
  Else
    Rhino.Print "Selected object count = " & CStr(UBound(objects) + 1)
  End If

  If (points > 0 )      Then Rhino.Print "  Points = " & CStr(points)
  If (pointclouds > 0 ) Then Rhino.Print "  Point clouds = " & CStr(pointclouds)
  If (curves > 0 )      Then Rhino.Print "  Curves = " & CStr(curves)
  If (surfaces > 0 )    Then Rhino.Print "  Surfaces = " & CStr(surfaces)
  If (polysrfs > 0 )    Then Rhino.Print "  PolySurfaces = " & CStr(polysrfs)
  If (meshes > 0 )      Then Rhino.Print "  Meshes = " & CStr(meshes)
  If (lights > 0 )      Then Rhino.Print "  Lights = " & CStr(lights)
  If (annotations > 0 ) Then Rhino.Print "  Annotations = " & CStr(annotations)
  If (blocks > 0 )      Then Rhino.Print "  Blocks instances = " & CStr(blocks)
  If (textdots > 0 )    Then Rhino.Print "  Text dots = " & CStr(textdots)
  If (grips > 0 )       Then Rhino.Print "  Grip objects = " & CStr(grips)
  If (details > 0 )     Then Rhino.Print "  Detailed views = " & CStr(details)
  If (hatches > 0 )     Then Rhino.Print "  Hatches = " & CStr(hatches)
  If (morphs > 0 )      Then Rhino.Print "  Morph objects = " & CStr(morphs)
  If (cages > 0 )       Then Rhino.Print "  Cage objects = " & CStr(cages)
  If (phantoms > 0 )    Then Rhino.Print "  Phantoms objects = " & CStr(phantoms)
  If (clips > 0 )       Then Rhino.Print "  Clipping planes = " & CStr(clips)

End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

' Add this script to the list of scripts to load at startup    
Rhino.AddStartupScript Rhino.LastLoadedScriptFile

' Define command aliases    
Rhino.AddAlias "CountAllObjects", "_-RunScript (CountAllObjects)"  
Rhino.AddAlias "CountSelectedObjects", "_-RunScript (CountSelectedObjects)"
```
