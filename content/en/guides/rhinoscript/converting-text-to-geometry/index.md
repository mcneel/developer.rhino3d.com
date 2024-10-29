+++
aliases = ["/en/5/guides/rhinoscript/converting-text-to-geometry/", "/en/6/guides/rhinoscript/converting-text-to-geometry/", "/en/7/guides/rhinoscript/converting-text-to-geometry/", "/en/wip/guides/rhinoscript/converting-text-to-geometry/"]
authors = [ "dale" ]
categories = [ "Miscellaneous", "Advanced" ]
description = "This guide demonstrates how to convert text to curves using RhinoScript."
keywords = [ "script", "Rhino", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Converting Text to Geometry"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/converttexttogeometry"
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

You have many text elements that you would like to convert to text objects (geometry) for engraving.  You can explode a text element and get curves that outline the text.  The problem is, when you change a text element to a single stroke font, it automatically closes each letter/number and is unreadable.  The only way you have been able to make a single stroke font work is by creating geometry using Rhino's TextObject command.  However, because you have so many text elements it would take forever to remake geometry for each of them.  It is possible to write a script to automate this.

## Solution

The following script demonstrates how to convert text elements to text objects (geometry).  In this sample, text objects (geometry) are created with the identical properties, such as font, height, bold, and italics, as the text element.  

```vbnet
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' ConvertTextToGeometry.rvb -- September 2008
' If this code works, it was written by Dale Fugier.
' If not, I don't know who wrote it.
' Works with Rhino 4.0.

Option Explicit

Sub ConvertTextToGeometry

  ' Declare local variables
  Dim obj_list, obj, saved_plane, cmd
  Dim font, height, plane, style, text, bold, italic

  ' Select annotation objects
  obj_list = Rhino.GetObjects("Select text to convert to geometry", 512, True, True)
  If Not IsArray(obj_list) Then Exit Sub

  ' For speed, turn of screen redrawing
  Call Rhino.EnableRedraw(False)

  ' Save the current construction plane
  saved_plane = Rhino.ViewCPlane()

  ' Process each selected object
  For Each obj In obj_list

    ' Weed out just the text objects
    If Rhino.IsText(obj) Then

      ' Acquire the text parameters
      font = Rhino.TextObjectFont(obj)
      height = Rhino.TextObjectHeight(obj)
      plane = Rhino.TextObjectPlane(obj)
      style = Rhino.TextObjectStyle(obj)
      text = Rhino.TextObjectText(obj)

      If (style And 1) Then
        bold = "_Yes"
      Else
        bold = "_No"
      End If

      If (style And 2) Then
        italic = "_Yes"
      Else
        italic = "_No"
      End If

      ' Set the current construction plane
      Call Rhino.ViewCPlane(, plane)

      ' Add a new text object (geometry)
      cmd = "_-TextObject "
      cmd = cmd & "_GroupOutput=_Yes "
      cmd = cmd & "_FontName=" & font & " "
      cmd = cmd & "_Italic=" & italic & " "
      cmd = cmd & "_Bold=" & bold & " "
      cmd = cmd & "_Height=" & CStr(height) & " "
      cmd = cmd & "_Output=_Curves "
      cmd = cmd & "_AllowOpenCurves=_Yes "
      cmd = cmd & Chr(34) & text & Chr(34) & " "
      cmd = cmd & "0"
      Call Rhino.Command(cmd, 0)

      ' Delete the original object
      Call Rhino.DeleteObject(obj)

    End If
  Next

  ' Restore the saved construction plane      
  Call Rhino.ViewCPlane(, saved_plane)

  ' Enable screen redrawing
  Call Rhino.EnableRedraw(True)

End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Rhino.AddStartupScript Rhino.LastLoadedScriptFile
Rhino.AddAlias "ConvertTextToGeometry", "_NoEcho _-RunScript (ConvertTextToGeometry)"
```

If you want to override the font to use a single stroke font, simply modify this line:

```vbnet
 font = Rhino.TextObjectFont(obj)
```

and replace it with something more like this:

```vbnet
 font = "<single_stroke_font_name>"
```
