---
title: Manually migrate your plugin project to Rhino 6
description: This guide walks you through manually migrating your Rhino 5 plugin project to Rhino 6.
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

1. Launch *Visual Studio 2015* and click *File* > *Open* > *Project/Solution...*.
2. Navigate to your project's folder and open either your plugin project *(.vcxproj)* or solution *(.sln)*
3. When your plugin project opens, navigate to the project's setting by clicking *Project* > *Properties...*.
4. In the project's settings, set the *Configuration* to *All Configurations*, and set the platform to *x64*.
5. Then, set the *Platform Toolset* to *Visual Studio 2015 (v140)* and the click *Apply*.
![Plugin Settings]({{ site.baseurl }}/images/migrate_plugin_windows_cpp.png)

## Remove 32-bit support

Rhino 6 plugins are 64-bit only. If your plugin project has *Win32* platform support, then it is safe to remove it using *Visual Studio’s Configuation Manager*.

1. From *Visual Studio 2015*, click *Build* > *Configuation Manager...*.
 ![Configuation Manager]({{ site.baseurl }}/images/migrate_plugin_windows_cpp_02.png)
2. In *Project Contexts*, click *Platform > Edit...*.
 ![Select Project Platforms]({{ site.baseurl }}/images/migrate_plugin_windows_cpp_03.png)
3. In *Edit Project Platforms*, select the *Win32* platform, click *Remove* and then click *Close*.
 ![Edit Project Platforms]({{ site.baseurl }}/images/migrate_plugin_windows_cpp_04.png)
4. Repeat the above step for the solution by click *Active solution platform > Edit...*.
5. In *Edit Solution Platforms*, select the *Win32* platform, click *Remove* and then click *Close*.

## Rename build configurations

Rhino 6 plugin projects have different project build configuration names. See [Understanding Build Configurations]({{ site.baseurl }}/guides/cpp/plugin_build_configurations) for details. In order to use the SDK Property Sheets, you will need to rename the plugin project's build configurations so they match the new build configuration names.

1. In *Project Contexts*, click *Configuration > Edit...*.
 ![Select Project Configurations]({{ site.baseurl }}/images/migrate_plugin_windows_cpp_05.png)
2. In *Edit Project Configurations*, rename the *Debug* configuration to *DebugRhino*.
3. And then, rename the *PseudoDebug* configuration to *Debug*. 
 ![Edit Project Configurations]({{ site.baseurl }}/images/migrate_plugin_windows_cpp_06.png)
4. When you have finished renaming the configurations, click *Close*.
 ![Rename Project Configurations]({{ site.baseurl }}/images/migrate_plugin_windows_cpp_07.png)
5. Repeat the above step for the solution by click *Active solution Configuration > Edit...*.
6. In *Edit Solution Configurations*, rename the *Debug* configuration to *DebugRhino*, and then rename the *PseudoDebug* configuration to *Debug*. 
7. When finished, click *Close*.
8. Close *Configuation Manager*.

## Add property sheet

The Rhino C/C++ SDK includes Visual Studio Property Sheets that provide a convenient way to synchronize or share common settings among other plugin projects.

1. From *Visual Studio 2015*, click *View* > *Property Manager*.
 ![Property Manager]({{ site.baseurl }}/images/migrate_plugin_windows_cpp_08.png)
2. Right-click on the *Debug &#124; x64* configuration and click *Add Existing Property Sheet*.
3. Navigate to the following location: *C:\Program Files\Rhino 6.0 SDK\Wizards\Command*
4. Select *Rhino.Cpp.PlugIn.props* and click *OK*.
5. Repeat the above steps for the the *DebugRhino &#124; x64* and *Release &#124; x64* configurations.
 ![Add Existing Property Sheet]({{ site.baseurl }}/images/migrate_plugin_windows_cpp_09.png)

## Modify the project

The project's pre-compiled header file, *stdafx.h*, needs to be modified so SDK header file inclusions point to the correct location. Also, the plugin .cpp file needs to include an additional SDK header. Finally, Visual Studio's resource editor and compiler requires the project contain a *targerver.h* file that identifies the target platform.

1. Using *Visual Studio’s Solution Explorer*, open *stdafx.h* and add the following preprocessor directive:

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
        
        ...
        
1. Also, remove the path specifiers to Rhino SDK header files found in *stdafx.h*, as the path to the SDK is provided by the SDK Property Sheet added above.

        // Rhino SDK Preamble
        //#include "C:\Program Files (x86)\Rhino 5.0 x64 SDK\Inc\RhinoSdkStdafxPreamble.h"
        #include "RhinoSdkStdafxPreamble.h"
        
        ...

        // Rhino Plug-in
        //#include "C:\Program Files (x86)\Rhino 5.0 x64 SDK\Inc\RhinoSdk.h"
        #include "RhinoSdk.h"

        // Render Development Kit
        //#include "C:\Program Files (x86)\Rhino 5.0 x64 SDK\Inc\RhRdkHeaders.h"
        #include "RhRdkHeaders.h"
        
        ...
        
        // Rhino Plug-in Linking Pragmas
        //#include "C:\Program Files (x86)\Rhino 5.0 x64 SDK\Inc\rhinoSdkPlugInLinkingPragmas.h"
        #include "rhinoSdkPlugInLinkingPragmas.h"

1. Using *Visual Studio’s Solution Explorer*, open the project's *PlugIn.cpp* file and add the following SDK include statement:

        #include "StdAfx.h"
        #include "SamplePlugIn.h"
        
        // Added for Rhino 6 Migration
        #include "rhinoSdkPlugInDeclare.h"
        
        ...
        
1. Using *Visual Studio’s Solution Explorer*, right-click on the *Header Files* folder and click *Add* > *New Item...*. 
1. Add a new *Header File (.h)* named *targetver.h*.
1. Add the following content to it:

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