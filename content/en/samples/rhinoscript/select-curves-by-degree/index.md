+++
aliases = ["/en/5/samples/rhinoscript/select-curves-by-degree/", "/en/6/samples/rhinoscript/select-curves-by-degree/", "/en/7/samples/rhinoscript/select-curves-by-degree/", "/wip/samples/rhinoscript/select-curves-by-degree/"]
authors = [ "dale" ]
categories = [ "Picking and Selection", "Curves" ]
description = "Demonstrates how to use RhinoScript to select all curves that are of a specified degree."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Select Curves by Degree"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/selcrvdegree"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' SelCrvDegree.rvb -- September 2011
' If this code works, it was written by Dale Fugier.
' If not, I don't know who wrote it.
' Works with Rhino 4.0.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Option Explicit

' Declare global variable
Public g__nDegree

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Selects curves of a user-specified degree
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Sub SelCrvDegree

  ' Declare local constants
  Const RH_CURVE = 4
  Const RH_MAX_DEGREE = 11
  Const RH_DEF_DEGREE = 3

  ' Declare local variables
  Dim nDegree, arrCurves, strCurve, nCount

  ' Make sure global variable is initialized
  If IsEmpty(g__nDegree) Or IsNull(g__nDegree) Then g__nDegree = RH_DEF_DEGREE
  nDegree = g__nDegree

  ' Get all curve objects
  Call Rhino.EnableRedraw(False)    
  arrCurves = Rhino.ObjectsByType(RH_CURVE)
  If IsNull(arrCurves) Then
    Call Rhino.Print("No curves to select.")
    Exit Sub
  End If

  ' Prompt for curve degree
  nDegree = Rhino.GetInteger("Degree of curves to select", nDegree, 1, RH_MAX_DEGREE)
  If IsNull(nDegree) Then Exit Sub

  ' Select curves of specified degree
  Call Rhino.EnableRedraw(False)
  nCount = 0
  For Each strCurve In arrCurves
    If nDegree = Rhino.CurveDegree(strCurve) Then
      If Not Rhino.IsObjectSelected(strCurve) Then
        Call Rhino.SelectObject(strCurve)
        nCount = nCount + 1
      End If        
    End If
  Next
  Call Rhino.EnableRedraw(True)

  ' Print results
  If 0 = nCount Then
    Call Rhino.Print("No degree=" & CStr(nDegree) & " curves added to selection.")
  ElseIf 1 = nCount Then
    Call Rhino.Print("1 degree=" & CStr(nDegree) & " curve added to selection.")
  Else
    Call Rhino.Print(CStr(nCount) & " degree=" & CStr(nDegree) & " curves added to selection.")
  End If  

  ' Remember curve degree
  g__nDegree = nDegree

End Sub

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Drag & drop support
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Rhino.AddStartUpScript Rhino.LastLoadedScriptFile
Rhino.AddAlias "SelCrvDegree", "_-RunScript (SelCrvDegree)"
```
