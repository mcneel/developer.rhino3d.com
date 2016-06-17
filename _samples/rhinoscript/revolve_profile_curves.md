---
title: Revolve Profile Curves
description: Demonstrates how to create a surface by revolving one or more profile curves using RhinoScript.
author: dale@mcneel.com
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Adding Objects', 'Surfaces']
origin: http://wiki.mcneel.com/developer/scriptsamples/revolve
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

```vbnet
Option Explicit

Sub MyRevolve

  ' Declare local variables
  Dim obj_list, crv_list, crv, axis0, axis1

  ' Select one or more curves to revolve
  obj_list = Rhino.GetObjects("Select curves to revolve", 4, True, True)
  If IsNull(obj_list) Then Exit Sub

  ' Pick start of revolve axis    
  axis0 = Rhino.GetPoint("Start of revolve axis")
  If IsNull(axis0) Then Exit Sub

  ' Pick end of revolve axis    
  axis1 = Rhino.GetPoint("End of revolve axis", axis0)
  If IsNull(axis1) Then Exit Sub

  ' If more than one curve as picked, try to join them
  If (UBound(obj_list) > 0) Then
    crv_list = Rhino.JoinCurves(obj_list, False)
  Else
    crv_list = Array(obj_list(0))
  End If

  ' Create the surfaces of revolution  
  For Each crv In crv_list
    Call Rhino.AddRevSrf(crv, Array(axis0, axis1))
  Next

  ' Delete the temporary joined curves
  Call Rhino.DeleteObjects(crv_list)

End Sub
```
