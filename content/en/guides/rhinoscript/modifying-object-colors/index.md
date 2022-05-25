+++
authors = [ "dale" ]
categories = [ "Miscellaneous", "Intermediate" ]
description = "This guide demonstrates how to modify the color of objects using RhinoScript."
keywords = [ "script", "Rhino", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Modifying Object Colors"
type = "guides"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/objectcolor"
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

Changing object colors using Rhino's properties command can be slow when assigning colors to lots of objects.  Imagine you would like to assign randomized colors across multiple objects or pick two colors and have Rhino generate all the blend colors.  All of this is possible with RhinoScript.

## Solution

All this is possible with the help of RhinoScript's `GetColor` and `ObjectColor` methods...

The following sample script contains the following subroutines:

- `SetObjectColor` - sets object colors.
- `SetObjectColorRandom` - sets random object colors.
- `SetObjectColorGraded` - sets gradient object colors based on the order picked.

```vbnet
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' ObjectColor.rvb -- February 2009
' If this code works, it was written by Dale Fugier.
' If not, I don't know who wrote it.
' Works with Rhino 4.0.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Option Explicit

Randomize

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Sets object colors  
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub SetObjectColor()

  Dim objects, color

  objects = Rhino.GetObjects("Select objects to change colors", 0, True, True)
  If IsNull(objects) Then Exit Sub

  color = Rhino.GetColor
  If IsNull(color) Then Exit Sub

  Rhino.ObjectColor objects, color

End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Set random object colors
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub SetObjectColorRandom()

  Dim objects, red, green, blue, i

  objects = Rhino.GetObjects("Select objects for randomly color change", 0, True, True)
  If IsNull(objects) Then Exit Sub

  Rhino.EnableRedraw False
  For i = 0 To UBound(objects)
    red = Int(255 * Rnd)
    green = Int(255 * Rnd)
    blue = Int(255 * Rnd)  
    Rhino.ObjectColor objects(i), RGB(red, green, blue)
  Next
  Rhino.EnableRedraw True

End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Sets gradient object colors (based on the order picked)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub SetObjectColorGraded()

  Dim objects, color0, color1, color, i, bound
  Dim red, red0, red1
  Dim green, green0, green1
  Dim blue, blue0, blue1, percent

  objects = Rhino.GetObjects("Select objects for gradient color change", 0, True, True)
  If IsNull(objects) Then Exit Sub

  color0 = Rhino.GetColor
  If IsNull(color0) Then Exit Sub

  color1 = Rhino.GetColor
  If IsNull(color1) Then Exit Sub

  ' Extract red-green-blue components
  red0 = color0 And &HFF
  red1 = color1 And &HFF
  green0 = (color0 \ &H100) And &HFF
  green1 = (color1 \ &H100) And &HFF
  blue0 = (color0 \ &H10000) And &HFF
  blue1 = (color1 \ &H10000) And &HFF
  bound = UBound(objects)

  Rhino.EnableRedraw False
  For i = 0 To bound
    ' A linearly interpreted gradient just calculates the new RGB values by applying a
    ' target value percent of the linear range to the each RGB component range.
    percent = i/bound
    red = red0 + Int(percent * (red1 - red0))
    green = green0 + Int(percent * (green1 - green0))
    blue = blue0 + Int(percent * (blue1 - blue0))    
    Rhino.ObjectColor objects(i), RGB(red, green, blue)
  Next
  Rhino.EnableRedraw True

End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Rhino.AddStartupScript Rhino.LastLoadedScriptFile
Rhino.AddAlias "SetObjectColor", "_NoEcho _-RunScript (SetObjectColor)"
Rhino.AddAlias "SetObjectColorRandom", "_NoEcho _-RunScript (SetObjectColorRandom)"
Rhino.AddAlias "SetObjectColorGraded", "_NoEcho _-RunScript (SetObjectColorGraded)"
```
