+++
authors = [ "dale" ]
categories = [ "Python in Rhino" ]
description = "This guide provides an overview of the RhinoScriptSyntax Point Geometry in Python."
keywords = [ "script", "Rhino", "python" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "Points in Python"
type = "guides"
weight = 2

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

## Points

In Python, a Rhino 3D point is represented as a [Point3d](http://developer.rhino3d.com/api/RhinoCommon/html/T_Rhino_Geometry_Point3d.htm) structure. Conceptually, Point3d exist in memory as a zero-based list containing three numbers.  These three numbers represent the X, Y and Z coordinate values of the point.

```
point3D contains [1.0, 2.0, 3.0]  
```

### Creating Points

A Point3D structure can be constructed in a number of different ways.  Two common ways are:

```python
import rhinoscriptsyntax as rs

pnt = rs.CreatePoint(1.0, 2.0, 3.0)
pnt = rs.CreatePoint(1.0, 2.0) # This creates a point with the Z coordinate set to 0
```
A point list can also be constructed one element at a time:

The 'CreatePoint()' function is very flexible.  It can take a list or tuple of two or 3 numbers and return a Point3d.  The function can also extract the coordinates of a Rhino GUID to return a Point3D.

It is not always necessary to construct a point before passing it to a function that requires a point. It is possible to construct points directly as an argument to a function.  A Point is a list like structure. Wrap coordinates in brackets`[]` when passing them directly to a function. For instance the `rs.addline(point, point)` function requires two points.  Use the following syntax to construct the points on the fly:

```python
rs.AddLine([45,56,32],[56,47,89])
```
Like 3-D points, Python represents a single 2-D point as a zero-based list of numbers.  The difference being that 2-D points contain only X and Y coordinate values.

Passing coordinates in `[]`  to a function is common with RhinoScriptSyntax.

### Accessing Point Coordinates

A Point3D list can be accessed like a simple python list, one element at a time:

```python
import rhinoscriptsyntax as rs

pnt = rs.CreatePoint(1.0, 2.0, 3.0)

print(pnt[0]) #Print the X coordinate of the Point3D
print(pnt[1]) #Print the Y coordinate of the Point3D
print(pnt[2]) #Print the Z coordinate of the Point3D
```

The coordinates of a Point3d may also be accessed through its .X, .Y and .Z properties.

```python
import rhinoscriptsyntax as rs

pnt = rs.CreatePoint(1.0, 2.0, 3.0)

print(pnt.X) # Print the X coordinate of the Point3D
print(pnt.Y) # Print the Y coordinate of the Point3D
print(pnt.Z) # Print the Z coordinate of the Point3D
```

Using Python's ability to assign values to multiple variables at one, here are is a way to create x, y, and z variables all at once:

```python
x, y, z = rs.CreatePoint(1.0, 2.0, 3.0)

# or #

x, y, z = rs.PointCoodinate(point)
```

### Editing Points

To change an individual coordinate of a Point3d simply assign a new value to the correct coordinate through the index location or coordinate property:

```python
import rhinoscriptsyntax as rs

pnt = rs.CreatePoint(1.0, 2.0, 3.0)

pnt[0] = 5.0 # Sets the X coordinate to 5.0
pnt.Y = 45.0 # Sets the Y coordinate to 45.0

print(pnt) #Print the new coordinates
```

Using the Python `for` function it is quite easy to walk through each coordinate in succession:

```
for c in pnt:
    print c # This will loop through each coordinate in the point3d
```

Rhinoscriptsyntax contains a number of methods to manipulate points.  See [RhinoScript Points and Vectors Methods](/guides/rhinopython/python-rhinoscriptsyntax-point-vector-methods) for details.

For those familiar with RhinoScript, which represents points as a pure list, the Python representation is a little different and offers a few more options.

### Adding a point to display in Rhino

It is important to understand the difference between a Point3d and a point object added to Rhino's document.  Any geometry object that exists in Rhino's database is assigned an object identifier.  This is represented as a [Guid](/guides/rhinopython/python-rhinoscriptsyntax-objects). The [Guid's object](/guides/rhinopython/python-rhinoscriptsyntax-objects) is something that can be drawn, belongs to a layer, is saved to a Rhino file and is counted as a Rhino object.  A Point3d is simply a structure of 3 numbers that exists in memory.  It can be manipulated in memory, but will not be seen in Rhino or saved.  A Point3d is added to the Rhino document through the `rs.AddPoint()` command.  To create a Point3d from a Guid, use the `rs.PointCoordinates(guid)` or the `rs.CreatePoint(Guid)` function.

## Related Topics

- [What is RhinoScriptSyntax and RhinoScript?](/guides/rhinopython/what-is-rhinopython)
- [Python List of Points](/guides/rhinopython/python-rhinoscriptsyntax-list-points)
- [Python Vectors](/guides/rhinopython/python-rhinoscriptsyntax-vectors)
- [Python Lines](/guides/rhinopython/python-rhinoscriptsyntax-lines)
- [Python Planes](/guides/rhinopython/python-rhinoscriptsyntax-plane)
- [Python Objects](/guides/rhinopython/python-rhinoscriptsyntax-objects)
- [RhinoScript Points and Vectors Methods](/guides/rhinopython/python-rhinoscriptsyntax-point-vector-methods)
- [Point3d RhinoCommon Documentation](http://developer.rhino3d.com/api/RhinoCommon/html/T_Rhino_Geometry_Point3d.htm)
