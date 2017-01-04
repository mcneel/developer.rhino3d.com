---
title: 2.3.4 None variable
description:
authors: ['Skylar Tibbits', 'Arthur van der Harten', 'Steve Baer']
author_contacts: ['steve']
apis: ['RhinoPython']
languages: ['Python']
platforms: ['Windows', 'Mac']
categories: ['Python Primer']
origin:
order: 11
keywords: ['python', 'commands']
layout: toc-guide-page
---

Whenever we ask Rhino a question which might not have an answer, we need a way for Rhino to say "I don't know". Using the example on page 5:

```python
curve = rs.AddLine([0,0,0], [somenumber,0,0])
```

It is not a certainty that a curve was created. If the user enters zero when he is asked to supply the value for somenumber, then the startpoint of the line would be coincident with the endpoint. Rhino does not like zero-length lines and will not add the object to the document. This means that the return value of `rs.AddLine()` is not a valid object ID. Almost all methods in Rhino will return a None variable if they fail, this way we can add error-checks to our script and take evasive action when something goes wrong: 

```python
curve = rs.AddLine([0,0,0], [somenumber,0,0])
if not curve:
   print "Something went terribly wrong!"
```

The statement, `if not x` in Python will return a value True if the variable "curve" is *None*, 0 or an empty list.


---

#### Related Topics

- [Where to find help - Next Topic >>]({{ site.baseurl }}/guides/rhinopython/primer-101/1-2-where-to-find-help/)
- [Rhino.Python Primer 101]({{ site.baseurl }}/guides/rhinopython/primer-101/rhinopython101)
- [Running Scripts]({{ site.baseurl }}/guides/rhinopython/python-running-scripts)
- [Canceling Scripts]({{ site.baseurl }}/guides/rhinopython/python-canceling-scripts)
- [Editing Scripts]({{ site.baseurl }}/guides/rhinopython/python-editing-scripts)
- [Scripting Options]({{ site.baseurl }}/guides/rhinopython/python-scripting-options)
- [Reinitializing Python]({{ site.baseurl }}/guides/rhinopython/python-scripting-reinitialize)
