---
title: Trimming Curves
description: This guide demonstrates how to trim curves using RhinoScript.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Miscellaneous', 'Advanced']
origin: http://wiki.mcneel.com/developer/scriptsamples/trimcurve
order: 1
keywords: ['script', 'Rhino', 'vbscript']
layout: toc-guide-page
---

# {{ page.title }}

{% include byline.html %}

{{ page.description }}

## Problem

Imagine you need to trim a lot of lines where they intersect.  How is this done?  What is a "domain?"

## Solution

If you can remember back to your pre-calculus days, a domain is most often defined as the set of values for which a function is defined.  As curves in Rhino have starting and ending points, they also have starting (minimum) and ending (maximum) domain values (parameters).  You can obtain a curve's minimum and maximum domain values using the `CurveDomain` function.

To trim a curve using TrimCurve, you must provide an interval, or sub-domain, of the curve that you want to keep.  For example, if you have a curve with a minimum domain value of 0 and a maximum domain value of 5 and you wanted everything from t=2 to the end of the curve trimmed away, then you'd do something like this:

```vbnet
domain = Rhino.CurveDomain(curve)
Call Rhino.TrimCurve(curve, Array(domain(0), 2), True)
```

Remember, the interval argument defines what you want to keep, not what you want to trim.

If two curves intersect, `CurveCurveIntersection` will return the parameter on the curve where the intersection event took place.  Using this parameter, you can begin to build an interval to pass to `TrimCurve`.

The following example script demonstrates how to interactively trim a curve using what was discussed above...

```vbnet
Sub TestTrimCurve

  Const rhCurve = 4

  ' Pick the cutting curve
  Dim cutter : cutter = Rhino.GetObject("Select cutting curve", rhCurve)
  If IsNull(cutter) Then Exit Sub

  ' Pick the curve to trim    
  Dim curve : curve = Rhino.GetCurveObject("Select curve to trim")
  If IsNull(curve) Then Exit Sub

  ' Calculate the intersection of the two curves      
  Dim ccx : ccx = Rhino.CurveCurveIntersection(curve(0), cutter)
  If IsNull(ccx) Then
    Rhino.Print "Curves do not intersect."
    Exit Sub
  End If

  Dim trim_t : trim_t = ccx(0, 5)             ' intersection parameter
  Dim pick_t : pick_t = curve(4)              ' pick parameter
  Dim domain : domain = CurveDomain(curve(0)) ' curve domain

  ' TrimCurve's interval argument defines what to keep.
  ' So, figure out what side of the curve to keep.
  Dim interval
  If (trim_t < pick_t) Then
    interval = Array(domain(0), trim_t)
  Else
    interval = Array(trim_t, domain(1))
  End If

  ' Trim the curve
  Rhino.TrimCurve curve(0), interval

End Sub
```
