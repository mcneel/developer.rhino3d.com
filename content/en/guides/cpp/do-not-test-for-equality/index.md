+++
authors = [ "dale" ]
categories = [ "Troubleshooting" ]
description = "This brief guide contains a technical tip for floating point programming."
keywords = [ "rhino", "floating point" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Do NOT Test for Equality"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/equalitytest"
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

 
## A Warning

You almost never want to write code like the following:

```cpp
double x;
double y;
...
if (x == y) {...}
```

Most floating point operations involve at least a tiny loss of precision and so even if two numbers are equal for all practical purposes, they may not be exactly equal down to the last bit, and so the equality test is likely to fail.  For example, the following code snippet prints `-1.778636e-015`.  Although in theory, squaring should undo a square root, the round-trip operation is slightly inaccurate.

```cpp
double x = 10;
double y = sqrt(x);
y *= y;
if (x == y)
  RhinoApp().Print(L"Square root is exact\n");
else
  RhinoApp().Print(L"%f\n", x-y);
```

In most cases, the equality test above should be written as something like the following:

```cpp
double tolerance = ...
if (fabs(x - y) < tolerance) {...}
```

Here, `tolerance` is some threshold that defines what is "close enough" for equality.  This begs the question of: how close is close enough?  This cannot be answered in the abstract; you have to know something about your particular problem to know how close is close enough in your context.
