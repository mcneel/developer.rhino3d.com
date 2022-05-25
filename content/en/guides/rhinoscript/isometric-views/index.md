+++
authors = [ "dale" ]
categories = [ "Miscellaneous", "Advanced" ]
description = "This guide demonstrates how to create isometric views using RhinoScript."
keywords = [ "script", "Rhino", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Isometric Views"
type = "guides"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/isometric"
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

 
## Overview

AutoCAD has a VPOINT command that allows you to create isometric views of the model.  The VPOINT command uses the point entered by the user to create a vector that defines the direction from which the drawing is viewed.  You can do this in Rhino using the ViewportProperties command.  In the ViewportProperties dialog, first set the view to parallel projection.  Then, set the target location to 0,0,0 and the camera location to where you want to be viewing from.

If this seems too cumbersome, then you can also use the following RhinoScript subroutine...

## Example

The following example subroutine mimics the VPOINT command using RhinoScript...

```vbnet
Sub VPoint

  Dim strView
  strView = Rhino.CurrentView
  If Rhino.ViewProjection(strView) = 2 Then
    Rhino.Print "Viewport must be set for parallel projection."
    Exit Sub
  End If

  Dim arrOptions
  arrOptions = Array("NE Isometric", "NW Isometric", "SE Isometric", "SW Isometric", "User Defined")

  Dim strOption
  strOption = Rhino.ListBox(arrOptions, "Select viewing direction", "VPoint")
  If IsNull(strOption) Then Exit Sub

  Dim arrCamera
  Select Case strOption
    Case "NE Isometric" arrCamera = Array( 1, 1,1)
    Case "NW Isometric" arrCamera = Array(-1, 1,1)
    Case "SE Isometric" arrCamera = Array( 1,-1,1)
    Case "SW Isometric" arrCamera = Array(-1,-1,1)
    Case Else arrCamera = Rhino.GetPoint("View point")
  End Select

  If Not IsArray(arrCamera) Then Exit Sub

  Dim arrTarget, v
  arrTarget = Array(0,0,0)
  v = Rhino.VectorCreate(arrCamera, arrTarget)
  If Rhino.IsVectorTiny(v) Then Exit Sub

  Rhino.EnableRedraw False    
  Rhino.ViewCameraTarget strView, arrCamera, arrTarget
  Rhino.ZoomExtents strView
  Rhino.EnableRedraw True

End Sub
```
