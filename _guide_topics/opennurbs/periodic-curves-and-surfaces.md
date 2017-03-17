---
title: Periodic Curves & Surfaces
description: This guide discusses periodic curves and surfaces and openNURBS toolkit.
authors: ['Dale Lear']
author_contacts: ['dalelear']
sdk: ['openNURBS']
languages: ['C/C++']
platforms: ['Windows', 'Mac']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/onperiodiccurvesurface
order: 1
keywords: ['openNURBS', 'Periodic', 'Curves', 'Surfaces']
layout: toc-guide-page
---

 
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

Chapter 12 of The NURBS Book has a few pages discussing periodic [NURBS]({{ site.baseurl }}/guides/opennurbs/nurbs-geometry-overview/) (look in the index), but the discussion is limited.  Chapter 14 of DeBoor's Practical Guide to Splines provides a few more details.

---

## Related topics

- [NURBS Geometry Overview]({{ site.baseurl }}/guides/opennurbs/nurbs-geometry-overview/)
