---
title: Installing Tools (Windows)
description: This guide covers all the necessary tools required to author Rhino plugins in C/C++ on Windows.
authors: ['Dale Fugier']
author_contacts: ['dale']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Getting Started']
origin: https://wiki.mcneel.com/developer/cplusplusplugins
order: 1
keywords: ['c', 'C/C++', 'plugin']
layout: toc-guide-page
TODO: 'needs to be written.'
---


By the end of this guide, you should have all the tools installed necessary for authoring, building, and debugging C/C++ plugins using the Rhino C/C++ SDK on Windows.

## Prerequisites

This guide presumes you have:

- A PC running Microsoft Windows 7 or later.
- [The Rhino Work-In-Progress (WIP)](https://www.rhino3d.com/download/rhino/wip).

---

## Install Visual Studio
In order to author, build, and debug C/C++ plugins for Rhino, you will need Microsoft [Visual Studio 2017](https://www.visualstudio.com/en-us/visual-studio-homepage-vs.aspx).

Visual Studio 2017 comes in [three editions](https://www.visualstudio.com/downloads): Community, Professional, and Enterprise. All of these editions will work with the Rhino C/C++ SDK.

*Note*: Rhino C/C++ SDK plugins **cannot** be authored in versions of Visual Studio other than 2017. The native classes and libraries that are made available via the Rhino C/C++ SDK are also used internally by Rhino. As a result of this tight linkage with Rhino itself, the libraries are very compiler specific, and work only with the same compiler that was used to build Rhino.

#### Step-by-Step

1. **[Visual Studio 2017 Community Edition](https://www.visualstudio.com/vs/community/)** is free from Microsoft for students, open-source contributors, and small teams. [Details here](https://www.visualstudio.com/license-terms/mlt553321/).  Click the **Community** button to download the installer.
2. Run the **Visual Studio installer** you downloaded from Microsoft, in this case ***vs_community_[build_number].exe***.
  ![Visual Studio Install]({{ site.baseurl }}/images/installing-tools-windows-cpp-01.png)
3. Follow the onscreen prompts to install Visual Studio. Make sure to select all of the **Desktop development with C++** features.
  ![Visual Studio Install]({{ site.baseurl }}/images/installing-tools-windows-cpp-02.png)
4. Depending on your internet connection, this can take minutes or hours.

## Install the Rhino C/C++ SDK

<div class="bs-callout bs-callout-danger">
  <h4>NOTE</h4>
  <p>Rhino 6 is in WIP, or Work-in-Progress, form. The Rhino WIP C/C++ SDK Version number changes with every Rhino WIP release, which tends to be weekly. Plug-ins built with this SDK will only load in a Rhino with exactly the same version number. Thus, it will be almost impossible for you to release plug-ins for customers to use. When Rhino 6 enters the Beta testing phase, the SDK will be frozen, thus preventing breaking changes, which will allow you to distribute your plug-ins for testing.</p>
</div>

The [Rhino C/C++ SDK](https://discourse.mcneel.com/t/rhino-wip-developers/30197) is a set of tools for creating plug-in using the C++ language. The SDK includes headers, libraries and Visual Studio project wizards to get you started creating plugins quickly.

1. Exit **Visual Studio**.
2. Download the **[Rhino C/C++ SDK](http://www.rhino3d.com/download/rhino-sdk/wip)**.
3. Run the **SDK installer** you downloaded, in this case ***rh60sdk_[build_number].msi***.
4. If the installation is successful, run Visual Studio.

---

## Next Steps

**Congratulations!** You have the tools to build a C/C++ plugin for Rhino for Windows. **Now what?**

Check out the [Creating your first C/C++ plugin for Rhino]({{ site.baseurl }}/guides/cpp/your-first-plugin-windows/) guide for instructions building - you guessed it - your first plugin.
