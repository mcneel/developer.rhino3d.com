---
title: Installing Tools (Mac)
description: This guide covers all the necessary tools required to author Rhino plugins on Mac.
authors: ['dan_belcher']
sdk: ['RhinoCommon']
languages: ['C#']
platforms: ['Mac']
categories: ['Getting Started']
origin: unset
order: 2
keywords: ['first', 'RhinoCommon', 'Plugin']
layout: toc-guide-page
---


By the end of this guide, you should have all the tools installed necessary for authoring, building, and debugging C# .NET plugins using RhinoCommon in Rhino for Mac.

## Prerequisites

This guide presumes you have an:

- [Apple Mac](http://store.apple.com/) running [macOS Sierra](https://www.apple.com/osx/) (10.12.5) or later.
- [Rhino 5 for Mac](https://www.rhino3d.com/mac) (5.1) or later.

---

## Install Xcode

[Xcode](https://developer.apple.com/xcode/) is Apple's development platform and IDE.  Though it is not *absolutely* required that you install Xcode in order to build, debug, and run C# plugins using RhinoCommon, it is *recommended* that you do.  In short: the Visual Studio for Mac works best with Xcode installed.  

#### Step-by-Step

1. *[Xcode](https://itunes.apple.com/us/app/xcode/id497799835?mt=12)* is free in the [Mac App Store](https://itunes.apple.com/us/app/xcode/id497799835?mt=12).  Click the *View in Mac App Store* button.
1. Click the *Get* > *Install App* button underneath the Xcode icon.
1. You will be prompted for your [Apple ID](https://appleid.apple.com/) (required to download apps on the App Store).
1. Xcode is large download - nearly 2.6 GB in size.  You can monitor the progress of the download in Launchpad.  When Xcode is finished downloading an installing, it will be your */Applications* folder.
1. *Launch* Xcode.  On initial launch, Xcode will install some additional components.
1. *Quit* Xcode.

---

## Install Visual Studio for Mac

Visual Studio for Mac (formerly Xamarin Studio, formerly MonoDevelop) is required to build RhinoCommon plugins on macOS.  The core components of the Mono platform that are required are the Mono Framework and Visual Studio for Mac.  Please check out the [What are Mono and Xamarin?]({{ site.baseurl }}/guides/rhinocommon/what-are-mono-and-xamarin/) guide for more information.

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
1. If you do not have Xcode installed, the installer may prompt you.  See [Install Xcode](#install-xcode) above.
1. The installer downloads and installs: *Mono Framework* and *Visual Studio for Mac*
1. When the installer is finished, click the *Launch Visual Studio* button.
1. *Visual Studio* - along with the Mono Framework and Profiler are now installed.
1. Visual Studio is installed in your */Applications* folder. You will want to *drag its icon to your Dock* for future use or - if it's running - right/option-click the icon in the Dock and select *Keep in Dock*.

---

## Install the RhinoCommon Extension

The RhinoCommon AddIn/Extension is required to debug your plugin code in an active session of Rhino for Mac.  Additionally, it contains project templates to get you started creating plugins quickly.

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

---

## Next Steps

*Congratulations!*  You have all the tools necessary to build a RhinoCommon plugin for Rhino for Mac.  *Now what?*

Check out the [Your First Plugin (Mac)]({{ site.baseurl }}/guides/rhinocommon/your-first-plugin-mac) guide for instructions building - your guessed it - your first plugin.

---

## Footnotes

[^1]: Xamarin.Android is used to build C# .NET applications for Android devices.  This is useful to have installed if you wish to use the RhinoMobile toolkit, but not required for RhinoCommon in Rhino for Mac.

[^2]: Xamarin.iOS is used to build C# .NET applications for Apple iOS devices.  This is useful to have installed if you wish to use the RhinoMobile toolkit, but not required for RhinoCommon in Rhino for Mac.

[^3]: Xamarin.Mac is Xamarin's proprietary closed-source toolkit build on the open-source MonoMac (aka Mono for macOS).  Xamarin.Mac provides a commercial license of Mono, bindings to additional frameworks, and the ability to create self-contained application bundles that do not require mono.  Rhino for Mac does not currently use Xamarin.Mac.
