+++
aliases = ["/en/5/guides/rhinocommon/installing-tools-windows/", "/en/6/guides/rhinocommon/installing-tools-windows/", "/en/7/guides/rhinocommon/installing-tools-windows/", "/en/wip/guides/rhinocommon/installing-tools-windows/"]
authors = [ "steve" ]
categories = [ "Getting Started" ]
description = "This guide covers the tools required to author, build and debug Rhino plugins on Windows."
keywords = [ "first", "RhinoCommon", "Plugin" ]
languages = [ "C#" ]
sdk = [ "RhinoCommon" ]
title = "Installing Tools (Windows)"
type = "guides"
weight = 1
thumbnail = "/images/dev-logo-rhino-small.png"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommon"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"
+++

By the end of this guide, you should have all the tools installed necessary for authoring, building, and debugging .NET plugins using RhinoCommon on Windows.

## Prerequisites

This guide presumes you have:

### Rhino 8

- A PC running Microsoft Windows 10 or later.
- [Rhino 8 for Windows](https://www.rhino3d.com/download).

### Rhino 7

- A PC running Microsoft Windows 8.1 or later.
- [Rhino 7 for Windows](https://www.rhino3d.com/download).


## Install Visual Studio

To write .NET plugins for Rhino using using RhinoCommon, you will Microsoft Visual Studio. As of this writing, the current version is [Visual Studio 2022](https://visualstudio.microsoft.com/downloads/).

1. Download [**Microsoft Visual Studio**](https://visualstudio.microsoft.com/downloads/).
2. Run the **Visual Studio installer** you just downloaded.

    ![Visual Studio Install](/images/installing-tools-windows-rhinocommon-01.png)
3. Follow the onscreen prompts to install Visual Studio.
4. Check the **.NET desktop development** workload.
5. Click the **Individual components** tab.
6. Scroll to the **.NET** section and check the following options:
    1. .NET 7.0 Runtime
    2. .NET Framework 4.8 SDK
    3. .NET Framework 4.8 targeting pack
7. Check any additional features required for your project.
8. When finished, click **Install**.
9. Depending on your internet connection, this can take several minutes to complete.

If you already have Microsoft Visual Studio installed, then you will want to re-run the **Visual Studio Installer** and verify you have all the the components installed.

## Installing Visual Studio Extension

The **Rhino Visual Studio Extension** contains templates to get you started creating plugin projects quickly.

1. Download the **[Rhino Visual Studio Extension (VSIX)](https://github.com/mcneel/RhinoVisualStudioExtensions/releases)**.
2. Run the **VSIX installer** you downloaded.
3. If the installation is successful, run Visual Studio.

## Next Steps

*Congratulations!*  You have the tools to build a RhinoCommon plugin for Rhino for Windows. *Now what?*

Check out the [Your First Plugin (Windows)](/guides/rhinocommon/your-first-plugin-windows) guide for instructions on how to build your first plugin.
