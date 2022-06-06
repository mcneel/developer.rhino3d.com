+++
aliases = ["/5/guides/rhinocommon/plugin-installers-mac/", "/6/guides/rhinocommon/plugin-installers-mac/", "/7/guides/rhinocommon/plugin-installers-mac/", "/wip/guides/rhinocommon/plugin-installers-mac/"]
authors = [ "dan" ]
categories = [ "Getting Started" ]
description = "This guide explains how to create a plugin installer for Rhino for Mac."
keywords = [ "first", "RhinoCommon", "Plugin", "installing" ]
languages = [ "C#" ]
sdk = [ "RhinoCommon" ]
title = "Plugin Installers (Mac)"
type = "guides"
weight = 6
override_last_modified = "2021-09-03T08:26:49Z"

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Mac" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

{{< call-out "warning" "Warning" >}}
⚠️ The .macrhi format is no longer in active development. Please see the <a class="alert-link" href="/guides/yak/creating-a-rhino-plugin-package/">Package Manager</a> instead.
{{< /call-out >}}

It is presumed you have a plugin that successfully builds and runs already.  If you are not there yet, see [Your First Plugin (Mac)](/guides/rhinocommon/your-first-plugin-mac).

## Overview

Rhino for Mac does not (yet) have a Plugin Manager.  However, installing plugins is very easy.  You simply rename your plugin's containing *folder* with an special extension (*.rhp*), compress the folder, and change the extension from *.rhp.zip* to *.macrhi*.  Once this is done, you can double-click the archive and Rhino will launch and install the plugin.  You can also drag the *.macrhi* onto the dock icon of a running instance of Rhino and it will install the plugin as well.  You will, in any case, need to Quit an Restart Rhino for the plugin to activate.

## Step-by-Step

1. *Locate* your plugin folder in *Finder*.  Let's imagine our plugin is called *HelloRhinoCommon* and we have built it for *Release*...
![Find Plugin In Finder](/images/plugin-installer-mac-01.png)
1. *Single-click the name* your plugin's *Release* (or *Debug*) folder to *Rename* it.  The new name should be your plugin assembly with a *.rhp* suffix.  For example, if your plugin is called *HelloRhinoCommon*, rename the folder that contains this file *HelloRhinoCommon.rhp*...
1. You will be prompted to confirm this change.  Click the "**Add**" button:
![Click Add](/images/plugin-installer-mac-02.png)
1. The icon of the folder[^1] should now look like this...
![New Icon](/images/plugin-installer-mac-03.png)
1. *Archive* the plugin *folder*.  *Right-click* (option-click) the plugin *.rhp* *folder* you created in the previous step and select "*Compress* (your plugin name)."  This creates a zip archive of the contents of the folder.
1. *Single-click the name* of the new archive you created in step 5.  This allows you *to rename* the archive.
1. Change the *extension* from *.rhp.zip* to *.macrhi*.  
1. You will be prompted to confirm this change.  Select the "*Use .macrhi*" button:
![Use rhi Extension](/images/plugin-installer-mac-04.png)
1. Notice that *the icon changes* from a zip archive to a Rhino RHI:
![use_macrhi_confirm](/images/plugin-installer-mac-05.png)
1. If Rhino for Mac is open, *drag the* *.macrhi* archive onto Rhino for Mac's icon in the *dock*; OR:
1. If Rhino for Mac is *not* currently open, *double-click the .macrhi archive* to launch and install the plugin...
   ![plugin_loaded](/images/plugin-installer-mac-06.png)
1. Click *OK* then *Quit* and *Restart* Rhino.  Your plugin should load.

## Behind the Scenes

The *.macrhi* extension is a file extension associated with the Rhino for Mac application (both *Rhinoceros.app* and *RhinoWIP.app*).  This extension denotes a "Rhino for Mac plugin installer."  Rhino for Mac knows that such files are actually .zip archives that need to be decompressed and copied into the user's Library folder at the appropriate location, specifically the *~/Library/Application Support/McNeel/Rhinoceros/MacPlugIns/* folder[^2].

When Rhino for Mac launches, it searches the contents of the

*~/Library/Application Support/McNeel/Rhinoceros/MacPlugIns/*

folder scanning the sub-folders looking for *.rhp* files.  When it finds such "file" (which are actually packages), Rhino for Mac attempts to load the assembly with the same name contained within this package.  If it cannot load the plugin, it will show an error at launch time.

For uninstallation/removal instructions, please see [Uninstalling Plugins (Mac)](/guides/rhinocommon/uninstalling-plugins-mac).

#### User Library

By default, the User Library folder is hidden from view.  

To make your Library visible in the Finder:

1. In *Finder*, navigate to your *Home* (*~*) folder.  You must be in your Home folder for this to work.
1. Press <kbd>Command</kbd>+<kbd>J</kbd> to bring up the *Finder View* options dialog...
![finder_view_options](/images/finder-view-options.png)
1. Check the *Show Library Folder* check box.  Now your Library should show up in the view.  You may want to drag this folder to your Favorites area of the Finder sidebar for easy access later.

## Related topics

- [Your First Plugin (Mac)](/guides/rhinocommon/your-first-plugin-mac)
- [Your First Plugin (Cross-Platform)](/guides/rhinocommon/your-first-plugin-crossplatform)
- [Uninstalling Plugins (Mac)](/guides/rhinocommon/uninstalling-plugins-mac)
- [Plugin Installers (Windows)](/guides/rhinocommon/plugin-installers-windows)

**Footnotes**

[^1]: macOS (and Unix) has a special kind of folder that masquerades as a file.  These are called "packages."  (Most apps found in */Applications/* are actually packages called "bundles").  You can access the contents in Finder by *right-clicking* on the package and selecting *Show Package Contents*.

[^2]: Do not confuse this path with */Library/Application Support/McNeel/Rhinoceros/*, which is the system-wide Library location.
