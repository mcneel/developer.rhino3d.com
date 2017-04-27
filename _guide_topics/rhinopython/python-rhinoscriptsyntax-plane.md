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

Note in a Plane, the Y axis is automatically thought as it would be 90-degrees with the original X axis. In fact, the only axis that can really stays easy to defined 100% of the times is the X axis. The Y axis is made orthogonal to the X vector, and the direction of the Z axis is just computed from the cross product of the other two vectors. It is easy to forget that there is a specific geometric relationship between the 3 axis.

Planes can be constructed in a number of ways. One common function is `PlaneFromPoints`:

```python
import rhinoscriptsyntax as rs

corners = rs.GetRectangle()
if corners:
    plane = rs.PlaneFromPoints(corners[0], corners[1], corners[3])

print plane[0] # origin point
print plane[1] # x-axis vector
print plane[2] # y-axis vector
```

Planes can also be created using the CreatePlane(), [PlaneFromFrame]({{ site.baseurl }}/api/RhinoScriptSyntax/win/#collapse-PlaneFromFrame),  [PlaneFromNormal]({{ site.baseurl }}/api/RhinoScriptSyntax/win/#collapse-PlaneFromNormal), and [PlaneFromPoints]({{ site.baseurl }}/api/RhinoScriptSyntax/win/#collapse-PlaneFromPoints) functions.

Plane also have a number of properties that can be used to get or set the individual values in the Point object.  In the example below the .Origin, .XAxis, .Yaxis, .Zaxis is used.

```
import rhinoscriptsyntax as rs

plane = rs.PlaneFromPoints([-2,-5,0],[1,2,0],[-3,3,0])

print plane.Origin # origin point
print plane.XAxis # x-axis vector
print plane.YAxis # y-axis vector

plane.Origin = rs.CreatePoint(3,4,5) # Changes the origin of the plane.

print plane.Origin
print plane.XAxis # x-axis vector
print plane.YAxis # y-axis vector
```

To change origin of a Plane simply assign a new value to the .Origin property.

Using the Python `for` function it is quite easy to walk through each point coordinate in succession:

```
for p in plane:
    print p
```

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
