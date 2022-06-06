+++
aliases = ["/5/guides/rhinopython/ghpython-question-answer/", "/6/guides/rhinopython/ghpython-question-answer/", "/7/guides/rhinopython/ghpython-question-answer/", "/wip/guides/rhinopython/ghpython-question-answer/"]
authors = [ "scottd" ]
categories = [ "GhPython" ]
description = "Here are the most common questions and answers about GhPython."
keywords = [ "python", "commands", "grasshopper" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "GhPython Common Questions and Answers"
type = "guides"
weight = 4
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac", "Grasshopper" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

The GhPython component allows to use both RhinoCommon and RhinoScript from within Grasshopper. Here some Q&As.

### How can I use the rhinoscriptsyntax?

By importing RhinoScript, for example by writing:

`import rhinoscriptsyntax as rs`

...and then calling some rhinoscript functions...

```python
import rhinoscriptsyntax as rs

line = rs.AddLine((1, 2, 3), (10, 11, 12))
a = line
```

### How can I use RhinoCommon?

By importing from the Rhino module, for example by writing:

`from Rhino.Geometry import Point3d, Line`

...and then assigning some new geometry to the results

```python
from Rhino.Geometry import Point3d, Line

a = Line(Point3d(1, 2, 3), Point3d(10, 11, 12))
```

### What is "ghdoc" and how does it relate to the rhinoscriptsyntax?

The `ghdoc` variable is provided by the component for better RhinoScript library support.

This library is imperative, and it is build from a set of functions that act on geometrical types through one level of indirection: most of the time, the user does not work with the geometry itself but with an identifier (Guid) of geometry that is present in a document.

This is exactly what ghdoc is: it is a reference to the document that the RhinoScript library implicitly targets with all Add__() calls (for example, AddLine()).

The scriptcontext module has a doc variable with the currently active document, that can be assigned by you to ghdoc, or RhinoDoc.ActiveDoc, the Rhino document.

### Is RhinoScript use within GhPython less ideal than RhinoCommon?

While targeting the `ghdoc` variable, the special Grasshopper document is used, therefore we can use Grasshopper while leaving the Rhino document unchanged. This saves uncountable Undo's, and makes it easy to structure ideas through the Grasshopper definition.

This means that both RhinoCommon or RhinoScript are good in practice.

### Is the rhinoscriptsyntax target irrelevant if using solely RhinoCommon classes?

Yes. If you create class instances (objects), you will need to create also your own collection objects to store them (mostly lists, trees). You can imagine the `ghdoc` as being an alternative to them, just that you do not access data by index (number), but by Guid. So you can use the RhinoScript or the RhinoCommon libraries independently or mix them. The RhinoScript implementation in Rhino is open-source and is all written in RhinoCommon. Also the `ghdoc` implementation is open-source, and is here.

### Are there RhinoScript and/or RhinoCommon objects which are not recognized as valid Grasshopper geometry?

Yes, sure, Grasshopper handles only a portion of all available types.

Basically, unhandled types are all the types that do not exists in the 'Params' tab.

For example, there is no text dot and no leader. When/if Grasshopper one day will support these types, these calls will be implemented.

### How do I use DataTree's?

[Here](http://www.grasshopper3d.com/forum/topics/datatreelistitem-access-from) is a small sample.

However, 80% of the times it is not necessary to program for DataTrees, as the logic itself can be applied per-list and Grasshopper handles list-iteration.

**If you have more questions, please go to the [Rhino Developers Forum](https://discourse.mcneel.com/c/rhino-developer)**

## Related Topics

- [Your first script with Python in Grasshopper](/guides/rhinopython/what-is-rhinopython)
- [What is Python and RhinoScript?](/guides/rhinopython/what-is-rhinopython)
- [Editing Python in Grasshopper](/guides/rhinopython/python-loading-scripts)
- [Python Guide for Rhino](/guides/rhinopython/)
