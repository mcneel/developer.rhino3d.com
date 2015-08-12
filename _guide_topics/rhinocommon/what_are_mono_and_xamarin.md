---
layout: toc-guide-page
title: What are Mono & Xamarin?
author: dan@mcneel.com
categories: ['Overview']
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#']
keywords: ['Mono', 'Xamarin', '.NET', 'Microsoft']
TODO: 0
origin: http://wiki.mcneel.com/developer/rhinocommon
order: 2
---

# What are Mono & Xamarin?
{: .toc-title }

This guide is an overview of [Mono](http://www.mono-project.com/), [Xamarin](http://www.xamarin.com), and how they relate to [RhinoCommon plugins]({{ site.baseurl }}/guides/rhinocommon/what_is_rhinocommon/).

---

## Mono
{: .toc-header }

The [Mono framework](http://www.mono-project.com/) is an [open source implementation](https://github.com/mono/mono) of [Microsoft's .NET Framework](http://www.microsoft.com/net) based on the [open standards](http://www.mono-project.com/docs/about-mono/languages/ecma/) for the C# language and the [Common Language Runtime](http://www.mono-project.com/docs/advanced/runtime/).

The Mono project has been in active development for [over a decade](https://en.wikipedia.org/wiki/Mono_(software)#History) and is used - behind the scenes - in many products.

#### Mono & Rhino for Mac
{: .toc-subheader }

Mono allows C# developers to write cross platform code targeting Windows, Mac OS X, Linux, Android, and iOS.  What this means for Rhino plugin developers is that they can - if written properly - run the same RhinoCommon plugin in *both* Rhino for Windows *and* Rhino for Mac...

<div align="center">
  <img src="{{ site.baseurl }}/images/rhino_mono_one_binary_two_platforms.png">
</div>

{::options parse_block_html="true" /}

RhinoCommon on Mac is executed through an embedded, custom, Mono framework.  That means Rhino for Mac is not using the public Mono, nor premium Xamarin.Mac.  However, the differences between public MonoMac and Rhino for Mac's MonoMac are inconsequential.

---

## Xamarin
{: .toc-header }

Xamarin is a private, for-profit, software company founded by the engineers who created Mono.  Xamarin is the primary maintainer and commercial sponsor of Mono.  Xamarin provides professional developer tools that make cross platform code easier to author, test, and maintain.

#### The Xamarin platform
{: .toc-subheader }

The **[Xamarin Platform](http://xamarin.com/platform)** is comprised of the following pieces:

- **[Xamarin Studio](http://xamarin.com/studio)**: C# IDE that runs on both Windows and Mac.
- **Xamarin.Android**: Used to build C# .NET applications for Android devices.  This is useful to have installed if you wish to use the [RhinoMobile]({{ site.baseurl }}/guides/#rhinomobile/) toolkit, but not required for RhinoCommon in Rhino for Mac.
- **Xamarin.iOS**: Used to build C# .NET applications for Apple iOS devices.  This is useful to have installed if you wish to use the [RhinoMobile]({{ site.baseurl }}/guides/#rhinomobile/) toolkit, but not required for RhinoCommon in Rhino for Mac.
- **Xamarin.Mac**: Xamarin's closed-source version of MonoMac.

For developing RhinoCommon plugins, *only* Xamarin Studio is required.

#### Xamarin Studio
{: .toc-subheader }

This is Xamarin's C# developer environment that runs on both Windows and Mac.  Xamarin Studio has many of the features of Microsoft's Visual Studio and uses *exactly the same formats* as Visual Studio: solutions (*.sln*) and C# projects (*.csproj*).  At McNeel, we use Xamarin Studio to develop [Rhino for Mac](http://www.rhino3d.com/mac) and [iRhino 3D](https://www.rhino3d.com/ios).  We highly recommend you use Xamarin Studio when developing RhinoCommon plugins for the Mac (or for Windows as well).

#### Xamarin.Mac?
{: .toc-subheader }

Rhino for Mac does not currently use Xamarin.Mac.

Xamarin.Mac is Xamarin's proprietary closed-source toolkit used to provide .NET access to native features of the Mac Operating System and to allow for compiling .NET projects into self-contained application bundles.  Rhino uses the open source MonoMac framework instead of Xamarin.Mac for accessing native OS X features (primarily native user interface features).

#### Visual Studio support
{: .toc-subheader }

Xamarin offers a [Visual Studio extension](http://xamarin.com/visual-studio), however this extension is only useful for Xamarin.iOS and Xamarin.Android development, **not** for RhinoCommon.  If you are writing RhinoCommon plugins you are free to use Visual Studio - when targeting either Rhino for Mac or Rhino for Windows - just as you normally would.  When you want to debug and test your plugin in Rhino for Mac, you will have to use Xamarin Studio, but you can use the *exactly same solution* and *project files* to do this.

#### Licensing Xamarin
{: .toc-subheader }

The Xamarin Platform requires a [paid license](https://store.xamarin.com/) to use.  

Xamarin's Platform can be [downloaded](https://xamarin.com/download) and tested before licensing.

Xamarin is [free for students](https://xamarin.com/student).

---

## Solution & Project
{: .toc-header }

Xamarin Studio uses the same formats as Visual Studio:

- **.sln**
- **.csproj**

It is important to stress: these *are* Visual Studio solutions and projects.  You can open solutions and projects created in Xamarin Studio in Visual Studio and vice-versa.

---

## Porting .NET code
{: .toc-header }

All of .NET is not yet implemented in Mono (although an awful lot is).  We recommend launching your plug-in project in Xamarin Studio and attempting to compile. That is the best way to find any potential problems with getting your plug-in to run on Mac Rhino. Please let McNeel know if you find something is missing from the SDK that you need, we may be able to provide this funcitonality in a Mac Rhino service release.

#### P/Invoke
{: .toc-subheader }

One of the areas that developers need to be aware of is any .NET code that uses P/invoke may experience problems when running on Mac. P/invoke is a technique to call unmanaged native functions from .NET code.  The feature is available on OS X/mono, but developers need to make sure that the P/invoke calls are calling native code written for OS X and not for Windows.  Many commercial .NET components use P/invoke so this is something we highly recommend you investigate.

#### UI and Eto
{: .toc-subheader }

User interface is where developers typically run into trouble with platform specific dependencies and features.  We use and support development of [Eto](https://github.com/picoe/Eto).  Using Eto can make your plugin look and work as a native application on all platforms, using a single UI codebase.  Eto ships with Rhino for Mac (and will ship with Rhino 6 for Windows).  Eto has an easy to use API and uses native toolkits, abstracting the platform-specific implementations for [WinForms](https://en.wikipedia.org/wiki/Windows_Forms) (GDI and Direct2D), [WPF](https://en.wikipedia.org/wiki/Windows_Presentation_Foundation), and [Cocoa](https://en.wikipedia.org/wiki/Cocoa_(API)) (on OS X).  Though Eto is powerful, it has a shallow learning curve and we're confident you will be hooked as quickly as we were.

---

## Related Topics
{: .toc-header }

- [Mono Project homepage](http://www.mono-project.com/)
- [Mono (software) - Wikipedia](http://en.wikipedia.org/wiki/Mono_(software))
- [Xamarin homepage](http://xamarin.com)
- [Xamarin - Wikipedia](https://en.wikipedia.org/wiki/Xamarin)
- [Installing Tools (Mac)]({{ site.baseurl }}/guides/rhinocommon/installing_tools_mac/)
- Cross Platform User Interface
