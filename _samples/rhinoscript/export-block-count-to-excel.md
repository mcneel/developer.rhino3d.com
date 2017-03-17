---
title: Export Block Count to Excel
description: Demonstrates how to count blocks and then export the results to Microsoft Excel.
authors: ['Dale Fugier']
author_contacts: ['dale']
sdk: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Blocks']
origin: http://wiki.mcneel.com/developer/scriptsamples/exportblockcount
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

```vbnet
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' ExportBlockCount.rvb -- May 2010
' If this code works, it was written by Dale Fugier.
' If not, I don't know who wrote it.
' Works with Rhino 4.0.

Option Explicit

Sub ExportBlockCount()

  Dim arrBlocks, strBlock, strName
  Dim objCounts, objKey
  Dim objExcel, objBook, objSheet, nCell

  ' Get all of the block instances in the document
  arrBlocks = Rhino.ObjectsByType(4096)
  If IsNull(arrBlocks) Then
    Call Rhino.Print("No blocks to export.")
    Exit Sub
  End If

  ' Create a dictionary object for counting blocks
  Set objCounts = CreateObject("Scripting.Dictionary")

  ' Count the blocks
  For Each strBlock In arrBlocks
    strName = Rhino.BlockInstanceName(strBlock)
    If objCounts.Exists(strName) Then
      objCounts(strName) = objCounts(strName) + 1
    Else
      Call objCounts.Add(strName, 1)
    End If
  Next

  ' Create a Excel object
  Set objExcel = CreateObject("Excel.Application")
  objExcel.Visible = True

  ' Initialize Excel
  Set objBook = objExcel.Workbooks.Add
  Set objSheet = objBook.Worksheets(1)

  ' Place titles on sheet
  nCell = 1
  objExcel.Cells(nCell, 1).Value = "Block Name"
  objExcel.Cells(nCell, 2).Value = "Count"
  nCell = nCell + 1

  ' Write the blocks and counts to the sheet
  Call Rhino.Print("Block counts:")
  For Each objKey In objCounts
    objExcel.Cells(nCell, 1).Value = CStr(objKey)
    objExcel.Cells(nCell, 2).Value = CStr(objCounts(objKey))
    ' Print to command line too
    Call Rhino.Print("  " & CStr(objKey) & " = " & CStr(objCounts(objKey)))
   nCell = nCell + 1
  Next

End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Drag & drop and alias creation stuff
Rhino.AddStartUpScript Rhino.LastLoadedScriptFile
Rhino.AddAlias "ExportBlockCount", "_-RunScript (ExportBlockCount)"
```
