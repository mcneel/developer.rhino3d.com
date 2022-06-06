+++
aliases = ["/5/guides/rhinopython/python-rhinoscriptsyntax-plane/", "/6/guides/rhinopython/python-rhinoscriptsyntax-plane/", "/7/guides/rhinopython/python-rhinoscriptsyntax-plane/", "/wip/guides/rhinopython/python-rhinoscriptsyntax-plane/"]
authors = [ "dale" ]
categories = [ "Python in Rhino" ]
description = "This guide provides an overview of RhinoScriptSyntax Plane Geometry in Python."
keywords = [ "script", "Rhino", "python" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "Planes in Python"
type = "guides"
weight = 5
override_last_modified = "2020-05-06T16:44:17Z"

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Mac", "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

## Planes

Planes are represented by a [Plane](/api/RhinoCommon/html/T_Rhino_Geometry_Plane.htm) structure.  Planes  can be thought of as a zero-based, one-dimensional list containing four elements: the plane's origin ([point3D](/guides/rhinopython/python-rhinoscriptsyntax-points)), the plane's X axis direction ([vector3d](/guides/rhinopython/python-rhinoscriptsyntax-vectors)), the plane's Y axis direction ([vector3d](/guides/rhinopython/python-rhinoscriptsyntax-vectors)), and the plane's Z axis direction ([vector3d](/guides/rhinopython/python-rhinoscriptsyntax-vectors)).

{{< image url="/images/primer-planedefinition.svg" alt="/images/primer-planedefinition.svg" class="image_center" width="45%" >}}

```
plane contains [pointOrigin, vectorX, vectorY, vectorZ]
```

It is easy to forget that there is a specific geometric relationship between the axes.  With Planes, the Y axis is automatically oriented 90-degrees to the X axis.  The X axis is the only axis that can be easily defined.  The Y axis is made orthogonal to the X vector, and the direction of the Z axis is computed from the cross-product of the other two vectors.

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

Planes can also be created using the `CreatePlane()`, [PlaneFromFrame](/api/rhinoscriptsyntax/#collapse-PlaneFromFrame),  [PlaneFromNormal](/api/rhinoscriptsyntax/#collapse-PlaneFromNormal), and [PlaneFromPoints](/api/rhinoscriptsyntax/#collapse-PlaneFromPoints) functions.

Plane also have a number of properties that can be used to get or set the individual values in the Point object.  In the example below the `.Origin`, `.XAxis`, `.Yaxis`, `.Zaxis` are used:

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

To change origin of a Plane, simply assign a new value to the `.Origin` property.

Use the Python `for` iterator to walk through each point coordinate in succession:

```
for p in plane:
    print p
```

RhinoScriptSyntax contains a number of functions to manipulate planes.  See [Lines and Planes](/guides/rhinopython/python-rhinoscriptsyntax-line-plane-methods) for details.

Also, please see the Python primer [Section 8.5 Planes](/guides/rhinopython/primer-101/8-geometry/#85-planes).

## Related Topics

- [What is Python and RhinoScript?](/guides/rhinopython/what-is-rhinopython)
- [Python Points](/guides/rhinopython/python-rhinoscriptsyntax-points)
- [Python Vectors](/guides/rhinopython/python-rhinoscriptsyntax-vectors)
- [Python Lines](/guides/rhinopython/python-rhinoscriptsyntax-lines)
- [Python Planes](/guides/rhinopython/python-rhinoscriptsyntax-planes)
- [Python Objects](/guides/rhinopython/python-rhinoscriptsyntax-objects)
