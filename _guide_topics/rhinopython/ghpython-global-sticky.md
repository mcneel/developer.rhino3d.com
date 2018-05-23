---
title: Creating Global Sticky Variables
description: Create a variable that sticks around for other components.
authors: ['Scott Davidson']
author_contacts: ['scottd']
sdk: ['RhinoPython']
languages: ['Python']
platforms: ['Windows', 'Mac', 'Grasshopper']
categories: ['GhPython']
origin:
order: 5
keywords: ['python', 'commands', 'grasshopper']
layout: toc-guide-page
---

Sometimes there is a need to share information between Grasshopper and Rhino.Python.  This can be done through a global [sticky variable](http://developer.rhino3d.com/samples/rhinopython/sticky-values/) creating a definition wide global sticky variable. Both Rhino.Python and gh.python use the same Python instance, so the Python sticky is shared between the two.

With a global sticky variable all the components in a definition can access the information.

As an example, here is a definition that creates a simple sticky variable and passes it to another component that is not connected:



![{{ site.baseurl }}/images/sticky-ghpython.png]({{ site.baseurl }}/images/sticky-ghpython.png){: .img-center width="65%"}


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

---

## Related Topics

- [Your first script with Python in Grasshopper]({{ site.baseurl }}/guides/rhinopython/what-are-python-rhinoscript)
- [What is Python and RhinoScript?]({{ site.baseurl }}/guides/rhinopython/what-are-python-rhinoscript)
- [Editing Python in Grasshopper]({{ site.baseurl }}/guides/rhinopython/python-loading-scripts)
- [Python Guide for Rhino]({{ site.baseurl }}/guides/rhinopython/)
