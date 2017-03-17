---
title: Planes in Python
description: This guide provides an overview of a RhinoScriptSytntax Plane Geometry in Python.
authors: ['Dale Fugier']
author_contacts: ['dale']
sdk: ['RhinoPython']
languages: ['Python']
platforms: ['Mac', 'Windows']
categories: ['Python in Rhino']
origin:
order: 5
keywords: ['script', 'Rhino', 'python']
layout: toc-guide-page
---

## Planes

Several RhinoscriptSyntax methods either require as an argument or return as a result a plane.  Planes are represented by a [Plane](http://developer.rhino3d.com/wip/api/RhinoCommonWin/html/T_Rhino_Geometry_Plane.htm) structure. Plane structures and be thought of as a zero-based,  one-dimensional list containing four elements: the plane's origin ([point3D]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-points)), the plane's X axis direction ([vector3d]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-vectors)), the plane's Y axis direction ([vector3d]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-vectors)), and the plane's Z axis direction ([vector3d]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-vectors)).

<img src="{{ site.baseurl }}/images/primer-planedefinition.svg">{: .img-center  width="45%"}

```
plane contains [pointOrigin, vectorX, vectorY, vectorZ]
```

Planes can be constructed in a number of ways. One common function is `PlaneFromPoints`:

```python
import rhinoscriptsyntax as rs

corners = rs.GetRectangle()

if corners:
    plane = rs.PlaneFromPoints(corners[0], corners[1], corners[3])
plane1.append([0.0, 1.0, 0.0]) # y-axis vector

print plane[2]
```

Planes can also be created using the CreatePlane(), [PlaneFromFrame]({{ site.baseurl }}/api/RhinoScriptSyntax/win/#collapse-PlaneFromFrame),  [PlaneFromNormal]({{ site.baseurl }}/api/RhinoScriptSyntax/win/#collapse-PlaneFromNormal), and [PlaneFromPoints]({{ site.baseurl }}/api/RhinoScriptSyntax/win/#collapse-PlaneFromPoints) functions.

RhinoScriptSyntax contains a number of functions to manipulate planes.  See [Lines and Planes]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-line-plane-methods) for details.

Also, read the Python primer [Section 8.5 Planes]({{ site.baseurl }}/guides/rhinopython/primer-101/8-geometry/#85-planes)

---

## Related Topics

- [What is Python and RhinoScript?]({{ site.baseurl }}/guides/rhinopython/what-are-python-rhinoscript)
- [Python Points]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-points)
- [Python Vectors]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-vectors)
- [Python Lines]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-lines)
- [Python Planes]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-planes)
- [Python Objects]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-objects)
