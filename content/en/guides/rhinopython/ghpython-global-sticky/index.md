+++
aliases = ["/en/5/guides/rhinopython/ghpython-global-sticky/", "/en/6/guides/rhinopython/ghpython-global-sticky/", "/en/7/guides/rhinopython/ghpython-global-sticky/", "/wip/guides/rhinopython/ghpython-global-sticky/"]
authors = [ "scottd" ]
categories = [ "GhPython" ]
description = "Create a variable that sticks around for other components."
keywords = [ "python", "commands", "grasshopper" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "Creating Global Sticky Variables"
type = "guides"
weight = 5
override_last_modified = "2018-12-05T14:59:06Z"
draft = false

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac", "Grasshopper" ]
since = 7
until = ""

[page_options]
block_webcrawlers = false
byline = true
toc = true
toc_type = "single"

+++

Sometimes there is a need to share information between Grasshopper and Rhino.Python.  This can be done through a global [sticky variable](http://developer.rhino3d.com/samples/rhinopython/sticky-values/) creating a definition wide global sticky variable. Both Rhino.Python and gh.python use the same Python instance, so the Python sticky is shared between the two.

With a global sticky variable all the components in a definition can access the information.

As an example, here is a definition that creates a simple sticky variable and passes it to another component that is not connected:



{{< image url="/images/sticky-ghpython.png" alt="/images/sticky-ghpython.png" class="image_center" width="65%" >}}


```python
import scriptcontext as rs

rs.sticky["someName"] = x #"x" is the input for the component

```

The scriptcontext.sticky creates a global variable names "someName".  This can be referenced in another component using this code:


```python
import scriptcontext as rs

a = rs.sticky["someName"] #output the value of the sticky

```

Within Rhino.Python, the same value can be accessed the same way through [Rhino.Python sticky](http://developer.rhino3d.com/samples/rhinopython/sticky-values/).

## Related Topics

- [Your first script with Python in Grasshopper](/guides/rhinopython/what-is-rhinopython)
- [What is Python and RhinoScript?](/guides/rhinopython/what-is-rhinopython)
- [Editing Python in Grasshopper](/guides/rhinopython/python-running-scripts)
- [Python Guide for Rhino](/guides/rhinopython/)
