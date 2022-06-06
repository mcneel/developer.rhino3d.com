+++
aliases = ["/5/samples/rhinoscript/untag-object-as-a-flamingo-plant/", "/6/samples/rhinoscript/untag-object-as-a-flamingo-plant/", "/7/samples/rhinoscript/untag-object-as-a-flamingo-plant/", "/wip/samples/rhinoscript/untag-object-as-a-flamingo-plant/"]
authors = [ "dale" ]
categories = [ "Flamingo" ]
description = "Demonstrates how to un-tag an object as a Flamingo nXt plant using RhinoScript."
keywords = [ "rhinoscript", "vbscript", "flamingo" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Un-tag an Object as a Flamingo Plant"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/flamingo/flamingosdk/untagobjectasplant"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
Option Explicit

Call Main()

Sub Main()
	Dim objPlugIn, strObject, plant
	On Error Resume Next
	Set objPlugIn = Rhino.GetPluginObject("8008880f-8d13-4b2d-92b0-727e12878a4c")
	If Err Then
		MsgBox Err.Description
		Exit Sub
	End If
	strObject = Rhino.GetObject("Select object")
  If Not IsNull(strObject) And Not strObject = "" Then
		If objPlugIn.UnTagObjectAsPlant(strObject) Then
      Rhino.Print("Plant tags removed from object")
    End If
	End If
	Set objPlugIn = Nothing
End Sub
```
