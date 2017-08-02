---
title: Switching to NuGet Packages (Windows)
description: This guide goes over how to do switch the RhinoCommon and Grasshopper SDK assembly references from those which are shipped with Rhino and Grasshopper (and installed on your computer), to those published on NuGet.
authors: ['Luis Fraguada']
author_contacts: ['luis']
sdk: ['RhinoCommon']
languages: ['C#']
platforms: ['Windows']
categories: ['Advanced']
origin: unset
order: 1
keywords: ['NuGet', 'RhinoCommon', 'Plugin', 'Grasshopper', 'Add-On']
layout: toc-guide-page
---

## Overview

In [previous guides](http://developer.rhino3d.com/guides/rhinocommon/your-first-plugin-windows/) you’ve seen how to set up a project to develop a RhinoCommon Plugin or Grasshopper Add-On. These guides relied on the Visual Studio Project Wizards that we publish to quickly get you going on plugin development. The wizards automatically reference the necessary assemblies to make RhinoCommon and Grasshopper SDKs available in your Visual Studio project. While this project setup should be fine for a number of cases, there might be some reasons to switch the RhinoCommon and Grasshopper assembly references to those which are published on NuGet:
* Cases where development includes continuous integration deployed on a remote server
* Projects where several developers are collaborating and may have Rhino installed in varying locations (see also this question), or not installed at all[^1].

Some negative consequences of using these NuGet packages for development:
* Using NuGet packages creates a disparity between what is used for building Rhino and what is used for debugging your plugin. For example, this disparity will lead to problems where a method that is available at compile time is not (yet) available at runtime (user did not update Rhino).

* After switching to NuGet packages, especially when targeting Rhino WIP versions or when there is a Rhino service release published, you should keep the package up-to-date with the current Rhino release. This adds additional burden when developing and debugging.

## Making the Switch

To switch to NuGet packages, follow these steps:

1. In Visual Studio, find the *Solution Explorer* and right-click on the *References* section of your project. Select *Manage NuGet Packages…* Alternatively, the same can be done through the Visual Studio Project menu, and choosing *Manage NuGet Packages…*

    ![Manage NuGet Packages]({{ site.baseurl }}/images/switching-to-nuget-packages-01.png)

2. In the NuGet tab which appears, click on *Browse*. In the search box, type in *RhinoCommon*. You should see an entry for RhinoCommon and one for Grasshopper. If you are writing a Plugin for Rhino WIP, ensure you check *Include prerelease*.

    * If your project is a RhinoCommon Plugin, select the RhinoCommon entry, choose the Version, and click *Install*. For Rhino 5 plugins the Version should be *Latest stable 5.12*. For Rhino WIP, chose the *Latest prerelease*.
    * If your project is a Grasshopper Add-on, select the Grasshopper entry, choose the Version, and click *Install*. For Grasshopper Add-ons on Rhino 5 the Version should be *Latest stable 0.9.76*. For Grasshopper Add-ons in Rhino WIP, chose the *Latest prerelease*.

    ![Choose NuGet Packages]({{ site.baseurl }}/images/switching-to-nuget-packages-02.png)

3. After the install is complete, ensure that the new references are not copied to the output directory. Select any of the following references if they exist in your project: RhinoCommon, Eto, Rhino.UI, Grasshopper, GH_IO. In the *Properties* window, set *Copy Local* to *False*.

    ![Copy Local]({{ site.baseurl }}/images/switching-to-nuget-packages-03.png)

---

## Related Topics

- [Your First Plugin (Windows)]({{ site.baseurl }}/guides/rhinocommon/your-first-plugin-windows/)
- [Your First Plugin (Mac)]({{ site.baseurl }}/guides/rhinocommon/your-first-plugin-mac/)
- [Your First Plugin (Cross-Platform)]({{ site.baseurl }}/guides/rhinocommon/your-first-plugin-crossplatform/)

---

## Footnotes
[^1]: We do not recommend developing plug-ins without Rhino, as debugging is essential.
