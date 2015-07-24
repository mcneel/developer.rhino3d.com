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

1. **RhinoCommon.dll** - This is a pure .NET DLL that plug-ins can reference and use to work with Rhino.
1. **RhinoCommon.xml** - This is an XML file that contains SDK documentation comments specific to RhinoCommon.dll. Programming development environments like Visual Studio and MonoDevelop use this XML file to display tooltips and other helpful information while the developer writes code.
1. **rhcommon_c.dll** and **monomanager.rhp** - These are C++ shared libraries compiled for specific target platforms (Win32, Win64, and OS X). These libraries are used by RhinoCommon, but should never be directly accessed by plug-in developers.

RhinoCommon on Mac OS X is executed through an embedded [Mono framework](http://www.mono-project.com/).

## Eating our own dog food
{: .toc-header }

The Python plug-in for Windows and Mac, Grasshopper, and all Rhino for Mac based .NET plug-ins are being built against RhinoCommon.

During 2011, Grasshopper was rewritten to be based on RhinoCommon.  This was a big project and took some time to complete, but once done it provided performance improvements and better memory management.  This has also been a step toward being able to run Grasshopper on Rhino for Mac!

The [Python]({{ site.baseurl }}/guides/rhinopython) script engine is entirely based on RhinoCommon.  All python scripts directly use RhinoCommon to work with Rhino. Typically if something in RhinoCommon is difficult to write a python script for, then the RhinoCommon SDK needs to be fixed in that area.

## Rhino.NET is dead
{: .toc-header }

RhinoCommon is *version 2* of the deprecated Rhino.NET SDK, and it improves on the design and implementation of *version 1*.  Rhino.NET still works in Rhino 5 for Windows, but will be replaced with RhinoCommon in future versions of Rhino.  

Some of the major improvements in RhinoCommon are:

- **Platform neutral**: RhinoCommon is built to run on Windows 32 bit, Windows 64 bit, and Mac OS X.
- **Faster for some data types**: All data types in Rhino.NET were wrappers around C++ pointers created on the unmanaged heap. This was a mistake when working with primitive data types (like 3D points and vectors). Primitive Rhino data types in RhinoCommon are written as value classes and implemented entirely in .NET.
   - Allows data type to be placed on the stack when only temporarily needed in a function
   - There is no requirement to call through to C++ to simply get the value of something like X,Y,Z in a point
   - No potential fragmentation of the C++ unmanaged heap because the type is entirely inside of .NET and under the control of the garbage collector
   - Operator overloading works much cleaner since value types can not have a value of null
- **A .NET style SDK**:
   - Multiple appropriately named namespaces in an attempt to better organize the SDK
   - Properties are used when they make sense
   - All parameter arguments are clearly named to describe their purpose
   - Standard .NET style events are used instead of forced subclassing when it makes sense
   - Descriptive enumerations are used instead of vague int for function parameters and returns
   - .NET attributes are used where appropriate
   - This is not a one-to-one conversion from C++ SDK to .NET
   - Removal of separate const/non-const versions of classes
- **Improved documentation**:
   - We are making an effort to provide descriptive XML comments for all classes/functions/properties
   - The current API documentation found on this site

---

## Related topics
{: .toc-header }

- [What are Mono and Xamarin?](/guides/rhinocommon/what_are_mono_and_xamarin/)
