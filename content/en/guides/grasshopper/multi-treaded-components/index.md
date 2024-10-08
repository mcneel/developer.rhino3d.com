+++
aliases = ["/en/5/guides/grasshopper/multi-treaded-components/", "/en/6/guides/grasshopper/multi-treaded-components/", "/en/7/guides/grasshopper/multi-treaded-components/", "/en/wip/guides/grasshopper/multi-treaded-components/"]
authors = [ "steve", "scottd" ]
categories = [ "In Depth" ]
description = "A guide to parallel computing in Grasshopper"
keywords = [ "developer", "grasshopper", "components" ]
languages = [ "C#" ]
sdk = [ "Grasshopper" ]
title = "Multi-threaded components"
type = "guides"
weight = 2
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
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


## Overview

Grasshopper for Rhino 6 provides multi-threaded solving in specific components. Benchmarks have shown that Grasshopper can be up to 20% faster when using multi-threaded components.  Results may vary as there are only specific components that can compute in parallel.

The following components have been modified to perform calculations using multiple threads.

* Curve Plane Intersection
* Project Curve
* Pull Curve
* Split with Brep
* Shatter
* Split with Breps
* Trim with Brep
* Trim with Breps
* Area
* Area Moments
* Volume
* Volume Moments
* Brep Closest Point
* Mesh Plane Intersection
* Brep Line Intersection
* Brep Brep Intersection
* Brep Plane Intersection
* Curve Curve Intersection
* Curve Curves Intersection
* Point in Brep
* Point in Breps
* Curve Self-Intersection 
* Contour
* Dash Pattern
* Divide Curve
* Boundary Surface

Multi-threaded components are decorated with small dots in the upper left corner to help you understand the component’s capabilities and current ‘mode’ of operation.

{{< image url="/images/gh-multi-threaded.png" alt="/images/gh-multi-threaded.png" class="image_center" width="100%" >}}

* No dots : the component does not currently support multi-threaded calculations
* One dot: the component does support multi-threaded calculations, but is currently calculating with a single thread (i.e. legacy mode)
* Two dots: the component does support multi-threaded calculations and is solving using multiple threads.

For components that support multi-threaded calculations, the feature can be enabled/disabled using the right click context menu on the component itself.

We continue to look for components that would be useful to have multi-threaded.  Join the [Multi-threaded Grasshopper component discussion](https://discourse.mcneel.com/t/v6-feature-multi-threaded-gh-components/47049) to participate.

## Creating you own multi-threaded components in Grasshopper

Custom multi-threaded components are also possible by programmer your own components in C# or Python. for details on this read the [Making Task Capable Components in Grasshopper](/guides/grasshopper/programming-task-capable-component/) guide
