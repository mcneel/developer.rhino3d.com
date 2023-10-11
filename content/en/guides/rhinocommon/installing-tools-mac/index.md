+++
aliases = ["/5/guides/rhinocommon/installing-tools-mac/", "/6/guides/rhinocommon/installing-tools-mac/", "/7/guides/rhinocommon/installing-tools-mac/", "/wip/guides/rhinocommon/installing-tools-mac/"]
authors = [ "dan" ]
categories = [ "Getting Started" ]
description = "This guide covers all the necessary tools required to author Rhino plugins on Mac."
keywords = [ "first", "RhinoCommon", "Plugin" ]
languages = [ "C#" ]
sdk = [ "RhinoCommon" ]
title = "Installing Tools (Mac)"
type = "guides"
weight = 2

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


By the end of this guide, you should have all the tools installed necessary for authoring, building, and debugging C# .NET plugins using RhinoCommon in Rhino for Mac.

## Prerequisites

This guide presumes you have an:

- [Apple Mac](http://store.apple.com/) running [macOS](https://www.apple.com/osx/) Monterey (12) or later.
- [Rhino for Mac](https://www.rhino3d.com/download/)

## Install Visual Studio for Mac

Visual Studio for Mac can be used to build RhinoCommon plugins on macOS.

{{< call-out note "Visual Studio 2019 and 2022" >}}
This guide is authored using Visual Studio 2022. These steps - or very similar ones - should work in Visual Studio 2019 as well.
{{< /call-out >}}

#### Step-by-Step

1. *[Download Visual Studio for Mac](https://www.visualstudio.com/vs/visual-studio-mac/)*.
1. Visual Studio for Mac uses an Installer app, which downloads and installs the components that you select. Once you have downloaded the *VisualStudioForMacInstaller.dmg*, double-click it to mount the disk image. Double-click the big *Install Visual Studio for Mac.app* icon to launch the installer.
1. You must accept the Visual Studio Software License Agreement.
1. Visual Studio for Mac can install the following items:
   - Visual Studio for Mac (required)
   - .NET Core (required for targeting Rhino 8 and later)
   - .NET Multi-Platform App UI or MAUI (not necessary)
   - .NET WebAssembly Build Tools (not necessary)
   - tvOS (not necessary)
   - macOS Cocoa (optional)
1. Verify that *Visual Studio for Mac* and *NET Core* are checked and click *Install*.
1. If you do not have Xcode installed, the installer may prompt you to install it. You can ignore this warning.
1. The installer downloads and installs *Visual Studio for Mac* and any additional components you checked.
1. When the installer is finished, click the *Launch Visual Studio* button.
1. Visual Studio is installed in your */Applications* folder. You will want to *drag its icon to your Dock* for future use or - if it's running - right/option-click the icon in the Dock and select *Keep in Dock*.

## Install the Rhino Visual Studio Extension

The Rhino AddIn/Extension is required to debug your plugin code in an active session of Rhino for Mac using Visual Studio for Mac. Additionally, it contains project templates to get you started creating plugins quickly.

#### Step-by-Step

1. Visit the [Extension's GitHub releases page](https://github.com/mcneel/RhinoVisualStudioExtensions/releases) and find the *Latest release* in the [list of releases](https://github.com/mcneel/RhinoVisualStudioExtensions/releases).
1. Download the *.mpack* file in the list of Downloads on that release. For example, at the time of this writing, the *Latest release* download is entitled *Rhino.VisualStudio.Mac.2022-8.0.0.mpack*. (If you are using Visual Studio for Mac 2019, you will want to get *Rhino.VisualStudio.Mac.2019-7.21.0.mpack*).
1. Launch *Visual Studio for Mac* if it not already open.
1. Navigate to *Visual Studio* > *Extensions...*...
1. Click the *Install from file...* button in the lower right-hand corner.
1. Navigate to the *.mpack* file you downloaded in step 2 above.
1. Click *Install*. The plugin should install.
1. *IMPORTANT*: You must *Quit* and *Restart* Visual Studio for Mac.
1. Navigate to *Visaul Studio* > *Extensions...* > *Installed* tab. Verify that *RhinoCommon Plugin Support* exists. If it's there, you have successfully installed the Extension and you are *DONE*.

## Next Steps

*Congratulations!*  You have all the tools necessary to build a RhinoCommon plugin for Rhino for Mac.  *Now what?*

Check out the [Your First Plugin (Mac)](/guides/rhinocommon/your-first-plugin-mac) guide for instructions building - your guessed it - your first plugin.
