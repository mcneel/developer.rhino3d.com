---
title: What is Rhino3dmIO?
description: This guide covers the RhinoCommon (.NET) build of openNURBS.
authors: ['dan_belcher']
sdk: ['openNURBS']
languages: ['C/C++', 'C#']
platforms: ['Windows', 'Mac']
categories: ['Overview']
origin: https://github.com/mcneel/rhinocommon/wiki/Rhino3dmIO-Toolkit-(OpenNURBS-build)
order: 2
keywords: ['openNURBS', 'C#', '.NET', 'Rhino3dmIO']
layout: toc-guide-page
---


## Overview

Rhino3dmIO is a .NET interface into the [OpenNURBS library](({{ site.baseurl }}/guides/opennurbs/what-is-opennurbs)).  This allows you to write .NET applications that can create and manipulate OpenNURBS Geometry.  The library also includes a full set of tools to read/write the *.3dm* file format.  And being OpenSource, you have access to the full source debug down to every little piece of code.

Install the Rhino3dmIO NuGet package into your project for the easiest access.

<div class="bs-callout bs-callout-danger">
  <h4>WARNING</h4>
  <p>This is NOT meant for any Rhino plugin development.  You should only be using Rhino3dmIO if you are attempting to read/write 3dm files from an application other than Rhino!</p>
</div>

---

## NuGet Package

This is the quickest method to access Rhino3DMio. The NuGet package is available for 3 platforms:

* Rhino3dmIO.Desktop (Windows/macOS)
* Rhino3dmIO.iOS
* Rhino3dmIO.Android

#### NuGet package using Visual Studio 2017 for Windows

1. *Right-click* your project file in *Solution Explorer* and select *Manage NuGet Packages ...*.
1. On the left side of the dialog expand the *Online* option and select *nuget.org*.
1. In the top right search box type "Rhino3dmIO" and click on a *Rhino3dmIO.Desktop* option (there are 3: Rhino3dmIO.Desktop (Windows/macOS), Rhino3dmIO.iOS and Rhino3dmIO.Android) and click on the *Install* button.
1. Close the *Manage NuGet Packages* dialog.  The NuGet package is installed and ready to use.

Changes that were made:

- The *Rhino3dmIO NuGet package* is installed in your project.
- The project references the *Rhino3dmIO* assembly.
- The project's *Post-build event* has been modified so the *rhino3dmio_native.dll* gets copied to the same output directory as *Rhino3dmIO.dll* when the project is built.


#### NuGet package using Xamarin Studio 4.2.5 for Mac

Follow the instructions in the [Including a NuGet package in your project](https://docs.microsoft.com/en-us/visualstudio/mac/nuget-walkthrough) from Microsoft.

<div class="bs-callout bs-callout-danger">
  <h4>NOTE</h4>
  <p>The following process has been tested with Xamarin Studio 4.2.5 and Xcode 5.1.1. You will need to have both Xamarin Studio and Xcode installed.</p>
</div>

---
