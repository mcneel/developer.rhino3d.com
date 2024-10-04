+++
aliases = ["/en/5/guides/rhinoscript/byref-vs-byval/", "/en/6/guides/rhinoscript/byref-vs-byval/", "/en/7/guides/rhinoscript/byref-vs-byval/", "/wip/guides/rhinoscript/byref-vs-byval/"]
authors = [ "dale" ]
categories = [ "Miscellaneous", "Intermediate" ]
description = "This guide discusses VBScript argument passing."
keywords = [ "script", "Rhino", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "ByRef vs ByVal"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/byrefvsbyval"
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

 
## Overview

There has always been confusion about what exactly `ByRef` and `ByVal` mean in VBScript.  The confusion arises because VBScript uses “by reference” to mean two similar, but different things.  VBScript supports:

1. Reference types
1. Variable references

The best way to illustrate the difference is with an example.  Consider this class:

```vbnet
Class Foo
  Public Bar
End Class
```

Now we can create an instance of this class:

```vbnet
Dim Blah, Baz
Set Blah = New Foo
Set Baz = Blah
Blah.Bar = 123
```

Both `Blah` and `Baz` are references to the same object. The fourth line changes both `Blah.Bar` and `Baz.Bar` because these are different names for the same thing.

That's the “reference type” feature.  We say that VBScript treats objects as reference types.

Now consider this little program:

```vbnet
Sub Change(ByRef XYZ)
  XYZ = 5
End Sub
Dim ABC
ABC = 123
Change ABC
```

This passes a reference to variable `ABC`. The local variable `XYZ` becomes an alias for `ABC`, so the assignment `XYZ = 5` changes `ABC` as well.

## Related Topics

- [Parentheses](/guides/rhinoscript/parentheses)
