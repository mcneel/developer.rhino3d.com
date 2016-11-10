---
title: Plugin Installers (Windows)
description: This guide provides an overview of how plugin installers are created on Windows.
authors: ['Brian Gillespie']
author_contacts: ['brian']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Getting Started']
origin: http://wiki.mcneel.com/developer/rhinoinstallerengine/authoring
order: 3
keywords: ['c', 'C/C++', 'plugin', 'installer']
layout: toc-guide-page
TODO: 'needs porting - see additional TODO'
---


# {{ page.title }}

{% include byline.html %}

{{ page.description }}

## Overview

Creating a plugin installer is easy.  The basic steps to "authoring" a plugin installer are as follows...

1. Compile your plugin.
1. Add your plugin to a zip archive.
1. Change the extension from *.zip* to *.rhi* (Rhino Installer Package).

## In Depth

In this in-depth example, we have the goals of:

- Install an older version of the plugin for Rhino 4
- Install a new version of the plugin for 32-bit Rhino 5
- Install a plugin for 64-bit Rhino 5
- Include a *MyToolbar.rhp* custom toolbar file.

### Organize the Files

Create a "Installer Image" folder (In this example, the folder is the name of the product: *Marmoset*.)  This folder will contain only the files you want to install on the user's system:

```cmd
Marmoset\
  Rhino 4.0\
    Marmoset.rhp
  Rhino 5.0\
    x86\
      Marmoset.rhp
    x64\
      Marmoset.rhp
  Common\
    Marmoset.rui
    Marmoset.chm
```

### Create the RHI file

1. Copy the appropriate files into the folders.  Note that all three versions of the plugin can have the same name, so long as they are in different folders.
1. Compress the three files using zip compression (currently other compression algorithms are not supported).
1. Change the extension from *.zip* to *.rhi*

### Everything but the kitchen sink

Because the Rhino Plugin Installer Engine unzips your *.rhi* file into a directory specific to your plugin, you can include anything you want: help files, documentation, etc.  But you can only install things inside your own plugin directory. So long as your *.rhi* file contains sub folders, everything should install correctly.

### Running the Installer

1. Double-click the *.rhi* file
1. Follow the steps in the Rhino Installation Wizard to install the plugin.

TODO: Also port from: http://wiki.mcneel.com/developer/rhinoinstallerengine/cpp
