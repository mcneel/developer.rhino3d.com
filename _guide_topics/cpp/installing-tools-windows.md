---
title: Installing Tools (Windows)
description: This guide covers all the necessary tools required to author Rhino plugins in C/C++ on Windows.
authors: ['dale_fugier']
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

- A PC running Microsoft Windows 8.1 or later.
- [Rhino 7 for Windows](https://www.rhino3d.com/download).

---

## Install Visual Studio
In order to author, build, and debug C/C++ plugins for Rhino, you will need Microsoft [Visual Studio 2019](https://www.visualstudio.com/en-us/visual-studio-homepage-vs.aspx).

Visual Studio 2019 comes in [three editions](https://www.visualstudio.com/downloads): Community, Professional, and Enterprise. All of these editions will work with the Rhino C/C++ SDK.

#### Step-by-Step

1. **[Visual Studio 2019 Community](https://www.visualstudio.com/vs/community/)** is free from Microsoft for students, open-source contributors, and small teams. [Details here](https://visualstudio.microsoft.com/license-terms/mlt031819/).  Click the **Community** button to download the installer.
2. Run the **Visual Studio installer** you downloaded from Microsoft, in this case ***vs_community_[build_number].exe***.
    ![Visual Studio Install]({{ site.baseurl }}/images/installing-tools-windows-cpp-01.png)
3. Follow the onscreen prompts to install Visual Studio. Make sure to select all of the **Desktop development with C++** features.
4. Click the **Individual components** tab, scroll to the **SDKs, libraries, and frameworks** section, and check **Visual Studio SDK**.
    ![Visual Studio Install]({{ site.baseurl }}/images/installing-tools-windows-cpp-02.png)
5. When finished, click **Install**.
6. Depending on your internet connection, this can take several minutes to complete.

## Modifying Visual Studio

If you already have Microsoft Visual Studio 2019 installed, then you will want to re-run the Visual Studio Installer and verify you have all the the components required to build Rhino plug-in installed.

#### Step-by-Step
1. Open the **[Visual Studio Installer](https://docs.microsoft.com/en-us/visualstudio/install/modify-visual-studio?view=vs-2019)**.
2. In the installer, look for the 2019 edition of Visual Studio that you installed, and then choose **Modify**.
3. As mentioned in **Install Visual Studio** above, select all of the **Desktop development with C++** features.
4. Also mentioned above, click the **Individual components** tab, scroll to the **SDKs, libraries, and frameworks** section, and check **Visual Studio SDK**.
5. When finished, click **Modify**.
6. Depending on your internet connection, this can take several minutes to complete.

## Install the Rhino C/C++ SDK

The **Rhino C/C++ SDK** is a set of tools for creating plug-in using the C++ language. The SDK includes headers, libraries and Visual Studio project wizards to get you started creating plugins quickly.

```
NOTE WELL: During the Rhino WIP development cycle, you MUST download the Rhino WIP C/C++ SDK which cooresponds to the version of Rhino WIP you are using. This SDK is extended/updated/bug fixed every week. But any plug-ins made with and of the updates will work in the released version of Rhino 7.
```

#### Step-by-Step

1. Exit **Visual Studio**.
2. Download the **[Rhino C/C++ SDK](https://www.rhino3d.com/download/Rhino-SDK/7.0/release)**.
3. Run the **SDK installer** you downloaded, in this case ***rh70sdk_[build_number].msi***.
4. If the installation is successful, run Visual Studio.

---

## Next Steps

**Congratulations!** You have the tools to build a C/C++ plugin for Rhino for Windows. **Now what?**

Check out the [Creating your first C/C++ plugin for Rhino]({{ site.baseurl }}/guides/cpp/your-first-plugin-windows/) guide for instructions building - you guessed it - your first plugin.
