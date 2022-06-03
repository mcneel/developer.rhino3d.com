+++
authors = [ "dale" ]
categories = [ "Miscellaneous", "Intermediate" ]
description = "This guide discusses efficient VBScript array comparison."
keywords = [ "script", "Rhino", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Comparing Arrays"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/arraycompare"
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

 
## Slow Comparison

Imagine you have two collections of items and you want to determine how many of those items have the same name.  In short, you want to compare the contents of two arrays.  Consider this straightforward method of comparison:

```vbnet
intSame = 0
For Each strFirst In arrFirst
  For Each strSecond In arrSecond
    If StrComp(strFirst, strSecond, vbTextCompare) = 0 Then
      intSame = intSame + 1
      Exit For
    End If
  Next
Next
```

This method, although simple, is extremely slow.  Let's say there are 5000 items in `arrFirst`, 3000 items in `arrSecond`, and 1500 of them have the same value. Every one of the 3500 unsuccessful searches checks all 3000 `arrSecond` items, and the 1500 successful searches on average check 1500 `arrSecond` items each. Each time through, the inner loop does one loop iteration and one string comparison. Add all those up and you get millions of function calls to determine this count. Now, each individual function call is only taking a few microseconds, but all of these calls add up!

There is another way...

## Fast Comparison

Try building a faster lookup table rather than doing a full search through the collection every time.

```vbnet
Set objLookup = CreateObject("Scripting.Dictionary")
For Each strFirst In arrFirst
  Call objLookup.Add(strFirst, 0) ' 0 = some useless value
Next
For Each strSecond In arrSecond
  If objLookup.Exists(strSecond) Then intSame = intSame + 1
Next
```

This is only a couple of thousand function calls.  So we believe that this will be much, much faster.

## Related Topics

- [Array Bounds](/guides/rhinoscript/array-bounds)
- [Array Utilities](/guides/rhinoscript/array-utilities)
- [VBScript Dictionaries](/guides/rhinoscript/vbscript-dictionaries)
- [VBScript Looping](/guides/rhinoscript/vbscript-looping)
