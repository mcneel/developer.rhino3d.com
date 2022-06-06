+++
aliases = ["/5/guides/rhinocommon/what-is-rhinocommon/", "/6/guides/rhinocommon/what-is-rhinocommon/", "/7/guides/rhinocommon/what-is-rhinocommon/", "/wip/guides/rhinocommon/what-is-rhinocommon/"]
authors = [ "steve" ]
categories = [ "Overview" ]
description = "This guide gives an overview of RhinoCommon."
keywords = [ "RhinoCommon", "What" ]
languages = [ "C#", "VB" ]
sdk = [ "RhinoCommon" ]
title = "What is RhinoCommon?"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommon"
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


RhinoCommon is the cross-platform .NET plugin SDK available for:

- Rhino for Windows
- Rhino for Mac
- Rhino.Python scripting
- Grasshopper

The term _common_ is meant to be just that: an SDK that can be used across Rhino platforms. A plugin built with RhinoCommon could potentially run on both Windows and Mac platforms with no changes...

<div align="center">
  <img src="/images/rhinocommon-one-binary-two-platforms.png">
</div>


## Inside RhinoCommon

RhinoCommon is composed of the following pieces.  These files are included with Rhino for Windows and Mac:

1. *RhinoCommon.dll* - This is a pure .NET DLL that plugins can reference and use to work with Rhino.
1. *RhinoCommon.xml* - This is an XML file that contains SDK documentation comments specific to RhinoCommon.dll. Programming development environments like Visual Studio and MonoDevelop use this XML file to display tooltips and other helpful information while the developer writes code.
1. *rhcommon_c.dll* and *monomanager.rhp* - These are C++ shared libraries compiled for specific target platforms (Win64 and macOS). These libraries are used by RhinoCommon, but should never be directly accessed by plugin developers.

RhinoCommon on macOS is executed through an embedded [Mono framework](http://www.mono-project.com/).

## Rhino uses RhinoCommon

All .NET plugins that ship with Rhino for Windows and Rhino for Mac, including the Python interpreter, reference RhinoCommon.

In 2011, Grasshopper was rewritten using RhinoCommon.  This was a big project and took some time to complete, but once done it provided performance improvements and better memory management.  This is also a step toward Grasshopper running on Rhino for Mac.

The [Python](/guides#rhinopython) script engine is entirely based on RhinoCommon.  All python scripts use RhinoCommon to work with Rhino. Typically, if it is difficult to write a Python script using a RhinoCommon API, then the RhinoCommon SDK needs to be fixed.

## Related topics

- [What are Mono and Xamarin?](/guides/rhinocommon/what-are-mono-and-xamarin/)
