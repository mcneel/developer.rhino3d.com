---
title: Offsetting Meshes
description: This guide demonstrates how to offset and solidify a mesh using RhinoScript.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Miscellaneous', 'Advanced']
origin: http://wiki.mcneel.com/developer/scriptsamples/offsetmeshsolidify
order: 1
keywords: ['script', 'Rhino', 'vbscript']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## Problem

RhinoScript can generate a closed mesh as a result of a base mesh and an offset.  Rhino's *OffsetMesh* command does this task very well if you use the solidify option, but RhinoScript's `MeshOffset` function does not have this option.  Let's take a look at creating a solid mesh with RhinoScript...

## Solution

RhinoScript's `MeshOffset` function does not have a solidify option, but you can accomplish what you want by simply scripting Rhino's *OffsetMesh* command, instead of calling RhinoScript's `MeshOffset` function.

The following example function will offset a mesh by scripting Rhino's OffsetMesh command...

```vbnet
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Offset and solidify a mesh object
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Function OffsetMeshSolidify(strMesh, dblDistance)

  ' Declare local variables
  Dim arrSaved, strCommand

  ' Save any selected objects
  arrSaved = Rhino.SelectedObjects

  ' Unselect all objects
  Rhino.UnSelectAllObjects

  ' Select the mesh
  Call Rhino.SelectObject(strMesh)

  ' Script the OffsetMesh command
  strCommand = "_-OffsetMesh _CapMeshes=_Yes " & CStr(dblDistance) & " _Enter"
  Call Rhino.Command(strCommand, 0)

  ' Get the results of the command
  If Rhino.LastCommandResult = 0 Then
    OffsetMeshSolidify = Rhino.LastCreatedObjects()(0)
  Else
    OffsetMeshSolidify = Null
  End If

  ' Unselect all objects
  Rhino.UnSelectAllObjects

  ' If any objects were selected before calling
  ' this function, re-select them
  If IsArray(arrSaved) Then Rhino.SelectObjects(arrSaved)

End Function
```

You can test the above function with the following code...

```vbnet
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' This procedure tests the OffsetMeshSolidify function
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub TestOffsetMeshSolidify()

  ' Declare local constants and variables
  Const rhMesh = 32
  Dim strMesh, dblDistance, strOffset

  ' Select a mesh to offset
  strMesh = Rhino.GetObject("Select mesh to offset", rhMesh, True)
  If IsNull(strMesh) Then Exit Sub

  ' Get the offset distance
  dblDistance = Rhino.GetReal("Offset distance", 1.0)
  If IsNull(dblDistance) Then Exit Sub
  If (dblDistance = 0.0) Then Exit Sub

  ' Call our mesh offsetting function...
  strOffset = OffsetMeshSolidify(strMesh, dblDistance)

End Sub
```
