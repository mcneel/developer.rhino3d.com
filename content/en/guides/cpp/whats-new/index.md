+++
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

For this reason, the Rhino C/C++ SDK was *not* broken between Rhino 6 and 7. Thus, plugins written for Rhino 6 using the Rhino 6 C/C++ SDK should load and run without modification in Rhino 7. However, we do encourage developers to migrate their plugin projects to Rhino 7 so they can take advantage to new and enhanced features.

## Visual Studio 2019

To write C++ plug-ins for Rhino 7 using the Rhino 7 C/C++ SDK, you will need [Visual Studio 2019](/guides/cpp/installing-tools-windows).

What’s really exciting is that the free Community edition of Visual Studio will work to build plug-ins for Rhino 7. Of course, you can also use either the Professional or Enterprise edition.

# Subdivision Surfaces

A new subdivision surface object has been added to Rhino 7. The core geometry component is ```ON_SubD``` class, which is also part of openNURBS. All subdivision code will be available in the Rhino plug-in SDK.

The ```ON_SubD``` class has full support for Catmull-Clark quad subdivision surfaces and for Loop-Warren triangle subdivision surfaces. The Rhino subdivision surface control polygons have no limits on vertex valences (edge and face counts) or facet edge counts.

Rhino subdivision objects are automatically converted to cubic NURBS polysurfaces or meshes when a subdivision object is selected as input to a command that is expecting a polysurface or mesh. This is how Rhino's lightweight extrusion object behaves.

## Deprecation

Obsolete functions from Rhino 6 are marked as deprecated with a message to help accomplish the same goal through alternate functions in the Rhino 6 SDK. These deprecations will generate compiler warnings when plug-in code attempts to call these functions.

Functions marked as deprecated may or may not continue to work in Rhino 7. Thus, you should replace all calls to deprecated functions with calls to their replacements before distributing any plug-in.

### Other
Coming soon...

## Related Topics

- [Installing Tools (Windows)](/guides/cpp/installing-tools-windows)
- [Migrate your plugin project to Rhino 7](/guides/cpp/migrate-your-plugin-windows)
- [C++ SDK samples on GitHub](https://github.com/mcneel/rhino-developer-samples/tree/7)
