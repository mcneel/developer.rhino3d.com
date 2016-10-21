---
title: Rhino Technology Overview
description: A summary of the Rhino technology architecture.
author: brian@mcneel.com
apis: ['General']
languages: ['All']
platforms: ['Windows', 'Mac']
categories: ['General']
origin: unset
order: 0
keywords: ['developer', 'rhino']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## Overview

Rhinoceros is composed of many layers - written in many languages - all stacked on top of each other.  The most foundational are at the bottom, but the top layers should by no means be considered superficial...

![The Rhino Stack]({{ site.baseurl}}/images/rhino_technology_overview_01.png)

Let's discuss each of the layers in turn, starting at the bottom with the...

## Foundation

### C++ Rhino Core

The C++ Core of Rhino is the oldest and broadest set of code.  We use Microsoft’s MFC in places, including the SDK.  This is where the runtime document is managed, where all the OpenGL viewport drawing code exists, and it’s where the computational geometry code written by our mathematicians lives.  Many of Rhino's commands are here.

Lots of user interface - the command line, the application mainframe, status bar, and the dialog boxes for many commands in the Rhino core.

### openNURBS

openNURBS is free C++ source code that lets you read and write Rhino *3dm* files - all the way back to version 1.  openNURBS was our first open-source project.

The code compiles on Windows, macOS, Linux, iOS, and Android.  It's used in various third-party applications like ArchiCAD, SolidWorks, Inventor, SketchUp and many other products to read or write *3dm* files directly.

openNURBS is what Rhino uses natively to read/write *3dm* files.  This toolkit is released before Rhino, so any product, including our competitors, can be compatible with the latest *3dm* files.  There is no difference between the *3dm* files Rhino writes and those of other applications using openNURBS to read and write *3dm*.

See also...

### C++ SDK

On top of all of this is our C++ SDK, available only on Windows.

Compiling against the C++ SDK requires a specific version of Microsoft Visual Studio and the Microsoft C-Runtime.  You have to recompile for every major version of Rhino.

Virtually everything Rhino can do is exposed through the C++ SDK. Some commands and features haven’t been exposed yet, but this SDK is very broad and rich.

Unfortunately, because it's so tightly coupled to the Rhino Core, plugin developers need to recompile their plugins for every Rhino release.

## C++

On the right column of the stack diagram above is the C++ portion of Rhino.  The C++ stack allows us - as well as third-party plugin developers - to write Rhino plugins using the same C++ SDK that we use to develop Rhino itself.  Note that you cannot author Grasshopper components using C++.

### C++ Plugins

On top of the C++ SDK are C++ plugins.  Many features that ship with Rhino, including some Commands, File I/O, Renderers are actually C++ plugins.  There are also dozens of third-party C++ plugins, like VisualARQ, RhinoCAM, Vray, etc.

See also...

### RhinoScript

One of the C++ plugins we ship with Rhino is [RhinoScript]({{ site.baseurl }}/guides/rhinoscript/what_are_vbscript_rhinoscript/).  RhinoScript exposes a useful subset of Rhino’s SDK via VBScript - a widely used and popular scripting language.  RhinoScript gives you access not only to Rhino, but to any other COM object on Windows.

For more information, see the [RhinoScript guides]({{ site.baseurl }}/guides/rhinoscript/), and more specifically the [What are VBScript and RhinoScript?]({{ site.baseurl }}/guides/rhinoscript/what_are_vbscript_rhinoscript/) guide.

## .NET

The .NET SDK is represented here in three layers:

- C API
- .NET Framework
- RhinoCommon

### C API

A straight C API wraps the C++ SDK, allowing us to Platform Invoke (P/Invoke) into the C++ SDK, forming a bridge between the native C++ code and the managed .NET layers.

### .NET Framework

Microsoft develops the .NET Framework.  .NET makes it possible to write plugins in C#, F#, VB.NET, and any other language that compiles down to Microsoft's IL.

The Microsoft .NET framework ships with Windows.

In Rhino for Mac product, we embed the Mono Runtime, a partial cross-platform implementation of the .NET Runtime.

For more information about .NET, see the [What are Mono & Xamarin?]({{ site.baseurl }}/guides/rhinocommon/what_are_mono_and_xamarin/).

### RhinoCommon

RhinoCommon is our .NET SDK for Rhino, built atop the portions of the .NET framework that are *common* on both Windows and macOS (via Mono).  RhinoCommon allows developers to run .NET code on both Rhino for Windows and Rhino for Mac.

For more information about RhinoCommon, see the [RhinoCommon guides]({{ site.baseurl }}/guides/rhinocommon/), or more specifically, the [What is RhinoCommon?]({{ site.baseurl }}/guides/rhinocommon/what_is_rhinocommon) guide.

### .NET Plugins
