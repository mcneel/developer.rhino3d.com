---
title: Plugin Installers (Windows)
description: This guide explains how to create a plugin installer for Rhino for Windows.
authors: ['Brian Gillespie']
author_contacts: ['brian']
sdk: ['RhinoCommon']
languages: ['C#']
platforms: ['Windows']
categories: ['Getting Started']
origin: http://wiki.mcneel.com/developer/rhinoinstallerengine/authoring
order: 6
keywords: ['first', 'RhinoCommon', 'Plugin', 'installing']
layout: toc-guide-page
TODO: 'needs updating and/or review.'
---


## Overview

Creating a plugin installer is very easy.  You simply add your compiled plugin to a zip archive and change the extension from *.zip* to *.rhi*.  Once this is done, you can double-click the archive and the [Rhino Installer Engine]({{ site.baseurl }}/guides/general/rhino-installer-engine) will begin to install your plugin.  That's all there is to it!

## An Example

Imagine you have a more complex plugin and want to support multiple versions of Rhino.  For example, you want to:

- Install an older version of the plugin for Rhino 4
- Install a new version of the plugin for Rhino 5
- Include a custom toolbar file (e.g. *MyToolbar.rui*)

This is possible.  You need to...

1. Create a "Installer Image" folder (In this example, the folder is the name of the product: Marmoset.)  This folder will contain only the files you want to install on the user's system.

        Marmoset/
        ├── Rhino 4.0/
        │   ├── Marmoset.rhp
        │   └── required_v4.dll
        ├── Rhino 5.0/
        │   ├── Marmoset.rhp
        │   └── required_v5.dll
        ├── Marmoset.rui
        └── Marmoset.chm


1. Copy the appropriate files into the folders.  Note that both versions of the plugin can have the same name, so long as they are in different folders.  The folder structure itself is not important (see "[Rhino Installer Engine]({{ site.baseurl }}/guides/general/rhino-installer-engine)" for more).
1. Compress the three plugin versions and any additional files you wish to distribute using zip[^1] compression.
1. Change the extension from *.zip* to *.rhi*

## Everything but the kitchen sink

Because the Rhino Plugin Installer Engine unzips your *.rhi* file into a directory specific to your plugin, you can include anything you want: help files, documentation, etc.  These files will end up inside your plugin directory; The Rhino Installer Engine cannot be used to install files to other parts of the hard drive.

---

## Related topics

- [Rhino Installer Engine]({{ site.baseurl }}/guides/general/rhino-installer-engine)



[^1]: Other compression algorithms are not supported.
