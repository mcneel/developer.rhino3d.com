---
layout: toc-guide-page
title: What is RhinoCommon?
author: steve@mcneel.com
categories: ['Overview']
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'VB.NET']
keywords: ['RhinoCommon', 'What']
TODO: 0
origin: http://wiki.mcneel.com/developer/rhinocommon
order: 1
---


# What is RhinoCommon?
{: .toc-title }

RhinoCommon is the cross-platform .NET plug-in SDK available for:

- Rhino 5 for Windows (both 32 and 64-bit versions)
- Rhino 5 for Mac
- Rhino.Python scripting
- Grasshopper

The term _common_ is meant to be just that: an SDK that can be used across Rhino platforms. A plug-in built with RhinoCommon could potentially run on both Windows and Mac platforms with no changes...

<div align="center">
  <img src="{{ site.baseurl }}/images/rhinocommon_one_binary_two_platforms.png">
</div>

{::options parse_block_html="true" /}

## Inside RhinoCommon
{: .toc-header }

RhinoCommon is composed of the following pieces.  These files are included with Rhino 5 for Windows and Mac:

1. ***RhinoCommon.dll*** - This is a pure .NET DLL that plug-ins can reference and use to work with Rhino.
1. ***RhinoCommon.xml*** - This is an XML file that contains SDK documentation comments specific to RhinoCommon.dll. Programming development environments like Visual Studio and MonoDevelop use this XML file to display tooltips and other helpful information while the developer writes code.
1. ***rhcommon_c.dll*** and ***monomanager.rhp*** - These are C++ shared libraries compiled for specific target platforms (Win32, Win64, and OS X). These libraries are used by RhinoCommon, but should never be directly accessed by plug-in developers.

RhinoCommon on Mac OS X is executed through an embedded [Mono framework](http://www.mono-project.com/).

## Rhino uses RhinoCommon
{: .toc-header }

All .NET plug-ins that ship with Rhino 5 for Windows and Rhino 5 for Mac, including the Python interpreter, reference RhinoCommon.

In 2011, Grasshopper was rewritten using RhinoCommon.  This was a big project and took some time to complete, but once done it provided performance improvements and better memory management.  This is also a step toward Grasshopper running on Rhino for Mac.

The [Python]({{ site.baseurl }}/guides/rhinopython) script engine is entirely based on RhinoCommon.  All python scripts use RhinoCommon to work with Rhino. Typically, if it is difficult to write a Python script using a RhinoCommon API, then the RhinoCommon SDK needs to be fixed.

---

## Related topics
{: .toc-header }

- [What are Mono and Xamarin?](/guides/rhinocommon/what_are_mono_and_xamarin/)
