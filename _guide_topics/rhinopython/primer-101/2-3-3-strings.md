---
title: 2.3.3 Strings
description:
authors: ['Skylar Tibbits', 'Arthur van der Harten', 'Steve Baer']
author_contacts: ['steve']
apis: ['RhinoPython']
languages: ['Python']
platforms: ['Windows', 'Mac']
categories: ['Python Primer']
origin:
order: 10
keywords: ['python', 'commands']
layout: toc-guide-page
---

Strings are used to store text. Whenever you add quotes around stuff in Python, it automatically becomes a String. So if we encapsulate a number in quotes, it will become text:

```python
variable1 = 5
variable2 = "5"
```

You could print these variables to the command line and they would both look like 5, but the String variable behaves differently once we start using it in calculations:

```python
print (variable1 + variable2)        # Results in an "Unsupported Operand Type" Error
```

Python throws an error when we try to add a String variable to an Integer Variable.  We must first convert the string to an integer, then we can add them together.

```python
print (variable1 + int(variable2))        # Results in 10
```

When you need to store text, you have no choice but to use Strings. The syntax for Strings is quite simple, but working with Strings can involve some very tricky code. For the time being we’ll only focus on simple operations such as assignment and concatenation:

```python
a = "Apfelstrudel"                # Apfelstrudel
a = "Apfel" + "strudel"                # Apfelstrudel
a = "4" + " " + "Apfelstrudel"            # 4 Apfelstrudel
a = "The sqrt of 2.0 = " + str(math.sqrt(2.0))    # The sqrt of 2.0 = 1.4142135623731 
```

Internally, a String is stored as a series of characters. Every character (or 'char') is taken from the Unicode table, which stores a grand total of ~100.000 different characters. The index into the unicode table for the question mark for example is 63, lowercase e is 101 and the blank space is 32:

<img src="{{ site.baseurl }}/images/primer-strings.svg" width="75%" align="middle">

Further down the road we'll be dealing with some advanced String functions which will require a basic 
understanding of how Strings work, but while we are still just using the simple stuff, it's good enough to know it just works the way you expect it to. 

Strings are used heavily in RhinoScript since object IDs are always written as strings. Object IDs are those weird codes that show up in the Object Property Details: *D7EFCF0A-DB47-427D-9B6B-44EC0670C573*. IDs are designed to be absolutely unique for every object which will ever exist in this universe, which is why we can use them to safely and unambiguously identify objects in the document.



---

#### Related Topics

- [Where to find help - Next Topic >>]({{ site.baseurl }}/guides/rhinopython/primer-101/1-2-where-to-find-help/)
- [Rhino.Python Primer 101]({{ site.baseurl }}/guides/rhinopython/primer-101/rhinopython101)
- [Running Scripts]({{ site.baseurl }}/guides/rhinopython/python-running-scripts)
- [Canceling Scripts]({{ site.baseurl }}/guides/rhinopython/python-canceling-scripts)
- [Editing Scripts]({{ site.baseurl }}/guides/rhinopython/python-editing-scripts)
- [Scripting Options]({{ site.baseurl }}/guides/rhinopython/python-scripting-options)
- [Reinitializing Python]({{ site.baseurl }}/guides/rhinopython/python-scripting-reinitialize)
