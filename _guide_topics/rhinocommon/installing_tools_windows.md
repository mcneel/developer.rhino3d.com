---
layout: toc-guide-page
title: Installing Tools (Windows)
author: steve@mcneel.com
categories: ['GettingStarted']
platforms: ['Windows']
apis: ['RhinoCommon']
languages: ['C#']
keywords: ['first', 'RhinoCommon', 'Plugin']
TODO: 0
origin: http://wiki.mcneel.com/developer/rhinocommon
order: 1
---

# Installing Tools (Windows)
{: .toc-title }

By the end of this guide, you should have all the tools installed necessary for authoring, building, and debugging C# .NET plugins using RhinoCommon in Rhino for Windows.

## Prerequisites
{: .toc-header }

This guide presumes you have an:

- A PC running Microsoft Windows 7 or later.
- [Rhino 5 for Windows](http://www.rhino3d.com/download) (SR-11) or later.

---

## Install Visual Studio
{: .toc-header }

[Visual Studio](https://www.visualstudio.com/en-us/visual-studio-homepage-vs.aspx) is Microsoft's flagship development platform and Integrated Development Environment (IDE).  Visual Studio now comes in three "flavors": Visual Studio Code[^1], Visual Studio Online[^2], and Visual Studio "proper"[^3].  In order to author RhinoCommon plugins, you will need Visual Studio "proper" (Visual Studio Code and Visual Studio Online are not supported).

At the time of this writing, Visual Studio 2015 "proper" comes in [three editions](https://www.visualstudio.com/vs-2015-product-editions): Community, Professional, and Enterprise.  Any of these editions will work.

*NOTE*: RhinoCommon plugins can be authored in Visual Studio 2010, 2012, 2013, and 2015 both in C# and Vb.Net, and included in Ultimate, Professional, Premium, C# Express, Vb Express and Windows Desktop Express (where available).  For the purposes of this guide, we will presume you are using Visual Studio 2015 Community Edition.

#### Step-by-Step

1. **[Visual Studio 2015 Community Edition](https://www.visualstudio.com/vs-2015-product-editions)** is free from Microsoft for students, open-source contributors, and small teams. [Details here](https://www.visualstudio.com/en-us/support/legal/mt171547).  Click the **Community** button to download the installer.
1. Run the **Visual Studio installer** you downloaded from Microsoft, in this case ***vs_community.exe***.
1. Follow the onscreen prompts to install Visual Studio.  It is recommended that you install the **Typical** installation.  Depending on your internet connection, this can take minutes or hours.  When successfully installed, click the **Launch** button.

---

## RhinoCommon templates
{: .toc-header }

The [RhinoCommon templates](https://visualstudiogallery.msdn.microsoft.com/16053049-7db2-4c9f-961a-53274ac92ace) contains wizards to get you started creating plugins quickly.

#### Step-by-Step

1. Launch **Visual Studio**.
1. Navigate to **Tools** > **Extensions and Updates...**
1. In the left-hand sidebar, expand the **Online** section, then select the **Visual Studio Gallery** entry...
![Extensions and Updates]({{ site.baseurl }}/images/installing_tools_windows_01.png)
1. In the **Search** field, search for *rhino*.  This filters the gallery list below.
1. Find **RhinoCommon templates for v5** and select it.
1. Click the **Download** button.  The extension installation should begin.
1. You must **Accept** the license agreement by clicking on the **Install** button.
1. If the installation is successful, you will be redirected to the RhinoCommon website and the extension should appear in your list of **Installed** extensions.

---

## Next Steps
{: .toc-header }

**Congratulations!**  You have the tools to build a RhinoCommon plugin for Rhino for Windows.  **Now what?**

Check out the [Your First Plugin (Windows)]({{ site.baseurl }}/guides/rhinocommon/your_first_plugin_windows) guide for instructions building - your guessed it - your first plugin.

---

## Footnotes
{: .toc-header }

[^1]: Visual Studio Code is Microsoft's cross-platform source code editor for Windows, Linux, and OS X.  At the time of this writing, Visual Studio code does not yet support the features required to author RhinoCommon plugins.

[^2]: Visual Studio Online is Microsoft's online counterpart to the desktop edition of Visual Studio (referred to as Visual Studio "proper" above).  We have not tested using Visual Studio Online to debug RhinoCommon plugins as having a copy of Rhino running would prove logistically difficult.

[^3]: Visual Studio "proper" is the desktop version of Visual Studio...we are only attaching the "proper" epithet to distinguish it from the Visual Studio Code and Visual Studio Online.  In subsequent guides this will be referred to as simply "Visual Studio."
