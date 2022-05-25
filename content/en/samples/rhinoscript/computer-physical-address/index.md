+++
authors = [ "dale" ]
categories = [ "Other" ]
description = "Illustrates RhinoScript code that determines the physical, or MAC, address of a computer."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Computer Physical Address"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/macaddress"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

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
