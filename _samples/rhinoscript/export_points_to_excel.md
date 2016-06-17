---
title: Export Points to Excel
description: Illustrates RhinoScript code that exports Rhino point coordinates to Microsoft Excel.
author: dale@mcneel.com
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/scriptsamples/exportpointstoexcel
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

```vbnet
Sub ExportPointsToExcel()

  Const rhPoint = 1

  Dim arrPoints
  arrPoints = Rhino.GetObjects("Select points to export", rhPoint, True, True)
  If Not IsArray(arrPoints) Then Exit Sub

  Dim objXL
  Set objXL = CreateObject("Excel.Application")

  objXL.Visible = True

  objXL.WorkBooks.Add

  objXL.Columns(1).ColumnWidth = 20
  objXL.Columns(2).ColumnWidth = 20
  objXL.Columns(3).ColumnWidth = 20

  objXL.Cells(1, 1).Value = "X"
  objXL.Cells(1, 2).Value = "Y"
  objXL.Cells(1, 3).Value = "Z"

  objXL.Range("A1:C1").Select
  objXL.Selection.Font.Bold = True
  objXL.Selection.Interior.ColorIndex = 1
  objXL.Selection.Interior.Pattern = 1 'xlSolid
  objXL.Selection.Font.ColorIndex = 2

  objXL.Columns("B:B").Select
  objXL.Selection.HorizontalAlignment = &hFFFFEFDD ' xlLeft

  Dim intIndex
  intIndex = 2

  Dim strPoint, arrPt
  For Each strPoint In arrPoints
    arrPt = Rhino.PointCoordinates(strPoint)
    objXL.Cells(intIndex, 1).Value = arrPt(0)
    objXL.Cells(intIndex, 2).Value = arrPt(1)
    objXL.Cells(intIndex, 3).Value = arrPt(2)
    intIndex = intIndex + 1
  Next

  objXL.UserControl = True

 End Sub
```
