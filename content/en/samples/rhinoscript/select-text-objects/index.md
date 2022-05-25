+++
authors = [ "dale" ]
categories = [ "Picking and Selection" ]
description = "Demonstrates how to use RhinoScript to select all text objects."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Select Text Objects"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/seltext"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
Sub SelText
  Dim arrObjects, strObject
  arrObjects = Rhino.AllObjects
  If IsArray(arrObjects) Then
    For Each strObject In arrObjects
      If Rhino.IsText(strObject) Then
        Rhino.SelectObject strObject
      End If
    Next
  End If
End Sub
```
