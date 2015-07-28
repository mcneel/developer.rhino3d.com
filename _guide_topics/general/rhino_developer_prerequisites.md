---
layout: toc-guide-page
title: Developer Prerequisites
author: dan@mcneel.com
categories: ['General']
platforms: ['Cross-Platform']
apis: ['General']
languages: ['All']
keywords: ['developer', 'rhino']
TODO: 1
origin: http://wiki.mcneel.com/developer/learningresources
order: 1
---


# Developer Prerequisites
{: .toc-title }

There are a number of prerequisites required to do Rhino development.  Broadly speaking, these can be divided into three categories, ranked in ascending order of difficulty:

1. [Hardware prerequisites](#hardware)
1. [Software prerequisites](#software)
1. [Programming Knowledge](#programming-knowledge)

## Hardware
{: .toc-header }

If you are reading this guide, you likely already have a computer that can run Rhino. (If not, Rhino has some minimum [System Requirements](http://www.rhino3d.com/system_requirements/) that you should review before acquiring any hardware).  Generally speaking, any computer that can run Rhino *ought* to be able to run the developer tools outlined in the [Software](#software) section.

If you are a Windows user and wish to develop plugins for Rhino for Mac, you will need an Apple Mac computer.  Conversely, if you are an OS X user and you wish to develop for Rhino for Windows, you will need a computer that can run Rhino for Windows (however, virtual machines running Windows under OS X can potentially work just fine).


## Software
{: .toc-header }

Depending on what you want to do, the software prerequisites vary.  However, in general, you will need:

- [Rhinoceros](http://www.rhino3d.com/download)
- A code editor.  There are many options...here are a few:
   - [Visual Studio](https://www.visualstudio.com): Microsoft's flagship IDE.
   - [Xamarin Studio](http://xamarin.com/studio): Xamarin's Cross-Platform C# IDE.
   - [Atom](https://atom.io/): A Cross-Platform Extensible Text Editor.

See the [SDK-specific guides]({{ site.baseurl }}/guides/) for the software prerequisites...normally found in the *"Installing Tools"* guides.

## Programming Knowledge
{: .toc-header }

Acquiring programming knowledge is the most labor intensive prerequisite.  However, learning to program - even trying out a new language - is fun and enriching.  Learning to program using Rhino is a great way to begin...

#### Learning C# .NET
{: .toc-subheader }

If you wish to write plugins with RhinoCommon, you will need to understand a .NET compatible programming language like C# (or VB.NET).  We recommend [C#](https://en.wikipedia.org/wiki/C_Sharp_(programming_language)) (C Sharp) because it is modern, safe, and easy to learn - and you can develop in C# on both Windows and OS X.

*Watch*...

- [Beginning C# Programming](http://shop.oreilly.com/product/0636920036036.do) By Eric Lippert - Published by O'Reilly Media
- [C# Fundamentals for Absolute Beginners](https://www.microsoftvirtualacademy.com/en-US/training-courses/c-fundamentals-for-absolute-beginners-8295) on Microsoft's Virtual Academy
- [C# Essential Training](http://www.lynda.com/C-tutorials/C-Essential-Training/188207-2.html) with David Gassner on Lynda.com

*Read*...

- [Programming C# 5.0](http://shop.oreilly.com/product/0636920024064.do) By Ian Griffiths - Published by O'Reilly Media
- [C# 5.0 in a Nutshell](http://shop.oreilly.com/product/0636920023951.do) By Joseph Albahari, Ben Albahari - Published by O'Reilly Media

*Do*...

- [Check out samples]({{ site.baseurl }}/samples/#rhinocommon) on this site
- [Ask for help on Discourse](http://discourse.mcneel.com/c/rhino-developer)

#### Learning C/C++
{: .toc-subheader }

To write plugins for Rhino using the C/C++ SDK, you first need to learn the [C++ programing language](https://en.wikipedia.org/wiki/C%2B%2B) itself.  C/C++ is sometimes considered an "advanced" programming language.

*Watch*...

- [C++: A General Purpose Language](https://www.microsoftvirtualacademy.com/en-us/training-courses/c-a-general-purpose-language-and-library-jump-start-8251) on Microsoft Virtual Academy
- [C++ Essential Training](http://www.lynda.com/C-tutorials/C-Essential-Training/182674-2.html) with Bill Weinmann on Lynda.com

*Read*...

- [The C Programming Language](https://en.wikipedia.org/wiki/The_C_Programming_Language) by Ian Kernighan and Dennis Ritchie
- [Practical C++ Programming](http://shop.oreilly.com/product/9780596004194.do) by Steve Oualline - Published by O'Reilly Media
- [C++ Primer Plus](http://www.amazon.com/Primer-Plus-Edition-Developers-Library/dp/0321776402) by Stephen Prata

*Do*...

- [Check out samples]({{ site.baseurl }}/samples/#cc) on this site
- [Ask for help on Discourse](http://discourse.mcneel.com/c/rhino-developer)

#### Learning Python
{: .toc-subheader }

[Python](https://en.wikipedia.org/wiki/Python_(programming_language)) is a fantastic first language and an amazingly flexible additional language to add to your toolkit.

*Watch*...

- [Google's Python Class](https://developers.google.com/edu/python/) by Google for Education
- [Up and Running with Python](http://www.lynda.com/Python-tutorials/Up-Running-Python/122467-2.html) with Joe Marini on Lynda.com


*Read*...

- [RhinoPython Primer](http://www.rhino3d.com/download/IronPython/5.0/RhinoPython101) by Skylar Tibbits, Arthur van der Harten, Steve Baer, and David Rutten
- [The Python Tutorial](https://docs.python.org/2/tutorial/index.html) by the Python Software Foundation
- [Learn Python the Hard Way](http://learnpythonthehardway.org/book/) by Zed A. Shaw - despite the title, this is a beginner's book
- [Automate The Boring Stuff With Python](https://automatetheboringstuff.com/) by Al Sweigart


*Do*...

- [Check out samples]({{ site.baseurl }}/samples/#rhinopython) on this site
- [Ask for help on Discourse](http://discourse.mcneel.com/c/scripting)

#### Learning RhinoScript
{: .toc-subheader }

RhinoScript is a scripting tool based on Microsoft's VBScript language.  RhinoScript runs in Rhino for Windows.

*Read*...

- [RhinoScript Primer](http://www.rhino3d.com/download/rhino/5.0/rhinoscript101) by David Rutten
- [Microsoft VBScript User's Guide and Language Reference](https://msdn.microsoft.com/en-us/library/t0aew7h6(VS.85).aspx)

*Do*...

- [Check out samples]({{ site.baseurl }}/samples/#rhinoscript) on this site
- [Ask for help on Discourse](http://discourse.mcneel.com/c/scripting)

---

## Related topics
{: .toc-header }

- [What is a Rhino Plugin?]({{ site.baseurl }}/guides/general/what_is_a_rhino_plugin/)
- <a href="https://en.wikipedia.org/wiki/C_Sharp_(programming_language">C Sharp on Wikipedia</a>
- [C++ on Wikipedia](https://en.wikipedia.org/wiki/C%2B%2B)
- [Python on Wikipedia](https://en.wikipedia.org/wiki/Python_(programming_language))
