---
title: Your First App (Windows)
description: This guide walks you through your first mobile app using RhinoMobile and Visual Studio on Windows.
authors: ['Dan Belcher']
author_contacts: ['dan']
apis: ['RhinoMobile']
languages: ['C#']
platforms: ['iOS', 'Android']
categories: ['Getting Started']
origin: http://wiki.mcneel.com/developer/rhinomobile/hellorhinomobile
order: 5
keywords: ['RhinoMobile', 'iRhino 3D']
layout: toc-guide-page
---

# {{ page.title }}

{% include byline.html %}

{{ page.description }}

This guide presumes you have gone through the [Installing Tools (Windows)]({{ site.baseurl }}/guides/rhinomobile/installing-tools-windows) guide and have successfully installed Xamarin  and all the requisite libraries.  These instructions presume you are using Visual Studio 2015 Professional.

## HelloRhinoMobile

These guide presumes you are using Visual Studio 2015 Professional, though this process should work with Visual Studio 2013 as well.

### Android Boilerplate Build

1. *Launch Visual Studio* and open the *HelloRhinoMobile* solution.
1. *Right-click* the *HelloRhino.Droid* project and select *Set As StartUp Project* from the drop-down menu. This makes *HelloRhino.Droid* the active project for the build. (HelloRhino.Droid is the Android target project. The .Droid suffix is a naming convention from Mono that avoids namespace collisions with the main Android libraries).
![hellorhinomobile solution]({{ site.baseurl }}/images/your-first-app-windows-01.png)
1. Open the *Android Emulator Manager*: Navigate to *Tools* > *Open Android Emulator Manager*. A window called the *Android Virtual Device (AVD) Manager* should appear. This is part of the Android SDK and will be familiar to you if you have done any Android development before. This is where you define your Android Virtual Devices (AVDs) that run in the Emulator.
![avd manager]({{ site.baseurl }}/images/your-first-app-windows-02.png)
1. The default AVDs are much too slow for development; *Highlight each of the existing AVDs* and click the *Delete* button.
1. To create a new AVD: Click the *New* button. The Create new Android Virtual Device (AVD) window appears. Create a new AVD with the following parameters. *AVD Name*: Nexus7-API17; *Device*: Nexus 7 (7.02“, 1200 x 1920:xhdpi); *Target*: Android 4.3 - API Level 18; *CPU/ABI*: Intel Atom (x86); *Skin*: Skin with dynamic hardware controls; *Front Camera*: Webcam0; *VM Heap*: 64 *Emulation Options*: Use Host GPU enabled ...
![create new avd]({{ site.baseurl }}/images/your-first-app-windows-03.png)
1. You should see your new AVD in the list. You have just created your first AVD. More information on creating Emulators can be found in the [Android documentation on Managing Devices](http://developer.android.com/tools/devices/index.html). You can create as many as you need. Tips on using the Emulator can be found in the [Using Simulators]({{ site.baseurl }}/guides/rhinomobile/using-simulators/] guide.
1. *Close* the *AVD Manager*. Switch back to *Visual Studio*.
1. Click the *Info* button in the Xamarin.Android Toolbar.
![info button]({{ site.baseurl }}/images/your-first-app-windows-04.png)
1. This brings up the *Android Device Logging* window. Click the *Change Device* button ...
![select device window]({{ site.baseurl }}/images/your-first-app-windows-05.png)
1. This brings up the *Select Device* window, listing all running devices (emulators and physical devices). Click the *Start emulator image* button.
![start emulator]({{ site.baseurl }}/images/your-first-app-windows-06.png)
1. This brings up the same list of Available AVD images that you saw in the Android Virtual Device (AVD) Manager window. Select the *Nexus7-API18 AVD* that you just created above. Click *OK*.
![select device]({{ site.baseurl }}/images/your-first-app-windows-07.png)
1. If all went well, after a brief startup period (take our word for it, it's much quicker than the standard emulators) you should see Android boot. It may take extra time to launch the first time and it is highly recommended that you leave this window open during your development session. Once Android boots, you are ready to go…you just need to unlock the device by sliding the lock to the right. We are now ready to send the app to the emulator.
1. In the *Solution Explorer*, *right-click* the *HelloRhino.Droid* project, and select *Deploy*. HelloRhino.Droid will build, along with its dependency, RhinoMobile.Droid. (NOTE: The first time you build RhinoMobile.Droid, the libopennurbs library must be compiled…this can take up to 20 minutes. Subsequent builds will be much, much faster).
1. Once the app has been deployed to the running emulator, you can now run the app. In *Visual Studio*, click the *Start* button. If all goes well, you should see something like this...
![hellorhinomobile android]({{ site.baseurl }}/images/your-first-app-windows-08.png)

*Congratulations!*  You've built a RhinoMobile app for Android.

### iOS Boilerplate Build

COMING SOON

---

## Related topics

- [Installing Tools (Windows)]({{ site.baseurl }}/guides/rhinomobile/installing-tools-windows)
- [Your First App (Mac)]({{ site.baseurl }}/guides/rhinomobile/your-first-app-mac)
- [Using Simulators]({{ site.baseurl }}/guides/rhinomobile/using-simulators)
- [Testing on Devices]({{ site.baseurl }}/guides/rhinomobile/testing-on-devices)
- [Managing Devices (Android Documentation](http://developer.android.com/tools/devices/index.html)
