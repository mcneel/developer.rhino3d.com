---
title: Vectors in Python
description: This guide provides an overview of a RhinoScriptSytntax Vector Geometry in Python.
authors: ['Scott Davidson']
author_contacts: ['scottd']
apis: ['RhinoPython']
languages: ['Python']
platforms: ['Mac', 'Windows']
categories: ['Python in Rhino']
origin:
order: 4
keywords: ['script', 'Rhino', 'python']
layout: toc-guide-page
---

## Vectors

Similar to 3d points, 3d vectors are stored as [Vector3d](http://developer.rhino3d.com/api/RhinoCommonWin/html/T_Rhino_Geometry_Vector3d.htm) structures.  They conceptually can be thought as a zero-based, one-dimensional list that contain three numbers. These three number represent to the X, Y and Z coordinate direction of the vector.  Note, unlike points, vectors define magnitude (length) and direction, not position.

```
vector3d contains [1.0, 2.0, 3.0]  
```

A Vector3d structure can be constructed in a number of different ways.  Two common ways are:

```
import rhinoscriptsyntax as rs

vec = rs.CreateVector(1.0, 2.0, 3.0)
```

A Vector3d coordinates can be accessed like a simple python list, one element at a time:

```python
import rhinoscriptsyntax as rs

vec = rs.CreateVector(1.0, 2.0, 3.0)

print(vec[0]) #Prints the X coordinate of the Vector3d
print(vec[1]) #Print the Y coordinate of the Vector3d
print(vec[2]) #Print the Z coordinate of the Vector3d
```

The coordinates of a Vector3d may also be accessed through its .X, .Y and .Z property.

```python
import rhinoscriptsyntax as rs

vec = rs.CreateVector(1.0, 2.0, 3.0)

print(vec.X) # Prints the X coordinate of the Vector3d
print(vec.Y) # Print the Y coordinate of the Vector3d
print(vec.Z) # Print the Z coordinate of the Vector3d
```

To change an individual coordinate of a Vector3d simply assign a new value to the correct coordinate through the index location or coordinate property:

```python
import rhinoscriptsyntax as rs

vec = rs.CreateVector(1.0, 2.0, 3.0)

vec[0] = 5.0 # Sets the X coordinate to 5.0
vec.Y = 45.0 # Sets the Y coordinate to 45.0

print(vec) #Print the new coordinates
```

Using the Python `for` function it is quite easy to walk through each coordinate in succession:

```
for c in vec:
    print c # This will loop through each coordinate in the vector3d
```

Rhinoscriptsyntax contains a number of methods to manipulate vectors.  See [RhinoScript Points and Vectors Methods]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-point-vector-methods) for details.

---

## Related Topics

- [What is Python and RhinoScript?]({{ site.baseurl }}/guides/rhinopython/what-are-python-rhinoscript)
- [Python Points]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-points)
- [Python Vectors]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-vectors)
- [Python Lines]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-lines)
- [Python Planes]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-planes)
- [Python Objects]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-objects)
