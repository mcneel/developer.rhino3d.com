+++
aliases = ["/en/5/samples/rhinoscript/select-text-by-height/", "/en/6/samples/rhinoscript/select-text-by-height/", "/en/7/samples/rhinoscript/select-text-by-height/", "/wip/samples/rhinoscript/select-text-by-height/"]
authors = [ "dale" ]
categories = [ "Picking and Selection" ]
description = "Demonstrates how to select text objects by their text height using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Select Text by Height"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/seltextheight"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' SelTextHeight.rvb -- July 2009
' If this code works, it was written by Dale Fugier.
' If not, I don't know who wrote it.
' Works with Rhino 4.0 and 5.0
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Option Explicit

' Global variables
Public g_min_height
Public g_max_height

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Selects text objects based on their text height
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub SelTextHeight()

  ' Local variables
  Dim min_height, max_height
  Dim objects, obj, height, sel_count

  ' Initialize global variables, if necessary
  If IsEmpty(g_min_height) Or IsNull(g_min_height) Then g_min_height = 1.0
  If IsEmpty(g_max_height) Or IsNull(g_max_height) Then g_max_height = 1.0

  ' Prompt for minimum height
  min_height = Rhino.GetReal("Minimum text height", g_min_height, 0.0)
  If IsNull(min_height) Then Exit Sub

  ' Prompt for maximum height
  max_height = Rhino.GetReal("Maximum text height", g_max_height, min_height)
  If IsNull(min_height) Then Exit Sub
  If (min_height > max_height) Then Exit Sub

  ' More initialization
  g_min_height = min_height
  g_max_height = max_height
  sel_count = 0

  Rhino.EnableRedraw False

  ' Find text objects that meet our criteria      
  objects = Rhino.ObjectsByType(512) 'annotations
  For Each obj In objects
    If Rhino.IsText(obj) Then
      height = Rhino.TextObjectHeight(obj)
      If (g_min_height <= height) And (height <= g_max_height) Then
        If Rhino.SelectObject(obj) Then sel_count = sel_count + 1
      End If    
    End If
  Next

  Rhino.EnableRedraw True

  Rhino.Print CStr(sel_count) & " text added to selection."

End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Rhino.AddStartupScript Rhino.LastLoadedScriptFile
Rhino.AddAlias "SelTextHeight", "_NoEcho _-RunScript (SelTextHeight)"
```
