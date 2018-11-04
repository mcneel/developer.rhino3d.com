---
title: RhinoScriptSyntax in Python
description: This guide provides an overview of the RhinoScriptSyntax in Python.
authors: ['Dale Fugier']
author_contacts: ['dale']
sdk: ['RhinoPython']
languages: ['Python']
platforms: ['Mac', 'Windows']
categories: ['Python in Rhino']
origin:
order: 1
keywords: ['script', 'Rhino', 'python']
layout: toc-guide-page
---

## Overview

The RhinoScriptSyntax module contains hundreds of easy-to-use functions that perform a variety of operations on Rhino.  The library allows Python to be aware of Rhino's:

* Geometry
* Commands
* Document objects
* Application methods

To make these methods easy-to-use, all RhinoScriptSyntax methods return simple Python variables or Python List-based data structures. Thus, once you are familiar with Python, you will be able to use any and all functions in the RhinoScriptSyntax methods library.

## Importing RhinoScriptSyntax

Before using RhinoScriptSyntax a line must be added to the top of each Python file to allow access to RhinoScriptSyntax:

```pyhon
import rhinoscriptsyntax as rs
```

The `import` above not only imports the library, but also renames the module to `rs.`.  This is done to just make it easier to type when accessing the methods in RhinoScriptSyntax.  Access to the methods can now be made by starting methods with 'rs.'.  For example, accessing the `AddCircle()` method in the RhinoScriptSyntax module can be used to create a circle:

```python
import rhinoscriptsyntax as rs

centerpoint = [1, 2, 4]
rs.AddCircle( centerpoint, 5.0 )
```

## Geometry

Rhino is a 3D modeler, therefore creating and modifying geometry is key to developing in Rhino.  Here are the primitive geometry types of Rhino:

- [Points]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-points)
- [List of Points]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-list-points)
- [Vectors]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-vectors)
- [Lines]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-lines)
- [Planes]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-planes)
- [Rhino Geometry Objects]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-objects)

Creating, accessing and manipulating geometry is one of the first places RhinoScriptSyntax is used.  Simple geometry such as points, lines, and planes can be described with lists in Python.  More complicated geometry objects such as NURBS curves, Surfaces and Poly-surfaces can be created by Rhino and referenced by an object ID in RhinoScriptSyntax.
