---
title: Flamingo Object Mapping Properties
description: Demonstrates how to set Flamingo nXt mapping properties for an object using RhinoScript.
authors: ['Dale Fugier']
author_contacts: ['dale']
sdk: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Flamingo']
origin: http://wiki.mcneel.com/flamingo/flamingosdk/setmapping
order: 1
keywords: ['rhinoscript', 'vbscript', 'flamingo']
layout: code-sample-rhinoscript
---

```vbnet
Option Explicit

Call Main()

Sub Main()
	Dim objPlugIn, strObject, scale, xscale, yscale, zscale
	On Error Resume Next
	Set objPlugIn = Rhino.GetPluginObject("8008880f-8d13-4b2d-92b0-727e12878a4c")
	If Err Then
		MsgBox Err.Description
		Exit Sub
	End If
	strObject = Rhino.GetObject("Select object")
  If Not IsNull(strObject) And Not strObject = "" Then
  	scale = objPlugIn.GetMappingScale(strObject)
    xscale = 1.0
    yscale = 1.0
    zscale = 1.0
    If Not IsNull(scale) Then
      xscale = CDbl(scale(0))
      yscale = CDbl(scale(1))
      zScale = CDbl(scale(2))
    End If
  	xscale = Rhino.GetReal("X-Scale", xscale)
	  If Not IsNull(xscale) Then
  	  yscale = Rhino.GetReal("Y-Scale", yscale)
	    If Not IsNull(xscale) Then
  	    zscale = Rhino.GetReal("Z-Scale", zscale)
	      If Not IsNull(xscale) Then
          If objPlugIn.SetMappingScale(strObject, xscale, yscale, zscale) Then
            Rhino.Print("Object mapping scale set to: x-scale:" & xscale & "  y-scale: " & yscale & "  z-scale: " & zscale)
          Else
            Rhino.Print("Error setting objects mapping scale")
          End If
        End If
      End If
    End If
	End If
	Set objPlugIn = Nothing
End Sub
```
