+++
aliases = ["/wip/guides/cpp/create-dependent-dll/"]
authors = [ "dale" ]
categories = [ "Advanced" ]
description = "This guide outlines the process of creating a Rhino-dependent C++ DLL."
keywords = [ "dll", "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Creating a Rhino-dependent C++ DLL"
type = "guides"
weight = 4

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

 
## Overview

A Rhino-dependent C++ DLL is one that links with Rhino C++ SDK libraries, and that can be used to add functionality that can be shared between multiple C++ plug-ins, or that can be used to add Platform Invoke (PInvoke), interop functionality to RhinoCommon or Grasshopper plug-ins.

## Create the DLL

To create a Rhino-dependent C++ DLL:

1. Download and install the [Rhino C++ SDK](https://developer.rhino3d.com/guides/cpp/installing-tools-windows/).
1. Launch Visual Studio.
1. Create a new [Rhino C/C++ plug-in project](https://developer.rhino3d.com/guides/cpp/your-first-plugin-windows/).
1. Using **Solution Explorer**, delete the `<Project>PlugIn` .cpp and .h files, and delete the `<Project>Command` .cpp file.
1. Using **Property Manager**, remove the `Rhino.Cpp.PlugIn` property page from both the `Debug|x64` and the `Release|x64` build configurations.
1. Again using **Property Manager**, add the `Rhino.Cpp.PlugInComponent.props` property page to both the `Debug|x64` and the `Release|x64` build configurations. The property page file is found in the `PropertySheets`` folder in the Rhino C++ SDK installation folder.
1. Build the project.

Done! You now have a Rhino-dependent DLL project. Now you are ready to add your functionality; either by adding or linking in other libraries, or by exporting custom C++ functions.

# More information

[Wrapping Native Libraries](https://developer.rhino3d.com/guides/rhinocommon/wrapping-native-libraries/)
