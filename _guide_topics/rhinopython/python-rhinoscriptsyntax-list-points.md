---
title: List of Points in Python
description: This guide provides an overview of a RhinoScriptSytntax list of Point Geometry in Python.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['RhinoPython']
languages: ['Python']
platforms: ['Mac', 'Windows']
categories: ['rhinoscriptsyntax-fundamentals']
origin:
order: 3
keywords: ['script', 'Rhino', 'python']
layout: toc-guide-page
---
 
## Lists of Points

Many RhinoScriptSyntax methods either require as an argument or return as a result an list of 3-D points. Lists of 3-D points are zero-based, one-dimensional lists of 3-D points (which in turn are zero-based, one-dimensional lists of X, Y, and Z coordinate values).  Lists of 3-D points can be constructed in a number of ways.  For example,

```python
pointcloud = []
pointcloud.append([0,0,0])
pointcloud.append([1.0, 2.0, 3.0])
pointcloud.append([5.0, 8.0, 9.0])
pointcloud.append([4.0, 7.0, 2.0])
pointcloud.append([8.0, 5.0, 6.0])

print pointcloud
```

Also, representing list of 3-D points as a one-dimensional array instead of a multi-dimensional list, makes it easy to repeat a group of statements for each element in the array .  For example along with the example above, use the `for` loop to walk through each point in the list,

```python
for i in pointcloud:
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
