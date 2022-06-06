+++
aliases = ["/5/guides/general/frequently-asked-questions/", "/6/guides/general/frequently-asked-questions/", "/7/guides/general/frequently-asked-questions/", "/wip/guides/general/frequently-asked-questions/"]
authors = [ "dan" ]
categories = [ "Overview" ]
description = "This guide is a list of Frequently Asked Questions (FAQ)."
keywords = [ "developer", "rhino", "faq" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "Frequently Asked Questions"
type = "guides"
weight = 4
override_last_modified = "2021-09-03T08:29:10Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptspage"
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


**Which SDK is right for me?**

It all depends on what you want to do.  If you are looking to automate repetitive tasks in Rhino, writing a [Python](/guides/#rhinopython) script is the way to go.  If you are looking to write a full-fledged plugin or Grasshopper component, we strongly suggest the [RhinoCommon SDK](/guides/rhinocommon/what-is-rhinocommon/).  If you are very proficient with C/C++, you should consider the native C/C++ SDK (only supported on Rhino for Windows).

**Can I write plugins that run on both Windows and Mac?**

Yes...even using [the same code](/guides/rhinocommon/what-is-rhinocommon/).

**What is Mono/Xamarin?**

Mono is an open-source version of Microsoft's .NET runtime that runs on Linux, macOS, iOS, and Android.  Check out the [What are Mono and Xamarin?](/guides/rhinocommon/what-are-mono-and-xamarin/) guide for more information.

**What are Macros?**
Macros are string of Rhino commands and command options that allow you to create an automated sequence of operations.  This macro (sequence) can then be repeated at the push of a toolbar button or by typing an alias.

**What are Scripts?**
For more complex tasks, macros are insufficient.  They lack the ability to make complex calculations, store and retrieve data, analyze that data and make conditional decisions, or reach deep into the inner workings of Rhino.  For this, one needs a real programming tool.  The simplest and most accessible of these is Python, which also includes its version of RhinoScript syntax.  When we talk about scripts we are usually referring to functions written with RhinoScript or Python.

**What are Plugins?**
Plugins are even more sophisticated tools: these are compiled computer programs that can be integrated into Rhino.  These can range from simple script-like functions to complex, full blown programs for doing rendering, animation, machining, etc.
