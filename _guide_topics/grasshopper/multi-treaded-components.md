---
title: Multi-threaded components
description: A guide to parallel computing in Grasshopper
authors: ['Steve Baer', 'Scott Davidson']
author_contacts: ['stevebaer','scottd']
sdk: ['Grasshopper']
languages: ['Grasshopper']
platforms: ['Windows', 'Mac']
categories: ['In Depth']
origin:
order: 2
keywords: ['developer', 'grasshopper', 'components']
layout: toc-guide-page
---


## A guide to parallel computing in Grasshopper

Grasshopper in Rhino 6 includes multi-threaded solving in specific components. Benchmarks have shown that Grasshopper can be up to 20% faster when using multi-threaded components.  Results may vary as there are only specific components that can compute in parallel.

The following 27 components have been modified to perform calculations using multiple threads.

| Curve Plane Intersection | Project Curve | Pull Curve |
| Split with Brep | Shatter | Split with Breps |
| Trim with Brep | Trim with Breps | Area |
| Area Moments | Volume | Volume Moments |
| Brep Closest Point | Mesh Plane Intersection | Brep Line Intersection |
| Brep Curve Intersection | Brep Brep Intersection | Brep Plane Intersection |
| Curve Curve Intersection | Curve Curves Intersection | Point in Brep |
| Point in Breps | Curve Self-Intersection | Contour |
| Dash Pattern | Divide Curve | Boundary Surface |
{: .guide_fullwidth}

Multi-threaded components are decorated with small dots in the upper left corner to help you understand the component’s capabilities and current ‘mode’ of operation.

<img src="{{ site.baseurl }}/images/gh-multi-threaded.png">{: .img-center  width="100%"}

* No dots : the component does not currently support multi-threaded calculations
* One dot: the component does support multi-threaded calculations, but is currently calculating with a single thread (i.e. legacy mode)
* Two dots: the component does support multi-threaded calculations and is solving using multiple threads.

For components that support multi-threaded calculations, the feature can be enabled/disabled using the right click context menu on the component itself.

We continue to look for components that would be useful to have multi-threaded.  Join the [Multi-threaded Grasshopper component discussion](https://discourse.mcneel.com/t/v6-feature-multi-threaded-gh-components/47049) to participate.

## Creating you own multi-threaded components in Grasshopper

Custom multi-threaded components are also possible by programmer your own components in C# or Python. for details on this read the [Making Task Capable Components in Grasshopper]({{ site.baseurl }}/guides/grasshopper/programming-task-capable-component/) guide
