---
title: 1.2 Scripts
description:
authors: ['Scott Davidson']
author_contacts: ['scott']
apis: ['RhinoPython']
languages: ['Python']
platforms: ['Windows', 'Mac']
categories: ['Python Primer']
origin:
order: 2
keywords: ['python', 'commands']
layout: toc-guide-page
---

The limitations of macros have led to the development of scripting languages. Scripts are something halfway between macros and true (compiled) programs and plug-ins. Unlike macros they can perform 
mathematical operations, evaluate variable conditions, respond to their environment and communicate with the user. Unlike programs they do not need to be compiled prior to running. Rhinoceros implements the standard 
‘Microsoft® Visual Basic® Scripting Edition’ language, as well as the Python Programming language.  This primer will introduce the Python Programming Language and how to utilize its functionality within Rhinoceros.

Scripts, then, are text files which are interpreted one line at a time. But here’s the interesting part; unlike macros, scripts have control over which line is executed next. This flow control enables the script to skip certain instructions or to repeat others. Flow control is achieved by what is called "conditional evaluation" and we must familiarize ourselves with the language rules of Python before we can take advantage of flow control.

The language rules are usually referred to as the syntax and they indicate what is and isn’t valid:

1. "There is no apple cake here."		» valid
1. "There is here no apple cake"		» invalid
1. "Here, there is no apple cake."		» valid
1. "There is no Apfelstrudel here."		» invalid

The above list is a validity check for English syntax rules. The first and third lines are proper English and the others are not. However, there are certain degrees of wrong. Nobody will misunderstand the second line just because the word order is wrong. The forth line is already a bit harder since it features a word from a different language.

Although most of us are smart enough to understand all four lines, a computer is not. 

Python is a wonderful language for beginners or advanced programmers.  It offers a simple and efficient syntax as well as powerful programming functions, object-oriented capabilities and a large fan-base with user-built libraries.  Also, since Rhino Python is available on both Windows and Mac, the exact same python scripts will run on both versions of Rhino!  Don't get too excited yet - will get more of the details in the following sections!

---

#### Related Topics

- [Where to find help - Next Topic >>]({{ site.baseurl }}/guides/rhinopython/primer-101/1-2-where-to-find-help/)
- [Rhino.Python Primer 101]({{ site.baseurl }}/guides/rhinopython/primer-101/rhinopython101)
- [Running Scripts]({{ site.baseurl }}/guides/rhinopython/python-running-scripts)
- [Canceling Scripts]({{ site.baseurl }}/guides/rhinopython/python-canceling-scripts)
- [Editing Scripts]({{ site.baseurl }}/guides/rhinopython/python-editing-scripts)
- [Scripting Options]({{ site.baseurl }}/guides/rhinopython/python-scripting-options)
- [Reinitializing Python]({{ site.baseurl }}/guides/rhinopython/python-scripting-reinitialize)
