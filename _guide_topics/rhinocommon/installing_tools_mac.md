---
layout: toc-page
title: Installing Tools (Mac)
author: dan@mcneel.com
categories: ['GettingStarted']
platforms: ['Mac']
apis: ['RhinoCommon']
languages: ['C#']
keywords: ['first', 'RhinoCommon', 'Plugin']
TODO: 1
origin: unset
order: 2
---

# Installing Tools (Mac)

By the end of this guide, you should have all the tools installed necessary for authoring, building, and debugging C# .NET plugins using RhinoCommon in Rhino for Mac.


## Prerequisites
{: .toc-header }

This guide presumes you have an:

- [Apple Mac](http://store.apple.com/) running [OS X Yosemite](https://www.apple.com/osx/) (10.10) or later.
- [Rhino 5 for Mac](https://www.rhino3d.com/mac) (5.1) or later.

---

## Install Xcode
{: .toc-header }

[Xcode](https://developer.apple.com/xcode/) is Apple's development platform and IDE.  Though it is not *absolutely* required that you install Xcode in order to build, debug, and run C# plugins using RhinoCommon, it is *recommended* that you do.  In short: the Xamarin on OS X works best with Xcode installed.  

#### Step-by-Step

1. **[Xcode](https://itunes.apple.com/us/app/xcode/id497799835?mt=12)** is free in the [Mac App Store](https://itunes.apple.com/us/app/xcode/id497799835?mt=12).  Click the **View in Mac App Store** button.
1. Click the **Get** > **Install App** button underneath the Xcode icon.
1. You will be prompted for your [Apple ID](https://appleid.apple.com/) (required to download apps on the App Store).
1. Xcode is large download - nearly 2.6 GB in size.  You can monitor the progress of the download in Launchpad.  When Xcode is finished downloading an installing, it will be your `/Applications` folder.
1. **Launch** Xcode.  On initial launch, Xcode will install some additional components.
1. **Quit** Xcode.

---

## Install Xamarin
{: .toc-header }

Xamarin's platform is currently required to build RhinoCommon plugins on OS X.  The core components of the Xamarin platform that are required are the Mono Framework and Xamarin Studio.  Please check out the [What are Mono and Xamarin?]({{ site.baseurl }}/guides/what_are_mono_and_xamarin/) guide for more information.

#### Step-by-Step

1. **[Download the Xamarin Platform](http://xamarin.com/download)**.
1. Xamarin uses an Installer app, which downloads and installs the components that you select.  Once you have downloaded the **XamarinInstaller.dmg**, double-click it to mount the disk image.  Click the big **Install Xamarin** button to launch the installer.
1. You must accept the Xamarin Software License Agreement to use the Xamarin platform.
1. The **Xamarin Platform** is comprised of three products:
   - Xamarin.Android[^1]
   - Xamarin.iOS[^2]
   - Xamarin.Mac[^3]
...verify that **Xamarin.Mac** is checked and click **Continue**.
1. If you do not have Xcode installed, Xamarin will prompt you.  See [Install Xcode](#install-xcode) above.
1. Xamarin installs: **Mono Framework**, **Xamarin Studio**, & **Xamarin.Mac**.  Click **Continue**.
1. Xamarin is will now download and install.  Depending on which products you selected in step 4 above, this can take a while.
1. When the installer is finished, click the **Launch Xamarin Studio** button.
1. **Xamarin Studio** - along with the Mono Framework and Xamarin.Mac - are now installed.
1. Xamarin Studio is installed in your `/Applications` folder. You will want to **drag its icon to your Dock** for future use or - if it's running - right/option-click the icon in the Dock and select **Keep in Dock**.

---

## Install the Rhino Add-in
{: .toc-header }

The [Rhino Xamarin Studio Add-in](https://github.com/mcneel/RhinoMonodevelopAddin/releases) (TODO: Update links to new version) is required to debug your plugin code in an active session of Rhino for Mac.  Additionally, it contains project wizards (TODO) and templates to get you started creating plugins quickly.

#### Step-by-Step

1. Download the latest release of the [Rhino Xamarin Studio Add-in](https://github.com/mcneel/RhinoMonodevelopAddin/releases) (TODO: Update links to new version).
1. Extract the downloaded zip file to get an **.mpack**.
1. Launch **Xamarin Studio**.
1. Navigate to **Xamarin Studio** > **Add-in manager...**.
2. Expand **Debugging**.
3. Uninstall all previous versions of the Mono Soft Debugger for Rhinoceros (BUT NOT the Mono Soft Debugger) - TODO: Update this.
1. Click **Install from file...** button in the lower-right corner.
1. Navigate to the mpack file you extracted, then click **Open**.
1. Click **Install**.
1. Click **Close**.
1. Verify that **Mono Soft Debugger Support for Rhinoceros** exists under the **Debugging** section of the **Installed** tab of the **Add-in Manager**.

**TODO**: Update the above steps when the Rhino Xamarin Studio Add-in has been updated.

---

[^1]: Xamarin.Android is used to build C# .NET applications for Android devices.  This is useful to have installed if you wish to use the RhinoMobile toolkit, but not required for RhinoCommon in Rhino for Mac.

[^2]: Xamarin.iOS is used to build C# .NET applications for Apple iOS devices.  This is useful to have installed if you wish to use the RhinoMobile toolkit, but not required for RhinoCommon in Rhino for Mac.

[^3]: Xamarin.Mac is Xamarin's proprietary closed-source toolkit build on the open-source MonoMac (aka Mono for Mac OS X).  Xamarin.Mac provides a commercial license of Mono, bindings to additional frameworks, and the ability to create self-contained application bundles that do not require mono.  Rhino for Mac does not currently use Xamarin.Mac, but rather MonoMac.
