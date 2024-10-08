+++
aliases = ["/en/5/guides/grasshopper/installing-tools-windows/", "/en/6/guides/grasshopper/installing-tools-windows/", "/en/7/guides/grasshopper/installing-tools-windows/", "/en/wip/guides/grasshopper/installing-tools-windows/"]
authors = [ "dan" ]
categories = [ "Getting Started" ]
description = "This guide covers all the necessary tools required to author custom Grasshopper components on Windows."
keywords = [ "developer", "grasshopper", "components" ]
languages = [ "C#", "VB" ]
sdk = [ "Grasshopper" ]
title = "Installing Tools (Windows)"
type = "guides"
weight = 1
thumbnail = "/images/dev-logo-grasshopper-small.png"

[admin]
TODO = ""
origin = ""
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


By the end of this guide, you should have all the tools installed necessary for authoring, building, and debugging custom Grasshopper components in Rhino for Windows.

## Prerequisites

This guide presumes you have an:

- A PC running Microsoft Windows 10 or later.
- [Rhino 7 for Windows](https://www.rhino3d.com/download)

## Install Visual Studio

[Visual Studio](https://www.visualstudio.com/en-us/visual-studio-homepage-vs.aspx) is Microsoft's flagship development platform and Integrated Development Environment (IDE).  Visual Studio now comes in three major "streams": Visual Studio Code[^1], Visual Studio Online[^2], and Visual Studio "proper"[^3].  In order to author custom Grasshopper components, you will need Visual Studio "proper" (Visual Studio Code and Visual Studio Online are not supported).

{{< call-out "note" "Visual Studio Editions" >}}
For the purposes of this guide, we will presume you are using Visual Studio 2022 Community Edition.
{{< /call-out >}}

#### Step-by-Step

1. **[Visual Studio Community Edition](https://visualstudio.microsoft.com/vs/)** is free from Microsoft for students, open-source contributors, and small teams. [Details here](https://www.visualstudio.com/en-us/support/legal/mt171547).  Click the **Community** button to download the installer.
1. Run the **Visual Studio installer** you downloaded from Microsoft, in this case *VisualStudioSetup.exe*.
1. Follow the onscreen prompts to install Visual Studio.  You will need the ".NET desktop development" workload for RhinoCommon based plug-in development. When successfully installed, click the *Launch* button.

## Grasshopper Templates

The [RhinoCommon and Grasshopper templates for Rhino 7](https://marketplace.visualstudio.com/items?itemName=McNeel.Rhino7Templates2022) contains wizards to get you started creating components quickly.

#### Step-by-Step

1. Launch **Visual Studio**.
1. Navigate to **Extensions** > **Manage Extensions**
1. In the left-hand sidebar, expand the **Online** section, then select the **Visual Studio Marketplace** entry...
![Extensions and Updates](/images/installing-tools-windows-grasshopper-01.png)
1. In the **Search** field, search for *RhinoCommon*.  This filters the gallery list below.
1. Find **RhinoCommon and Grasshopper templates for Rhino 7** and select it.
1. Click the **Download** button.  The extension installation should begin.
1. You must **Accept** the license agreement by clicking on the **Install** button.
1. Press the **Close** button and **Quit** Visual Studio.
1. The extension installer should start once you quit. Click the **Modify** button to install the extension.
1. Once this is done, the extension should appear in your list of **Installed** extensions in **Extensions** > **Manage Extensions**.

## Next Steps

**Congratulations!**  You have the tools to build custom Grasshopper components for Grasshopper for Windows.  **Now what?**

Check out the [Your First Component (Windows)](/guides/grasshopper/your-first-component-windows) guide for instructions building - your guessed it - your first component.

**Footnotes**

[^1]: Visual Studio Code is Microsoft's cross-platform source code editor for Windows, Linux, and macOS.  At the time of this writing, Visual Studio code does not yet support the features required to author Grasshopper components

[^2]: Visual Studio Online is Microsoft's online counterpart to the desktop edition of Visual Studio (referred to as Visual Studio "proper" above).  We have not tested using Visual Studio Online to debug Grasshopper components as having a copy of Rhino and Grasshopper running would prove logistically difficult.

[^3]: Visual Studio "proper" is the desktop version of Visual Studio...we are only attaching the "proper" epithet to distinguish it from the Visual Studio Code and Visual Studio Online.  In subsequent guides this will be referred to as simply "Visual Studio."
