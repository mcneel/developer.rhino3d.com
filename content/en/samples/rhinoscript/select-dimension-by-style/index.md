+++
aliases = ["/en/5/samples/rhinoscript/select-dimension-by-style/", "/en/6/samples/rhinoscript/select-dimension-by-style/", "/en/7/samples/rhinoscript/select-dimension-by-style/", "/wip/samples/rhinoscript/select-dimension-by-style/"]
authors = [ "dale" ]
categories = [ "Picking and Selection" ]
description = "Demonstrates how to select an objects (dimensions) by their dimension style using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Select Dimensions by Style"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/seldimstyle"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
Sub SelDimStyle

  ' Declare local constants and variables
  Const rhAnnotation = 512
  Dim strStyle, arrObjects, strObject

  ' Prompt the user to enter the name of the dimension style
  strStyle = Rhino.GetString("Dimension style to select", Rhino.CurrentDimStyle)
  If IsNull(strStyle) Then Exit Sub
  If Not Rhino.IsDimStyle(strStyle) Then Exit Sub

  ' Create an array of all annotation objects
  arrObjects = Rhino.ObjectsByType(rhAnnotation)
  If Not IsArray(arrObjects) Then Exit Sub

  Rhino.EnableRedraw False

  ' Process each annotation object
  For Each strObject In arrObjects
    If Rhino.IsDimension(strObject) Then
      If StrComp(Rhino.DimensionStyle(strObject), strStyle, 1) = 0 Then
        Rhino.SelectObject strObject
      End If
    End If
  Next

  Rhino.EnableRedraw True

End Sub
```

This one allows selection of a dimension style from a list...

```vbnet
Sub SelDimStyleList

' Declare local constants and variables
Const rhAnnotation = 512
Dim strStyle, arrObjects, strObject, arrStyles

'get the existing styles
arrStyles = Rhino.DimStyleNames ()

' Prompt the user to select the name of the dimension style
strStyle = Rhino.ListBox(arrStyles, "Dimension style to select", "Dimension styles")
If IsNull(strStyle) Then Exit Sub
If Not Rhino.IsDimStyle(strStyle) Then Exit Sub

' Create an array of all annotation objects
arrObjects = Rhino.ObjectsByType(rhAnnotation)
If Not IsArray(arrObjects) Then Exit Sub

Rhino.EnableRedraw False

' Process each annotation object
For Each strObject In arrObjects
  If Rhino.IsDimension(strObject) Then
    If StrComp(Rhino.DimensionStyle(strObject), strStyle, 1) = 0 Then
      Rhino.SelectObject strObject
    End If
End If
Next

Rhino.EnableRedraw True

End Sub
```

This one selects dimensions matching the styles of selected dimensions...

```vbnet
Sub SelDimStyleMatch

' Declare local constants and variables
Const rhAnnotation = 512
Dim sStyle, aDims, sDim, strObject, aStyles(),aStyles1, aSel, sSel, i

' Create an array of all annotation objects
aDims = Rhino.ObjectsByType(rhAnnotation)
If Not IsArray(aDims) Then Exit Sub

'Get the selected dimensions to match
aSel = Rhino.GetObjects("Select dimensions",rhAnnotation,True,True,True,aDims)

'create an array of the selcted dimension styles
If isarray(aSel) Then
 For Each sSel In  aSel
   ReDim Preserve aStyles(i)
   aStyles(i) =  Rhino.DimensionStyle(sSel)    
   i = i + 1
 Next
Else Exit Sub
End If

'cull duplicate styles from the array
aStyles1 = Rhino.CullDuplicateStrings(aStyles)

Rhino.EnableRedraw False

' Process each annotation object with each selected dim stlye

For Each sDim In aDims
 For Each sStyle In aStyles1
   If StrComp(Rhino.DimensionStyle(sDim), sStyle, 1) = 0 Then
     Rhino.SelectObject sDim
   End If
 Next
Next

Rhino.EnableRedraw True

End Sub
```
