---
title: Vectors in Python
description: This guide provides an overview of a RhinoScriptSytntax Vector Geometry in Python.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['RhinoPython']
languages: ['Python']
platforms: ['Mac', 'Windows']
categories: ['rhinoscriptsyntax-fundamentals']
origin:
order: 4
keywords: ['script', 'Rhino', 'python']
layout: toc-guide-page
---
 
## Vectors

Like 3-D points, 3-D vectors are also represented as zero-based, one-dimensional list that contain three numbers. These three number represent to the X, Y and Z coordinate values of the vector.  Note, unlike points, vectors define magnitude (length) and direction, not position. A 3-D vector can be constructed in a number of different ways.  For example,

```python
vector1 = [1.0, 2.0, 3.0]
```
A point list can also be constructed one element at a time:

```python
vector2 = []
vector2.append(1.0)
vector2.append(2.0)
vector2.append(5.0)
```

Vectors can also be created from two 3-D points using the `VectorCreate` method:

```python
import rhinoscriptsyntax as rs

point1 = [1,2,3]
point2 = [4,6,7]
vector = rs.VectorCreate(point2, point1)

print vector
```

RhinoScript contains a number of methods to manipulate vectors.  See Points and Vectors for details.

---

## Related Topics

- [What is Python and RhinoScript?]({{ site.baseurl }}/guides/rhinopython/what-are-python-rhinoscript)
- [Python Points]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-points)
- [Python Vectors]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-vectors)
- [Python Lines]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-lines)
- [Python Planes]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-planes)
- [Python Objects]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-objects)
