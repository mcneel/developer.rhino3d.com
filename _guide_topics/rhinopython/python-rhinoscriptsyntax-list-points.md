---
title: List of Points in Python
description: This guide provides an overview of a rhinoscriptsyntax list of Point Geometry in Python.
authors: ['dale_fugier']
sdk: ['RhinoPython']
languages: ['Python']
platforms: ['Mac', 'Windows']
categories: ['Python in Rhino']
origin:
order: 3
keywords: ['script', 'Rhino', 'python']
layout: toc-guide-page
---
 
## Lists of Points

Many rhinoscriptsyntax functions require a list of points as an argument or return a list of [Point3d]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-points) structures. For example the 'DivideCurve()' function will return a list of points:

```python
import rhinoscriptsyntax as rs

obj = rs.GetObject("Select a curve")

if obj:
    points = rs.DivideCurve(obj, 4)
    
print(points[0])
```

There are a number of ways to access the information in these lists.

Use an index to access any one of the points as in the line:

```python
print(points[0]) # Returns a Point3d structure
```

With Python, it is easy to use the `for` loop to walk through the list and print out the coordinates for each point,

```python
for i in points:
    print i
```

It is also possible to use nested indexes to access a specific coordinate of a point in the list.  This example will access the Y coordinate of the second point in the list:


```python
print(points[1][1])
```

Using the .Y property on the [Point3d]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-points) also would work:

```python
print(points[1].Y)
```

To add a point to this list, first create the point3d with `CreatePoint()`, then [append](https://docs.python.org/2/tutorial/datastructures.html) it:

```python
points.append(rs.CreatePoint(1.0, 2.0, 3.0))

for i in points:
    print i
```

---

## Related Topics

- [What is Python and RhinoScript?]({{ site.baseurl }}/guides/rhinopython/what-are-python-rhinoscript)
- [Python Points]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-points)
- [Python Vectors]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-vectors)
- [Python Lines]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-lines)
- [Python Planes]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-planes)
- [Python Objects]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-objects)
