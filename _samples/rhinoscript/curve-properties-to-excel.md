---
title: Curve Properties to Excel
description: Illustrates RhinoScript code that extracts curve properties into Excel.
authors: ['dale_fugier']
author_contacts: ['dale']
sdk: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Curves']
origin: http://wiki.mcneel.com/developer/scriptsamples/excelcurveproperties
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

```vbnet
Option Explicit

Sub ExtractProperties

  ' Declare variables
  Dim xlApp, xlBook, xlSheet  ' Declare variable to hold the reference.
  Dim strObject
  Dim arrObjects
  Dim intCount
  Dim arrStart, arrEnd

  'Set Default Values
  intCount = 0

  ' Select some objects      
  arrObjects = Rhino.GetObjects("Select objects for extraction",4)
  If Not IsArray(arrObjects) Then Exit Sub

  ' Open Excel object
  Set xlApp = CreateObject("excel.application")
   ' You may have to set Visible property to True
   ' if you want to see the application.
  xlApp.Visible = True
   ' Use xlApp to access Microsoft Excel's
   ' other objects.
   Set xlBook = xlApp.Workbooks.Add
   Set xlSheet = xlBook.Worksheets(1)

  'Place titles on sheet
      xlApp.Cells(1, 1).Value = "Name"
      xlApp.Cells(1, 2).Value = "Length"
      xlApp.Cells(1,3).Value = "StartX"
      xlApp.Cells(1,4).Value = "StartY"
      xlApp.Cells(1,5).Value = "StartZ"
      xlApp.Cells(1,6).Value = "EndX"
      xlApp.Cells(1,7).Value = "EndY"
      xlApp.Cells(1,8).Value = "EndZ"

  'Extract Properties of Curves
  For Each strObject In arrObjects
      'Curves Processed
    If Rhino.IsCurve(strObject) Then
     xlApp.Cells(intCount + 2, 1).Value = Rhino.ObjectName(strObject)
     xlApp.Cells(intCount + 2, 2).Value = Rhino.CurveLength(strObject)
     'Extract StartPoint
     arrStart = Rhino.CurveStartPoint(strObject)
     xlApp.Cells(intCount + 2, 3).Value = arrStart(0)
     xlApp.Cells(intCount + 2, 4).Value = arrStart(1)
     xlApp.Cells(intCount + 2, 5).Value = arrStart(2)
     'Extract EndPoint
     arrEnd = Rhino.CurveEndPoint(strObject)
     xlApp.Cells(intCount + 2, 6).Value = arrEnd(0)
     xlApp.Cells(intCount + 2, 7).Value = arrEnd(1)
     xlApp.Cells(intCount + 2, 8).Value = arrEnd(2)
    End If
    intCount = intCount + 1
  Next

'xlApp.Quit   ' When you finish, use the Quit method to close

 Set xlApp = Nothing   ' the application, then release the reference.

End Sub
```
