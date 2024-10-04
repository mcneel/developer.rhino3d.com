+++
aliases = ["/en/5/guides/rhinopython/python-rhinoscriptsyntax-line/", "/en/6/guides/rhinopython/python-rhinoscriptsyntax-line/", "/en/7/guides/rhinopython/python-rhinoscriptsyntax-line/", "/wip/guides/rhinopython/python-rhinoscriptsyntax-line/"]
authors = [ "dale" ]
categories = [ "Python in Rhino" ]
description = "This guide provides an overview of a RhinoScriptSytntax Line Geometry in Python."
keywords = [ "script", "Rhino", "python" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "Lines in Python"
type = "guides"
weight = 4
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

## Lines

3-D lines, or chords, are represented as  zero-based, one-dimensional arrays that contain two elements:  the starting 3-D point and the ending 3-D point.  A 3-D line is represented by a start pint and an ednpoint.


line1 = ((1.0, 2.0, 3.0), (4.0, 5.0, 6.0))

To add the line to the current Rhino file, and see it drawn on screen, you can use the `AddLine` method in RhinoscriptSytnax:

```python
import rhinoscriptsyntax as rs

startPoint = (1.0, 2.0, 3.0)
endPoint = (4.0, 5.0, 6.0)

lineID = rs.AddLine(startPoint,endPoint)

print(lineID)
```

When adding geometry to Rhino, rhinoscriptsyntax will return an 'Object ID' for the added object. The Rhino file has the object added as geometry in the file. Just like an object added using a Rhino command, it has an ID that is a unique reference to this object. This makes it possible and easy to get access to the specific object later in the script.  Saving this ID in a variable or a list is what allows it to be used later to select and manipulate the object.

RhinoScript contains a number of methods to manipulate lines.  See [Lines and Planes](/guides/rhinopython/python-rhinoscriptsyntax-line-plane-methods) for details.

## Related Topics

- [What is Python and RhinoScript?](/guides/rhinopython/what-is-rhinopython)
- [Python Points](/guides/rhinopython/python-rhinoscriptsyntax-points)
- [Python Vectors](/guides/rhinopython/python-rhinoscriptsyntax-vectors)
- [Python Lines](/guides/rhinopython/python-rhinoscriptsyntax-lines)
- [Python Planes](/guides/rhinopython/python-rhinoscriptsyntax-planes)
- [Python Objects](/guides/rhinopython/python-rhinoscriptsyntax-objects)
