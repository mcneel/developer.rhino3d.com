---
title: Rhinoscript Syntax in Python
description: This guide provides an overview of the RhinoScriptSytntax in Python.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['RhinoPython']
languages: ['Python']
platforms: ['Mac', 'Windows']
categories: ['Python in Rhino']
origin:
order: 1
keywords: ['script', 'Rhino', 'python']
layout: toc-guide-page
---

## Overview

The RhinoScriptSyntax methods library contains hundreds of easy-to-use functions that perform a variety of operations on Rhino.  The library allows Python to be aware of the Rhino's:

* Geometry
* Commands
* Document objects
* Application methods

To make these methods easy-to-use, all RhinoScriptSyntax methods return simple Python variables or Python List-based data structures. Thus, once you are familiar with Python, you will be able to use any and all functions in the RhinoScriptSyntax methods library.

## Importing RhinoScriptSyntax

Before using RhinoScriptSyntax a line must be added to the top of each Python file to allow access to the RhinoScriptSyntax:

```pyhon
import rhinoscriptsyntax as rs
```

The `import` above not only imports the library, but also renames the namespace to `rs.`.  This is done to just make it easier to type when accessing the methods in RhinoScriptSyntax.  Access the methods by starting methods with 'rs.'.  For example, the `Addpoint()` method in the RhinoScriptSyntax namespace can  be entered:

```python
import rhinoscriptsyntax as rs

centerpoint = [1, 2, 4]
rs.AddCircle( centerpoint, 5.0 )
```

## Geometry

Creating, accessing and maniputlating Geometry is one of the primary uses for RhinoScriptSytnax in Rhino's implementation of Python.  Simple geometry such as points, lines, planes can be described with simple lists in Python.  More complicated geomtry objects such as NURBS curves, Surfaces and Polysurfaces can be created by Rhino and referenced by an object ID by RhinoScriptSyntax.

*Note:* Although not required, having some understanding of the computational methods used in 3-D modeling and computer graphics can be helpful when using RhinoScriptSyntax. A good introductory resource is the [Essential Mathematics for Computational Design](http://www.rhino3d.com/download/Rhino/4.0/EssentialMathematicsSecondEdition). This material is directed towards designers who have little or no background in mathematics beyond high school. And although all concepts are explained visually using Grasshopper®, they are directly applicable to RhinoScriptSyntax.

#### Basic Geometry

Here are the basic geometry types of RhinoScript:

- [Points]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-points)
- [List of Points]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-list-points)
- [Vectors]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-vectors)
- [Lines]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-lines)
- [Planes]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-planes)
- [Rhino Geometry Objects]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-objects)

Creating, accessing and maniputlating geometry is one of the first places RhinoScriptSytnax is used.  SImple geometry such as points, lines, planes can be described with simple lists in Python.  More complicated geometry objects such as NURBS curves, Surfaces and Poly-surfaces can be created by Rhino and referenced by an object ID by RhinoScriptSyntax.
