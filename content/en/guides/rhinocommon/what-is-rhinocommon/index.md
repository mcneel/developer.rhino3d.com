+++
aliases = ["/en/en/5/guides/rhinocommon/what-is-rhinocommon/", "/en/6/guides/rhinocommon/what-is-rhinocommon/", "/en/7/guides/rhinocommon/what-is-rhinocommon/", "/wip/guides/rhinocommon/what-is-rhinocommon/"]
authors = [ "steve" ]
categories = [ "Overview" ]
description = "This guide gives an overview of RhinoCommon."
keywords = [ "RhinoCommon", "What" ]
languages = [ "C#", "VB", "Python" ]
sdk = [ "RhinoCommon" ]
title = "What is RhinoCommon?"
type = "guides"
weight = 1

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
- Rhino.Python Scripting
- Grasshopper

The term _Common_ is meant to be just that: an SDK that can be used across Rhino platforms. A plugin built with RhinoCommon could potentially run on both Windows and Mac platforms with no changes.

<div align="center">
  <img src="/images/rhinocommon-one-binary-two-platforms.png">
</div>

RhinoCommon is available as [NuGet package](https://www.nuget.org/packages/rhinocommon).

## Inside RhinoCommon

RhinoCommon is composed of the following components:

| Assembly       | Description                                                  |
| :-------------- | :----------------------------------------------------------- |
| **RhinoCommon.dll** | [RhinoCommon](https://developer.rhino3d.com/api/rhinocommon/html/R_Project_RhinoCommon.htm?version=8.x) is the core .NET assembly that plugins reference in order to interact with Rhino. |
| **Eto.dll**         | [Eto](https://github.com/picoe/Eto) is a framework can be used to build user interfaces that run across multiple platforms using their native toolkit, with an easy to use API. This will make your plug-in look and work as a native application on all platforms, using a single UI codebase. |
| **Rhino.UI.dll**    | [Rhino.UI](https://developer.rhino3d.com/api/rhinocommon/rhino.ui) is a utility .NET assembly that contains Rhino-specific user interface and other miscellaneous classes. |

## Types of Plugins

RhinoCommon supports five different types of plugins:

| Type                 | Description                                                  |
|:-------------------- |:------------------------------------------------------------ |
| **General Utility**  | A general purpose utility that can contain one or more commands. |
| **File Import**      | Imports data from other file formats into Rhino; can support multiple file formats. |
| **File Export**      | Exports data from Rhino to other file formats; can support multiple file formats. |
| **Custom Rendering** | Applies materials, textures, and lights to a scene to produce rendered images. |
| **3D Digitizing**    | Interfaces with 3D digitizing and other alternative input devices. |

Note: File Import, File Export, Custom Rendering and 3D Digitizing plugins are all specialized enhancements to the General Utility plugin. Thus, all plugin types can contain one or more commands.

As with all of our development tools, RhinoCommon is free, royalty free, and includes free developer support.
