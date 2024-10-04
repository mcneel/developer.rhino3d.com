+++
aliases = ["/en/5/samples/rhinoscript/revolve-profile-curves/", "/en/6/samples/rhinoscript/revolve-profile-curves/", "/en/7/samples/rhinoscript/revolve-profile-curves/", "/wip/samples/rhinoscript/revolve-profile-curves/"]
authors = [ "dale" ]
categories = [ "Adding Objects", "Surfaces" ]
description = "Demonstrates how to create a surface by revolving one or more profile curves using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Revolve Profile Curves"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/revolve"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

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
