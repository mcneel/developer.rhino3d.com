+++
aliases = ["/5/samples/rhinoscript/convert-dots-to-text/", "/6/samples/rhinoscript/convert-dots-to-text/", "/7/samples/rhinoscript/convert-dots-to-text/", "/wip/samples/rhinoscript/convert-dots-to-text/"]
authors = [ "dale" ]
categories = [ "Adding Objects" ]
description = "Illustrates RhinoScript code that converts annotation dots to text object."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Convert Dots to Text"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/convertdotstotext"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
Sub ConvertDotsToText
  Dim arrDots, strDot
  arrDots = Rhino.GetObjects("Select dots", 0, True, True )
  If Not IsArray(arrDots) Then Exit Sub

  Dim arrPt, strText
  For Each strDot In arrDots
    If Rhino.IsTextDot(strDot) Then
      strText = Rhino.TextDotText(strDot)
      arrPt = Rhino.TextDotPoint(strDot)
      Rhino.AddText strText, arrPt
      Rhino.DeleteObject strDot
    End If
  Next
End Sub
```
