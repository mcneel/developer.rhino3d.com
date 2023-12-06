+++
aliases = ["/5/guides/rhinopython/python-rhinoscriptsyntax-list-points/", "/6/guides/rhinopython/python-rhinoscriptsyntax-list-points/", "/7/guides/rhinopython/python-rhinoscriptsyntax-list-points/", "/wip/guides/rhinopython/python-rhinoscriptsyntax-list-points/"]
authors = [ "dale" ]
categories = [ "Python in Rhino" ]
description = "This guide provides an overview of a rhinoscriptsyntax list of Point Geometry in Python."
keywords = [ "script", "Rhino", "python" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "List of Points in Python"
type = "guides"
weight = 3
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Mac", "Windows" ]
since = 0
version = [ "7", "8" ]

[page_options]
byline = true
toc = true
toc_type = "single"

+++
 
## Lists of Points

Many rhinoscriptsyntax functions require a list of points as an argument or return a list of [Point3d](/guides/rhinopython/python-rhinoscriptsyntax-points) structures. For example the 'DivideCurve()' function will return a list of points:

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
    print (i)
```

It is also possible to use nested indexes to access a specific coordinate of a point in the list.  This example will access the Y coordinate of the second point in the list:


```python
print(points[1][1])
```

Using the .Y property on the [Point3d](/guides/rhinopython/python-rhinoscriptsyntax-points) also would work:

```python
print(points[1].Y)
```

To add a point to this list, first create the point3d with `CreatePoint()`, then [append](https://docs.python.org/2/tutorial/datastructures.html) it:

```python
points.append(rs.CreatePoint(1.0, 2.0, 3.0))

for i in points:
    print (i)
```

## Related Topics

- [What is Python and RhinoScript?](/guides/rhinopython/what-is-rhinopython)
- [Python Points](/guides/rhinopython/python-rhinoscriptsyntax-points)
- [Python Vectors](/guides/rhinopython/python-rhinoscriptsyntax-vectors)
- [Python Lines](/guides/rhinopython/python-rhinoscriptsyntax-lines)
- [Python Planes](/guides/rhinopython/python-rhinoscriptsyntax-planes)
- [Python Objects](/guides/rhinopython/python-rhinoscriptsyntax-objects)
