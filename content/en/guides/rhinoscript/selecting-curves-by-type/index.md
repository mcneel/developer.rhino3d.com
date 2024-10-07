+++
aliases = ["/en/5/guides/rhinoscript/selecting-curves-by-type/", "/en/6/guides/rhinoscript/selecting-curves-by-type/", "/en/7/guides/rhinoscript/selecting-curves-by-type/", "/en/wip/guides/rhinoscript/selecting-curves-by-type/"]
authors = [ "dale" ]
categories = [ "Miscellaneous", "Intermediate" ]
description = "This brief guide demonstrates how to select linear and non-linear curves using RhinoScript."
keywords = [ "script", "Rhino", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Selecting Curves by Type"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/selcurve"
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

 
## Non-Linear Curves

The following RhinoScript subroutine will select all non-linear curves in the document:

```vbnet
Sub SelNonLinearCrv()
  Dim arrCurves, strCurve
  arrCurves = Rhino.ObjectsByType(4)
  If IsArray(arrCurves) Then
    Rhino.EnableRedraw False
    For Each strCurve In arrCurves
      If Not Rhino.IsCurveLinear(strCurve) Then
        Rhino.SelectObject strCurve
      End If
    Next
    Rhino.EnableRedraw True
  End If
End Sub
```

## Linear Curves

The following RhinoScript subroutine will select all linear curves in the document:

```vbnet
Sub SelLinearCrv()
  Dim arrCurves, strCurve
  arrCurves = Rhino.ObjectsByType(4)
  If IsArray(arrCurves) Then
    Rhino.EnableRedraw False
    For Each strCurve In arrCurves
      If Rhino.IsCurveL
      inear(strCurve) Then
        Rhino.SelectObject strCurve
      End If
    Next
    Rhino.EnableRedraw True
  End If
End Sub
```
