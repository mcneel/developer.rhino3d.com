+++
aliases = ["/5/guides/general/rhino-technology-overview/", "/6/guides/general/rhino-technology-overview/", "/7/guides/general/rhino-technology-overview/", "/wip/guides/general/rhino-technology-overview/"]
authors = [ "brian" ]
categories = [ "Overview" ]
description = "A summary of the Rhino technology architecture."
keywords = [ "developer", "rhino" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "Rhino Technology Overview"
type = "guides"
weight = 0
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = ""
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


## Overview

Rhinoceros is composed of many layers - written in many languages - all stacked on top of each other.  The most foundational are on the bottom, but the top layers should by no means be considered superficial...

![The Rhino Stack](/images/rhino-technology-overview-01.png)

Let's discuss each of the layers in turn, starting on the bottom with the...

## Foundation

### C++ Rhino Core

The C++ Core of Rhino is the oldest and broadest set of code.  We use Microsoft’s MFC in places, including the SDK.  This is where the runtime document is managed, where all the OpenGL viewport drawing code exists, and it’s where the computational geometry code written by our mathematicians lives.  Many of Rhino's commands are here.

Lots of user interface - the command line, the application mainframe, status bar, and the dialog boxes for many commands in the Rhino core.

### openNURBS

openNURBS is free C++ source code that lets you read and write Rhino *3dm* files - all the way back to version 1.  openNURBS was our first open-source project.

The code compiles on Windows, macOS, Linux, iOS, and Android.  It's used in various third-party applications like ArchiCAD, SolidWorks, Inventor, SketchUp and many other products to read or write *3dm* files directly.

openNURBS is what Rhino uses natively to read/write *3dm* files.  This toolkit is released before Rhino, so any product, including our competitors, can be compatible with the latest *3dm* files.  There is no difference between the *3dm* files Rhino writes and those of other applications using openNURBS to read and write *3dm*.

For more information about openNURBS, please see the [openNURBS guides](/guides/opennurbs/).

### C++ SDK

On top of all of this is our C++ SDK, available only on Windows.

Compiling against the C++ SDK requires a specific version of Microsoft Visual Studio and the Microsoft C-Runtime.  You have to recompile for every major version of Rhino.

Virtually everything Rhino can do is exposed through the C++ SDK. Some commands and features haven’t been exposed yet, but this SDK is very broad and rich.

Unfortunately, because it's so tightly coupled to the Rhino Core, plugin developers need to recompile their plugins for every Rhino release.

For more information about the C++ SDK, check out the [C/C++ guides](/guides/cpp/).

## C++ Stack

On the right column of the stack diagram above is the C++ portion of Rhino.  The C++ stack allows us - as well as third-party plugin developers - to write Rhino plugins using the same C++ SDK that we use to develop Rhino itself.  Note that you cannot author Grasshopper components using C++.

### C++ Plugins

On top of the C++ SDK are C++ plugins.  Many features that ship with Rhino, including some Commands, File I/O, Renderers are actually C++ plugins.  There are also dozens of third-party C++ plugins, like [VisualARQ by Asuni](http://www.visualarq.com/), [RhinoCAM by MecSoft](https://mecsoft.com/rhinocam-software/), and [V-Ray by Chaos Software](https://www.chaosgroup.com/vray/rhino).

For more information about the C++ SDK, check out the [C/C++ guides](/guides/cpp/).

### RhinoScript

One of the C++ plugins we ship with Rhino is [RhinoScript](/guides/rhinoscript/what-are-vbscript-rhinoscript/).  RhinoScript exposes a useful subset of Rhino’s SDK via VBScript - a widely used and popular scripting language.  RhinoScript gives you access not only to Rhino, but to any other COM object on Windows.

For more information, see the [RhinoScript guides](/guides/rhinoscript/), and more specifically the [What are VBScript and RhinoScript?](/guides/rhinoscript/what-are-vbscript-rhinoscript/) guide.

## .NET Stack

The .NET SDK is represented here in three layers:

- C API
- .NET Framework
- RhinoCommon
- Eto

### C API

A straight C API wraps the C++ SDK, allowing us to Platform Invoke (P/Invoke) into the C++ SDK, forming a bridge between the native C++ code and the managed .NET layers.

### .NET Framework

Microsoft develops the [.NET Framework](https://www.microsoft.com/net/framework).  .NET makes it possible to write plugins in C#, F#, VB.NET, and any other language that compiles down to Microsoft's IL.

The Microsoft .NET framework ships with Windows.

In Rhino for Mac product, we embed the [Mono Runtime](https://www.mono-project.com), a partial cross-platform implementation of the .NET Runtime.

For more information about .NET and how it relates to Rhino development, see the [What are Mono & Xamarin?](/guides/rhinocommon/what-are-mono-and-xamarin/).

### RhinoCommon

RhinoCommon is our .NET SDK for Rhino, built atop the portions of the .NET framework that are *common* on both Windows and macOS (via Mono).  RhinoCommon allows developers to run .NET code on both Rhino for Windows and Rhino for Mac.

For more information about RhinoCommon, see the [RhinoCommon guides](/guides/rhinocommon/), or more specifically, the [What is RhinoCommon?](/guides/rhinocommon/what-is-rhinocommon) guide.

### Eto

Using RhinoCommon, you can write .NET plugins that work on Windows and Mac...except for the User Interface.  The Mono team did not clone WinForms or WPF, so neither of those technologies work on the Mac.  To address this problem, Rhino now ships with Eto.Forms.  Eto lets you write user interface once in C#, XAML, or JSON and use it on Windows and macOS.  Actually, your UI written in Eto, can run on iOS, Android, and Linux, too.

For more information about Eto, check out [Eto.Forms on GitHub](https://github.com/picoe/Eto).

### .NET Plugins

Built on top of RhinoCommon are numerous plugins, both internal and third-party developed plugins.  [Grasshopper](http://www.grasshopper3d.com/), for example, is a RhinoCommon plugin.  Some commands, renderers, and file IO plugins in Rhino are actually written as RhinoCommon plugins.  As time goes on, we are moving more and more convenient functionality into RhinoCommon/.NET plugins so as to share more code between platforms.  Many successful third-party plugins are also written using RhinoCommon and .NET, such as [RhinoGold](http://www.tdmsolutions.com/) and [Matrix by GEMVision](http://www.stuller.com/matrix), and [Orca3D](http://orca3d.com/).

For more information about RhinoCommon, see the [RhinoCommon guides](/guides/rhinocommon/).

### Grasshopper Components

Rhino now ships with Grasshopper, our visual programming language for algorithmic and parametric design.  Grasshopper is a development platform unto itself, with [hundreds of third-party authored Grasshopper components](http://www.food4rhino.com/grasshopper-addons), for doing all sorts of things from [physics simulation](http://www.food4rhino.com/project/kangaroo), to [creating custom user-interfaces](http://www.food4rhino.com/project/human-ui), to [industrial robotic programming and control](http://www.food4rhino.com/project/hal).

For more information about Grasshopper, more specifically developing Grasshopper components, check out the [Grasshopper guides](/guides/grasshopper/).

### Python Scripts

One of the .NET plugins that ships with Rhino is RhinoPython.  Written using [IronPython](http://ironpython.net/), a .NET implementation of the [python](https://www.python.org/) runtime, RhinoPython exposes the entire RhinoCommon SDK to the python scripting language.  That means any time we add a feature to RhinoCommon, it shows up automatically in RhinoPython.

For more information about RhinoPython, see the [RhinoPython guides](/guides/rhinopython/).

## Related Topics

- [C/C++ guides](/guides/cpp/)
- [openNURBS guides](/guides/opennurbs/)
- [RhinoScript guides](/guides/rhinoscript/)
- [Microsoft .NET Framework (on microsoft.com)](https://www.microsoft.com/net/framework)
- [What is RhinoCommon?](/guides/rhinocommon/what-is-rhinocommon)
- [RhinoCommon guides](/guides/rhinocommon/)
- [What are Mono & Xamarin?](/guides/rhinocommon/what-are-mono-and-xamarin/)
- [Mono Project](https://www.mono-project.com)
- [Eto.Forms on GitHub](https://github.com/picoe/Eto)
- [Grasshopper guides](/guides/grasshopper/)
- [RhinoPython guides](/guides/rhinopython/)
