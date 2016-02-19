---
title: Plugin Installers (Windows)
description: This guide explains how to create a plugin installer for Rhino for Windows.
author: brian@mcneel.com
apis: ['RhinoCommon']
languages: ['C#']
platforms: ['Windows']
categories: ['GettingStarted']
origin: http://wiki.mcneel.com/developer/rhinoinstallerengine/authoring
order: 6
keywords: ['first', 'RhinoCommon', 'Plugin', 'installing']
layout: toc-guide-page
TODO: 'needs updating and/or review.'
---


# Plugin Installers (Windows)

{{ page.description }}

## Overview

Creating a plugin installer is very easy.  You simply add your compiled plugin to a zip archive and change the extension from *.zip* to *.rhi*.  Once this is done, you can double-click the archive and the [Rhino Installer Engine]({{ site.baseurl }}/guides/general/rhino_installer_engine) will begin to install your plugin.  That's all there is to it!

## A Complex Example

Imagine you have a more complex plugin and want to support multiple versions of Rhino.  For example, you want to:

- Install an older version of the plugin for Rhino 4.0
- Install a new version of the plugin for 32-bit Rhino 5
- Install a plugin for 64-bit Rhino 5
- Include a *MyToolbar.rhp* custom toolbar file

This is possible.  You need to ...

1. *Organize the files*:  Create a "Installer Image" folder (In this example, the folder is the name of the product: Marmoset.)  This folder will contain only the files you want to install on the user's system...

    - *Marmoset*\\
        - *Rhino 4.0*\\
            - *Marmoset.rhp*
        - *Rhino 5.0*\\
            - *x86*\\
                - *Marmoset.rhp*
            - *x64*\\
                - *Marmoset.rhp*
        - *Common*\\
            - *Marmoset.rui*
            - *Marmoset.chm*

1. *Create the RHI file*: Copy the appropriate files into the folders.  Note that all three versions of the plugin can have the same name, so long as they are in different folders.
1. Compress the three files using zip compression (currently other compression algorithms are not supported).
1. Change the extension from *.zip* to *.rhi*

## Everything but the kitchen sink

Because the Rhino Plugin Installer Engine unzips your *.rhi* file into a directory specific to your plugin, you can include anything you want: help files, documentation, etc.  But you can only install things inside your own *plugin* directory.  So long as your *.rhi* file contains sub folders, everything will install correctly.

---

## Related topics

- [Rhino Installer Engine]({{ site.baseurl }}/guides/general/rhino_installer_engine)
