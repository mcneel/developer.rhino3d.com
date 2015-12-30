---
layout: code-sample-rhinoscript
title: Auto Label Objects
author: dale@mcneel.com
platforms: ['Windows']
apis: ['RhinoScript']
languages: ['VBScript']
keywords: ['rhinoscript', 'vbscript']
categories: ['Uncategorized']
description: Demonstrates how to automatically label objects using RhinoScript.
origin: http://wiki.mcneel.com/developer/scriptsamples/autolabel
order: 1
---

```vbnet
Option Explicit

'
' AutoLabel Subroutine
'
Sub AutoLabel
   ' Declare variables
   Dim arrDirPoint1, arrDirPoint2, arrSortDir, arrObjects, arrPoint, arrItem, arrArea, arrPrompts, arrCollect()
   Dim strObject, strName, strDot
   Dim intCount, intSuffix, intXDir, intYDir, intZDir
   Dim i, j, temp

   ' Select objects      
   arrObjects = Rhino.GetObjects("Select objects to name")
   If Not IsArray(arrObjects) Then Exit Sub

   ' Prompt for a prefix to add to the labels
   strName = Rhino.GetString("Prefix for labels, press Enter for none")
   If Not IsString(strName) Then Exit Sub

   ' Prompt for a suffix starting number
   intSuffix = Rhino.GetInteger("Starting base number to increment",0)
   If IsNull(intSuffix) Then Exit Sub

   ' Prompt for direction
   arrDirPoint1 = Rhino.GetPoint("Base point for sort direction")
   If IsNull (arrDirPoint1) Then Exit Sub
   arrDirPoint2 = Rhino.GetPoint("Pick point for sort direction", arrDirPoint1)
   If IsNull (arrDirPoint2) Then Exit Sub

   ' Determine Direction of sort for each axis, 0 is Negative Direction, 1 is positive
   If arrDirPoint1(0) > arrDirPoint2(0) Then
     intXDir = 0
   Else
     intXDir = 1
   End If
   If arrDirPoint1(1) > arrDirPoint2(1) Then
     intYDir = 0
   Else
     intYDir = 1
   End If
   If arrDirPoint1(2) > arrDirPoint2(2) Then
     intZDir = 0
   Else
     intZDir = 1
   End If
   arrSortDir = Array(intXDir, intYDir, intZDir)

  ' Initialize collection counter
   intCount = 0

   ' Process each seleted object
   For Each strObject In arrObjects

     ' Process curves
     If Rhino.IsCurve(strObject) Then
       ' Get the curve starting point
       arrPoint = Rhino.CurveStartPoint(strObject)
       ' Append the object name to the point array
       ReDim Preserve arrPoint(3)
       arrPoint(3) = strObject

       ' Append the modified point array to the collection     
       ReDim Preserve arrCollect(intCount)
       arrCollect(intCount) = arrPoint

       ' Increment collection counter
       intCount = intCount + 1
     End If

     ' Process surfaces
     If Rhino.IsSurface(strObject) Then
       ' Get the Surface center point
       arrArea = Rhino.SurfaceAreaCentroid (strObject)
       arrPoint = arrArea(0)
       ' Append the object name to the point array
       ReDim Preserve arrPoint(3)
       arrPoint(3) = strObject

       ' Append the modified point array to the collection     
       ReDim Preserve arrCollect(intCount)
       arrCollect(intCount) = arrPoint

       ' Increment collection counter
       intCount = intCount + 1
     End If

     ' Process points
     If Rhino.IsPoint(strObject) Then
       ' Get the Point Corrdinates point
       arrPoint = Rhino.PointCoordinates (strObject)
       ' Append the object name to the point array
       ReDim Preserve arrPoint(3)
       arrPoint(3) = strObject

       ' Append the modified point array to the collection     
       ReDim Preserve arrCollect(intCount)
       arrCollect(intCount) = arrPoint

       ' Increment collection counter
       intCount = intCount + 1
     End If

     '
     ' TODO: add support for additional object types here
     '

   Next

   ' Validate the collection
   If Not IsUpperBound(arrCollect) Then Exit Sub

  ' Bubble sort the collection
   For i = UBound(arrCollect) - 1 To 0 Step -1
     For j = 0 To i
       If CompareItems(arrCollect(j), arrCollect(j+1), arrSortDir) = True Then
         temp = arrCollect(j+1)
         arrCollect(j+1) = arrCollect(j)
         arrCollect(j) = temp
       End If
     Next
   Next

   ' Process each item in the collection
   For i = 0 To UBound(arrCollect)
     ' Get an item from the collection
     arrItem = arrCollect(i)
     ' Rebuild the point array
     arrPoint = Array(arrItem(0), arrItem(1), arrItem(2))
   'Curves need to have the textdot at thier Midpoint
    If Rhino.IsCurve(arrItem(3)) Then
     arrPoint = Rhino.CurveMidPoint(arrItem(3))
    End If
    ' Add a text dot at the point location
    strDot = Rhino.AddTextDot(strName & CStr(intSuffix + i), arrPoint)
    ' Set the dot name to the originating object
    Rhino.ObjectName strDot, arrItem(3)
    Rhino.ObjectName arrItem(3), strName & CStr(intSuffix +i)
    Rhino.SetObjectData arrItem(3), "AutoCount", "DotUiid", strDot
   Next
End Sub

'
' Compare function for bubble sort
'
Function CompareItems(x, y, dir)
   If x(0) > y(0) Then
     If dir(0) = 1 Then
       CompareItems = True
     Else
       CompareItems = False
     End If
   ElseIf x(0) = y(0) Then
     If x(1) > y(1) Then
       If dir(1) = 1 Then
         CompareItems = True
       Else
         CompareItems = False
       End If
     ElseIf x(1) = y(1) And x(2) >= y(2) Then
       If dir(2) = 1 Then
        CompareItems = True
       Else
         CompareItems = False
       End If
     Else
       If dir(1) = 1 Then
         CompareItems = False
       Else
         CompareItems = True
       End If
     End If
   Else
     If dir(0) = 1 Then
       CompareItems = False
     Else
       CompareItems = True
     End If
   End If
End Function

'
' Returns a Boolean value indicating whether an
' expression can be evaluated as a string
'
Function IsString(ByVal str)
  IsString = False
  If VarType(str) = vbString Then IsString = True
End Function  

'
' Returns a Boolean value indicating whether an
' array has been dimensioned.
'
Function IsUpperBound(ByVal arr)
   IsUpperBound = False
   If IsArray(arr) Then
     On Error Resume Next
     UBound arr
     If Err.Number = 0 Then IsUpperBound = True
   End If
End Function  
```
