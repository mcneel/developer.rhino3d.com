+++
authors = [ "dale" ]
categories = [ "Python in Rhino" ]
description = "This guide provides an overview of the RhinoScriptSyntax in Python."
keywords = [ "script", "Rhino", "python" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "RhinoScriptSyntax in Python"
type = "guides"
weight = 1
override_last_modified = "2019-10-24T16:29:52Z"

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

- [Points](/guides/rhinopython/python-rhinoscriptsyntax-points)
- [List of Points](/guides/rhinopython/python-rhinoscriptsyntax-list-points)
- [Vectors](/guides/rhinopython/python-rhinoscriptsyntax-vectors)
- [Lines](/guides/rhinopython/python-rhinoscriptsyntax-line)
- [Planes](/guides/rhinopython/python-rhinoscriptsyntax-plane)
- [Rhino Geometry Objects](/guides/rhinopython/python-rhinoscriptsyntax-objects)

Creating, accessing and manipulating geometry is one of the first places RhinoScriptSyntax is used.  Simple geometry such as points, lines, and planes can be described with lists in Python.  More complicated geometry objects such as NURBS curves, Surfaces and Poly-surfaces can be created by Rhino and referenced by an object ID in RhinoScriptSyntax.
