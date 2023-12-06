+++
aliases = ["/5/guides/rhinopython/python-rhinoscriptsyntax-point-vector-methods/", "/6/guides/rhinopython/python-rhinoscriptsyntax-point-vector-methods/", "/7/guides/rhinopython/python-rhinoscriptsyntax-point-vector-methods/", "/wip/guides/rhinopython/python-rhinoscriptsyntax-point-vector-methods/"]
authors = [ "dale" ]
categories = [ "Python in Rhino" ]
description = "This guide provides an overview of the RhinoScriptSytntax Point and Vector methods."
keywords = [ "script", "Rhino", "python" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "Point and Vector Methods"
type = "guides"
weight = 97
override_last_modified = "2018-12-05T14:59:06Z"
draft = false

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Mac", "Windows" ]
since = 7
until = ""

[page_options]
block_webcrawlers = false
byline = true
toc = true
toc_type = "single"

+++
 
## Point  & Vector Methods

The following methods are available for creating and manipulating 3-D points and 3-D vectors.  3-D points and 3-D vectors are represented as  zero-based, one-dimensional arrays that contain three numbers. For more information, see the [Points](/guides/rhinopython/python-rhinoscriptsyntax-points) and [Vectors](/guides/rhinopython/python-rhinoscriptsyntax-vectors) discussion in [RhinoScript Fundamentals](/guides/rhinopython/python-rhinoscriptsyntax-introduction).

| Method | | |  Description |
|:--------|:-:|:-:|:--------|
| IsVectorParallelTo | | | Compares two vectors to see if they are parallel.  |
| IsVectorPerpendicularTo | | | Compares two vectors to see if they are perpendicular.  |
| IsVectorTiny | | | Verifies a vector is tiny.  |
| IsVectorZero | | | Verifies a vector is zero. |
| PointAdd | | | Adds a point or a vector to a point. |
| PointArrayBoundingBox | | | Returns the bounding box of an array of 3-D points. |
| PointArrayClosestPoint | | | Finds the point in an array of 3-D points that is closest to a test point |
| PointArrayTransform | | | Transforms an array of 3-D points.|
| PointClosestObject | | | Finds the object that is closest to a test point.|
| PointCompare | | | Compares two points.|
| PointDivide | | | Divides a point by a value.|
| PointsAreCoplanar | | | Verifies that a list of 3-D points are coplanar.|
| PointScale | | | Scales a point by a value.|
| PointSubtract | | | Subtracts a point or a vector from a point.|
| PointTransform | | | Transforms a point.|
| ProjectPointToMesh | | | Projects one or more points onto one or more meshes.|
| ProjectPointToSurface | | | Projects one or more points onto one or more surfaces |
| PullPoints | | | Pulls points to a surface or a mesh object.|
| VectorAdd | | | Adds two vectors.|
| VectorAngle | | | Returns the angle between two 3-D vectors.|
| VectorCompare | | | Compares two vectors.|
| VectorCreate | | | Create a vector from two 3-D points.|
| VectorCrossProduct | | | Returns the cross product of two vectors.|
| VectorDivide | | | Divides a vector.|
| VectorDotProduct | | | Returns the dot product of two vectors.|
| VectorLength | | | Returns the length of a vector.|
| VectorMultiply | | | Multiplies two vectors.|
| VectorReverse | | | Reverses a vector. |
| VectorRotate | | | Rotates a vector. |
| VectorScale | | | Scales a vector. |
| VectorSubtract | | | Subtracts two vectors. |
| VectorTransform | | | Transforms a vector. | 
| VectorUnitaze | | | Unitizes, or normalizes, a vector. |

## Related Topics

- [What is RhinoScriptSyntax and RhinoScript?](/guides/rhinopython/what-is-rhinopython)
- [Python List of Points](/guides/rhinopython/python-rhinoscriptsyntax-list-points)
- [Python Vectors](/guides/rhinopython/python-rhinoscriptsyntax-vectors)
- [Python Lines](/guides/rhinopython/python-rhinoscriptsyntax-lines)
- [Python Planes](/guides/rhinopython/python-rhinoscriptsyntax-planes)
- [Python Objects](/guides/rhinopython/python-rhinoscriptsyntax-objects)
- [RhinoScript Points and Vectors Methods](/guides/rhinopython/python-rhinoscriptsyntax-point-vector-methods)
