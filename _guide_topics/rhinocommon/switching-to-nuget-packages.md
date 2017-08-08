---
title: Switching to NuGet Packages (Windows)
description: This guide goes over how to do switch the RhinoCommon and Grasshopper SDK assembly references from those which are shipped with Rhino and Grasshopper (and installed on your computer), to those published on NuGet.
authors: ['Luis Fraguada', 'Will Pearson']
author_contacts: ['luis', 'will']
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

In [previous guides](http://developer.rhino3d.com/guides/rhinocommon/your-first-plugin-windows/) you’ve seen how to set up a project to develop a RhinoCommon Plugin or Grasshopper Add-On. These guides relied on the Visual Studio Project Wizards that we publish to quickly get you going on plugin development. The wizards automatically reference the necessary assemblies to make RhinoCommon and Grasshopper SDKs available in your Visual Studio project. While this project setup should be fine for a number of cases, there might be some reasons to switch the RhinoCommon and Grasshopper assembly references to those which are published by [McNeel on NuGet](https://www.nuget.org/profiles/McNeel):
* Are you using continuous integration (CI)? Your build servers can automatically download the correct version of the SDK before compiling and publishing your shiny new release.
* Projects where several developers are collaborating and may have Rhino installed in varying locations (see also [this  question](https://stackoverflow.com/questions/1786917/is-there-a-way-to-specify-assembly-references-based-on-build-configuration-in-vi)), or not installed at all[^1].
* NuGet runs on Windows and Mac and is baked into Visual Studio and Xamarin Studio. You're probably already using it to install packages like [Json.NET](https://www.nuget.org/packages/newtonsoft.json).

Some negative consequences of using these NuGet packages for development:
* Using NuGet packages creates a disparity between what is used for building Rhino and what is used for debugging your plugin. For example, this disparity will lead to problems where a method that is available at compile time is not (yet) available at runtime (user did not update Rhino).
* After switching to NuGet packages, especially when targeting Rhino WIP versions or when there is a Rhino service release published, you should keep the package up-to-date with the current Rhino release. This adds additional burden when developing and debugging.

## Making the Switch

<div class="bs-callout bs-callout-danger">

<strong>Note</strong>: This short guide assumes you already know how to <a href="https://docs.microsoft.com/en-gb/nuget/quickstart/use-a-package">install a NuGet package</a>.

</div>

To switch to NuGet packages, follow these steps:

1. In Visual Studio, find the *Solution Explorer* and right-click on the *References* section of your project. Select *Manage NuGet Packages…* Alternatively, the same can be done through the Visual Studio Project menu, and choosing *Manage NuGet Packages…*

    ![Manage NuGet Packages]({{ site.baseurl }}/images/switching-to-nuget-packages-01.png)

2. In the NuGet tab which appears, click on *Browse*. In the search box, type in *RhinoCommon*. You should see an entry for RhinoCommon and one for Grasshopper. If you are writing a Rhino Plugin or Grasshopper Add-on for Rhino WIP, ensure you check *Include prerelease*.

    * If your project is a RhinoCommon Plugin, select the [RhinoCommon] entry, choose the Version, and click *Install*[^2].
      * For Rhino 5 plugins the Version should be *Latest stable 5.12*. NuGet will install `RhinoCommon.dll`.
      * For Rhino WIP, chose the *Latest prerelease*. NuGet will install `RhinoCommon.dll`, `Rhino.UI`, and `Eto.dll`.
      
    * If your project is a Grasshopper Add-on, select the [Grasshopper] entry, choose the Version, and click *Install*[^2]. For Grasshopper Add-ons on Rhino 5 the Version should be *Latest stable 0.9.76*. For Grasshopper Add-ons in Rhino WIP, chose the *Latest prerelease*. NuGet will install `Grasshopper.dll` and `GH_IO.dll` as well as the corresponding version of the RhinoCommon assemblies.

    ![Choose NuGet Packages]({{ site.baseurl }}/images/switching-to-nuget-packages-02.png)

3. After the install is complete, ensure that the new references are not copied to the output directory. Select any of the following references if they exist in your project: RhinoCommon, Eto, Rhino.UI, Grasshopper, GH_IO. In the *Properties* window, set *Copy Local* to *False*[^3].

    ![Copy Local]({{ site.baseurl }}/images/switching-to-nuget-packages-03.png)

---

## Related Topics

- [Your First Plugin (Windows)]({{ site.baseurl }}/guides/rhinocommon/your-first-plugin-windows/)
- [Your First Plugin (Mac)]({{ site.baseurl }}/guides/rhinocommon/your-first-plugin-mac/)
- [Your First Plugin (Cross-Platform)]({{ site.baseurl }}/guides/rhinocommon/your-first-plugin-crossplatform/)

---

## Footnotes
[^1]: We do not recommend developing plugins without Rhino, as debugging is essential.
[^2]: If your project already references one of the above assemblies, don't worry! NuGet will handle it.
[^3]: You might have noticed that the references created by these packages have `CopyLocal` set to `true`. Again, don't worry. We've included some MSBuild witchcraft that will ensure that `CopyLocal` is set to `false` when compiling your project, regardless of what it says in the Properties pane.

[RhinoCommon]: https://www.nuget.org/packages/rhinocommon
[Grasshopper]: https://www.nuget.org/packages/grasshopper
