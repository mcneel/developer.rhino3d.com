+++
aliases = ["/5/guides/general/what-is-a-rhino-plugin/", "/6/guides/general/what-is-a-rhino-plugin/", "/7/guides/general/what-is-a-rhino-plugin/", "/wip/guides/general/what-is-a-rhino-plugin/"]
authors = [ "dan" ]
categories = [ "Fundamentals" ]
description = "This guide outlines what a Rhino plugin is and what forms it comes in."
keywords = [ "developer", "rhino" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "What is a Rhino Plugin?"
type = "guides"
weight = 3
override_last_modified = "2021-09-03T08:29:10Z"

[admin]
TODO = ""
origin = "https://wiki.mcneel.com/developer/whatisarhinoplugin"
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


A Rhino plugin is a software module that extends the functionality of Rhino or Grasshopper by adding commands, features, or capabilities.  A Rhino plugin is a Dynamic Link Library, or DLL.

On Windows, a Rhino plugin built with the [C/C++ SDK](/guides/cpp/what-is-the-cpp-sdk/) is a regular DLL using shared MFC DLL.

On Windows and Mac, a Rhino plugin built with the [RhinoCommon SDK](/guides/rhinocommon/what-is-rhinocommon/) is a .NET assembly.

Examples of Rhino plugins include [Grasshopper](http://www.grasshopper3d.com), [Brazil](http://brazil.rhino3d.com/), [Flamingo](http://nxt.flamingo3d.com/), and [Bongo](http://bongo.rhino3d.com/).  See [food4rhino.com](http://www.food4rhino.com/) for more.


## Types of Plugins

Rhino supports five different types of plugins:

1. *General Utility*: A general purpose utility that can contain one or more commands.
1. *File Import*: Imports data from other file formats into Rhino; can support more that one format.
1. *File Export*: Exports data from Rhino to other file formats; can support more than one format.
1. *Custom Rendering*: Applies materials, textures, and lights to a scene to produce rendered images.
1. *3D Digitizing*: Interfaces with 3D digitizing devices, such as those made by MicroScribe, Faro, & Romer.

***Note***: File Import, File Export, Custom Rendering and 3D Digitizing plugins are all specialized enhancements to the General Utility plugin.  Thus, all plugin types can contain one or more commands.


## Plugin Compatibility

For Rhino to successfully load and run your plugin, several conditions must be met:

1. The "RhinoSdkVersion" number of your plugin must match the "RhinoSdkVersion" of Rhino.
1. The "RhinoSdkServiceRelease" number of Rhino must be greater than or equal to the "RhinoSdkServiceRelease" of your plugin.

We occasionally make changes to our SDKs.  When we do, we change the "RhinoSdkServiceRelease" number.  

As a plugin developer you are unlikely to encounter a problem with the first condition.  This would occur, for instance, if a user tried to load a plugin built for Rhino 6 in Rhino 4.

You may however, occassionally encounter problems with the second condition.  If you compiled your plugin using the 6.2 (RhinoSdkVersion.RhinoSdkServiceRelease) SDK and a user running a 6.1 Rhino tries to run it, they will get an error message and the plugin will refuse to load.  If your customer gets this message, they need to get the latest Rhino (could be 6.2 or greater in this example) and that should resolve the problem.

## Related topics

- [Developer Prerequisites](/guides/general/rhino-developer-prerequisites)
