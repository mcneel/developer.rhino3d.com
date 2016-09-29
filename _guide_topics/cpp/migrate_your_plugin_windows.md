---
title: Migrate your plugin project to Rhino 6
description: This guide walks you through migrating your plugin project to Rhino 6.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Getting Started']
order: 6
keywords: ['c', 'C/C++', 'plugin']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

It is presumed you already have the necessary tools installed and are ready to go.  If you are not there yet, see [Installing Tools (Windows)]({{ site.baseurl }}/guides/cpp/installing_tools_windows).

## Migrate the project

1. Launch *Visual Studio 2015* and navigate to *File* > *Open* > *Project/Solution...*.
1. Navigate to your project's folder and open either your plugin project *(.vcxproj)* or solution *(.sln)*
1. When your plugin project opens, navigate to the project's setting by clicking *Project* > *[ProjectName] Properties...*.
1. In the project's settings, select *All Configurations* and set the platform to *x64*. Then, set the *Platform Toolset* to *Visual Studio 2015 (v140)* and the click *Apply*.
![Plugin Settings]({{ site.baseurl }}/images/migrate_plugin_windows_cpp.png)

## Modify the project

1. Using *Visual Studio’s Solution Explorer*, open *stdafx.h* and add the following preprocessor definitons:

        /////////////////////////////////////////////////////////////////////////////
        // stdafx.h : include file for standard system include files,
        // or project specific include files that are used frequently, but
        // are changed infrequently

        #pragma once

        #ifndef VC_EXTRALEAN
        #define VC_EXTRALEAN        // Exclude rarely-used stuff from Windows headers
        #endif

        // Added for Rhino 6 Migration
        #define RHINO_V6_READY
        #if defined(DEBUG)
        #define RHINO_LIB_DIR "C:/Program Files/Rhino 6.0 SDK/lib/Debug"
        #else
        #define RHINO_LIB_DIR "C:/Program Files/Rhino 6.0 SDK/lib/Release"
        #endif
        
        ...
        
1. Also, modify the path to SDK headers, found in *stdafx.h* to reflect the path to the Rhino 6 C/C++ SDK:

        // Rhino SDK Preamble
        //#include "C:\Program Files (x86)\Rhino 5.0 x64 SDK\Inc\RhinoSdkStdafxPreamble.h"
        #include "C:/Program Files/Rhino 6.0 SDK/Inc/RhinoSdkStdafxPreamble.h"
        
        ...

        // Rhino Plug-in
        //#include "C:\Program Files (x86)\Rhino 5.0 x64 SDK\Inc\RhinoSdk.h"
        #include "C:/Program Files/Rhino 6.0 SDK/Inc/RhinoSdk.h"

        // Render Development Kit
        //#include "C:\Program Files (x86)\Rhino 5.0 x64 SDK\Inc\RhRdkHeaders.h"
        #include "C:/Program Files/Rhino 6.0 SDK/Inc/RhRdkHeaders.h"
        
        ...
        
        // Rhino Plug-in Linking Pragmas
        //#include "C:\Program Files (x86)\Rhino 5.0 x64 SDK\Inc\rhinoSdkPlugInLinkingPragmas.h"
        #include "C:/Program Files/Rhino 6.0 SDK/Inc/rhinoSdkPlugInLinkingPragmas.h"

1. Using *Visual Studio’s Solution Explorer*, open the project's *PlugIn.cpp* file and add the following SDK include statement:

        #include "StdAfx.h"
        #include "SamplePlugIn.h"
        // Added for Rhino 6 Migration
        #include "C:/Program Files/Rhino 6.0 SDK/Inc/rhinoSdkPlugInDeclare.h"
        
        ...
        
1. Using *Visual Studio’s Solution Explorer*, right-click on the *Header Files* folder and click *Add* > *New Item...*. Add a new *Header File (.h)* named *targetver.h* and add the following content to it:

        #pragma once
        
        // Including SDKDDKVer.h defines the highest available Windows platform.
        // If you wish to build your application for a previous Windows platform, 
        // include WinSDKVer.h and set the _WIN32_WINNT macro to the platform you
        // wish to support before including SDKDDKVer.h.
        #include "rhinoSdkWindowsVersion.h"
        
        #include <SDKDDKVer.h>
        
Your plugin project should now be ready to build with the Rhino 6 C/C++ SDK.

## Related Topics

- [What is a Rhino Plugin?]({{ site.baseurl }}/guides/general/what_is_a_rhino_plugin)
- [Installing Tools (Windows)]({{ site.baseurl }}/guides/cpp/installing_tools_windows)
