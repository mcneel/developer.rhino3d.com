---
title: Computer Physical Address
description: Illustrates RhinoScript code that determines the physical, or MAC, address of a computer.
authors: ['dale_fugier']
author_contacts: ['dale']
sdk: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/scriptsamples/macaddress
order: 1
keywords: ['rhinoscript', 'vbscript']
layout: code-sample-rhinoscript
---

```vbnet
Sub PrintMacAddress

  Dim strComputer
  strComputer = "."

  Dim objWMIService
  Set objWMIService = GetObject("winmgmts:" _
      & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")

  Dim colAdaptors
  Set colAdapters = objWMIService.ExecQuery _
      ("SELECT * FROM Win32_NetworkAdapterConfiguration WHERE IPEnabled = True")

  Dim n
  n = 1

  For Each objAdapter In colAdapters
   Rhino.Print
   Rhino.Print "Network Adapter " & n
   Rhino.Print "  Description: " & objAdapter.Description
   Rhino.Print "  Physical (MAC) address: " & objAdapter.MACAddress
   n = n + 1
  Next

End Sub
```
