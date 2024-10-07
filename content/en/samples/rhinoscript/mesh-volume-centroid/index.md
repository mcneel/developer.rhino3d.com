+++
aliases = ["/en/5/samples/rhinoscript/mesh-volume-centroid/", "/en/6/samples/rhinoscript/mesh-volume-centroid/", "/en/7/samples/rhinoscript/mesh-volume-centroid/", "/en/wip/samples/rhinoscript/mesh-volume-centroid/"]
authors = [ "dale" ]
categories = [ "Other" ]
description = "Demonstrates how to calculate the volume centroid of a mesh."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Mesh Volume Centroid"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/meshvolumecentroid"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0
+++

```vbnet
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' MeshVolumeCentroid.rvb -- July 2009
' Mary Fugier, Robert McNeel & Associates
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Option Explicit

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Calculates the volume centroid of a mesh object.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub MeshVolumeCentroid()

  Const RHINO_MESH = 32
  Dim strObject, arrCentroid

  strObject = Rhino.GetObject("Select mesh for volume centroid calculation", RHINO_MESH)
  If Not IsNull(strObject) Then
    arrCentroid = Rhino.MeshVolumeCentroid(strObject)
    If IsArray(arrCentroid) Then
      Call Rhino.AddPoint(arrCentroid)
      Call Rhino.Print("Volume Centroid = " & Rhino.Pt2Str(arrCentroid))
    End If
  End If

End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' If dragged and dropped on Rhino, a "MeshVolumeCentroid" alias
' will be created.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Rhino.AddStartupScript Rhino.LastLoadedScriptFile
Rhino.AddAlias "MeshVolumeCentroid", "_NoEcho _-RunScript (MeshVolumeCentroid)"
```
