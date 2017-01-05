---
title: 2.1 Language origin
description:
authors: ['Scott Davidson']
author_contacts: ['scottd']
apis: ['RhinoPython']
languages: ['Python']
platforms: ['Windows', 'Mac']
categories: ['Python Primer']
origin:
order: 4
keywords: ['python', 'commands']
layout: toc-guide-page
---

Like conversational languages, programming languages group together in clusters. Python is a high level language, indicating that the language was designed to be easy for humans to understand.  On the opposite end of the spectrum are extremely low level languages, (often referred to as machine-code), that are most definitely not easy to understand.  In between are languages such as C or C++ which offer layers of abstraction above machine-code.  As I mentioned, Python is a step even higher, meaning that it is far easier to read (closer to the English language) and we don't need to manage difficult functionality like memory allocation, or declaring variables!

Lucky us.

Python was first released in 1991, since then it has grown to become freely available with a user-group exceeding tens of thousands.  The Python documentation claims, " Python plays well with others," " Python runs everywhere," " Python is friendly... and easy to learn" and " Python is Open!"  For more information about the Python programming language and its development see: [http://www.python.org](http://www.python.org).

Assuming that you might be reading these pages without any prior programming experience whatsoever, I still dare guess that the following example will not give you much trouble:

```python
import rhinoscriptsyntax as rs

somenumber = rs.GetReal("Line length")
line = rs.AddLine([0,0,0], [somenumber,0,0])
print "Line curve inserted with id", line
```
Of course you might have no conception of what [0,0,0] actually means and you might be confused by rs.GetReal() but on the whole it is pretty much the same as the English you use at the grocers:

```
Ask Rhino to assign a number to something called 'somenumber'.
Tell Rhino to add a line from the world origin to the point on the x-axis indicated by 'somenumber'
print a success message
```

Translating Python code to and from regular English should not be very difficult, at least not at this featherweight level. It is possible to convolute the code so that it becomes unreadable, but this is not something you should take pride in. The syntax resembles English for a good reason, I suggest we stick to it.

As mentioned before, there are three things the syntax has to support, and the above script uses them all:

1. Flow control		» Depending on the outcome of the second line, some lines are not run
2. Variable data		» somenumber is used to store a variable number
3. Communication		» The user is asked to supply information and is informed about the result
 
---

#### Related Topics

- [Where to find help - Next Topic >>]({{ site.baseurl }}/guides/rhinopython/primer-101/1-2-where-to-find-help/)
- [Rhino.Python Primer 101]({{ site.baseurl }}/guides/rhinopython/primer-101/rhinopython101)
- [Running Scripts]({{ site.baseurl }}/guides/rhinopython/python-running-scripts)
- [Canceling Scripts]({{ site.baseurl }}/guides/rhinopython/python-canceling-scripts)
- [Editing Scripts]({{ site.baseurl }}/guides/rhinopython/python-editing-scripts)
- [Scripting Options]({{ site.baseurl }}/guides/rhinopython/python-scripting-options)
- [Reinitializing Python]({{ site.baseurl }}/guides/rhinopython/python-scripting-reinitialize)
