+++
authors = [ "dale" ]
categories = [ "Miscellaneous", "Advanced" ]
description = "This short guide demonstrate how to pad numbers with leading zeros in RhinoScript."
keywords = [ "script", "Rhino", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Padding Digits"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/paddigits"
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

 
## Problem

How do you pad digits with leading zeros?  For example, if you have the number 24, how can you print it as “0024”?

## Solution

The following utility function will pad an integer with a specified number of digits:

```vbnet
Function PadDigits(val, digits)
  PadDigits = Right(String(digits,"0") & val, digits)
End Function
```

You can use this function as such:

```vbnet
For i = 0 To 25
  Rhino.Print PadDigits(i, 4)
Next
```

The output will be:

```vbs
0000
0001
0002
0003
0004
0005
0006
0007
0008
0009
0010
...
```
