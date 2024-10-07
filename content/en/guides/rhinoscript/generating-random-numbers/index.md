+++
aliases = ["/en/5/guides/rhinoscript/generating-random-numbers/", "/en/6/guides/rhinoscript/generating-random-numbers/", "/en/7/guides/rhinoscript/generating-random-numbers/", "/en/wip/guides/rhinoscript/generating-random-numbers/"]
authors = [ "dale" ]
categories = [ "Miscellaneous", "Intermediate" ]
description = "This guide demonstrates how to generate random numbers that fall within a specified range using RhinoScript."
keywords = [ "script", "Rhino", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Generating Random Numbers"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/randomnumber"
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

 
## Standard VBScript

The following code sample demonstrates how to generate random integers that fall within a specified range.

First, the standard VBScript method:

```vbnet
Sub Test1()
  nLow = 1
  nHigh = 100
  Randomize
  Rhino.Print Int((nHigh - nLow + 1) * Rnd + nLow)
End Sub
```

**NOTE**: since the `Int` function always rounds down, we add one to the difference between the limits.

## Using .NET

Now, a little help from the .NET Framework:

```vbnet
Sub Test2()
  nLow = 1
  nHigh = 100
  Set objRandom = CreateObject("System.Random")
  Rhino.Print objRandom.Next_2(nLow, nHigh)
End Sub
```

## Floating Point

If you want a random floating point number that falls within a specified range, you can use the technique below...

```vbnet
Sub Test3()
  dblLow = 10.0
  dblHigh = 50.0
  Randomize
  Rhino.Print Rnd * (dblHigh - dblLow) + dblLow
End Sub
```
