---
title: Using NuGet
description: This guide describes how developers can use the NuGet packages available for RhinoCommon and Grasshopper.
authors: ['Luis Fraguada', 'Will Pearson']
author_contacts: ['fraguada', 'will']
sdk: ['RhinoCommon']
languages: ['C#']
platforms: ['Windows', 'Mac']
categories: ['Advanced']
origin: unset
order: 1
keywords: ['nuget']
layout: toc-guide-page
---

<div class="bs-callout bs-callout-danger">

<strong>Warning</strong>: Here be dragons! This is work-in-progress. We have some ideas as to how NuGet packages for <a href="https://www.nuget.org/packages/rhinocommon">RhinoCommon</a> and <a href="https://www.nuget.org/packages/grasshopper">Grasshopper</a> might be useful, but we need developers like yourself to use them and figure out if and how they can improve your development workflows. Currently we're publishing NuGet packages for each Rhino release.

</div>

## Why NuGet?

In [previous]({{ site.baseurl }}/guides/rhinocommon/your-first-plugin-windows/) [guides]({{ site.baseurl }}/guides/rhinocommon/your-first-plugin-mac/) you’ve seen how to set up a project to develop a RhinoCommon Plugin or Grasshopper component.  These guides relied on the Visual Studio Project Wizards that we publish to quickly get you going on plugin development.  The wizards automatically reference the necessary assemblies to make RhinoCommon and Grasshopper SDKs available in your Visual Studio project.  While this project setup should be fine for a number of cases, there might be some reasons to switch the RhinoCommon and Grasshopper assembly references to those which are published by [McNeel on NuGet](https://www.nuget.org/profiles/McNeel)...

### Advantages

There are several potential advantages to using NuGet packages for RhinoCommon SDKs:

* It's great for projects with multiple developers (or developers with multiple computers). No more references to `Grasshopper.dll` that include `C:\Users\<username>\AppData\...`.
* NuGet runs on Windows and Mac and is baked into Visual Studio (for both Window and Mac).
* Are you using Continuous Integration (CI)?  Your build servers can automatically download the correct version of the SDK before compiling and publishing your shiny new release.
* You're probably already using it to install packages like [Json.NET](https://www.nuget.org/packages/newtonsoft.json).

### Potential Pitfalls

NuGet makes it easy to compile plug-ins against versions of Rhino other than those installed on your computer. This is handy for backwards-compatible and/or cross-platform development. However, the fact that your Rhino installation and your RhinoCommon/Grasshopper references are "out of sync" can cause problems.

* NuGet packages will need to be updated separately to Rhino
* You _may_ have trouble debugging your plug-in if it was built against a version of RhinoCommon that is newer than the one included with Rhino[^a]

## Getting Started

<div class="bs-callout">

<strong>Note</strong>: You may wish to read Microsoft's guide to <a href="https://docs.microsoft.com/en-gb/nuget/quickstart/use-a-package">installing NuGet packages</a> in addition to this one.

</div>

You can install the RhinoCommon package like you would any other, with one caveat – when searching for the package make sure you check "include prerelease". We're publishing packages for each Rhino WIP for Windows release, and as such all the packages are marked with the `-wip` suffix which NuGet interprets as "prerelease".

The [RhinoCommon] package includes

* *RhinoCommon.dll*
* *Eto.dll*
* *Rhino.UI.dll*

The [Grasshopper] package depends[^1] on the RhinoCommon package _with the same version_ and includes

* *Grasshopper.dll*
* *GH_IO.dll*

### Step-by-Step (Windows)

To switch to NuGet packages, follow these steps:

1. In Visual Studio, find the *Solution Explorer* and right-click on the *References* section of your project. Select *Manage NuGet Packages...* Alternatively, the same can be done through the Visual Studio *Project* menu, and choosing *Manage NuGet Packages...*

    ![Manage NuGet Packages - Windows]({{ site.baseurl }}/images/using-nuget-01.png)

2. In the NuGet tab which appears, click on *Browse*. In the search box, type in *RhinoCommon*. You should see an entry for RhinoCommon and one for Grasshopper. If you are writing a Rhino Plugin or Grasshopper Add-on for Rhino WIP, ensure you check *Include prerelease*.

    If your project is a **RhinoCommon Plug-in**, select the [RhinoCommon] package. For Rhino WIP choose the *Latest prerelease* and click *Install*. NuGet will install[^2] *RhinoCommon.dll*, *Rhino.UI* and *Eto.dll*.

    If your project is a **Grasshopper Add-on**, select the [Grasshopper] package. For Grasshopper Add-ons in Rhino WIP choose the *Latest prerelease* and click *Install*. NuGet will install[^2] *Grasshopper.dll* and *GH_IO.dll* as well as the corresponding version of the RhinoCommon assemblies.

    ![Choose NuGet Packages - Windows]({{ site.baseurl }}/images/using-nuget-02.png)

3. *(Optional)* The references created by these packages have `CopyLocal` set to `true`.  Normally, it is a best practice to make sure that the references are not copied to the output directory, since they are included with Rhino. You can do this by selecting any of the following references if they exist in your project - *RhinoCommon*, *Eto*, *Rhino.UI*, *Grasshopper*, *GH_IO* - and, in the *Properties* window, set `CopyLocal` to `false`.  The reason this step is *optional* is that we've included some MSBuild witchcraft that will ensure that `CopyLocal` is set to `false` when compiling your project, regardless of what it says in the *Properties* window.

    ![Copy Local]({{ site.baseurl }}/images/using-nuget-03.png)

4. _(Optional)_ If you're using version control, don't forget to commit the new _packages.config_ file!

### Step-by-Step (Mac)

1. In Visual Studio for Mac, find the *Solution Explorer* and double-click on the *Packages* section of your project.  Alternatively, the same can be done through the Visual Studio *Project* menu, and choosing *Add NuGet Packages...*

    ![Manage NuGet Packages - Mac]({{ site.baseurl }}/images/using-nuget-04.png)

2. The *Add Packages* dialog which appears. In the search box, type in *RhinoCommon*. You should see an entry for RhinoCommon and one for Grasshopper. If you are writing a Rhino Plugin or Grasshopper Add-on for Rhino WIP, ensure you check *Show pre-release packages*.

    If your project is a **RhinoCommon Plug-in**, select the [RhinoCommon] package. For Rhino WIP choose the *Latest version* and click *Add Package*. NuGet will install[^2] *RhinoCommon.dll*, *Rhino.UI* and *Eto.dll*.

    If your project is a **Grasshopper Add-on**, select the [Grasshopper] package. For Grasshopper Add-ons in Rhino WIP choose the *Latest version* and click *Add Package*. NuGet will install[^2] *Grasshopper.dll* and *GH_IO.dll* as well as the corresponding version of the RhinoCommon assemblies.

    ![Choose NuGet Packages - Mac]({{ site.baseurl }}/images/using-nuget-05.png)

3. *(Optional)* The references created by these packages have *Local Copy* set to `true`.  Normally, it is a best practice to make sure that the references are not copied to the output directory, since they are included with Rhino. You can do this by selecting any of the following references if they exist in your project - *RhinoCommon*, *Eto*, *Rhino.UI*, *Grasshopper*, *GH_IO* - and, in the *Properties* window, set *Local Copy* to `false` (or unchecked).  The reason this step is *optional* is that we've included some MSBuild witchcraft that will ensure that *Local Copy* is set to `false` when compiling your project, regardless of what it says in the *Properties* window.

    <p style="text-align:center;"><img src="{{ site.baseurl }}/images/using-nuget-06.png" alt="Copy Local - Mac" style="width: 450px;"/></p>
4. _(Optional)_ If you're using version control, don't forget to commit the new _packages.config_ file!

---

## Related topics

- [Your First Plugin (Windows)]({{ site.baseurl }}/guides/rhinocommon/your-first-plugin-windows)
- [Your First Plugin (Mac)]({{ site.baseurl }}/guides/rhinocommon/your-first-plugin-mac)

---

## Footnotes
[^1]: This means that if you install the Grasshopper NuGet package, the matching RhinoCommon package will be installed automatically.
[^2]: If your project already references one of the above assemblies, don't worry! NuGet will handle it.
[^a]: Your plug-in will not load if it uses parts of the API which don't exist in the running version of Rhino.

[RhinoCommon]: https://www.nuget.org/packages/rhinocommon
[Grasshopper]: https://www.nuget.org/packages/grasshopper
