---
layout: toc-guide-page
title: Debug in RhinoWIP (Mac)
author: dan@mcneel.com
categories: ['Fundamentals']
platforms: ['Mac']
apis: ['RhinoCommon']
languages: ['C#']
keywords: ['first', 'RhinoCommon', 'Plugin', 'RhinoWIP']
TODO: 0
origin: unset
order: 1
---

# Debug in RhinoWIP (Mac)
{: .toc-title }

By the end of this guide, you should understand how to modify your plugin's C# project file in order to target and debug using RhinoWIP.


## Prerequisites
{: .toc-header }

This guide presumes you have [installed all the necessary tools]({{ site.baseurl }}/guides/rhinocommon/installing_tools_mac) and know how to [build and debug a plugin using RhinoCommon with Rhinoceros]({{ site.baseurl }}/guides/rhinocommon/your_first_plugin_mac).  

It also presumes you have downloaded and installed [the latest RhinoWIP](http://www.rhino3d.com/go/download/rhino-for-mac/wip/latest).

---

## Edit References
{: .toc-header }

Your plugin requires references to RhinoCommon dlls that are contained within the Rhino application bundle.  The default RhinoCommon Plugin template that comes with the Rhino Xamarin Studio AddIn references `Eto`, `Rhino.UI`, and `RhinoCommon`:

![Bundle References]({{ site.baseurl }}/images/debug_rhinowip_mac_01.png)

...which are all contained within the `Rhinoceros.app` bundle.

We want to target those found in the `RhinoWIP.app` bundle.  Unfortunately, Xamarin Studio does not allow you to browse to references that are contained within an application bundle.  We will have to use a text editor to change these references so that they target the appropriate versions contained in RhinoWIP.

#### Step-by-Step

1. With your plugin Solution open in Xamarin Studio, **right/option-click** on the project name and select **Open Containing Folder**.  This should open a Finder window in the folder containing your project...
![Finder Project Folder]({{ site.baseurl }}/images/debug_rhinowip_mac_02.png)
1. **Open** your plugin's **project** `.csproj` with your **favorite text editor**.  TextEdit comes with OS X and will work.
1. Use your text editor's Find/Replace functions to find `\Applications\Rhinoceros.app` and replace it with `\Applications\RhinoWIP.app`...
![Find and Replace]({{ site.baseurl }}/images/debug_rhinowip_mac_03.png)
1. Verify that these changes are only happening with the `<ItemGroup>` that contains `<Reference>` entries.  Accept your `RhinoWIP.app` replacements to make the change (in Text Edit, this is Replace **All**).
1. In your text editor of choice, **Save** and **Close** your project's `.csproj`.  You may Quit the text editor.
1. In **Xamarin Studio**, the project will reload automatically.  In the **Solution Explorer**, select any of the three references you just changed above.  If you examine their properties (**right/option-click** > **Properties**), you will notice they are now referencing the `RhinoWIP.app` versions.
1. **Build** and **Run**.  Your plugin's **debugging session** should now **launch with RhinoWIP**.
