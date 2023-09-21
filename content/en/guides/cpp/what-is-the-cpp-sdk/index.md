+++
aliases = ["/5/guides/cpp/what-is-the-cpp-sdk/", "/6/guides/cpp/what-is-the-cpp-sdk/", "/7/guides/cpp/what-is-the-cpp-sdk/", "/wip/guides/cpp/what-is-the-cpp-sdk/"]
authors = [ "dale" ]
categories = [ "Overview" ]
description = "This guide gives an overview of C/C++ SDK."
keywords = [ "c", "C/C++", "plugin" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "What is the C/C++ SDK?"
type = "guides"
weight = 1

[admin]
TODO = ""
origin = "https://wiki.mcneel.com/developer/cplusplusplugins"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++


The Rhino C/C++ Software Development Kit (SDK) is an set of developer resources for customizing and extending Rhino for Windows. The SDK provides tools that provide direct access to its database structures, geometry, graphics system, file I/O, command definitions, and much more.

The Rhino C/C++ SDK consists primarily of C++ headers and libraries that can be used to build Rhino extensions called *Plugins*. Plugins are Windows DLLs that can be loaded into the Rhino process and interact directly with the Rhino application. Rhino plugin modules use the file extension *.rhp* instead of the more common *.dll*.

The Rhino C/C++ SDK is for Rhino for Windows only. There currently is no Rhino C/C++ SDK for Rhino for Mac.

## Types of Plugins

Rhino supports five different types of plugins:

| Type                 | Description                                                  |
|:-------------------- |:------------------------------------------------------------ |
| **General Utility**  | A general purpose utility that can contain one or more commands. |
| **File Import**      | Imports data from other file formats into Rhino; can support multiple file formats. |
| **File Export**      | Exports data from Rhino to other file formats; can support multiple file formats. |
| **Custom Rendering** | Applies materials, textures, and lights to a scene to produce rendered images. |
| **3D Digitizing**    | Interfaces with 3D digitizing and other alternative input devices. |

Note: File Import, File Export, Custom Rendering and 3D Digitizing plugins are all specialized enhancements to the General Utility plugin.  Thus, all plugin types can contain one or more commands.

As with all of our development tools, the Rhino C/C++ SDK is free, royalty free, and includes free developer support.
