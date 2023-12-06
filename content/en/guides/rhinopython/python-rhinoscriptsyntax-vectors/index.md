+++
aliases = ["/5/guides/rhinopython/python-rhinoscriptsyntax-vectors/", "/6/guides/rhinopython/python-rhinoscriptsyntax-vectors/", "/7/guides/rhinopython/python-rhinoscriptsyntax-vectors/", "/wip/guides/rhinopython/python-rhinoscriptsyntax-vectors/"]
authors = [ "dale" ]
categories = [ "Python in Rhino" ]
description = "This guide provides an overview of RhinoScriptSyntax Vector Geometry in Python."
keywords = [ "script", "Rhino", "python" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "Vectors in Python"
type = "guides"
weight = 4
override_last_modified = "2023-03-09T10:09:10Z"
draft = false

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Mac", "Windows" ]
since = 8
until = ""

[page_options]
block_webcrawlers = false
byline = true
toc = true
toc_type = "single"

+++

## Vectors

Similar to 3D points, 3D vectors are stored as [Vector3d](https://developer.rhino3d.com/api/RhinoCommon/html/T_Rhino_Geometry_Vector3d.htm) structures.  They can be thought as a zero-based, one-dimensional list that contain three numbers. These three number represent to the X, Y and Z coordinate direction of the vector.

```
vector3d contains [1.0, 2.0, 3.0]  
```

Here is an easy way to construct a vector:

```
import rhinoscriptsyntax as rs

vec = rs.CreateVector(1.0, 2.0, 3.0)
```

A Vector3d's coordinates can be accessed as a list, one element at a time:

```python
import rhinoscriptsyntax as rs

vec = rs.CreateVector(1.0, 2.0, 3.0)

print(vec[0]) #Prints the X coordinate of the Vector3d
print(vec[1]) #Print the Y coordinate of the Vector3d
print(vec[2]) #Print the Z coordinate of the Vector3d
```

The coordinates of a Vector3d may also be accessed through its `.X`, `.Y` and `.Z` properties:

```python
import rhinoscriptsyntax as rs

vec = rs.CreateVector(1.0, 2.0, 3.0)

print(vec.X) # Prints the X coordinate of the Vector3d
print(vec.Y) # Print the Y coordinate of the Vector3d
print(vec.Z) # Print the Z coordinate of the Vector3d
```

To change the individual coordinate of a Vector3d, simply assign a new value to the coordinate through the index location or coordinate property:

```python
import rhinoscriptsyntax as rs

point1 = [1,2,3]
point2 = [4,6,7]
vec = rs.CreateVector(1.0, 2.0, 3.0)

vec[0] = 5.0 # Sets the X coordinate to 5.0
vec.Y = 45.0 # Sets the Y coordinate to 45.0

print(vec) #Print the new coordinates
```

To find the vector between two points, use vector subtraction:

{{< image url="/images/math-image180.png" alt="/images/image180.png" class="float_right" >}}

```python
point1 = rs.CreatePoint(1,2,3)
point2 = rs.CreatePoint(4,5,6)

vector = rs.VectorAdd(point1, point2)

print(vector) #prints the new coordinates.
```

In the above example, the vector goes from point1 to point2.  Reversing this direction is a common mistake.  It is important to be sure that the starting point is subtracted from the ending point.

Vectors can also be added to points to create new point locations.  Here is an example of moving a point location by a vector:

{{< image url="/images/math-image172.png" alt="/images/image172.png" class="float_right" >}}

```python
#  A base point
point1 = rs.CreatePoint(1,1,1)

# A vector with a direction of 2 units in the X direction
vector1 = rs.CreateVector(2.0, 0.0, 0.0)

# Setting the coordinate of point1 to to units more in the X direction.
vector = rs.VectorAdd(point1, vector1)
# point1 + vector1 = [1+2, 1+0, 1+0] = [3,1,1]
```

Use a `for` loop to walk through each coordinate in succession:

```python
for c in (vector.X, vector.Y, Vector.Z):
    print (c) # This will loop through each coordinate in the vector3d
```

RhinoScriptSyntax contains a number of methods to manipulate vectors.  See [RhinoScript Points and Vectors Methods](/guides/rhinopython/python-rhinoscriptsyntax-point-vector-methods) for details.

## Related Topics

- [Python Points](/guides/rhinopython/python-rhinoscriptsyntax-points)
- [Python Vectors](/guides/rhinopython/python-rhinoscriptsyntax-vectors)
- [Python Lines](/guides/rhinopython/python-rhinoscriptsyntax-line)
- [Python Planes](/guides/rhinopython/python-rhinoscriptsyntax-plane)
- [Python Objects](/guides/rhinopython/python-rhinoscriptsyntax-objects)
