---
title: What is Rhino3dmIO?
description: This guide covers the RhinoCommon (.NET) build of openNURBS.
authors: ['Dan Belcher']
author_contacts: ['dan']
apis: ['openNURBS']
languages: ['C/C++', 'C#']
platforms: ['Windows', 'Mac']
categories: ['Overview']
origin: https://github.com/mcneel/rhinocommon/wiki/Rhino3dmIO-Toolkit-(OpenNURBS-build)
order: 2
keywords: ['openNURBS', 'C#', '.NET', 'Rhino3dmIO']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## Overview

RhinoCommon supports a build "flavor" that allows it to be a .NET SDK for the openNURBS library.  This allows you to write .NET applications that can read/write the *.3dm* file format and since you have access to the full source debug down to every little piece of code.

<div class="bs-callout bs-callout-danger">
  <h4>WARNING</h4>
  <p>This is NOT meant for any Rhino plugin development.  You should only be using Rhino3dmIO if you are attempting to read/write 3dm files from an application other than Rhino!</p>
</div>

When built for openNURBS, RhinoCommon compiles will consist of two dynamic libraries:

1. *Rhino3dmIO.DLL* (C# DLL which .NET applications would reference)
1. *rhino3dmio_native.DLL* (Native C++ DLL which includes all of the opennurbs library; this file is called *libopennurbs.dylib* on macOS)

*Rhino3dmIO.DLL* uses pInvoke to call C functions exported from *rhino3dmio_native.DLL* in order to do most of the "heavy lifting" in openNURBS.  On Windows, make sure that both of these DLLs are in the same directory when used as a reference in your .NET application.

---

## Windows

There are two ways to use the Rhino3dmIO library.  You can either compile from the source code for maximum flexibility or you can install the Rhino3dmIO NuGet package into your project for simplicity.

### Steps to compile from source

<div class="bs-callout bs-callout-danger">
  <h4>NOTE</h4>
  <p>Currently, the only tested and supported compiled for the following process is Visual Studio 2010</p>
</div>

1. Clone or download all of the source code for the [RhinoCommon project](https://github.com/mcneel/rhinocommon).
1. Download the [OpenNURBS C++ toolkit](http://www.rhino3d.com/opennurbs).  Unzip the source code and place it in the folder titled *opennurbs*.  This is located in the RhinoCommon project under *rhinocommon/c/opennurbs*.
1. Open the *Rhino3dmIO.sln* in Visual Studio 2010.  This solution contains the C# and C++ projects needed along with sample C# console applications for testing.  You should now be able to compile and test the samples.

### Steps to install the NuGet package

1. Install the NuGet package manager, if you haven't already, by following [these instructions](http://docs.nuget.org/docs/start-here/installing-nuget).
1. *Right-click* your project file in *Solution Explorer* and select *Manage NuGet Packages ...*.
1. On the left side of the dialog expand the *Online* option and select *nuget.org*.
1. In the top right search box type "Rhino3dmIO" and click on a *Rhino3dmIO.dll* option (there are 3: *x86*, *x64*, and *AnyCPU*) and click on the *Install* button.
1. Close the *Manage NuGet Packages* dialog.  The Nuget package is installed and ready to use.

Changes that were made:

- The *Rhino3dmIO NuGet package* is installed in your project.
- The project references the *Rhino3dmIO* assembly.
- The project's *Post-build event* has been modified so the *rhino3dmio_native.dll* gets copied to the same output directory as *Rhino3dmIO.dll* when the project is built.

---

## Mac

<div class="bs-callout bs-callout-danger">
  <h4>NOTE</h4>
  <p>The following process has been tested with Xamarin Studio 4.2.5 and Xcode 5.1.1. You will need to have both Xamarin Studio and Xcode installed.</p>
</div>

### Steps to compile from source

1. Clone or download all of the source code for the [RhinoCommon project](https://github.com/mcneel/rhinocommon).
1. Download the [OpenNURBS C++ toolkit](http://www.rhino3d.com/opennurbs).  Unzip the source code and place it in the folder titled *opennurbs*.  This is located in the RhinoCommon project under *rhinocommon/c/opennurbs*.
1. Open the *Rhino3dmIO.sln* in *Xamarin Studio* for macOS.  You may get a number of warnings that some of the projects will not open correctly...it is safe to ignore these. This solution contains the C# projects needed along with a sample console application (*example_read_mac*) for testing.
1. *Right-click* on the *example_read_mac* project and select *Set as Startup Project*. In the *Project* drop-down menu, select *Build libopennurbs.dylib*.  This will build the native library.  When this is finished, you should be able to compile and test the sample project (see [these instructions](https://github.com/mcneel/rhinocommon/tree/master/examples/rhino3dmio/example_read_mac)).

More details:

- Your project will need to reference two assemblies: *Rhino3dmIo.dll* and *libopennurbs.dylib*.
- The *Build libopennurbs.dylib* command uses a script that instructs the Xcode command-line tools to build the native C++ library.  This script is named *build_native.py* and is located in the *rhinocommon/c/* folder.
- You can run *build_native.py* as a *Before Build* event in your project.  The *example_read_mac* project shows how this is done.  (You can find the *Before Build* commands in Xamarin Studio by *double-clicking* on the project to bring up the *Options* dialog.  *Custom Commands* are listed under the *Build* section.)
- Your project will need to create a *After Build* event that assures that the native library (*libopennurbs.dylib*) is copied to the appropriate location.  (Console applications - like *example_read_mac* - require that the library is in the same folder as the executable and be renamed to *rhino3dmio_native* as well.)
- If your project is targeting *MonoMac/Xamarin.Mac* - the most likely scenario - you will need to copy *libopennurbs.dylib* into the Application Bundle using an *After Build* command.  The conventional location for frameworks and libraries is: `$TARGET_DIR/Contents/Frameworks/$FRAMEWORK_NAME`
- The most convenient way to reference *libopennurbs.dylib* in a *MonoMac/Xamarin.Mac* project is to add an *.dll.config* file to your project so that *Rhino3dmIO.dll* can consume the native library.  This file should be named *Rhino3dmIO.dll.config* with the *Copy to output directory* property set to *Copy if newer* or *Always copy.*  This config file should contain the following:

```
<configuration> <dllmap dll="rhino3dmio_native" target="@executable_path/../Frameworks/libopennurbs.dylib"/> </configuration>
```

- The *exe.config* file sits next to the executable within the Application bundle and redirects mono to reference the specified file.
