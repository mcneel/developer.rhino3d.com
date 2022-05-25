+++
authors = [ "dan" ]
categories = [ "Getting Started" ]
description = "This guide covers all the necessary tools required to author custom Grasshopper components on Windows."
keywords = [ "developer", "grasshopper", "components" ]
languages = [ "C#", "VB" ]
sdk = [ "Grasshopper" ]
title = "Installing Tools (Windows)"
type = "guides"
weight = 1

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

- A PC running Microsoft Windows 7 or later.
- [Rhino 6 for Windows](https://www.rhino3d.com/)

## Install Visual Studio

[Visual Studio](https://www.visualstudio.com/en-us/visual-studio-homepage-vs.aspx) is Microsoft's flagship development platform and Integrated Development Environment (IDE).  Visual Studio now comes in three major "streams": Visual Studio Code[^1], Visual Studio Online[^2], and Visual Studio "proper"[^3].  In order to author custom Grasshopper components, you will need Visual Studio "proper" (Visual Studio Code and Visual Studio Online are not supported).

At the time of this writing, Visual Studio "proper" comes in [three editions](https://www.visualstudio.com/vs-2015-product-editions): Community, Professional, and Enterprise.  Any of these editions will work. Additionally, [Visual Studio Express 2015 for Windows Desktop](https://www.visualstudio.com/products/visual-studio-express-vs.aspx) will work with more limited debugging support[^4]. Other Express versions, such as Express for Windows, Express for Web or Team Foundation Server 2015 Express, will not work.

*NOTE*: Grasshopper components can be authored in Visual Studio 2010, 2012, 2013, 2015, and 2017 both in C# and VB, and included in Ultimate, Professional, Premium, C# Express, Vb Express and Windows Desktop Express (where available).  For the purposes of this guide, we will presume you are using Visual Studio Community Edition.

#### Step-by-Step

1. **[Visual Studio 2017 Community Edition](https://visualstudio.microsoft.com/vs/)** is free from Microsoft for students, open-source contributors, and small teams. [Details here](https://www.visualstudio.com/en-us/support/legal/mt171547).  Click the **Community** button to download the installer.
1. Run the **Visual Studio installer** you downloaded from Microsoft, in this case ***vs_community.exe***.
1. Follow the onscreen prompts to install Visual Studio.  It is recommended that you install the **Typical** installation.  Depending on your internet connection, this can take minutes or hours.  When successfully installed, click the **Launch** button.

## Grasshopper Assembly

The [Grasshopper Assembly templates](https://visualstudiogallery.msdn.microsoft.com/dc7014d0-c37f-4148-ba47-5d537f6c5f22) contains wizards to get you started creating components quickly.

#### Step-by-Step

1. Launch **Visual Studio**.
1. Navigate to **Tools** > **Extensions and Updates...**
1. In the left-hand sidebar, expand the **Online** section, then select the **Visual Studio Gallery** entry...
![Extensions and Updates](/images/installing-tools-windows-grasshopper-01.png)
1. In the **Search** field, search for *Grasshopper*.  This filters the gallery list below.
1. Find **Grasshopper Assembly for v6** and select it.
1. Click the **Download** button.  The extension installation should begin.
1. You must **Accept** the license agreement by clicking on the **Install** button.
1. If the installation is successful, you will be redirected to this developer website and the extension should appear in your list of **Installed** extensions.

## Next Steps

**Congratulations!**  You have the tools to build custom Grasshopper components for Grasshopper for Windows.  **Now what?**

Check out the [Your First Component (Windows)](/guides/grasshopper/your-first-component-windows) guide for instructions building - your guessed it - your first component.

**Footnotes**

[^1]: Visual Studio Code is Microsoft's cross-platform source code editor for Windows, Linux, and macOS.  At the time of this writing, Visual Studio code does not yet support the features required to author Grasshopper components

[^2]: Visual Studio Online is Microsoft's online counterpart to the desktop edition of Visual Studio (referred to as Visual Studio "proper" above).  We have not tested using Visual Studio Online to debug Grasshopper components as having a copy of Rhino and Grasshopper running would prove logistically difficult.

[^3]: Visual Studio "proper" is the desktop version of Visual Studio...we are only attaching the "proper" epithet to distinguish it from the Visual Studio Code and Visual Studio Online.  In subsequent guides this will be referred to as simply "Visual Studio."

[^4]: Visual Studio 2017 Community Edition offers a development platform that has a less strict licensing agreement policy than the Community edition. Please refer to the EULA for complete details, available during installation. In this edition, debugging of Rhino and Grasshopper can be started, but the location of the Rhino executable (rhino.exe), usually available in the Project property page, in the Debug tab, cannot be changed in the UI. After Wizard completion, the location of the Rhino executable can only be edited in the XML of the resulting **.csproj** file, in the main folder of the solution.
