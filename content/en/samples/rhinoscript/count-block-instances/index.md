+++
aliases = ["/en/5/samples/rhinoscript/count-block-instances/", "/en/6/samples/rhinoscript/count-block-instances/", "/en/7/samples/rhinoscript/count-block-instances/", "/wip/samples/rhinoscript/count-block-instances/"]
authors = [ "dale" ]
categories = [ "Blocks" ]
description = "Demonstrates how to count block instances using RhinoScript."
keywords = [ "rhinoscript", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Count Block Instances"
type = "samples/rhinoscript"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/countblocks"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```vbnet
Sub CountAllInstancesOfAllBlocks
  arrNames = Rhino.BlockNames(True)
  If IsArray(arrNames) Then
    For Each strName In arrNames
      Rhino.Print strName & " = " & CStr(Rhino.BlockInstanceCount(strName))
    Next
  End If
End Sub
```
