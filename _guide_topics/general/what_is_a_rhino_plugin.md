---
layout: toc-guide-page
title: What is a Rhino Plugin?
author: dan@mcneel.com
categories: ['General']
platforms: ['Cross-Platform']
apis: ['General']
languages: ['All']
keywords: ['developer', 'rhino']
TODO: 0
origin: https://wiki.mcneel.com/developer/whatisarhinoplugin
order: 2
---


# What is a Rhino Plugin?
{: .toc-title }

A Rhino plugin is a software module that extends the functionality of Rhino or Grasshopper by adding commands, features, or capabilities.  A Rhino plugin is a Dynamic Link Library, or DLL.

On Windows, a Rhino plugin built with the [C/C++ SDK]({{ site.baseurl }}/guides/cpp/what_is_the_cpp_sdk/) is regular DLL using shared MFC DLL.

On Windows and Mac, a Rhino plugin built with the [RhinoCommon SDK]({{ site.baseurl }}/guides/rhinocommon/what_is_rhinocommon/) is a .NET assembly.

Examples of Rhino plugins include [Grasshopper](http://www.grasshopper3d.com), [Brazil](http://brazil.rhino3d.com/), [Flamingo](http://nxt.flamingo3d.com/), and [Bongo](http://bongo.rhino3d.com/).  See [food4rhino.com](http://www.food4rhino.com/) for more.


## Types of Plugins
{: .toc-header }

Rhino supports five different types of plugins:

1. **General Utility**: A general purpose utility that can contain one or more commands.
1. **File Import**: Imports data from other file formats into Rhino; can support more that one format.
1. **File Export**: Exports data from Rhino to other file formats; can support more than one format.
1. **Custom Rendering**: Applies materials, textures, and lights to a scene to produce rendered images.
1. **3D Digitizing**: Interfaces with 3D digitizing devices, such as those made by MicroScribe, Faro, & Romer.

***Note***: File Import, File Export, Custom Rendering and 3D Digitizing plugins are all specialized enhancements to the General Utility plugin.  Thus, all plugin types can contain one or more commands.


---

## Related topics
{: .toc-header }

- [Developer Prerequisites]({{ site.baseurl }}/guides/general/rhino_developer_prerequisites)
