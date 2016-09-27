---
title: Installing Tools (Windows)
description: This guide covers all the necessary tools required to author Rhino plugins in C/C++ on Windows.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Getting Started']
origin: https://wiki.mcneel.com/developer/cplusplusplugins
order: 1
keywords: ['c', 'C/C++', 'plugin']
layout: toc-guide-page
TODO: 'needs to be written.'
---

# {{ page.title }}

{{ page.description }}

By the end of this guide, you should have all the tools installed necessary for authoring, building, and debugging C/C++ plugins using the Rhino C/C++ SDK on Windows.

## Prerequisites

This guide presumes you have:

- A PC running Microsoft Windows 7 or later.
- [The Rhino Work-In-Progress (WIP)](https://discourse.mcneel.com/t/welcome-to-serengeti/9612).

---

## Install Visual Studio

In order to author, build, and debug C/C++ plugins for Rhino, you will need Microsoft [Visual Studio 2015](https://www.visualstudio.com/en-us/visual-studio-homepage-vs.aspx).

Visual Studio 2015 comes in [three editions](https://www.visualstudio.com/downloads): Community, Professional, and Enterprise. All of these editions will work with the Rhino C/C++ SDK.

*Note*: Rhino C/C++ SDK plugins **cannot** be authored in version of Visual Studio older than 2015. Rhino is built with Visual Studio 2015, and your plugin must link with the same versions of C-Runtime and MFC and Rhino. 

#### Step-by-Step

1. **[Visual Studio 2015 Community Edition](https://www.visualstudio.com/vs-2015-product-editions)** is free from Microsoft for students, open-source contributors, and small teams. [Details here](https://www.visualstudio.com/en-us/support/legal/mt171547).  Click the **Community** button to download the installer.
1. Run the **Visual Studio installer** you downloaded from Microsoft, in this case ***vs_community.exe***.
1. Follow the onscreen prompts to install Visual Studio. Make sure to select all of the **Visual C++** features. 
![Visual Studio Install]({{ site.baseurl }}/images/installing_tools_windows_cpp_01.png)
1. Depending on your internet connection, this can take minutes or hours.  When successfully installed, click the **Launch** button.

## Downloads

- [Rhino 5 for Windows C++ SDK](http://download.rhino3d.com/rhino/5.0/sdk)
- [Rhino 5 for Windows (Evaluation)](http://download.rhino3d.com/rhino/5.0/evaluation/download)
- [Rhino 5 for Windows Service Release](http://www.rhino3d.com/download/rhino/5.0/sr)

## Next Steps

---

## Related Topics
