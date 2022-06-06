+++
aliases = ["/5/guides/rhinocommon/what-are-mono-and-xamarin/", "/6/guides/rhinocommon/what-are-mono-and-xamarin/", "/7/guides/rhinocommon/what-are-mono-and-xamarin/", "/wip/guides/rhinocommon/what-are-mono-and-xamarin/"]
authors = [ "dan" ]
categories = [ "Overview" ]
description = "This guide is an overview of Mono and Xamarin and how they relate to RhinoCommon plugins."
keywords = [ "Mono", "Xamarin", ".NET", "Microsoft" ]
languages = [ "C#" ]
sdk = [ "RhinoCommon" ]
title = "What are Mono & Xamarin?"
type = "guides"
weight = 2
override_last_modified = "2021-09-03T08:29:10Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommon"
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


## Mono

The [Mono framework](http://www.mono-project.com/) is an [open source implementation](https://github.com/mono/mono) of [Microsoft's .NET Framework](http://www.microsoft.com/net) based on the [open standards](http://www.mono-project.com/docs/about-mono/languages/ecma/) for the C# language and the [Common Language Runtime](http://www.mono-project.com/docs/advanced/runtime/).

The Mono project has been in active development for [over a decade](https://en.wikipedia.org/wiki/Mono_(software)#History) and is used - behind the scenes - in many products.

### Mono & Rhino for Mac

Mono allows C# developers to write cross platform code targeting Windows, macOS, Linux, Android, and iOS.  What this means for Rhino plugin developers is that they can - if written properly - run the same RhinoCommon plugin in *both* Rhino for Windows *and* Rhino for Mac...

<div align="center">
  <img src="/images/rhino-mono-one-binary-two-platforms.png">
</div>


RhinoCommon on Mac is executed through an embedded, custom, Mono framework.  That means Rhino for Mac is not using the public Mono, nor premium Xamarin.Mac.  However, the differences between public MonoMac and Rhino for Mac's MonoMac are inconsequential.

## Xamarin

Xamarin - a subsidiary of Microsoft - is a company founded by the engineers who created Mono.  Xamarin is the primary maintainer and commercial sponsor of Mono.  Xamarin provides professional developer tools that make cross platform code easier to author, test, and maintain.  *NOTE*: As Xamarin's platform is being integrated into Microsoft more deeply, some of these titles may change.

### The Xamarin platform

The [Xamarin Platform](http://xamarin.com/platform) is comprised of the following pieces:

- *[Visual Studio for Mac](https://www.visualstudio.com/vs/visual-studio-mac/)*: C# Integrated Developer Environment (IDE) for Mac.  (Visual Studio for Mac was formerly known as Xamarin Studio, which was formerly known as MonoDevelop).
- *Xamarin.Android*: Used to build C# .NET applications for Android devices.  This is useful to have installed if you wish to use the [RhinoMobile](/guides/#rhinomobile) toolkit, but not required for RhinoCommon in Rhino for Mac.
- *Xamarin.iOS*: Used to build C# .NET applications for Apple iOS devices.  This is useful to have installed if you wish to use the [RhinoMobile](/guides/#rhinomobile) toolkit, but not required for RhinoCommon in Rhino for Mac.
- *Xamarin.Mac*: Xamarin's closed-source version of MonoMac.

For developing RhinoCommon plugins, *only* Visual Studio for Mac is required.  

### Visual Studio for Mac

(Formerly known as Xamarin Studio, formerly known as MonoDevelop).  This is Microsoft's C# developer environment that runs on Mac.  Visual Studio for Mac has many of the features of Microsoft's Visual Studio for Windows and uses *exactly the same formats* as Visual Studio for Windows: solutions (*.sln*) and C# projects (*.csproj*).  At McNeel, we use Visual Studio for Mac to develop [Rhino for Mac](http://www.rhino3d.com/mac) and [iRhino 3D](https://www.rhino3d.com/ios).  We highly recommend you use Visual Studio for Mac when developing RhinoCommon plugins for the Mac.

### Xamarin.Mac?

Rhino for Mac does not currently use Xamarin.Mac.

Xamarin.Mac is Microsoft's proprietary closed-source toolkit used to provide .NET access to native features of the Mac Operating System and to allow for compiling .NET projects into self-contained application bundles.  Rhino uses the open source MonoMac framework instead of Xamarin.Mac for accessing native macOS features (primarily native user interface features).

### Visual Studio for Windows support?

Xamarin offers a [Visual Studio for Windows extension](http://xamarin.com/visual-studio), however this extension is only useful for Xamarin.iOS and Xamarin.Android development, *not* for RhinoCommon.  If you are writing RhinoCommon plugins you are free to use Visual Studio for Windows - when targeting either Rhino for Mac or Rhino for Windows - just as you normally would.  When you want to debug and test your plugin in Rhino for Mac, you will have to use Visual Studio for Mac, but you can use the *exactly same solution* and *project files* to do this.

## Solution & Project

Visual Studio for Mac uses the same formats as Visual Studio for Windows:

- *.sln*
- *.csproj*

It is important to stress: these *are* Visual Studio solutions and projects.  You can open solutions and projects created in Visual Studio for Mac in Visual Studio for Windows and vice-versa.

## Porting .NET code

All of .NET is not yet implemented in Mono (although an awful lot is).  We recommend launching your plugin project in Visual Studio for Mac and attempting to compile. That is the best way to find any potential problems with getting your plugin to run on Rhino for Mac.  Please let McNeel know if you find something is missing from the SDK that you need, we may be able to provide this functionality in a Rhino for Mac service release.

### P/Invoke

One of the areas that developers need to be aware of is any .NET code that uses P/invoke may experience problems when running on Mac. P/invoke is a technique to call unmanaged native functions from .NET code.  The feature is available on macOS/mono, but developers need to make sure that the P/invoke calls are calling native code written for macOS and not for Windows.  Many commercial .NET components use P/invoke so this is something we highly recommend you investigate.

### UI and Eto

User interface is where developers typically run into trouble with platform specific dependencies and features.  We use and support development of [Eto](https://github.com/picoe/Eto).  Using Eto can make your plugin look and work as a native application on all platforms, using a single UI codebase.  Eto ships with Rhino for Mac (and will ship with Rhino 6 for Windows).  Eto has an easy to use API and uses native toolkits, abstracting the platform-specific implementations for [WinForms](https://en.wikipedia.org/wiki/Windows_Forms) (GDI and Direct2D), [WPF](https://en.wikipedia.org/wiki/Windows_Presentation_Foundation), and [Cocoa](https://en.wikipedia.org/wiki/Cocoa_(API)) (on macOS).  Though Eto is powerful, it has a shallow learning curve and we're confident you will be hooked as quickly as we were.

## Related Topics

- [Mono Project homepage](http://www.mono-project.com/)
- [Mono (software) - Wikipedia](http://en.wikipedia.org/wiki/Mono_(software))
- [Xamarin homepage](http://xamarin.com)
- [Xamarin - Wikipedia](https://en.wikipedia.org/wiki/Xamarin)
- [Installing Tools (Mac)](/guides/rhinocommon/installing-tools-mac/)
- Cross Platform User Interface
