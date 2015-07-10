---
layout: toc-guide-page
title: Your First Plugin (Mac)
author: dan@mcneel.com
categories: ['GettingStarted']
platforms: ['Mac']
apis: ['RhinoCommon']
languages: ['C#']
keywords: ['first', 'RhinoCommon', 'Plugin']
TODO: 1
origin: unset
order: 4
---


# Your First Plugin (Mac)
{: .toc-title }

This guide walks you through your first plugin for Rhino for Mac using RhinoCommon and Xamarin Studio. It is presumed you already have the necessary tools installed and are ready to go.  If you are not there yet, see [Installing Tools (Mac)]({{ site.baseurl }}/guides/rhinocommon/installing_tools_mac).

## HelloRhinoCommon
{: .toc-header }

We will use the Rhino Xamarin Addin to create a new, basic, command plugin called HelloRhinoCommon.

#### Step-by-Step

If you are familiar with Visual Studio or Xamarin Studio, these step-by-step instructions may be overly detailed for you.  The executive summary: create a new Solution using the RhinoCommon Plugin template, build and run, and then make a change.

We are presuming you have never used Xamarin Studio before, so we'll go through this one step at a time.

#### File New
{: .toc-subheader }

1. If you have not done so already, **launch Xamarin Studio**.
1. Navigate to **File** > **New** > **Solution**...
![File New Solution]({{ site.baseurl }}/images/your_first_plugin_mac_01.png)
1. A **New Project** wizard should appear.  In the left column, find the **Other** > **Miscellaneous** section.  Under General, select the RhinoCommon Plug-In template...
![New Project]({{ site.baseurl }}/images/your_first_plugin_mac_02.png)
1. Click the **Next** button.
1. You will now **Configure your new project**.  For the purposes of this Guide, we will name our demo plugin `HelloRhinoCommon`.  Fill in the **Project Name** field.  **Browse** and select a location for this plugin on your Mac...
![Project Configuration]({{ site.baseurl }}/images/your_first_plugin_mac_03.png)
1. Check **Create a project within the solution directory**.  *NOTE*: This is optional depending on how you want to structure your projects.
1. Click the **Create** button.  *NOTE*: You don't have to create a .git repository for this demo.
1. A **new solution** called **HelloRhinoCommon** should open...
![HelloRhinoCommon Solution]({{ site.baseurl }}/images/your_first_plugin_mac_04.png)

#### Boilerplate Build
{: .toc-subheader }

1. Before we do anything, let's **build** and **run** HelloRhinoCommon to make sure everything is working as expected.  We'll just build the boilerplate Plugin template.  Click the large **Build > Run** (play) button in the upper-left corner of Xamarin Studio...
![Play Button]({{ site.baseurl }}/images/your_first_plugin_mac_05.png)
1. **Rhinoceros** launches.  Create a **New Model**...
![New Model Button]({{ site.baseurl }}/images/your_first_plugin_mac_06.png)
1. Enter the **HelloRhinoCommonCommand** command.  TODO: Describe what it does.
TODO: screencapture
1. **Quit** Rhinoceros.  This stops the session.  Go back to **Xamarin Studio**.  Let's take a look at the...


#### Project Anatomy
{: .toc-subheader }

1. Do more stuff...
1. Do even more stuff...

TODO


#### Make Changes
{: .toc-subheader }

1. Do more stuff...
1. Do even more stuff...

TODO


## Debugging
{: .toc-header }

1. Do more stuff...
1. Do even more stuff...

TODO

---

## Solution & Project
{: .toc-header }

Xamarin Studio uses the same formats as Visual Studio:

- **.sln**
- **.csproj**

It is important to stress: these *are* Visual Studio solutions and projects.  You can open solutions and projects created in Xamarin Studio in Visual Studio and vice-versa.

1. Do more stuff...
1. Do even more stuff...

TODO

---

## Next Steps
{: .toc-header }

**Congratulations!**  You have just built your first RhinoCommon plugin for Rhino for Mac.  **Now what?**

Well, you're using RhinoCommon, so this plugin will actually run on both platforms.  Check out the [Your First Plugin (Cross Platform)]({{ site.baseurl }}/guides/rhinocommon/your_first_plugin_crossplatform) guide.

---

## Related topics
{: .toc-header }

- [Installing Tools (Mac)]({{ site.baseurl }}/guides/rhinocommon/installing_tools_mac)
- [Your First Plugin (Cross-Platform)]({{ site.baseurl }}/guides/rhinocommon/your_first_plugin_crossplatform)
- [Plugin Installers (Mac)]({{ site.baseurl }}/guides/rhinocommon/plugin_installers_mac)
