---
layout: code-sample-rhinoscript
title: Select Named Objects from a List
author: dale@mcneel.com
platforms: ['Windows']
apis: ['RhinoScript']
languages: ['VBScript']
keywords: ['rhinoscript', 'vbscript']
categories: ['Uncategorized']
description: Demonstrates how to use a dialog box to select named objects using RhinoScript.
TODO: 0
origin: http://wiki.mcneel.com/developer/scriptsamples/selnamedobject
order: 1
---

```vbnet
Option Explicit

Sub SelNamedObjects

  ' Get all the objects in the document
  Dim arrAll
  arrAll = Rhino.AllObjects
  If Not IsArray(arrAll) Then
    Rhino.Print "No objects added to selection."
    Exit Sub
  End If

  ' Find all of the object names    
  Dim arrNames(), strName, nBound, i
  nBound = 0
  For i = 0 To UBound(arrAll)
    strName = Rhino.ObjectName(arrAll(i))
    If Not IsNull(strName) Then
      ReDim Preserve arrNames(nBound)
      arrNames(nBound) = strName
      nBound = nBound + 1
    End If
  Next

  ' Exit if no names found
  If nBound = 0 Then
    Rhino.Print "No objects added to selection."
    Exit Sub
  End If

  ' Cull the duplicate names    
  Dim arrCulled
  arrCulled = Rhino.CullDuplicateStrings(arrNames)  

  ' Sort the list alphabetically  
  Dim arrSorted
  arrSorted = Rhino.Sort(arrCulled) 'Error =>SortStrings

  ' Select one or more objects names from a list    
  Dim arrSelected
  arrSelected = Rhino.MultiListBox(arrSorted, "Object names to select", "Select Named Objects")
  If Not IsArray(arrSelected) Then Exit Sub

  ' Select, and count, the objects
  Dim arrObjs, nCount
  nCount = 0
  For i = 0 To UBound(arrSelected)    
    arrObjs = Rhino.ObjectsByName(arrSelected(i), True)
    If IsArray(arrObjs) Then
      nCount = nCount + UBound(arrObjs) + 1
    End If
  Next

  'Print report to commandline
  If nCount = 0 Then
    Rhino.Print "No objects added to selection."
  ElseIf nCount = 1 Then
    Rhino.Print "1 object added to selection."
  Else
    Rhino.Print CStr(nCount) & " objects added to selection."
  End If

End Sub
```
