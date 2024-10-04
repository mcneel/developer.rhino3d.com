+++
aliases = ["/en/5/guides/opennurbs/periodic-curves-and-surfaces/", "/en/6/guides/opennurbs/periodic-curves-and-surfaces/", "/en/7/guides/opennurbs/periodic-curves-and-surfaces/", "/wip/guides/opennurbs/periodic-curves-and-surfaces/"]
authors = [ "dalelear" ]
categories = [ "Fundamentals" ]
description = "This guide discusses periodic curves and surfaces and openNURBS toolkit."
keywords = [ "openNURBS", "Periodic", "Curves", "Surfaces" ]
languages = [ "C/C++" ]
sdk = [ "openNURBS" ]
title = "Periodic Curves & Surfaces"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/onperiodiccurvesurface"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

 
A periodic knot vector can be either uniform or non-uniform.

A periodic degree d NURBS curve has (d-1) continuous derivatives at the start/end point.

The differences between successive knot values are equal near the start and end of the spline; that is, the differences repeat themselves and hence the term “periodic”.

Specifically, when -degree < i < degree, a periodic knot vector satisfies:

```
k[(degree-1)+i+1] - k[(degree-1)+i] = k[(cv_count-1)+i+1] - k[(cv_count)+i]
```

For example a cubic periodic knot vector looks like:

```
{a,b,c,d,e, ...,  p+a,p+b,p+c,p+d,p+e}
```

with a < b < c < d < e and e < p+a.

Chapter 12 of The NURBS Book has a few pages discussing periodic [NURBS](/guides/opennurbs/nurbs-geometry-overview/) (look in the index), but the discussion is limited.  Chapter 14 of DeBoor's Practical Guide to Splines provides a few more details.

## Related topics

- [NURBS Geometry Overview](/guides/opennurbs/nurbs-geometry-overview/)
