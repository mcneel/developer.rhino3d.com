+++
aliases = ["/en/5/samples/rhinoscript/render-named-views/", "/en/6/samples/rhinoscript/render-named-views/", "/en/7/samples/rhinoscript/render-named-views/", "/wip/samples/rhinoscript/render-named-views/"]
authors = [ "dale" ]
categories = [ "Viewports and Views" ]
description = "Demonstrates how to render named views using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Render Named Views"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/rendernamedviews"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
Option Explicit

' Renders one or more named views to a user-defined folder
Sub RenderNamedViews

  ' Let the user pick the named view to render
  Dim render_views
  render_views = GetRenderViews
  If Not IsArray(render_views) Then Exit Sub

  ' Let the user pick the folder to save the renderings  
  Dim folder  
  folder = Rhino.BrowseForFolder(Rhino.DocumentPath, "Browse for folder", "Batch Render")
  If IsNull(folder) Then Exit Sub

  ' Save the active view
  Dim saved_view_name
  saved_view_name = Rhino.CurrentView
  Rhino.Command "_-NamedView _Save $$_save_$$ _Enter", 0

  ' Process each named view
  Dim view
  For Each view In render_views
    If IsStandardView(view) Then
      ' If the named view is a standard view
      Rhino.Command "_-SetView _World _" & view, 0
    Else
      ' If the named view is not a standard view
      Rhino.Command "_-NamedView _Restore " & view & " _Enter", 0
    End If
    ' Render the scene with the current render engine
    Rhino.Command "_-Render"
    ' Save the render to a jpg file
    Rhino.Command "_-SaveRenderWindowAs " & GetRenderFileName(folder, view, "jpg")
    ' Close the render window
    Rhino.Command "_-CloseRenderWindow"    
  Next

  ' Restore the active view
  Rhino.Command "_-NamedView _Restore $$_save_$$ _Enter", 0
  Rhino.RenameView Rhino.CurrentView, saved_view_name

  ' Delete the temporary named view
  Rhino.Command "_-NamedView _Delete $$_save_$$ _Enter", 0

End Sub

' Returns an array of view names to render
Function GetRenderViews()
  GetRenderViews = vbNull  
  Dim all_views, selected_views
  all_views = GetAllViews
  selected_views = Rhino.MultiListBox(all_views, "Select views to render.", "Batch Render")
  If IsArray(selected_views) Then
    GetRenderViews = selected_views
  End If
End Function

' Returns a render-formatted file name
Function GetRenderFileName(folder, view, ext)
  Dim doc, file, temp
  doc = Rhino.DocumentName
  temp = "_" & view & "." & ext
  file = LCase(Replace(doc, ".3dm", temp, 1, -1, 1))
  GetRenderFileName = Chr(34) & folder & file & Chr(34)
End Function

' Returns an array of both standard and named view names
Function GetAllViews()
  Dim all_views, std_views, named_views
  std_views = GetStandardViews
  named_views = Rhino.NamedViews
  If IsArray(named_views) Then
    all_views = Rhino.JoinArrays(std_views, named_views)
    all_views = Rhino.CullDuplicateStrings(all_views)
    GetAllViews = Rhino.SortStrings(all_views)
  Else
    GetAllViews = std_views
  End If
End Function

' Returns an array of standard view names
Function GetStandardViews()
  GetStandardViews = Array("Back", "Bottom", "Front", "Left", "Perspective", "Right", "Top")
End Function

' Verifies a string is a standard view name
Function IsStandardView(str)
  IsStandardView = vbFalse
  Dim std_views, i
  std_views = GetStandardViews
  For i = 0 To UBound(std_views)
    If StrComp(std_views(i), str, 1) = 0 Then
      IsStandardView = vbTrue
      Exit For
    End If
  Next
End Function
```
