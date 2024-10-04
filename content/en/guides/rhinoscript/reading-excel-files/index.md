+++
aliases = ["/en/5/guides/rhinoscript/reading-excel-files/", "/en/6/guides/rhinoscript/reading-excel-files/", "/en/7/guides/rhinoscript/reading-excel-files/", "/wip/guides/rhinoscript/reading-excel-files/"]
authors = [ "dale" ]
categories = [ "Miscellaneous", "Advanced" ]
description = "This brief guide demonstrates how to read a Microsoft Excel file from RhinoScript."
keywords = [ "script", "Rhino", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Reading Excel Files"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/readexcelfile"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

 
## Problem

You would like to read a Microsoft Excel file from RhinoScript into an array that can be accessed in Rhino.

## Solution

The following general purpose function will read an Excel worksheet into a two-dimensional array...

```vbnet
' Description:
'   Reads a Microsoft Excel file.
' Parameters:
'   strFile - [in] The name of the Excel file to read.
' Returns:
'   A two-dimension array of cell values, if successful.
'   Null on error
Option Explicit

Function ReadExcelFile(ByVal strFile)

  ' Local variable declarations
  Dim objExcel, objSheet, objCells
  Dim nUsedRows, nUsedCols, nTop, nLeft, nRow, nCol
  Dim arrSheet()

  ' Default return value
  ReadExcelFile = Null

  ' Create the Excel object
  On Error Resume Next
  Set objExcel = CreateObject("Excel.Application")
  If (Err.Number <> 0) Then
    Exit Function
  End If

  ' Don't display any alert messages
  objExcel.DisplayAlerts = 0  

  ' Open the document as read-only
  On Error Resume Next
  Call objExcel.Workbooks.Open(strFile, False, True)
  If (Err.Number <> 0) Then
    Exit Function
  End If

  ' If you wanted to read all sheets, you could call
  ' objExcel.Worksheets.Count to get the number of sheets
  ' and the loop through each one. But in this example, we
  ' will just read the first sheet.
  Set objSheet = objExcel.ActiveWorkbook.Worksheets(1)

  ' Get the number of used rows
  nUsedRows = objSheet.UsedRange.Rows.Count

  ' Get the number of used columns
  nUsedCols = objSheet.UsedRange.Columns.Count

  ' Get the topmost row that has data
  nTop = objSheet.UsedRange.Row

  ' Get leftmost column that has data
  nLeft = objSheet.UsedRange.Column

  ' Get the used cells
  Set objCells = objSheet.Cells

  ' Dimension the sheet array
  ReDim arrSheet(nUsedRows - 1, nUsedCols - 1)

  ' Loop through each row
  For nRow = 0 To (nUsedRows - 1)
    ' Loop through each column
    For nCol = 0 To (nUsedCols - 1)
  ' Add the cell value to the sheet array
  arrSheet(nRow, nCol) = objCells(nRow + nTop, nCol + nLeft).Value
    Next
  Next

  ' Close the workbook without saving
  Call objExcel.ActiveWorkbook.Close(False)

  ' Quit Excel
  objExcel.Application.Quit

  ' Return the sheet data to the caller
  ReadExcelFile = arrSheet

End Function
```

You can use this function to dump the contents of a spreadsheet to Rhino's command line:

```vbnet
Sub ExcelDumper()

  ' Local variable declarations
  Dim strFile, arrSheet, i, j, varCell, strFormat

  ' Prompt for the Excel file to read  
  strFile = Rhino.OpenFileName("Open", "Excel Files (*.xls)|*.xls|")
  If IsNull(strFile) Then Exit Sub

  ' Read the Excel file
  arrSheet = ReadExcelFile(strFile)
  If IsNull(arrSheet) Then Exit Sub

  ' Dump the worksheet to the command line
  For i = 0 To UBound(arrSheet, 1)
    For j = 0 To UBound(arrSheet, 2)
      strFormat = "Sheet(" & CStr(i) & "," & CStr(j) & ") = "      
      varCell = arrSheet(i, j)
      If IsEmpty(varCell) Then
        Rhino.Print strFormat & "<empty>"
      Else
        Rhino.Print strFormat & CStr(varCell)
      End If      
    Next
  Next

End Sub
```
