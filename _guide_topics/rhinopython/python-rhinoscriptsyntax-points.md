---
title: Points in Python
description: This guide provides an overview of the RhinoScriptSytntax Point Geometry in Python.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['RhinoPython']
languages: ['Python']
platforms: ['Mac', 'Windows']
categories: ['rhinoscriptsyntax-fundamentals']
origin:
order: 2
keywords: ['script', 'Rhino', 'python']
layout: toc-guide-page
---
 
## Points

In Python, 3-D points are represented as zero-based lists that contain three numbers.  These three number represent to the X, Y and Z coordinate values of the point.

A 3-D point can be constructed in a number of different ways.  For example:

```python
point1 = [1.0, 2.0, 3.0]
```
A point list can also be constructed one element at a time:

```python
point2 = []
point2.append(1.0)
point2.append(2.0)
point2.append(5.0)
```
Like 3-D points, Python represents a single 2-D point as a zero-based list of numbers.  The difference being that 2-D points contain only X and Y coordinate values.

Rhinoscriptsyntax contains a number of methods to manipulate points.  See Points and Vectors for details.

---

## Related Topics

- [What is RhinoScriptSyntax and RhinoScript?]({{ site.baseurl }}/guides/rhinopython/what-are-python-rhinoscript)
- [Python List of Points]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-list-points)
- [Python Vectors]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-vectors)
- [Python Lines]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-lines)
- [Python Planes]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-planes)
- [Python Objects]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-objects)
- [RhinoScript Points and Vectors Methods]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-point-vector-methods)
