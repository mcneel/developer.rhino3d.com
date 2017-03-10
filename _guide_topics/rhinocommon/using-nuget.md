---
title: Using NuGet
description: This guide describes how developers can use the NuGet packages available for RhinoCommon and Grasshopper.
authors: ['Will Pearson']
author_contacts: ['will']
apis: ['RhinoCommon']
languages: ['C#']
platforms: ['Windows']
categories: ['Advanced']
order: 1
keywords: ['nuget']
layout: toc-guide-page
---

<div class="bs-callout bs-callout-danger">

<strong>Note</strong>: Here be dragons! This is work-in-progress. We have some ideas as to how NuGet packages for <a href="https://www.nuget.org/packages/rhinocommon">RhinoCommon</a> and <a href="https://www.nuget.org/packages/grasshopper">Grasshopper</a> might be useful, but we need developers like yourself to use them and figure out if and how they can improve your development workflows. Currently we're publishing NuGet packages for each Rhino WIP for Windows release.

</div>

## Why NuGet?

There are several potential advantages to using NuGet packages for Rhino's .NET SDKs:

* It's great for projects with multiple developers (or developers with multiple computers). No more references to `Grasshopper.dll` that include the `C:\Users\<username>\AppData\...`.
* NuGet runs on Windows and Mac and is baked into Visual Studio and Xamarin Studio.
* Are you using CI? Your build servers can automatically download the correct version of the SDK before compiling and publishing your shiny new release
* You're probably already using it to install packages like [Json.NET](https://www.nuget.org/packages/newtonsoft.json).

## Getting Started

<div class="bs-callout bs-callout-danger">

<strong>Note</strong>: This short guide assumes you already know how to <a href="https://docs.microsoft.com/en-gb/nuget/quickstart/use-a-package">install a NuGet package</a>.

</div>

You can install the RhinoCommon package like you would any other, with one caveat – when searching for the package make sure you check "include prerelease". We're only releasing packages for Rhino WIP for Windows right now, and as such all the packages are marked with the `-wip` suffix which NuGet interprets as "prerelease".

The [RhinoCommon] package includes

* `RhinoCommon.dll`
* `Eto.dll`
* `Rhino.UI.dll`

The [Grasshopper] package depends[^1] on the RhinoCommon package _with the same version_ and includes

* `Grasshopper.dll`
* `GH_IO.dll`

Finally a few important things to mention:

* If your project already references one of the above assemblies, don't worry! NuGet will handle it.
* You might have noticed that the references created by these packages have `CopyLocal` set to `true`. Again, don't worry. We've included some MSBuild witchcraft that will ensure that `CopyLocal` is set to `false` when compiling your project, regardless of what it says in the Properties pane.
* Don't forget to add `packages.config` to source control, if you're using it. (Hint: you should be!)

---

## Related topics

- [Your First Plugin (Windows)]({{ site.baseurl }}/guides/rhinocommon/your-first-plugin-windows)
- [Your First Plugin (Mac)]({{ site.baseurl }}/guides/rhinocommon/your-first-plugin-mac)

---

## Footnotes

[^1]: This means that if you install the Grasshopper NuGet package, the matching RhinoCommon package will be installed automatically.

[RhinoCommon]: https://www.nuget.org/packages/rhinocommon
[Grasshopper]: https://www.nuget.org/packages/grasshopper
