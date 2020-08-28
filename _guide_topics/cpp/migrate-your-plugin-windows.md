---
title: Migrate your plugin project to Rhino 7
description: This guide walks you through manually migrating your Rhino 6 plugin project to Rhino 7.
authors: ['dale_fugier']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Getting Started']
origin: unset
order: 6
keywords: ['c', 'C/C++', 'plugin']
layout: toc-guide-page
---

## Prerequisites

It is presumed you already have the necessary tools installed and are ready to go.  If you are not there yet, see [Installing Tools (Windows)]({{ site.baseurl }}/guides/cpp/installing-tools-windows)

## Migrate the project

1. Launch *Visual Studio 2019* and click *File* > *Open* > *Project/Solution...*.

2. Navigate to your project's folder and open either your plugin project *(.vcxproj)* or solution *(.sln)*

3. When your plugin project opens, Visual Studio will display the *Retarget Projects* dialog box. Specify the following actions and then click *OK*.  
![*Retarget Projects*]({{ site.baseurl }}/images/migrate-plugin-windows-cpp-02.png)

## Replace property sheets

The Rhino C/C++ SDK includes Visual Studio Property Sheets that provide a convenient way to synchronize or share common settings among other plugin projects. You will need to remove references to Rhino 6 C/C++ SDK property sheets and replace them with references to Rhino 7 C/C++ SDK property sheets.

   1. From *Visual Studio 2019*, click *View* > *Property Manager*.
      ![Property Manager]({{ site.baseurl }}/images/migrate-plugin-windows-cpp-01.png)
   2. Right-click on the *Rhino.Cpp.PlugIn* property sheets in both *Debug &#124; x64* and *Release &#124; x64* configurations and click *Remove*.
   3. Right-click on the *Debug &#124; x64* configuration and click *Add Existing Property Sheet*.
2. Navigate to the following location: *C:\Program Files\Rhino 7.0 SDK\PropertySheets*
3. Select *Rhino.Cpp.PlugIn.props* and click *OK*.
   6. Repeat the above steps for the the *Release &#124; x64* configuration.
   7. Save the changes to your solution.

Your plugin project should now be ready to build with the Rhino 7 C/C++ SDK.

## Related Topics

- [What's New?]({{ site.baseurl }}/guides/general/whats-new)

