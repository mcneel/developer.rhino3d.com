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

<img src="{{ site.baseurl }}/images/primer-valriable-type.svg" width="60%" align="middle">


Don't worry about all those weird variable types, some we will get to in later chapters, others you will probably never use. The scope (sometimes called "lifetime") of a variable refers to the region of the script where it is accessible. Whenever you declare a variable inside a function, only that one function can read and write to it. Variables go 'out of scope' whenever their containing function terminates. 'Lifetime' is not a very good description in my opinion, since some variables may be very much alive, yet unreachable due to being in another scope. But we'll worry about scopes once we get to function declarations. For now, let's just look at an example with proper variable usage:

strComplaint = "I don't like "
strFood = "Apfelstrudel. "
strNag = "Can I go now?"

print(strComplaint + strFood + strNag)

An important note to reiterate is Python's case sensitivity.  Unlike other languages, in Python "Apfelstrudel", "apfelstrudel" and "ApfelStrudel" are not equivalent, this is also true for all variable names, functions, classes and any other part of the code. Just remember to be very careful with upper and lower case letters!

Now, high time for an example. We'll be using the macro from page 2, but we'll replace some of the hard coded numbers with variables for added flexibility. This script looks rather intimidating, but keep in mind that the messy looking bits (line 10 and beyond) are caused by the script trying to mimic a macro, which is a bit like trying to drive an Aston-Martin down the sidewalk. Usually, we talk to Rhino directly without using the command-line and the code looks much friendlier:

---

#### Related Topics

- [Where to find help - Next Topic >>]({{ site.baseurl }}/guides/rhinopython/primer-101/1-2-where-to-find-help/)
- [Rhino.Python Primer 101]({{ site.baseurl }}/guides/rhinopython/primer-101/rhinopython101)
- [Running Scripts]({{ site.baseurl }}/guides/rhinopython/python-running-scripts)
- [Canceling Scripts]({{ site.baseurl }}/guides/rhinopython/python-canceling-scripts)
- [Editing Scripts]({{ site.baseurl }}/guides/rhinopython/python-editing-scripts)
- [Scripting Options]({{ site.baseurl }}/guides/rhinopython/python-scripting-options)
- [Reinitializing Python]({{ site.baseurl }}/guides/rhinopython/python-scripting-reinitialize)
