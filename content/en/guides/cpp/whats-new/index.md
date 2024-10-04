+++
aliases = ["/en/5/guides/cpp/whats-new/", "/en/6/guides/cpp/whats-new/", "/en/7/guides/cpp/whats-new/", "/wip/guides/cpp/whats-new/"]
authors = [ "dale" ]
categories = [ "Overview" ]
description = "This brief guide outlines the new and changed features in the Rhino C/C++ SDK."
keywords = [ "c", "C/C++", "plugin" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "What's New?"
type = "guides"
weight = 2

[admin]
TODO = "needs review and the original contained links to empty wiki entries."
origin = "http://wiki.mcneel.com/developer/rhino/5/sdkfeatures"
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


## Overview

The Rhino C/C++ SDK is *not* an abstract SDK. That is, the native classes and functions that are made available in the SDK are also used internally by Rhino. Thus, when the signatures of classes or functions change, all developers, both internal and external, are required to modify their source code to accommodate for the change.

For this reason, the Rhino C/C++ SDK was *not* broken between Rhino 6, 7 and 8. Thus, plug-ins written for Rhino 7 using the Rhino 7 C/C++ SDK should load and run without modification in Rhino 8. However, we do encourage developers to migrate their plug-in projects to Rhino 8 so they can take advantage to new and enhanced features.

## Rhino 8

### Visual Studio 2019 (v142)

To write C++ plug-ins for Rhino 8 using the Rhino 8 C/C++ SDK, you will need a version of Microsoft Visual Studio that includes the Visual Studio 2019 (v142) platform toolset. Thus, you can use either [Visual Studio 2022](https://visualstudio.microsoft.com/downloads/) or [Visual Studio 2019](https://visualstudio.microsoft.com/vs/older-downloads/).

There is a new [Rhino Visual Studio Extension](https://github.com/mcneel/RhinoVisualStudioExtensions/releases), which includes project and command templates, that installs independently of Rhino C/C++ SDK.

## Rhino 7

### Visual Studio 2019 (v142)

To write C++ plug-ins for Rhino 7 using the Rhino 7 C/C++ SDK, you will need a version of Microsoft Visual Studio that includes the Visual Studio 2019 (v142) platform toolset. Thus, you can use either [Visual Studio 2022](https://visualstudio.microsoft.com/downloads/) or [Visual Studio 2019](https://visualstudio.microsoft.com/vs/older-downloads/).

Rhino 7 C/C++ SDK includes project and command wizards. Thus, you'll need to have Visual Studio 2019 installed on your system before installing the Rhino 7 C/C++ SDK.

### Subdivision Surfaces

A new subdivision surface object has been added to Rhino 7. The core geometry component is ```ON_SubD``` class, which is also part of openNURBS. All subdivision code will be available in the Rhino plug-in SDK.

The ```ON_SubD``` class has full support for Catmull-Clark quad subdivision surfaces and for Loop-Warren triangle subdivision surfaces. The Rhino subdivision surface control polygons have no limits on vertex valences (edge and face counts) or facet edge counts.

Rhino subdivision objects are automatically converted to cubic NURBS polysurfaces or meshes when a subdivision object is selected as input to a command that is expecting a polysurface or mesh. This is how Rhino's lightweight extrusion object behaves.

## Deprecation

Obsolete functions from Rhino are marked as deprecated with a message to help accomplish the same goal through alternate functions in the Rhino C/C++ SDK. These deprecations will generate compiler warnings when plug-in code attempts to call these functions.

Functions marked as deprecated may or may not continue to work in future Rhino versions. Thus, you should replace all calls to deprecated functions with calls to their replacements before distributing any plug-in.

## Related Topics

- [Installing Tools (Windows)](/guides/cpp/installing-tools-windows)
- [C++ SDK samples on GitHub](https://github.com/mcneel/rhino-developer-samples)
- [Migrate Rhino 6 plug-in projects to Rhino 7](/guides/cpp/migrate-your-plugin-windows)
