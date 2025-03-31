+++
aliases = ["/en/5/guides/general/rhino-developer-prerequisites/", "/en/6/guides/general/rhino-developer-prerequisites/", "/en/7/guides/general/rhino-developer-prerequisites/", "/en/wip/guides/general/rhino-developer-prerequisites/"]
authors = [ "dan", "callum" ]
categories = [ "Getting Started" ]
description = "This guide describes the main requirements to develop for Rhino."
keywords = [ "developer", "rhino" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "Developer Prerequisites"
type = "guides"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/learningresources"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"
+++


There are a number of prerequisites required to do Rhino development.  Broadly speaking, these can be divided into three categories, ranked in ascending order of difficulty:

1. [Hardware prerequisites](#hardware)
1. [Software prerequisites](#software)
1. [Programming Knowledge](#programming-knowledge)

## Hardware

If you are reading this guide, you likely already have a computer that can run Rhino. (If not, Rhino has some minimum [System Requirements](http://www.rhino3d.com/system_requirements/) that you should review before acquiring any hardware).  Generally speaking, any computer that can run Rhino *ought* to be able to run the developer tools outlined in the [Software](#software) section.

If you are a Windows user and wish to develop plugins for Rhino for Mac, you will need an Apple Mac computer.  Conversely, if you are an macOS user and you wish to develop for Rhino for Windows, you will need a computer that can run Rhino for Windows (however, virtual machines running Windows under macOS can potentially work just fine).


## Software

Depending on what you want to do, the software prerequisites vary.  However, in general, you will need:

- [Rhinoceros](http://www.rhino3d.com/download)
- A code editor.  There are many options...here are a few:
   - [Visual Studio for Windows](https://www.visualstudio.com): Microsoft's flagship Integrated Development Environment (IDE) for Windows.
   - [Visual Studio Code](https://code.visualstudio.com/): The best free cross-platform editor

See the [SDK-specific guides](/guides/) for the software prerequisites...normally found in the *"Installing Tools"* guides.

## Programming Knowledge

Acquiring programming knowledge is the most labor intensive prerequisite.  However, learning to program - even trying out a new language - is fun and enriching.  Learning to program using Rhino is a great way to begin...

### Learning C# .NET

If you wish to write plugins with RhinoCommon, you will need to understand a .NET compatible programming language like C# (or VB).  We recommend [C#](https://en.wikipedia.org/wiki/C_Sharp_(programming_language)) (C Sharp) because it is modern, safe, and easy to learn - and you can develop in C# on both Windows and macOS.

*Watch*...

- [Beginning C# Programming](http://shop.oreilly.com/product/0636920036036.do) By Eric Lippert - Published by O'Reilly Media
- [C# Fundamentals for Absolute Beginners](https://learn.microsoft.com/en-us/shows/csharp-fundamentals-for-absolute-beginners/) on Microsoft's Virtual Academy
- [C# and .NET Essential Training](https://www.linkedin.com/learning/c-sharp-and-dot-net-essential-training) on LinkedIn Learning

*Read*...

- [Programming C# 5.0](http://shop.oreilly.com/product/0636920024064.do) By Ian Griffiths - Published by O'Reilly Media
- [C# 5.0 in a Nutshell](http://shop.oreilly.com/product/0636920023951.do) By Joseph Albahari, Ben Albahari - Published by O'Reilly Media

*Do*...

- [Check out samples](/samples/#rhinocommon) on this site
- [Ask for help on Discourse](http://discourse.mcneel.com/c/rhino-developer)

### Learning C/C++

To write plugins for Rhino using the C/C++ SDK, you first need to learn the [C++ programing language](https://en.wikipedia.org/wiki/C%2B%2B) itself.  C/C++ is sometimes considered an "advanced" programming language.

*Watch*...

- [C++: A General Purpose Language](https://learn.microsoft.com/en-us/shows/cplusplus-language-library/) on Microsoft Virtual Academy
- [C++ Essential Training](https://www.linkedin.com/learning/c-plus-plus-essential-training-15106801) with Bill Weinmann on LinkedIn Learning

*Read*...

- [The C Programming Language](https://en.wikipedia.org/wiki/The_C_Programming_Language) by Ian Kernighan and Dennis Ritchie
- [Practical C++ Programming](http://shop.oreilly.com/product/9780596004194.do) by Steve Oualline - Published by O'Reilly Media
- [C++ Primer Plus](http://www.amazon.com/Primer-Plus-Edition-Developers-Library/dp/0321776402) by Stephen Prata

*Do*...

- [Check out samples](/samples/#cc) on this site
- [Ask for help on Discourse](http://discourse.mcneel.com/c/rhino-developer)

### Learning Python

[Python](https://en.wikipedia.org/wiki/Python_(programming_language)) is a fantastic first language and an amazingly flexible additional language to add to your toolkit.

*Watch*...

- [Google's Python Class](https://developers.google.com/edu/python/) by Google for Education
- [Up and Running with Python](http://www.lynda.com/Python-tutorials/Up-Running-Python/122467-2.html) with Joe Marini on Lynda.com


*Read*...

- [The Python Tutorial](https://docs.python.org/2/tutorial/index.html)
- [RhinoPython Primer](http://www.rhino3d.com/download/IronPython/5.0/RhinoPython101) by Skylar Tibbits, Arthur van der Harten, Steve Baer, and David Rutten
- [The Python Tutorial](https://docs.python.org/2/tutorial/index.html) by the Python Software Foundation
- [Learn Python the Hard Way](http://learnpythonthehardway.org/book/) by Zed A. Shaw - despite the title, this is a beginner's book
- [Automate The Boring Stuff With Python](https://automatetheboringstuff.com/) by Al Sweigart

*Do*...

- [Check out samples](/samples/#rhinopython) on this site
- [Ask for help on Discourse](http://discourse.mcneel.com/c/scripting)

### Learning RhinoScript

RhinoScript is a scripting tool based on Microsoft's VBScript language.  RhinoScript runs in Rhino for Windows.

*Read*...

- [RhinoScript Primer](http://www.rhino3d.com/download/rhino/5.0/rhinoscript101) by David Rutten
- [Microsoft VBScript User's Guide and Language Reference](https://msdn.microsoft.com/en-us/library/t0aew7h6(VS.85).aspx)

*Do*...

- [Check out samples](/samples/#rhinoscript) on this site
- [Ask for help on Discourse](http://discourse.mcneel.com/c/scripting)

### Learning More

- [Crafting Interpreters](https://craftinginterpreters.com/) by Robert Nystrom
- [Clean Code](https://www.oreilly.com/library/view/clean-code-a/9780136083238/) by Robert C. Martin


## Related topics

- [What is a Rhino Plugin?](/guides/general/what-is-a-rhino-plugin/)
- <a href="https://en.wikipedia.org/wiki/C_Sharp_(programming_language">C Sharp on Wikipedia</a>
- [C++ on Wikipedia](https://en.wikipedia.org/wiki/C%2B%2B)
- [Python on Wikipedia](https://en.wikipedia.org/wiki/Python_(programming_language))
