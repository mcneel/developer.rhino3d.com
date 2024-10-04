+++
aliases = ["/en/5/samples/rhinoscript/extract-isocurve-intersection-points/", "/en/6/samples/rhinoscript/extract-isocurve-intersection-points/", "/en/7/samples/rhinoscript/extract-isocurve-intersection-points/", "/wip/samples/rhinoscript/extract-isocurve-intersection-points/"]
authors = [ "dale" ]
categories = [ "Curves" ]
description = "Demonstrates how to get the intersection points of a surface's isocurves using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Extract Isocurve Intersection Points"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/extractuvintersectpts"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' ExtractUVIntersectPts.rvb -- November 2008
' If this code works, it was written by Dale Fugier.
' If not, I don't know who wrote it.
' Works with Rhino 4.0.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Option Explicit

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'Extracts surface wireframe curves
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Function RhExtractWireframe(sSurface)

  Dim aResults
  RhExtractWireframe = Null

  Call Rhino.SelectObject(sSurface)

  Call Rhino.Command("_-ExtractWireframe", 0)
  aResults = Rhino.LastCreatedObjects
  If IsArray(aResults) Then
    RhExtractWireframe = aResults
    Rhino.UnselectObjects(aResults)
  End If

  Call Rhino.UnselectObject(sSurface)

End Function

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'Intersects curves
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Function RhIntersect(aCurves)  

  Dim aResults, aPoints(), i
  RhIntersect = Null

  Call Rhino.SelectObjects(aCurves)  

  Call Rhino.Command("_-Intersect", 0)
  aResults = Rhino.LastCreatedObjects
  If IsArray(aResults) Then
    ReDim aPoints(UBound(aResults))
    For i = 0 To UBound(aResults)
      aPoints(i) = Rhino.PointCoordinates(aResults(i))
    Next
    Call Rhino.DeleteObjects(aResults)
    RhIntersect = aPoints
  End If

  Call Rhino.UnselectObjects(aCurves)

End Function  

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' The one and only ExtractUVIntersectPts subroutine    
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub ExtractUVIntersectPts

  Dim sSurface, aCurves, aPoints, aObjects

  sSurface = Rhino.GetObject("Select surface", 24, True)
  If IsNull(sSurface) Then Exit Sub

  Call Rhino.EnableRedraw(False)
  aCurves = RhExtractWireframe(sSurface)
  If IsArray(aCurves) Then
    aPoints = RhIntersect(aCurves)
    Call Rhino.DeleteObjects(aCurves)
    If IsArray(aPoints) Then
      aObjects = Rhino.AddPoints(Rhino.CullDuplicatePoints(aPoints))
      Call Rhino.SelectObjects(aObjects)
    End If
  End If
  Call Rhino.EnableRedraw(True)

End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Rhino.AddStartupScript Rhino.LastLoadedScriptFile
Rhino.AddAlias "ExtractUVIntersectPts", "_NoEcho _-RunScript (ExtractUVIntersectPts)"
```
