+++
aliases = ["/5/guides/rhinopython/python-rhinoscriptsyntax-color/", "/6/guides/rhinopython/python-rhinoscriptsyntax-color/", "/7/guides/rhinopython/python-rhinoscriptsyntax-color/", "/wip/guides/rhinopython/python-rhinoscriptsyntax-color/"]
authors = [ "scottd" ]
categories = [ "Python in Rhino" ]
description = "This guide provides an overview of a RhinoScriptSyntax Color type in Python."
keywords = [ "script", "Rhino", "python" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "Colors in Python"
type = "guides"
weight = 4
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Mac", "Windows" ]
since = 0
version = [ "8" ]

[page_options]
byline = true
toc = true
toc_type = "single"

+++

## Colors

Colors in Rhino are represented as  zero-based, one-dimensional arrays that contain four values.  The first 3 values are the Red, Green and Blue channels.  Each channel may contain a value from 0 to 255.  The fourth value is the Alpha Channel.  This control transparency of the color.  0 is completely transparent and the default value of 255 is completely opaque. 

```
color contains [Red, Green, Blue, Alpha]
```

Use the `CreateColor()` function to create a new color structure:

```python
import rhinoscriptsytnax as rs

color1 = rs.CreateColor(128, 128, 128) # Creates a medium grey color.
```

The `CreateColor()` function assumes the alpha value is 255 by default. 

```python
import rhinoscriptsyntax as rs

col = rs.CreateColor(43,45,56)

print col[0]
print col[1]
print col[2]
```
Unlike many other Rhino types, colors are immutable.  This means you cannot set one channel by itself, but must always create a new color when trying to make a color.  Setting one channel will not work, for instance `color1[1] = 56` will throw an error. 

Here is a table of commonly used colors:

| Color       |      |  Red |      | Green |      | Blue |
| ----------- | ---- | ---: | ---- | ----: | ---- | ---: |
| Black       |      |    0 |      |     0 |      |    0 |
| White       |      |  255 |      |   255 |      |  255 |
| Medium Gray |      |  128 |      |   128 |      |  128 |
| Aqua        |      |    0 |      |   128 |      |  128 |
| Navy Blue   |      |    0 |      |     0 |      |  128 |
| Green       |      |    0 |      |   255 |      |    0 |
| Orange      |      |  255 |      |   165 |      |    0 |
| Yellow      |      |  255 |      |   255 |      |    0 |

For more colors see an [Online RGB Color table](http://www.rapidtables.com/web/color/RGB_Color.htm#color-table). 

## Related Topics

- [What is Python and RhinoScript?](/guides/rhinopython/what-is-rhinopython)
- [Python Points](/guides/rhinopython/python-rhinoscriptsyntax-points)
- [Python Vectors](/guides/rhinopython/python-rhinoscriptsyntax-vectors)
- [Python Lines](/guides/rhinopython/python-rhinoscriptsyntax-lines)
- [Python Planes](/guides/rhinopython/python-rhinoscriptsyntax-planes)
- [Python Objects](/guides/rhinopython/python-rhinoscriptsyntax-objects)
