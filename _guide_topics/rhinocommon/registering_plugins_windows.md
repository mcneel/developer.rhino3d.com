---
title: Registering Plugins (Windows)
description: This guide provides instructions for registering plugins for Windows.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['RhinoCommon', 'C/C++']
languages: ['C#', 'C/C++']
platforms: ['Windows']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/installingandregisteringaplugin
order: 1
keywords: ['RhinoCommon', 'Registering', 'Plugin']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## Overview

While a Rhino plugin can simply be distributed as an *rhp* file, and loaded using Rhino's *PlugInManager* command, it is often necessary to install the plugin as part of a product installation process.  To install plugin from an installer, your installer will be required to access a number of entries in the Windows Registry.

While reading this article, it is helpful to use the standard Windows Registry editing tool, *REGEDIT.EXE*, to follow along and see how Rhino's Registry entries are structured.

## Finding the Rhino Registry Key

Rhino plugins are registered in the following locations in the Windows Registry:

### On 32-bit Windows

Rhino 5 32-bit:

`HKEY_LOCAL_MACHINE\Software\McNeel\Rhinoceros\5.0\Plug-ins`

### On 64-bit Windows

Rhino 5 64-bit:

`HKEY_LOCAL_MACHINE\Software\McNeel\Rhinoceros\5.0x64\Plug-ins`

Rhino 5 32-bit:

`HKEY_LOCAL_MACHINE\Software\Wow6432Node\McNeel\Rhinoceros\5.0\Plug-ins`

## Registering Your Plugin

To register your plugin with Rhino, you will need to create a new Registry key in the following locations depending on the Rhino version.  The name of the Registry key will be your plugin's GUID, formatted as a string.  For example:

### On 32-bit Windows

Rhino 5 32-bit:

`HKEY_LOCAL_MACHINE\SOFTWARE\McNeel\Rhinoceros\5.0\Plug-ins\<your_plugin_guid>`

### On 64-bit Windows

Rhino 5 64-bit:

`HKEY_LOCAL_MACHINE\Software\McNeel\Rhinoceros\5.0x64\Plug-ins\<your_plugin_guid>`

Rhino 5 32-bit:

`HKEY_LOCAL_MACHINE\Software\Wow6432Node\McNeel\Rhinoceros\5.0\Plug-ins\<your_plugin_guid>`

Under this new Registry key, create two new value names, *Name* and *FileName* that contain strings that identify your plugin's name and the full path to the *.rhp* file, respectively.  For example, if I had created a new plugin named *"FooBar"* that I has installed in Rhino's plugins folder, the registry would look like the following:

### On 32-bit Windows

Rhino 5 32-bit:

```
HKEY_LOCAL_MACHINE\SOFTWARE\McNeel\Rhinoceros\5.0\Plug-Ins\F3CF4A28-EA9E-4E08-BABA-5FC6645A5D72

Value:  Name
Type:   REG_SZ
Data:   FooBar

Value:  FileName
Type:   REG_SZ
Data:   C:\Program Files\Rhinoceros 5\Plug-Ins\FooBar.rhp
```

### On 64-bit Windows

Rhino 5 64-bit:

```
HKEY_LOCAL_MACHINE\Software\McNeel\Rhinoceros\5.0x64\Plug-ins\F3CF4A28-EA9E-4E08-BABA-5FC6645A5D72

Value:  Name
Type:   REG_SZ
Data:   FooBar

Value:  FileName
Type:   REG_SZ
Data:   C:\Program Files\Rhinoceros 5 (64-Bit)\Plug-Ins\FooBar.rhp
```

Rhino 5 32-bit:

```
HKEY_LOCAL_MACHINE\Software\Wow6432Node\McNeel\Rhinoceros\5.0\Plug-ins\F3CF4A28-EA9E-4E08-BABA-5FC6645A5D72

Value:  Name
Type:   REG_SZ
Data:   FooBar

Value:  FileName
Type:   REG_SZ
Data:   C:\Program Files (x86)\Rhinoceros 5\Plug-Ins\FooBar.rhp
```

## Automatic Loading

Rhino will attempt to load your plugin the next time Rhino launches if the *Name* and *FileName* Registry values and data are present in your plugin's Registry key.  Rhino will briefly display a *Preparing plugins for first use* dialog if the plugin loads correctly.

When your plugin loads for the first time, the rest of the normal Registry keys/value pairs in your plugin's Registry key will be filled in.

## Other Useful Values

There are other useful key values that are found in the following locations depending on the Rhino version:

`HKEY_LOCAL_MACHINE\SOFTWARE\McNeel\Rhinoceros\5.0\Install`

where...

- *InstallPath* contains the full path to the Rhino installation folder.
- *Path* contains the full path to the System folder under the Rhino folder.

## Hints

Look in the Registry with *REGEDIT.EXE* and confirm that existing plugins follow these conventions.

Use the right-click context menu in *REGEDIT.EXE* to access the "Copy Key Name" and "Rename" functions so you can get accurate copies of names and values in the Registry.

Test your installer to handle all of these situations:

1. No Rhino is installed on the computer.
1. Only the Rhino Evaluation or Beta editions are installed.
1. Rhino is too old to run your plugin.
1. Your plugin is already installed.
1. The user wants to uninstall your plugin and its Registry entries.
