+++
aliases = ["/en/5/guides/cpp/migrate-your-plugin-windows/", "/en/6/guides/cpp/migrate-your-plugin-windows/", "/en/7/guides/cpp/migrate-your-plugin-windows/", "/wip/guides/cpp/migrate-your-plugin-windows/"]
authors = [ "dale" ]
categories = [ "Getting Started" ]
description = "This guide walks you through migrating your Rhino 7 plug-in project to Rhino 8."
keywords = [ "c", "C/C++", "plugin" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Migrate your plug-in project to Rhino 8"
type = "guides"
weight = 4
override_last_modified = "2020-08-28T14:47:34Z"

[admin]
TODO = ""
origin = ""
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

## Prerequisites

It is presumed you already have the necessary tools installed and are ready to go.  If you are not there yet, see [Installing Tools (Windows)](/guides/cpp/installing-tools-windows)

## Migrate the project

To migrate your Rhino 7 C++ plugin project to Rhino 8:

   1. Launch *Visual Studio* and click *File* > *Open* > *Project/Solution...*.
   2. Navigate to your project's folder and open either your plugin project *(.vcxproj)* or solution *(.sln)*
   3. When your plugin project opens, Visual Studio may display the *Retarget Projects* dialog box. Just click **Cancel**.  

      ![*Retarget Projects*](/images/migrate-plugin-windows-8-cpp-01.png)

## Replace property sheets

The Rhino C/C++ SDK includes Visual Studio Property Sheets that provide a convenient way to synchronize or share common settings among other plugin projects. You will need to remove references to Rhino 7 C/C++ SDK property sheets and replace them with references to Rhino 8 C/C++ SDK property sheets.

   1. From *Visual Studio*, click *View* > *Property Manager*.

      ![Property Manager](/images/migrate-plugin-windows-8-cpp-02.png)
   2. Right-click on the *Rhino.Cpp.PlugIn* property sheets in both *Debug &#124; x64* and *Release &#124; x64* configurations and click *Remove*.
   3. Right-click on the *Debug &#124; x64* configuration and click *Add Existing Property Sheet*.
   4. Navigate to the following location: *C:\Program Files\Rhino 8.0 SDK\PropertySheets*
   5. Select *Rhino.Cpp.PlugIn.props* and click *OK*.
   6. Repeat the above steps for the the *Release &#124; x64* configuration.
   7. Save the changes to your solution.

Your plugin project should now be ready to build with the Rhino 8 C/C++ SDK.

## Related Topics

- [What's New?](/guides/cpp/whats-new)

