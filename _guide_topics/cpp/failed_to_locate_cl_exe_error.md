---
title: Failed to locate CL.exe error
description: This guide discusses the Failed to locate CL error using Visual Studio 2010.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Troubleshooting']
origin: http://wiki.mcneel.com/developer/sdksamples/trackererror
order: 1
keywords: ['rhino', 'troubleshooting']
layout: toc-guide-page
TODO: 'needs updated screen captures'
---

# Failed to locate CL.exe error

{{ page.description }}

## Problem

You recently downloaded the Rhino C/C++ SDK and installed it on my system, along with Visual Studio 2010 Professional, per the instructions on this site.  However, when you went to build a test plugin, it failed to compile with this error:

```cmd
1>------ Build started: Project: Test, Configuration: Debug Win32 ------
1>Build started 3/15/2013 10:47:05 AM.
1>PrepareForBuild:
1>  Creating directory "C:\Visual Studio 2010\Projects\Test\Debug\".
1>InitializeBuildStatus:
1>  Creating "Debug\Test.unsuccessfulbuild" because "AlwaysCreate" was specified.
1>TRACKER : error TRK0005: Failed to locate: "CL.exe". The system cannot find the file specified.
1>
1>Build FAILED.
1>
1>Time Elapsed 00:00:00.24
========== Build: 0 succeeded, 1 failed, 0 up-to-date, 0 skipped ==========
```

## Solution

Visual Studio 2010 will only build 64-bit plugins for Rhino.  To build 32-bit plugins for Rhino, you need Visual Studio 2005.

If you do not have a copy of Visual Studio 2005, you can obtain one by purchasing a Visual Studio Professional with MSDN subscription.

If you are unable to obtain a copy of Visual Studio 2005, then you will only be able to build 64-bit plugins.

## More Info

With Visual Studio 2010, a project can target a different version of the Visual C++ libraries and compiler.  This is done by configuring the project use a different Platform toolset...

![Properties Page]({{ site.baseurl }}/images/failed_to_locate_cl_exe_error_01.png)

Reviewing the above image, you can see that the Rhino plugin project wizard configures 32-bit builds to use the `v80rhinos` platform toolset, which equates to using Visual Studio 2005's libraries and compiler.  This platform toolset configuration is installed on your system by the Rhino C++ SDK Installer.

If you change the active platform from Win32 to x64, you will see that 64-bit builds will use `v100`, or Visual Studio 2010.

The advantage that platform toolsets provide is that they enable you to take advantage of the IDE enhancements in Visual Studio 2010 while you continue to use an older version of the Visual C++ libraries and compiler.
