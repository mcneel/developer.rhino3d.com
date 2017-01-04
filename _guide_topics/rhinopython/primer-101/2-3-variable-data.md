---
title: 2.3 Variable data
description:
authors: ['Scott Davidson']
author_contacts: ['scott']
apis: ['RhinoPython']
languages: ['Python']
platforms: ['Windows', 'Mac']
categories: ['Python Primer']
origin:
order: 6
keywords: ['python', 'commands']
layout: toc-guide-page
---

Whenever we want our code to be dynamic we have to make sure it can handle all kinds of different situations. In order to do that we must have the ability to store variables. For instance we might want to store a selection of curves in our 3D model so we can delete them at a later stage. Or perhaps our script needs to add a line from the mouse pointer to the origin of the 3D scene. Or we need to check the current date to see whether or not our software has expired. This is information which was not available at the time the script was written.

Whenever we need to store data or perform calculations or logic operations we need variables to remember the results. Since these operations are dynamic we cannot add them to the script prior to execution. We need placeholders.

In the example on the previous page the thing named *"somenumber"* is a placeholder for a number. It starts out by being just a name without any data attached to it, but it will be assigned a numeric value in the line:

```python
somenumber = rs.GetNumber("Line length")
```

Then later on we retrieve that specific value when we add the line curve to Rhino:

```python
curve = rs.AddLine([0,0,0], [somenumber,0,0])
```

All the other coordinates that define the line object are hard-coded into the script. There is no limit to how often a variable can be read or re-assigned a new value, but it can never contain more than one value and there’s no undo system for retrieving past values. Apart from numbers we can also store other types of data in variables. For the time being, we’ll restrict ourselves to the four most essential ones, plus a special one which is used for error-trapping:

1. Integers
2. Doubles
3. Booleans
4. Strings
5. Null variable

---

#### Related Topics

- [Where to find help - Next Topic >>]({{ site.baseurl }}/guides/rhinopython/primer-101/1-2-where-to-find-help/)
- [Rhino.Python Primer 101]({{ site.baseurl }}/guides/rhinopython/primer-101/rhinopython101)
- [Running Scripts]({{ site.baseurl }}/guides/rhinopython/python-running-scripts)
- [Canceling Scripts]({{ site.baseurl }}/guides/rhinopython/python-canceling-scripts)
- [Editing Scripts]({{ site.baseurl }}/guides/rhinopython/python-editing-scripts)
- [Scripting Options]({{ site.baseurl }}/guides/rhinopython/python-scripting-options)
- [Reinitializing Python]({{ site.baseurl }}/guides/rhinopython/python-scripting-reinitialize)
