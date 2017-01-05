---
title: 2.3.5 Using variables
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

Conventionally, whenever we intend to use variables in a script, we would have to declare them first.  However, with Python, we are relieved of this duty and we can simply create and use variables without initially declaring them. Python also does not require that we declare the type of variable we are using, as in other programming languages.  Both of these qualities emphasize why Python is such a quick and easy to learn language. So, to declare a variable we simply write: 

```python
a = "Apfelstrudel"
```

When using a variable, you choose the name and then set it equal to a value (Number, String, Boolean etc).The name you get to pick yourself. In the example above we have used a, which is not the best of all possible choices. For one, it doesn't tell us anything about what the variable is used for or what kind of data it contains. A better name would be `strFood`. The str prefix indicates that we are dealing with a String variable here and the Food bit is hopefully fairly obvious. A widely used system for variable prefixes is as follows:

<img src="{{ site.baseurl }}/images/primer-variable-type.svg" width="60%" height="300px">

Don't worry about all those weird variable types, some we will get to in later chapters, others you will probably never use. The scope (sometimes called "lifetime") of a variable refers to the region of the script where it is accessible. Whenever you declare a variable inside a function, only that one function can read and write to it. Variables go 'out of scope' whenever their containing function terminates. 'Lifetime' is not a very good description in my opinion, since some variables may be very much alive, yet unreachable due to being in another scope. But we'll worry about scopes once we get to function declarations. For now, let's just look at an example with proper variable usage:

```python
strComplaint = "I don't like "
strFood = "Apfelstrudel. "
strNag = "Can I go now?"

print(strComplaint + strFood + strNag)
```

An important note to reiterate is Python's case sensitivity.  Unlike other languages, in Python "Apfelstrudel", "apfelstrudel" and "ApfelStrudel" are not equivalent, this is also true for all variable names, functions, classes and any other part of the code. Just remember to be very careful with upper and lower case letters!

Now, high time for an example. We'll be using the macro from page 2, but we'll replace some of the hard coded numbers with variables for added flexibility. This script looks rather intimidating, but keep in mind that the messy looking bits (line 10 and beyond) are caused by the script trying to mimic a macro, which is a bit like trying to drive an Aston-Martin down the sidewalk. Usually, we talk to Rhino directly without using the command-line and the code looks much friendlier:


|--:|:---------------|
|  1|import rhinoscriptsyntax as rs |
|  2|
|  3|dblMajorRadius = rs.GetReal("Major radius", 10.0, 1.0, 1000.0) |
|  4|dblMinorRadius = rs.GetReal("Minor radius", 2.0, 0.1, 100.0) |
|  5|intSides = rs.GetInteger("Number of sides", 6, 3, 20) |

strPoint1 = " w" + str(dblMajorRadius) + ",0,0"
strPoint2 = " w" + str(dblMajorRadius + dblMinorRadius) + ",0,0"

rs.Command ("_SelNone")
rs.Command ("_Polygon _NumSides=" + str(intSides) + " w0,0,0" + strPoint1)
rs.Command ("_SelLast")
rs.Command ("-_Properties _Object _Name Rail _Enter _Enter")
rs.Command ("_SelNone")
rs.Command ("_Polygon _NumSides=" + str(intSides) + strPoint1 + strPoint2)
rs.Command ("_SelLast")
rs.Command ("_Rotate3D w0,0,0 w1,0,0 90")
rs.Command ("-_Properties _Object _Name Profile _Enter _Enter")
rs.Command ("_SelNone")
rs.Command ("-_Sweep1 _SelName Rail _SelName Profile _Enter _Enter _Closed=Yes _Enter")
rs.Command ("_SelName Rail")
rs.Command ("_SelName Profile")
rs.Command ("_Delete")

<!--TODO: This page is not finished.  Needs a lot of formatting tricks-->

---

#### Related Topics

- [Where to find help - Next Topic >>]({{ site.baseurl }}/guides/rhinopython/primer-101/1-2-where-to-find-help/)
- [Rhino.Python Primer 101]({{ site.baseurl }}/guides/rhinopython/primer-101/rhinopython101)
- [Running Scripts]({{ site.baseurl }}/guides/rhinopython/python-running-scripts)
- [Canceling Scripts]({{ site.baseurl }}/guides/rhinopython/python-canceling-scripts)
- [Editing Scripts]({{ site.baseurl }}/guides/rhinopython/python-editing-scripts)
- [Scripting Options]({{ site.baseurl }}/guides/rhinopython/python-scripting-options)
- [Reinitializing Python]({{ site.baseurl }}/guides/rhinopython/python-scripting-reinitialize)
