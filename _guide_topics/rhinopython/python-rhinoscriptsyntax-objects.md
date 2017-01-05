---
title: Rhino objects in Python
description: This guide provides an overview of a RhinoScriptSytntax Object Geometry in Python.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['RhinoPython']
languages: ['Python']
platforms: ['Mac', 'Windows']
categories: ['Python in Rhino']
origin:
order: 6
keywords: ['script', 'Rhino', 'python']
layout: toc-guide-page
---
 
## Objects

Rhino can create and manipulate a number of geometric objects, including points, point clouds, curves, surfaces, B-reps, meshes, lights, annotations, and references.  Each object in the Rhino document is identified by a globally unique identifier, or GUID, that is generated and assigned to objects when they are created.  Because identifiers are saved in the 3DM file, an object's identifier will be the same between editing sessions.

To view an object's unique identifier, use Rhino's Properties command.

For convenience, RhinoScriptSyntax returns object identifiers in the form of a string.  For example, an object's identifier will look something like the following:

F6E01514-3264-4598-8A07-A58BFE739C38

The majority of RhinoScriptSyntax's object manipulation methods require one or more object identifiers to be acquired before the method can be executed.

## Geometry and Attributes

Rhino objects consist of two components: the object's geometry and the object's attributes.

The types of geometry support by Rhino include points, point clouds, curves, surfaces, polysurfaces, extrusions, meshes, annotations and dimensions, and other.

The attributes of an object include such properties as object color, layer, linetype, render material, group membership, and more.

## Example

Here is an example using Object IDs to work reference geometry:

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
---

## Related Topics

- [What is Python and RhinoScript?]({{ site.baseurl }}/guides/rhinopython/what-are-python-rhinoscript)
- [Points]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-points)
- [Vectors]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-vectors)
- [Lines]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-lines)
- [Planes]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-planes)
- [Rhino NURBs Geometry]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-nurbs)
