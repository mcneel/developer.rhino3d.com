+++
aliases = ["/en/5/guides/rhinomobile/testing-on-devices/", "/en/6/guides/rhinomobile/testing-on-devices/", "/en/7/guides/rhinomobile/testing-on-devices/", "/wip/guides/rhinomobile/testing-on-devices/"]
authors = [ "dan" ]
categories = [ "Fundamentals" ]
description = "This guide walks you through setting up devices for testing mobile applications."
keywords = [ "RhinoMobile", "iRhino 3D" ]
languages = [ "C#" ]
sdk = [ "RhinoMobile" ]
title = "Testing On Devices"
type = "guides"
weight = 7

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinomobile/devices_and_testing"
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
 
## Android Devices

In order to debug your code on an Android device, you must enable USB debugging on the device. This mode makes your device somewhat more vulnerable to damage - from you and from others - so it should be used with caution. You can enable and disable it between development sessions if you like.

#### Android 4.0 (JellyBean - API 14) or higher devices

Enable the *USB Debugging* option under *Settings* > *Developer options*.

For Android 4.2 and newer, *Developer options is hidden* by default; use the following steps:

1. On the device, go to *Settings* > *About* <device>.
1. Tap the *Build number* seven times to make *Settings* > *Developer* options available.
1. Then enable the *USB Debugging* option.

On Windows, it is sometimes necessary to switch your device to Camera (PTP) mode, rather than Media device (MTP) mode. To change this mode, use the following steps:

1. On the device, go to *Settings* > *Storage* > *More options (…)* > *USB computer connection*
1. Switch from *Media device (MTP)* to *Camera (PTP)*.

#### Kindle Fire Devices

On the device, select *Settings* > *Security* and set Enable ADB to On.

For more information, see the [Amazon developer documentation](https://developer.amazon.com/sdk/fire/connect-adb.html#Connecting).

You might also want to enable the Stay awake option, to prevent your Android device from sleeping while plugged into the USB port.

## iOS Devices

iOS devices must be registered with Apple before you can use them for development or testing. This process is known as Device Provisioning. Follow these directions from Xamarin to get your iOS device ready to go.

Once you have your device provisioned and connected via USB, you can run and debug your app from Xamarin Studio or Visual Studio (via the Mac Build host).

Devices are the best place to test your app. The four areas where devices differ most from the simulator are:

1. Networking and connectivity
1. Location services
1. *Memory*
1. *OpenGL ES*

The last two are the most critical to RhinoMobile apps. Large meshes in .3dm files can consume lots of memory; the simulator will try to invoke OutOfMemory warnings, but there will not be as consistent (or realistic) as running and debugging on the device. Finally, OpenGL ES calls will be interpreted differently on the simulator than on the device…it is possible that code working on the simulator will not work on all devices.

## Related Topics

- [Using Simulators](/guides/rhinomobile/using-simulators/)
