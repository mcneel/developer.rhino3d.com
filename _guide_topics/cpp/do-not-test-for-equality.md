---
title: Do NOT Test for Equality
description: This brief guide contains a technical tip for floating point programming.
authors: ['dale_fugier']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Troubleshooting']
origin: http://wiki.mcneel.com/developer/sdksamples/equalitytest
order: 1
keywords: ['rhino', 'floating point']
layout: toc-guide-page
---

 
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
