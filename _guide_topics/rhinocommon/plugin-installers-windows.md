---
title: Plugin Installers (Windows)
description: This guide explains how to create a plugin installer for Rhino for Windows.
authors: ['brian_gillespie', 'will_pearson']
sdk: ['RhinoCommon', 'C/C++']
languages: ['C#', 'C/C++']
platforms: ['Windows']
categories: ['Getting Started']
origin: http://wiki.mcneel.com/developer/rhinoinstallerengine/authoring
order: 6
keywords: ['first', 'RhinoCommon', 'Plugin', 'installing', 'c', 'C/C++', 'plugin', 'installer']
layout: toc-guide-page
TODO: Also port from http://wiki.mcneel.com/developer/rhinoinstallerengine/cpp
---

<div class="alert alert-info" role="alert">
<strong>Note</strong>: This process is the same for both C/C++ and RhinoCommon plug-ins!
</div>


## Overview

Creating a plugin installer is very easy.  You simply add your compiled plugin to a zip archive and change the extension from *.zip* to *.rhi*.  Once this is done, you can double-click the archive and the [Rhino Installer Engine]({{ site.baseurl }}/guides/general/rhino-installer-engine) will begin to install your plugin.  That's all there is to it!

<div class="alert alert-info" role="alert">
<strong>Note:</strong> This is intended to be a quickstart guide. For a more general overview please see the <a href="{{ site.baseurl }}/guides/general/rhino-installer-engine">Rhino Installer Engine</a> guide.
</div>

## An Example

Imagine you have a plugin and want to support multiple versions of Rhino.  For example, you want to:

- Install the latest version of the plugin for Rhino WIP
- Install an older version of the plugin for 64-bit Rhino 5
- Install yet another version of the plugin for 32-bit Rhino 5
- Include a custom toolbar file (e.g. *MyToolbar.rui*)

This is possible. You need to:

1. Create an "installer image" folder. In this example, the folder is the name of the product – _Marmoset_. This folder will contain only the files you want to install on the user's system.

        Marmoset/
        ├── Rhino 6/
        │   ├── Marmoset.rhp
        │   └── required_wip.dll
        ├── Rhino 5.0/
        │   ├── x86/
        │   │   ├── Marmoset.rhp
        │   │   └── required_v5_x86.dll
        │   └── x64/
        │       ├── Marmoset.rhp
        │       └── required_v5_x86.dll
        ├── Marmoset.rui
        ├── Marmoset.chm
        └── README.txt


1. Copy the appropriate files into the folders[^1].  Note that all three versions of the plugin can have the same name, so long as they are in different folders.
1. Add all the files inside the "installer image" folder to a new ZIP[^2] archive
1. Change the extension from *.zip* to *.rhi*

## Everything but the kitchen sink

Because the Rhino Plugin Installer Engine unzips your *.rhi* file into a directory specific to your plugin, you can include anything you want: help files, documentation, etc.  These files will end up inside your plugin directory; The Rhino Installer Engine cannot be used to install files to other parts of the hard drive.

---

## Related topics

- [Rhino Installer Engine]({{ site.baseurl }}/guides/general/rhino-installer-engine)
- [Plugin Installers (Mac)]({{ site.baseurl }}/guides/rhinocommon/plugin-installers-mac)

---

## Footnotes

[^1]: Folder names are not important; the *.rhp* files themselves are inspected to determine for which versions of Rhino they will be installed.
[^2]: Other compression algorithms are not supported.
