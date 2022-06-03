+++
authors = [ "dale" ]
categories = [ "Python in Rhino" ]
description = "This guide provides an overview of RhinoScriptSyntax Object Geometry in Python."
keywords = [ "script", "Rhino", "python" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "Rhino objects in Python"
type = "guides"
weight = 6
override_last_modified = "2018-12-05T14:59:06Z"

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
 
## Objects

Rhino can create and manipulate a number of objects, including points, point clouds, curves, surfaces, B-reps, meshes, lights, annotations, and references.  Each object in the Rhino document is identified by a globally unique identifier, or GUID, that is generated and assigned to objects when they are created.  Object identifiers are saved in the 3dm file, so an object's identifier will be the same between editing sessions.

To view an object's unique identifier, use Rhino's `Properties` command.

For convenience, RhinoScriptSyntax returns object identifiers in the form of a string.  For example, an object's identifier will look something like the following:

`F6E01514-3264-4598-8A07-A58BFE739C38`

The majority of RhinoScriptSyntax's object manipulation methods require one or more object identifiers to be acquired before the method can be executed.

## Geometry and Attributes

Rhino objects consist of two components: the object's geometry and the object's attributes.

The types of geometry support by Rhino include points, point clouds, curves, surfaces, polysurfaces, extrusions, meshes, annotations and dimensions.

The attributes of an object include such properties as color, layer, linetype, render material, and group membership, amongst others.

## Example

The following example uses Object IDs to create reference geometry:

```python
import rhinoscriptsyntax as rs

startPoint = [1.0, 2.0, 0.0]
endPoint = [4.0, 5.0, 0.0]
line1 = [startPoint, endPoint]

line1ID = rs.AddLine(line1[0],line1[1]) # Adds a line to the Rhino Document and returns an ObjectID

startPoint2 = [1.0, 4.0, 0.0]
endPoint2 = [4.0, 2.0, 0.0]
line2 = [startPoint2, endPoint2]

line2ID = rs.AddLine(line2[0],line2[1]) # Returns another ObjectID

int1 = rs.LineLineIntersection(line1ID,line2ID) # passing the ObjectIDs to the function.
```
## Related Topics

- [What is Python and RhinoScript?](/guides/rhinopython/what-is-rhinopython)
- [Points](/guides/rhinopython/python-rhinoscriptsyntax-points)
- [Vectors](/guides/rhinopython/python-rhinoscriptsyntax-vectors)
- [Lines](/guides/rhinopython/python-rhinoscriptsyntax-lines)
- [Planes](/guides/rhinopython/python-rhinoscriptsyntax-planes)
- [Rhino NURBs Geometry](/guides/rhinopython/python-rhinoscriptsyntax-nurbs)
