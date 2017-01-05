---
title: Planes in Python
description: This guide provides an overview of a RhinoScriptSytntax Plane Geometry in Python.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['RhinoPython']
languages: ['Python']
platforms: ['Mac', 'Windows']
categories: ['rhinoscriptsyntax-fundamentals']
origin:
order: 5
keywords: ['script', 'Rhino', 'python']
layout: toc-guide-page
---
 
## Planes

Several RhinoscriptSyntax methods either require as an argument or return as a result a plane.  Planes are represented as zero-based,  one-dimensional list containing four elements: the plane's origin (3-D point), the plane's X axis direction (3-D vector), the plane's Y axis direction (3-D vector), and the plane's Z axis direction (3-D vector).

Planes can be constructed in a number of ways.  For example,

```python
plane1 = [ ] # create an empty list.
plane1.append([0.0, 0.0, 0.0]) # origin point
plane1.append([1.0, 0.0, 0.0]) # x-axis vector
plane1.append([0.0, 1.0, 0.0]) # y-axis vector
plane1.append([0.0, 0.0, 1.0]) # z-axis vector
```

Planes can also be created using the [PlaneFromFrame]({{ site.baseurl }}/api/RhinoScriptSyntax/win/#collapse-PlaneFromFrame), [PlaneFromNormal]({{ site.baseurl }}/api/RhinoScriptSyntax/win/#collapse-PlaneFromNormal), and [PlaneFromPoints]({{ site.baseurl }}/api/RhinoScriptSyntax/win/#collapse-PlaneFromPoints) methods.

RhinoScriptSyntax contains a number of methods to manipulate planes.  See [Lines and Planes]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-line-plane-methods) for details.

---

## Related Topics

- [What is Python and RhinoScript?]({{ site.baseurl }}/guides/rhinopython/what-are-python-rhinoscript)
- [Python Points]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-points)
- [Python Vectors]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-vectors)
- [Python Lines]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-lines)
- [Python Planes]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-planes)
- [Python Objects]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-objects)
