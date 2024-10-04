+++
aliases = ["/en/5/guides/rhinoscript/quadratic-solver/", "/en/6/guides/rhinoscript/quadratic-solver/", "/en/7/guides/rhinoscript/quadratic-solver/", "/wip/guides/rhinoscript/quadratic-solver/"]
authors = [ "dale" ]
categories = [ "Advanced" ]
description = "This brief guide demonstrates how to solve quadratic equations in RhinoScript."
keywords = [ "script", "Rhino", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "Quadratic Solver"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/quadraticsolver"
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

If you are trying to solve quadratic equations like:

{{< mathjax >}}$${-b \pm \sqrt{b^2 - 4ac} \over 2a }$${{< /mathjax >}}

the results may seem incorrect at times.

## Solution

Most likely, the problem that is that there are floating point rounding errors.  Being that you only get 15 decimal places of accuracy, you can use them all up if you are dealing with small numbers.

The following algorithm should produce more accurate results:

```vbnet
Function QuadraticSolver(a, b, c)
  Dim d, s0, s1
  d = b * b - 4 * a * c
  If d < 0 Then
    ' No real solution
    QuadraticSolver = Null
  Else
    s0 = (-b - Sqr(d)) / (2 * a)
    s1 = (-b + Sqr(d)) / (2 * a)
    If Abs(s0) < Abs(s1) Then s0 = s1
    s1 = c / (a * s0)
    QuadraticSolver = Array(s0,s1)
  End If
End Function
```
