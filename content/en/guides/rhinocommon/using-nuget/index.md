+++
aliases = ["/5/guides/rhinocommon/using-nuget/", "/6/guides/rhinocommon/using-nuget/", "/7/guides/rhinocommon/using-nuget/", "/wip/guides/rhinocommon/using-nuget/"]
authors = [ "luis", "will", "callum" ]
categories = [ "Advanced" ]
description = "This guide describes how developers can use the NuGet packages available for RhinoCommon and Grasshopper."
keywords = [ "nuget" ]
languages = [ "C#" ]
sdk = [ "RhinoCommon" ]
title = "Using NuGet"
type = "guides"
weight = 1
override_last_modified = "2019-05-18T06:45:18Z"

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++


## Why NuGet?

In [previous](/guides/rhinocommon/your-first-plugin-windows/) [guides](/guides/rhinocommon/your-first-plugin-mac/) you’ve seen how to set up a project to develop a RhinoCommon Plugin or Grasshopper component.  These guides relied on the Visual Studio Project Wizards that we publish to quickly get you going on plugin development.  The wizards automatically reference the necessary assemblies to make RhinoCommon and Grasshopper SDKs available in your Visual Studio project.  While this project setup should be fine for a number of cases, there might be some reasons to switch the RhinoCommon and Grasshopper assembly references to those which are published by [McNeel on NuGet](https://www.nuget.org/profiles/McNeel)...

### Advantages

There are several potential advantages to using NuGet packages for RhinoCommon SDKs:

* It's great for projects with multiple developers (or developers with multiple computers). No more references to `Grasshopper.dll` that include `C:\Users\<username>\AppData\...`.
* NuGet runs on Windows and Mac and is baked into Visual Studio (for Windows).
* Are you using Continuous Integration (CI)?  Your build servers can automatically download the correct version of the SDK before compiling and publishing your shiny new release.
* You're probably already using it to install packages like [Json.NET](https://www.nuget.org/packages/newtonsoft.json).
* You can target a lower version of RhinoCommon than you have installed to ensure full compatibility across all Rhino versions

### Potential Pitfalls

NuGet makes it easy to compile plug-ins against versions of Rhino other than those installed on your computer. This is handy for backwards-compatible and/or cross-platform development. However, the fact that your Rhino installation and your RhinoCommon/Grasshopper references are "out of sync" can cause problems.

* NuGet packages will need to be updated separately to Rhino
* You _may_ have trouble debugging your plug-in if it was built against a version of RhinoCommon that is newer than the one included with Rhino[^a]

## Getting Started

<div class="bs-callout">

<strong>Note</strong>: You may wish to read Microsoft's guide to <a href="https://docs.microsoft.com/en-gb/nuget/quickstart/use-a-package">installing NuGet packages in Visual Studio</a> in addition to this one.
And how to <a href="https://code.visualstudio.com/docs/csharp/package-management">install a Nuget Package in Visual Studio Code.</a>

</div>

We have a few NuGet packages available and you can install them like you would any other. 

The [RhinoCommon] package includes

* *RhinoCommon.dll*
* *Eto.dll*
* *Rhino.UI.dll*

The [Grasshopper] package depends[^1] on the RhinoCommon package _with the same version_ and includes

* *Grasshopper.dll*
* *GH_IO.dll*

We also have a [RhinoWindows](https://www.nuget.org/packages/RhinoWindows) package.

We're currently publishing new package versions for every public release of Rhino for Windows, including preleases (WIP, release candidate and beta). If you're developing for Rhino WIP for Mac, choose the latest 6.* package – RhinoCommon and Grasshopper are cross-platform!

If you're searching for a version of one of our packages that corresponds to a prerelease version of Rhino then make sure you check "include prerelease". These packages are marked with a prerelease suffix in the version number, such as `-wip` or `-rc`.

### Step-by-Step (Windows)

To switch to NuGet packages, follow these steps:

1. In Visual Studio, find the *Solution Explorer* and right-click on the *References* section of your project. Select *Manage NuGet Packages...* Alternatively, the same can be done through the Visual Studio *Project* menu, and choosing *Manage NuGet Packages...*

    ![Manage NuGet Packages - Windows](/images/using-nuget-01.png)

2. In the NuGet tab which appears, click on *Browse*. In the search box, type in *RhinoCommon*. You should see an entry for RhinoCommon and one for Grasshopper. If you are writing a Rhino Plugin or Grasshopper Add-on for Rhino WIP, ensure you check *Include prerelease*.

    If your project is a **RhinoCommon Plug-in**, select the [RhinoCommon] package. For Rhino WIP choose the *Latest prerelease* and click *Install*. NuGet will install[^2] *RhinoCommon.dll*, *Rhino.UI* and *Eto.dll*.

    If your project is a **Grasshopper Add-on**, select the [Grasshopper] package. For Grasshopper Add-ons in Rhino WIP choose the *Latest prerelease* and click *Install*. NuGet will install[^2] *Grasshopper.dll* and *GH_IO.dll* as well as the corresponding version of the RhinoCommon assemblies.

    ![Choose NuGet Packages - Windows](/images/using-nuget-02.png)

3. *(Optional)* The references created by these packages have `CopyLocal` set to `true`.  Normally, it is a best practice to make sure that the references are not copied to the output directory, since they are included with Rhino. You can do this by selecting any of the following references if they exist in your project - *RhinoCommon*, *Eto*, *Rhino.UI*, *Grasshopper*, *GH_IO* - and, in the *Properties* window, set `CopyLocal` to `false`.  The reason this step is *optional* is that we've included some MSBuild witchcraft that will ensure that `CopyLocal` is set to `false` when compiling your project, regardless of what it says in the *Properties* window.

    ![Copy Local](/images/using-nuget-03.png)


### Step-by-Step (Mac)
Further Reading [NuGet in Visual Studio Code](https://code.visualstudio.com/docs/csharp/package-management)

1. In Visual Studio Code, open the Command Palette _(⌘ ⇧ P)_ and search nuget, choose *Add NuGet Package*. Alternatively, the same can be done through the Solution Explorer  by right clicking the Project you wish to add the package to, and choosing *Add NuGet Package...*

    {{< call-out hint "Required Plugin" >}}
[C# Dev Kit](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csdevkit))
    {{< /call-out >}}

    ![Manage NuGet Packages - Mac](/images/using-nuget-04.png)


2. The command palette will appear at the top of Visual Studio Code. In the search box, type in *RhinoCommon* and press enter. You should see an entry for RhinoCommon and one for Grasshopper.

    ![Manage NuGet Packages - Mac](/images/using-nuget-05.png)

3. Now you can choose the version of the NuGet package you wish to target

    ![Choose NuGet Packages - Mac](/images/using-nuget-06.png)

{{< call-out hint "Pre-release Versions" >}}
If you are writing a Rhino Plugin or Grasshopper Add-on for Rhino WIP, you will need to install a pre-release NuGet Package.
At the time of writing time the C# Dev Kit does not include a way to show pre-release versions.
You must use _dotnet add package RhinoCommon_ in the terminal, _([The RhinoCommon NuGet Page](https://www.nuget.org/packages/rhinocommon) has a handy copy paste to make this easier)_.
Or you can use the [NuGet Gallery Plugin](https://marketplace.visualstudio.com/items?itemName=patcx.vscode-nuget-gallery) which offers this functionality.
{{< /call-out >}}

If your project is a **RhinoCommon Plug-in**, select the [RhinoCommon] package. NuGet will install *RhinoCommon.dll*, *Rhino.UI* and *Eto.dll* once you have selected a version.

If your project is a **Grasshopper Add-on**, select the [Grasshopper] package. NuGet will install[^1] *Grasshopper.dll* and *GH_IO.dll* as well as the corresponding version of the RhinoCommon assemblies once you have selected a version.

4. Confirm your NuGet Packages installed correctly
Check your Project in the Solution Explorer, you should see a new entry under dependencies > Packages
    
    ![Choose NuGet Packages - Mac](/images/using-nuget-07.png)

## Related topics

- [Your First Plugin (Windows)](/guides/rhinocommon/your-first-plugin-windows)
- [Your First Plugin (Mac)](/guides/rhinocommon/your-first-plugin-mac)

**Footnotes**
[^1]: This means that if you install the Grasshopper NuGet package, the matching RhinoCommon package will be installed automatically.
[^2]: If your project already references one of the above assemblies, don't worry! NuGet will handle it.
[^a]: Your plug-in will not load if it uses parts of the API which don't exist in the running version of Rhino.

[RhinoCommon]: https://www.nuget.org/packages/rhinocommon
[Grasshopper]: https://www.nuget.org/packages/grasshopper
