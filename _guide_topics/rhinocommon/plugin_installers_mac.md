---
layout: toc-guide-page
title: Plugin Installers (Mac)
author: dan@mcneel.com
categories: ['GettingStarted']
platforms: ['Mac']
apis: ['RhinoCommon']
languages: ['C#']
keywords: ['first', 'RhinoCommon', 'Plugin', 'installing']
TODO: 0
origin: unset
order: 6
---


# Plugin Installers (Mac)
{: .toc-title }

This guide explains how to create a plugin installer for Rhino for Mac, which presumes you have a plugin that successfully builds and runs already.  If you are not there yet, see [Your First Plugin (Mac)]({{ site.baseurl }}/guides/rhinocommon/your_first_plugin_mac).

## Overview
{: .toc-header }

Rhino for Mac does not (yet) have a Plugin Manager.  However, installing plugins is very easy.  You simply create a zip archive of your plugin folder with an special extension (*.rhp*), compress the folder, and change the extension from *.zip* to *.macrhi*.  Once this is done, you can double-click the archive and Rhino will launch and install the plugin.  You can also drag the *.macrhi* onto the dock icon of a running instance of Rhino and it will install the plugin as well.  You will, in any case, need to Quit an Restart Rhino for the plugin to activate.

---

## Step-by-Step
{: .toc-header }

1. **Locate** your plugin folder in **Finder**.  Let's imagine our plugin is called **HelloRhinoCommon** and we have built it for **Release**...
![Find Plugin In Finder]({{ site.baseurl }}/images/plugin_installer_mac_01.png)
1. **Single-click the name** your plugin's **Release** (or **Debug**) folder to **Rename** it.  The new name should be your plugin assembly with a *.rhp* suffix.  For example, if your plug-in is called *HelloRhinoCommon.dll*, rename the folder that contains this file *HelloRhinoCommon.rhp*...
1. You will be prompted to confirm this change.  Click the "**Add**" button:
![Click Add]({{ site.baseurl }}/images/plugin_installer_mac_02.png)
1. The icon of the folder[^1] should now look like this...
![New Icon]({{ site.baseurl }}/images/plugin_installer_mac_03.png)
1. **Archive** the plugin **folder**.  **Right-click** (option-click) the plugin *.rhp* **folder** you created in the previous step and select "**Compress** (your plugin name)."  This creates a zip archive of the contents of the folder.
1. **Single-click the name** of the new archive you created in step 5.  This allows you **to rename** the archive.
1. Change the **extension** from *.zip* to *.macrhi*.  
1. You will be prompted to confirm this change.  Select the "**Use .macrhi**" button:
![Use rhi Extension]({{ site.baseurl }}/images/plugin_installer_mac_04.png)
1. Notice that **the icon changes** from a zip archive to a Rhino RHI:
![use_macrhi_confirm]({{ site.baseurl }}/images/plugin_installer_mac_05.png)
1. If Rhino for Mac is open, **drag the** ***.macrhi*** archive onto Rhino for Mac's icon in the **dock**; OR:
1. If Rhino for Mac is *not* currently open, **double-click the** ***.macrhi*** **archive** to launch and install the plugin...
   ![plugin_loaded]({{ site.baseurl }}/images/plugin_installer_mac_06.png)
1. Click **OK** then **Quit** and **Restart** Rhino.  Your plugin should load.

---

## Behind the Scenes
{: .toc-header }

The *.macrhi* extension is a file extension associated with the Rhino for Mac application (both *Rhinoceros.app* and *RhinoWIP.app*).  This extension denotes a "Rhino for Mac plugin installer."  Rhino for Mac knows that such files are actually .zip archives that need to be decompressed and copied into the user's Library folder at the appropriate location, specifically the *~/Library/Application Support/McNeel/Rhinoceros/MacPlugIns/* folder[^2].

When Rhino for Mac launches, it searches the contents of the

*~/Library/Application Support/McNeel/Rhinoceros/MacPlugIns/*

folder scanning the sub-folders looking for *.rhp* files.  When it finds such "file" (which are actually packages), Rhino for Mac attempts to load the assembly with the same name contained within this package.  If it cannot load the plugin, it will show an error at launch time.

For uninstallation/removal instructions, please see [Uninstalling Plugins (Mac)]({{ site.baseurl }}/guides/rhinocommon/uninstalling_plugins_mac).


#### User Library
{: .toc-subheader }

By default, the User Library folder is hidden from view.  

To make your Library visible in the Finder:

1. In **Finder**, navigate to your **Home** (*~*) folder.  You must be in your Home folder for this to work.
1. Press **Command-J** to bring up the **Finder View** options dialog...
![finder_view_options]({{ site.baseurl }}/images/finder_view_options.png)
1. Check the **Show Library Folder** check box.  Now your Library should show up in the view.  You may want to drag this folder to your Favorites area of the Finder sidebar for easy access later.

---

## Related topics
{: .toc-header }

- [Your First Plugin (Mac)]({{ site.baseurl }}/guides/rhinocommon/your_first_plugin_mac)
- [Your First Plugin (Cross-Platform)]({{ site.baseurl }}/guides/rhinocommon/your_first_plugin_crossplatform)
- [Uninstalling Plugins (Mac)]({{ site.baseurl }}/guides/rhinocommon/uninstalling_plugins_mac)

---

## Footnotes
{: .toc-header }

[^1]: OS X (and Unix) has a special kind of folder that masquerades as a file.  These are called "packages."  (Most apps found in */Applications/* are actually packages called "bundles").  You can access the contents in Finder by **right-clicking** on the package and selecting **Show Package Contents**.

[^2]: Do not confuse this path with */Library/Application Support/McNeel/Rhinoceros/*, which is the system-wide Library location.
