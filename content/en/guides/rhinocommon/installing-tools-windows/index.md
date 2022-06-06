+++
aliases = ["/5/guides/rhinocommon/installing-tools-windows/", "/6/guides/rhinocommon/installing-tools-windows/", "/7/guides/rhinocommon/installing-tools-windows/", "/wip/guides/rhinocommon/installing-tools-windows/"]
authors = [ "steve" ]
categories = [ "Getting Started" ]
description = "This guide covers the tools required to author, build and debug Rhino plugins on Windows."
keywords = [ "first", "RhinoCommon", "Plugin" ]
languages = [ "C#" ]
sdk = [ "RhinoCommon" ]
title = "Installing Tools (Windows)"
type = "guides"
weight = 1
override_last_modified = "2021-06-07T11:23:48Z"

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


## Prerequisites

This guide presumes you have [Rhino 7 for Windows](http://www.rhino3d.com/download)

## Install Visual Studio

[Visual Studio](https://www.visualstudio.com/en-us/visual-studio-homepage-vs.aspx) is Microsoft's development platform and Integrated Development Environment (IDE).  Visual Studio comes in three major "streams": Visual Studio Code[^1], Visual Studio Online[^2], and Visual Studio "proper"[^3].  In order to author RhinoCommon plugins, you will need Visual Studio "proper" (Visual Studio Code and Visual Studio Online are not supported).

At the time of this writing, Visual Studio "proper" comes in [three editions](https://www.visualstudio.com/vs-2015-product-editions): Community, Professional, and Enterprise.  Any of these editions will work.

**Note**: For the purposes of this guide, we will presume you are using Visual Studio 2019 Community Edition.

#### Step-by-Step

1. *[Visual Studio Community Edition](https://visualstudio.microsoft.com/vs/)* is free from Microsoft for students, open-source contributors, and small teams. [Details here](https://www.visualstudio.com/en-us/support/legal/mt171547).  Click the *Community* button to download the installer.
1. Run the *Visual Studio installer* you downloaded from Microsoft.
1. Follow the onscreen prompts to install Visual Studio.  You will need the ".NET desktop development" workload for RhinoCommon based plug-in development. When successfully installed, click the *Launch* button.

## RhinoCommon templates

The [RhinoCommon templates](https://marketplace.visualstudio.com/items?itemName=McNeel.Rhino7Templates) contains wizards to get you started creating plugins quickly.

#### Step-by-Step

1. Launch *Visual Studio*.
1. Navigate to *Tools* > *Extensions and Updates...*
1. In the left-hand sidebar, expand the *Online* section, then select the *Visual Studio Gallery* entry...
![Extensions and Updates](/images/installing-tools-windows-01.png)
1. In the *Search* field, search for *rhinocommon*.  This filters the gallery list below.
1. Find *RhinoCommon templates* and select it.
1. Click the *Download* button.  The extension installation should begin after you close Visual Studio.
1. You must *Accept* the license agreement by clicking on the *Install* button.
1. If the installation is successful, the extension should appear in your list of *Installed* extensions.

## Next Steps

*Congratulations!*  You have the tools to build a RhinoCommon plugin for Rhino for Windows.  *Now what?*

Check out the [Your First Plugin (Windows)](/guides/rhinocommon/your-first-plugin-windows) guide for instructions building - your guessed it - your first plugin.

**Footnotes**

[^1]: Visual Studio Code is Microsoft's cross-platform source code editor for Windows, Linux, and macOS.  At the time of this writing, Visual Studio code does not yet support the features required to author RhinoCommon plugins.

[^2]: Visual Studio Online is Microsoft's online counterpart to the desktop edition of Visual Studio (referred to as Visual Studio "proper" above).  We have not tested using Visual Studio Online to debug RhinoCommon plugins as having a copy of Rhino running would prove logistically difficult.

[^3]: Visual Studio "proper" is the desktop version of Visual Studio...we are only attaching the "proper" epithet to distinguish it from the Visual Studio Code and Visual Studio Online.  In subsequent guides this will be referred to as simply "Visual Studio."
