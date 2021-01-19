---
title: Running and Debugging Compute Locally
description: Deploy Compute for Production
authors: ['brian_gillespie', 'will_pearson']
sdk: ['Compute']
languages: ['C#', 'VB']
platforms: ['Windows']
categories: ['Getting Started', 'Development']
order: 2
keywords: ['developer', 'compute', 'production']
layout: toc-guide-page
TODO: 'needs editing'
---

How to develop Compute on your Windows 10 computer.

1. [Download](https://www.rhino3d.com/download/rhino-for-windows/7/latest) and install Rhino 7.
1. Start Rhino at least once to configure its license.
1. Clone the [compute.rhino3d](https://github.com/mcneel/compute.rhino3d) repository from GitHub.
1. Open `src\compute.sln` in Visual Studio 2019 and compile as `Debug`.
1. Make sure that `compute.geometry` is set as the startup project.
1. Start the application in the debugger.
1. Wait for Compute to load... ☕️

    ![compute.geometry.exe]({{site.basurl }}/images/compute_geometry_screenshot.png)

1. Browse to [http://localhost:8081/version](http://localhost:8081/version) to check that it's working!
