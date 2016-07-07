---
title: Your First Component (Mac)
description: This guide walks you through your first Grasshopper component for Rhino for Mac using RhinoCommon and Xamarin Studio.
author: steve@mcneel.com
apis: ['Grasshopper']
languages: ['C#']
platforms: ['Mac']
categories: ['Getting Started']
order: 3
keywords: ['developer', 'grasshopper', 'components']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## Prerequisites

Grasshopper for Mac only exists in the RhinoWIP until the next major version of Rhino for Mac is released.  

<div class="bs-callout bs-callout-danger">
  <h4>WARNING</h4>
  <p><b>Early-adopters</b>: the following steps will <b>NOT</b> work with the currently released Rhinoceros (5.x.x).  You will need to use WIP version of Rhinoceros.</p>
</div>

Due to this, there are a few additional steps that need to be taken to install all of the tools needed to develop components.  You will need to do the following:

1. Install the [latest RhinoWIP](http://www.rhino3d.com/go/download/rhino-for-mac/wip/latest). The WIP can be safely installed along side the stable release of Rhino for Mac (but they cannot be run simultaneously).
1. Install Xamarin Studio.  Instructions can be found in the [Installing Tools (Mac)]({{ site.baseurl }}/guides/rhinocommon/installing_tools_mac) guide.
1. Install the Rhino Xamarin Add-in.  Instructions can be found in the [Installing Tools (Mac)]({{ site.baseurl }}/guides/rhinocommon/installing_tools_mac) guide in the [Install the Rhino Add-in]({{ site.baseurl }}/guides/rhinocommon/installing_tools_mac/#install-the-rhino-add-in) section.


## HelloGrasshopper

We will use the Rhino Xamarin Add-in to create a new, basic, Grasshopper component called *HelloGrasshopper*.

If you are familiar with Visual Studio or Xamarin Studio, these step-by-step instructions may be overly detailed for you.  The executive summary: create a new Solution using the Grasshopper Component template, build and run, and then make a change.

We are presuming you have never used Xamarin Studio before, so we'll go through this one step at a time.

### File New

1. If you have not done so already, **launch Xamarin Studio**.
1. Navigate to **File** > **New** > **Solution**...
![File New Solution]({{ site.baseurl }}/images/your_first_plugin_mac_01.png)
1. A **New Project** wizard should appear.  In the left column, find the **Other** > **Miscellaneous** section.  Under General, select the **Grasshopper Component** template...
![New Project]({{ site.baseurl }}/images/your_first_component_mac_02.png)
1. Click the **Next** button.
1. You will now **Configure your new project**.  For the purposes of this Guide, we will name our demo component *HelloGrasshopper*.  Fill in the **Project Name** field.  **Browse** and select a location for this component on your Mac...
![Project Configuration]({{ site.baseurl }}/images/your_first_component_mac_03.png)
1. Click the **Create** button.
1. A **new solution** called **HelloGrasshopper** should open...
![HelloRhinoCommon Solution]({{ site.baseurl }}/images/your_first_component_mac_04.png)

### Boilerplate Build

1. Before we do anything, let's **build** and **run** HelloGrasshopper to make sure everything is working as expected.  We'll just build the boilerplate Component template.  Click the large **Build > Run** (play) button in the upper-left corner of Xamarin Studio...
![Play Button]({{ site.baseurl }}/images/your_first_plugin_mac_05.png)
1. **Rhinoceros** launches.  Create a **New Model**...
![New Model Button]({{ site.baseurl }}/images/your_first_plugin_mac_06.png)
1. Enter the **ExplicitHistory** command.  Notice that your new component is listed a loaded by Grasshopper...
![HelloGrasshopper Loaded]({{ site.baseurl }}/images/your_first_component_mac_05.png)
1. Go to the **Curve** tab in Grasshopper and you should see a new blank icon for your new component...
![Curve Tab]({{ site.baseurl }}/images/your_first_component_mac_06.png)
1. Drag this component on to the Grasshopper canvas to verify that it is working...
![Command Starts]({{ site.baseurl }}/images/your_first_component_mac_07.png)
1. **Quit** Rhinoceros.  This stops the session.  Go back to **Xamarin Studio**.  Let's take a look at the...


### Component Anatomy

1. Use the **Solution Explorer** to expand the **Solution** (*.sln*) so that it looks like this...
![Solution Anatomy]({{ site.baseurl }}/images/your_first_component_mac_08.png)
1. The **HelloGrasshopper** project (*.csproj*) has the same name as its parent solution...this is the project that was created for us by the **Grasshopper Component** template wizard earlier.
1. **References**: Just as with most projects, you will be referencing other libraries.  The **Grasshopper Component** template added the necessary references to create a basic Grasshopper component.
1. **Eto** is the cross-platform User Interface (UI) library Rhino uses.  If you examine its properties, you will notice it comes bundled as part of Rhino for Mac.
1. **GH_IO** is used for reading and writing Grasshopper definitions.
1. **Grasshopper** is the Rhino for Mac main grasshopper DLL. Classes in this DLL are subclassed and used by your custom component.
1. **Rhino.UI** is the Rhino-specific User Interface (UI) library associated with...
1. **RhinoCommon** is used by your component to work with all of the geometry defined in Rhino.
1. **System**, **System.Core**, and **System.Drawing** are .NET foundational libraries...in this case, we are referencing the Mono versions of these libraries (on Windows, these references will point to the canonical, Microsoft-provided, versions).
1. **Packages** is used the the [NuGet](https://www.nuget.org/) package-manager.  There are no referenced packages in this boilerplate project, but note that Xamarin Studio supports NuGet, just like Visual Studio does.
1. **Properties** contains the **AssemblyInfo.cs** source file.  This file contains general information about your component.
1. **HelloGrasshopperComponent.cs** is where a custom `Grasshopper.Kernal.GH_Component` subclass is defined. Your project may contain multiple subclasses of GH_Component if you want to ship multiple components in a single *gha*.  
1. **HelloGrasshopperInfo.cs** defines general information about this *gha*.

### Debugging

1. Set a breakpoint on line[^1] 103 of *HelloGrasshopperComponent.cs*.  You set breakpoints in Xamarin Studio by clicking in the gutter...
![Set a breakpoint]({{ site.baseurl }}/images/your_first_component_mac_09.png)
1. **Build** and **Run**.  Drag one of your new components on to the Grasshopper canvas...as soon as you do, you should hit your breakpoint and pause...
![Hit a breakpoint]({{ site.baseurl }}/images/your_first_component_mac_10.png)
1. With Rhino paused, in **Xamarin Studio** switch to the **Locals** tab.  In the list, you can inspect all of the values for the variables in your function...  
![Locals panel]({{ site.baseurl }}/images/your_first_component_mac_11.png)
1. **Continue Executing** in Rhino by pressing the **Play** button in the upper navigation menu of **Xamarin Studio**...
![Continue Executing]({{ site.baseurl }}/images/your_first_plugin_mac_15.png)
1. Control is passed back to **Rhino** and your command finishes.  **Quit** Rhino or **Stop** the debugging session.
1. **Remove** the breakpoint you created above by clicking on it in the gutter.

**DONE!**

**Congratulations!**  You have just built your first Grasshopper component for Rhino for Mac.  **Now what?**

---

## Next Steps

### Adding components

A single gha can contain more than one GH_Component derived class (and commonly does). The Xamarin Studio has support for adding more custom components to your project.

1. Navigate to **File** > **New** > **File**...
![File New Solution]({{ site.baseurl }}/images/your_first_component_mac_12.png)
1. A **New File** wizard should appear.  In the left column, find the **Rhinoceros** section.  This should give you the ability to select an "Empty Grasshopper Component"...
![New Project]({{ site.baseurl }}/images/your_first_component_mac_13.png)
1. After deciding on a name for the component click the **New** button.

---

## Related topics

This article is focused on initial setup and debugging a Grasshopper component in Rhino for Mac.  For further reading on customizing your component please see: **TODO - provide good reference for component development**

- [Installing Tools (Mac)]({{ site.baseurl }}/guides/rhinocommon/installing_tools_mac)

---

## Footnotes

[^1]: **Line numbers** in Xamarin Studio can be enabled and disabled in **Xamarin Studio** > **Preferences...** > **Text Editor** section > **Markers and Rulers** entry > check **Show line numbers**.
