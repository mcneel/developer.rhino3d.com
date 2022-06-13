+++
aliases = ["/5/guides/rhinomobile/installing-tools-mac/", "/6/guides/rhinomobile/installing-tools-mac/", "/7/guides/rhinomobile/installing-tools-mac/", "/wip/guides/rhinomobile/installing-tools-mac/"]
authors = [ "dan" ]
categories = [ "Getting Started" ]
description = "This guide covers all the necessary tools required for RhinoMobile on Mac."
keywords = [ "RhinoMobile", "iRhino 3D" ]
languages = [ "C#" ]
sdk = [ "RhinoMobile" ]
title = "Installing Tools (Mac)"
type = "guides"
weight = 2

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinomobile/getting-started"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Mac" ]
since = 5
until = 7

[page_options]
byline = true
toc = true
toc_type = "single"
block_webcrawlers = true

[_build]
list = "never"
+++

{{< call-out "warning" "RhinoMobile: Deprecated" >}}
RhinoMobile is no longer supported. Rhino 3dm file I/O is still available on iOS and Android via the [rhino3dm library](https://github.com/mcneel/rhino3dm).
{{< /call-out >}}
 
By the end of this guide, you should have all the tools installed necessary for authoring, building, and debugging C# mobile applications using RhinoMobile in Xamarin Studio.

## Prerequisites

If you have not done so already, please read the [What is RhinoMobile?](/guides/rhinomobile/what-is-rhinomobile/) guide.

This guide presumes you have an:

- [Apple Mac](http://store.apple.com/) running [OS X Yosemite](https://www.apple.com/osx/) (10.10) or later.

## Install Xcode

[Xcode](https://developer.apple.com/xcode/) is Apple's development platform and IDE.

#### Step-by-Step

1. *[Xcode](https://itunes.apple.com/us/app/xcode/id497799835?mt=12)* is free in the [Mac App Store](https://itunes.apple.com/us/app/xcode/id497799835?mt=12).  Click the *View in Mac App Store* button.
1. Click the *Get* > *Install App* button underneath the Xcode icon.
1. You will be prompted for your [Apple ID](https://appleid.apple.com/) (required to download apps on the App Store).
1. Xcode is large download - nearly 2.6 GB in size.  You can monitor the progress of the download in Launchpad.  When Xcode is finished downloading an installing, it will be your */Applications* folder.
1. *Launch* Xcode.  On initial launch, Xcode will install some additional components.
1. *Quit* Xcode.

## Install Xamarin

Xamarin's platform is currently required to build RhinoMobile apps.  Please check out the [What are Mono and Xamarin?](/guides/rhinocommon/what-are-mono-and-xamarin/) guide for more information.

#### Step-by-Step

1. *[Download the Xamarin Platform](http://xamarin.com/download)*.
1. Xamarin uses an Installer app, which downloads and installs the components that you select.  Once you have downloaded the *XamarinInstaller.dmg*, double-click it to mount the disk image.  Double-click the big *Install Xamarin* icon to launch the installer.
1. You must accept the Xamarin Software License Agreement to use the Xamarin platform.
1. The *Xamarin Platform* is comprised of these pieces:
   - Xamarin Studio
   - Xamarin.Android[^1]
   - Xamarin.iOS[^2]
   - Xamarin.Mac[^3]
...verify that *Xamarin.Android* and *Xamarin.iOS* are checked and click *Continue*.
1. If you do not have Xcode installed, Xamarin will prompt you.  See [Install Xcode](#install-xcode) above.
1. Xamarin installs: *Mono Framework*, *Xamarin Studio*, *Xamarin.Android*, and *Xamarin.iOS*.  Click *Continue*.
1. Xamarin is will now download and install.  Depending on which products you selected in step 4 above, this can take a while.
1. When the installer is finished, click the *Launch Xamarin Studio* button.
1. *Xamarin Studio* - along with the Mono Framework, Xamarin.Android, and Xamarin.iOS - are now installed.
1. Xamarin Studio is installed in your */Applications* folder. You will want to *drag its icon to your Dock* for future use or - if it's running - right/option-click the icon in the Dock and select *Keep in Dock*.

## Update the Android SDK

Once Xamarin Studio itself has been updated, you need to fetch the updates for the Android SDK.

#### Step-by-Step

1. In *Xamarin Studio*, navigate to *Tools* > *Open Android SDK Manager...*.
1. In the *Android SDK Manager* window, wait until manager has finished fetching the update manifest.
1. Depending on when you downloaded the Xamarin tools, you will want to install the most recent API (21 at the time of writing) as well as the last couple (20 and 19) for backward compatibility. Select the small check boxes next the names and then click *Install N packages...* button.
1. This brings up a (very buggy) window in which you must accept all the licenses of each item before continuing. If you can't get the *Install* button to work, exit out of the window, open it again, and individually click the Accept radio button on the left until it works.
![android sdk](/images/rhinomobile-installing-tools-mac-01.png)
1. *Note:* Downloads can take awhile depending on your internet connection.

## Install the Intel HAXM

The [Intel HAXM is the Intel Hardware Acceleration Execution Manager](http://software.intel.com/en-us/articles/intel-hardware-accelerated-execution-manager/).  HAXM provides a hardware-accelerated engine for the x86 Android emulators. Without HAXM, the emulators are nearly unusable, as their performance lags so much. However, with HAXM, the x86 emulators are responsive and usable. Not as fast as an actual device, but at least passable. It’s available to install via the Android SDK manager, but the version there is ineffective. Instead, get it from the link above.  HAXM will not work in a virtualized environment, e.g. a VM, so if you’re doing your Android development in a Windows VM, you will need to use a device.

#### Step-by-Step

1. Visit the [Intel Hardware Acceleration Execution website](http://software.intel.com/en-us/articles/intel-hardware-accelerated-execution-manager/).
1. Find the *macOS* section of the page.
1. Download the *haxm-macosx_rxx.zip*.  You may be asked to accept an license agreement before downloading can begin.
1. Unzip *haxm-macosx_rxx.zip*.
1. Mount the *IntelHAXM_x.x.x.dmg* by double-clicking it.
1. Install the HAXM by double-clicking the *IntelHAXM_x.x.x.mpkg* file.

## Clone RhinoCommon

RhinoMobile is built around [RhinoCommon's rhino3dmio branch](https://github.com/mcneel/rhinocommon/tree/rhino3dmio). You can either download RhinoCommon as a zip or clone the repository using git (recommended). (If you are new to GitHub, there is a [GitHub Mac Desktop](https://desktop.github.com/) app to get you started).

#### Step-by-Step

1. Unzip or clone *[rhinocommon (rhino3dmio branch)](https://github.com/mcneel/rhinocommon/tree/rhino3dmio)* in a convenient folder, such as the */Users/you/Development/Repositories/rhinocommon* folder:
![clone rhinocommon](/images/rhinomobile-installing-tools-mac-02.png)
1. *[Download openNURBS](http://www.rhino3d.com/download/opennurbs/5.0/commercial)*. RhinoMobile requires the C++ openNURBS SDK.
1. Unzip openNURBS and place the contents in the *rhinocommon/c/opennurbs/* folder (the folder containing only the *readme.md* file):
![opennurbs](/images/rhinomobile-installing-tools-mac-03.png)

## Clone RhinoMobile

You will need to download or clone [RhinoMobile](http://github.com/mcneel/RhinoMobile) and the [RhinoMobileSamples](http://github.com/mcneel/RhinoMobileSamples) repositories. (If you are new to GitHub, there is a [GitHub Mac Desktop](https://desktop.github.com/) app to get you started).

#### Step-by-Step

1. Unzip or clone *[RhinoMobile](http://github.com/mcneel/RhinoMobile)* into a folder *parallel to rhinocommon* (cloned above). For example, if *rhinocommon* is in the     */Users/you/Development/Repositories/rhinocommon* folder, then RhinoMobile should be in the */Users/you/Development/Repositories/RhinoMobile* folder:
![rhinomobile](/images/rhinomobile-installing-tools-mac-04.png)
1. Unzip or clone *[RhinoMobileSamples](http://github.com/mcneel/RhinoMobileSamples)* into a folder *parallel to rhinocommon* and *RhinoMobile*:
![rhinomobilesamples](/images/rhinomobile-installing-tools-mac-05.png)

## Next Steps

*Congratulations!*  You have all the tools necessary to build a mobile app that uses RhinoMobile.  *Now what?*

Check out the [Your First App (Mac)](/guides/rhinomobile/your-first-app-mac) guide for instructions building - your guessed it - your first app.

## Related Topics

- [What is RhinoMobile?](/guides/rhinomobile/what-is-rhinomobile/)
- [What is RhinoCommon?](/guides/rhinocommon/what-is-rhinocommon/)
- [What are Mono and Xamarin?](/guides/rhinocommon/what-are-mono-and-xamarin/)
- [Installing Tools (Windows)](/guides/rhinomobile/installing-tools-windows/)
- [Your First App (Mac)](/guides/rhinomobile/your-first-app-mac)

**Footnotes**

[^1]: Xamarin.Android is used to build C# .NET applications for Android devices.

[^2]: Xamarin.iOS is used to build C# .NET applications for Apple iOS devices.

[^3]: Xamarin.Mac is Xamarin's proprietary closed-source toolkit build on the open-source MonoMac (aka Mono for macOS).  Xamarin.Mac provides a commercial license of Mono, bindings to additional frameworks, and the ability to create self-contained application bundles that do not require mono.  RhinoMobile does not currently use Xamarin.Mac.
