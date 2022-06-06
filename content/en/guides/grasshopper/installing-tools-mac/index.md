+++
aliases = ["/5/guides/grasshopper/installing-tools-mac/", "/6/guides/grasshopper/installing-tools-mac/", "/7/guides/grasshopper/installing-tools-mac/", "/wip/guides/grasshopper/installing-tools-mac/"]
authors = [ "dan" ]
categories = [ "Getting Started" ]
description = "This guide covers all the necessary tools required to author Grasshopper components on Mac."
keywords = [ "first", "grasshopper", "components" ]
languages = [ "C#" ]
sdk = [ "Grasshopper" ]
title = "Installing Tools (Mac)"
type = "guides"
weight = 2
override_last_modified = "2021-09-03T08:29:10Z"

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Mac" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++


By the end of this guide, you should have all the tools installed necessary for authoring, building, and debugging Grasshopper components using RhinoCommon in Rhino for Mac.

## Prerequisites

This guide presumes you have an:

- [Apple Mac](http://store.apple.com/) running [macOS Sierra](https://www.apple.com/osx/) (10.12.5) or later.
- [Rhino 5 for Mac](https://www.rhino3d.com/mac) (5.1) or later.

## Install Visual Studio for Mac

Visual Studio for Mac (formerly Xamarin Studio, formerly MonoDevelop) is required to build Grasshopper components on macOS.  The core pieces of the Mono platform that are required are the Mono Framework and Visual Studio for Mac.  Please check out the [What are Mono and Xamarin?](/guides/rhinocommon/what-are-mono-and-xamarin/) guide for more information.

#### Step-by-Step

1. *[Download Visual Studio for Mac](https://www.visualstudio.com/vs/visual-studio-mac/)*.
1. Visual Studio for Mac uses an Installer app, which downloads and installs the components that you select.  Once you have downloaded the *VisualStudioInstaller.dmg*, double-click it to mount the disk image.  Double-click the big *Install Visual Studio.app* icon to launch the installer.
1. You must accept the Visual Studio Software License Agreement.
1. Visual Studio for Mac can install the following items:
   - Visual Studio + Profiler (required)
   - Android + Xamarin.Forms[^1] (optional)
   - iOS + Xamarin.Forms[^2] (optional)
   - macOS - formerly Xamarin.Mac[^3] (optional)
   - Workbooks and Inspector (optional)
1. Verify that *Visual Studio + Profiler* is checked and click *Continue*.
1. The installer downloads and installs: *Mono Framework* and *Visual Studio for Mac*
1. When the installer is finished, click the *Launch Visual Studio* button.
1. *Visual Studio* - along with the Mono Framework and Profiler are now installed.
1. Visual Studio is installed in your */Applications* folder. You will want to *drag its icon to your Dock* for future use or - if it's running - right/option-click the icon in the Dock and select *Keep in Dock*.

## Install the RhinoCommon Extension

The RhinoCommon AddIn/Extension is required to debug your RhinoCommon plugins and Grasshopper components in an active session of Rhino for Mac.  Additionally, it contains project templates to get you started creating components and plugins quickly.

#### Step-by-Step

1. Visit the [AddIn's GitHub releases page](https://github.com/mcneel/RhinoCommonXamarinStudioAddin/releases) and find the *Latest release* in the [list of releases](https://github.com/mcneel/RhinoCommonXamarinStudioAddin/releases).
1. Download the *.mpack* file in the list of Downloads on that release.  For example, at the time of this writing, the *Latest release* download is entitled *RhinoXamarinStudioAddIn_7.4.3.1.mpack*.
1. Launch *Visual Studio for Mac* if it not already open.
1. Navigate to *Visual Studio* > *Extensions...*...
1. Click the *Install from file...* button in the lower left-hand corner.
1. Navigate to the *.mpack* file you downloaded in step 2 above.
1. Click *Install*.  The plugin should install.
1. *IMPORTANT*: You must *Quit* and *Restart* Visual Studio for Mac.
1. Navigate to *Extensions Studio* > *Add-ins..* > *Installed* tab.  Verify that *RhinoCommon Plugin Support* exists under the *Debugging* category.  If it's there, you have successfully installed the Extension and you are *DONE*.

## Next Steps

*Congratulations!*  You have all the tools necessary to build a Grasshopper component on macOS.  *Now what?*

Check out the [Your First Component (Mac)](/guides/grasshopper/your-first-component-mac) guide for instructions building - your guessed it - your first component.

**Footnotes**

[^1]: Xamarin.Android is used to build C# .NET applications for Android devices.  This is useful to have installed if you wish to use the RhinoMobile toolkit, but not required for RhinoCommon in Rhino for Mac.

[^2]: Xamarin.iOS is used to build C# .NET applications for Apple iOS devices.  This is useful to have installed if you wish to use the RhinoMobile toolkit, but not required for RhinoCommon in Rhino for Mac.

[^3]: Xamarin.Mac is Xamarin's proprietary closed-source toolkit build on the open-source MonoMac (aka Mono for macOS).  Xamarin.Mac provides a commercial license of Mono, bindings to additional frameworks, and the ability to create self-contained application bundles that do not require mono.  Rhino for Mac does not currently use Xamarin.Mac.
