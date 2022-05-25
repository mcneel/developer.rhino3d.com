+++
authors = [ "dale" ]
categories = [ "Other" ]
description = "How to read point files that describe airfoils and create interpolated curves using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Airfoil Shapes"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/airfoil"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
Option Explicit

' Subroutine to import "Selig" formatted airfoil shapes
Sub ImportAirfoil

  ' Local constants
  Const ForReading = 1

  ' Local variables
  Dim objFSO, objFile
  Dim strFileName, strAirfoil, strLine, strCurve
  Dim arrPt, arrPoints(), nCount

  ' Prompt for an airfoil data file
  strFileName = Rhino.OpenFileName("Open", "Airfoil Data File (*.dat)|*.dat|")
  If IsNull(strFileName) Then Exit Sub

  ' Create a file system object
  Set objFSO = CreateObject("Scripting.FileSystemObject")

  ' Open the data file for reading
  On Error Resume Next
  Set objFile = objFSO.OpenTextFile(strFileName, ForReading)
  If Err Then
    MsgBox Err.Description
    Exit Sub
  End If  

  ' Read the name of the airfoil
  strAirfoil = objFile.ReadLine

  ' Read through the file looking for point coordinates
  nCount = 0
  Do While objFile.AtEndOfStream <> True
    strLine = objFile.ReadLine
    ' Convert the string to a point
    arrPt = PointFromString(strLine)
    If IsArray(arrPt) Then
      ReDim Preserve arrPoints(nCount)
      arrPoints(nCount) = arrPt
      nCount = nCount + 1
    End If
  Loop

  ' Close the curve
  ReDim Preserve arrPoints(nCount)
  arrPoints(nCount) = arrPoints(0)

  ' Add the named interpolated curve
  If IsArray(arrPoints) Then
    strCurve = Rhino.AddInterpCurveEx(arrPoints)
    Rhino.ObjectName strCurve, strAirfoil
  End If

  ' Close the file and release objects
  objFile.Close
  Set objFile = Nothing
  Set objFSO = Nothing

End Sub

' Function to generate a point from a string
Function PointFromString( strLine )
  Dim arrTokens, arrPoint, x, y
  PointFromString = Null
  If VarType(strLine) = vbString Then
    strLine = Trim(strLine)
    arrTokens = Rhino.StrTok(strLine, " ")
    If IsArray(arrTokens) And UBound(arrTokens) = 1 Then
      x = CDbl(arrTokens(0))
      y = CDbl(arrTokens(1))
      arrPoint = Array(x, y, 0.0)
      PointFromString = arrPoint
    End If
  End If
End Function
```
