+++
aliases = ["/en/5/guides/rhinocommon/whats-new/", "/en/6/guides/rhinocommon/whats-new/", "/en/7/guides/rhinocommon/whats-new/", "/en/wip/guides/rhinocommon/whats-new/", "/en/8/new"]
authors = [ "steve" ]
categories = [ "Overview" ]
description = "This brief guide outlines the changes in the RhinoCommon SDK."
keywords = [ "C#", "plugin" ]
languages = [ "C#" ]
sdk = [ "RhinoCommon" ]
title = "What's New?"
type = "guides"
weight = 2

[admin]
TODO = "needs review"
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

The following document describes what has been added, what has changed, and how to deal with these changes in the RhinoCommon SDK. A lot of effort has been put into keeping RhinoCommon compatible with versions found in earlier Rhino releaes. One goal of this document is to describe these breaking changes and what to do about them.

## Rhino 8

Rhino 8 now uses the open source [.NET Core Runtime](https://github.com/dotnet/runtime) for running .NET code on both Windows and Mac. This brings some performance improvements and aligns the .NET runtimes used across platforms. Previously, Rhino 7 and earlier used the [Mono runtime](https://www.mono-project.com/) on Mac, and .NET Framework exclusively on Windows.

On Windows, you can still optionally run using the .NET Framework runtime in the case of compatibility issues or running inside other software that requires it (e.g. Rhino.Inside Revit).

Most plugins are already compatible when running in .NET Core without any recompilation, but in the case of any incompatibilities you may need to update your plugin.

For more details, see [Moving to .NET 7](/guides/rhinocommon/moving-to-dotnet-7).

Also, we've updated the [Rhino Visual Studio Extension](https://github.com/mcneel/RhinoVisualStudioExtensions/releases) for both Windows and Mac.

And, there is an all new [RhinoCommon API Reference](https://developer.rhino3d.com/api/rhinocommon/html/R_Project_RhinoCommon.htm) online.

Here is what is new in [RhinoCommon 8](https://developer.rhino3d.com/api/rhinocommon/whatsnew/8.0).

## Rhino 7

RhinoCommon plug-ins for Rhino 7 are based on the Microsoft .NET Framework 4.8.

To developer plug-is Windows, use either [Visual Studio 2022](https://visualstudio.microsoft.com/downloads/) or [Visual Studio 2019](https://visualstudio.microsoft.com/vs/older-downloads/).

To develop plug-in on Mac, use [Visual Studio 2022 for Mac](https://visualstudio.microsoft.com/vs/mac/). Visual Studio 2019 for Mac should work as well.

Here is what is new in [RhinoCommon 7](https://developer.rhino3d.com/api/rhinocommon/whatsnew/7.0).
