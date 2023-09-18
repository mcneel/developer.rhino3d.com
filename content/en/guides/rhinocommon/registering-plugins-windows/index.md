+++
aliases = ["/5/guides/rhinocommon/registering-plugins-windows/", "/6/guides/rhinocommon/registering-plugins-windows/", "/7/guides/rhinocommon/registering-plugins-windows/", "/wip/guides/rhinocommon/registering-plugins-windows/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This guide provides instructions for registering plugins for Windows."
keywords = [ "RhinoCommon", "Registering", "Plugin" ]
languages = [ "C#", "C/C++" ]
sdk = [ "RhinoCommon", "C/C++" ]
title = "Registering Plugins (Windows)"
type = "guides"
weight = 1
override_last_modified = "2020-09-10T10:41:11Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/installingandregisteringaplugin"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++


## Overview

While a Rhino plugin can simply be distributed as a *.rhp* file, and loaded using Rhino's *PlugInManager* command, it is often necessary to install the plugin as part of a product installation process.  To install plugin from an installer, your installer will be required to access a number of entries in the Windows Registry.

While reading this article, it is helpful to use the standard Windows Registry editing tool, *REGEDIT.EXE*, to follow along and see how Rhino's Registry entries are structured.

## Finding the Rhino Registry Key

Rhino plugins are registered at the following location in the Windows Registry:

`HKEY_LOCAL_MACHINE\Software\McNeel\Rhinoceros\MajorVersion.0\Plug-ins`

Where `MajorVersion` is the major version of Rhino (e.g. 6, 7, 8).

## Registering Your Plugin

To register your plugin with Rhino, you will need to create a new Registry key at the above location.  The name of the Registry key will be your plugin's GUID, formatted as a string.  For example:

`HKEY_LOCAL_MACHINE\Software\McNeel\Rhinoceros\MajorVersion.0\Plug-ins\<your_plugin_guid>`

Under this new Registry key, create two new value names, ```Name``` and ```FileName``` that contain strings that identify your plugin's name and the full path to the *.rhp* file, respectively.  For example, if you had created a new plugin named *"MySamplePlugIn"*, the registry might look something like the following:

```
HKEY_LOCAL_MACHINE\SOFTWARE\McNeel\Rhinoceros\7.0\Plug-Ins\F3CF4A28-EA9E-4E08-BABA-5FC6645A5D72

Value:  Name
Type:   REG_SZ
Data:   MySamplePlugIn

Value:  FileName
Type:   REG_SZ
Data:   C:\Program Files\My Company\My Sample PlugIn\MySamplePlugIn.rhp
```

## Automatic Loading

Rhino will attempt to load your plugin the next time Rhino launches if the ```Name``` and ```FileName``` Registry values and data are present in your plugin's Registry key.  Rhino will briefly display a *"Preparing plugins for first use"* dialog if the plugin loads correctly.

When your plugin loads for the first time, the rest of the normal Registry keys/value pairs in your plugin's Registry key will be filled in.

## Other Useful Values

There are other useful key values that are found in the following locations depending on the Rhino version:

`HKEY_LOCAL_MACHINE\SOFTWARE\McNeel\Rhinoceros\MajorVersion.0\Install`

where...

- ```InstallPath``` contains the full path to the Rhino installation folder.
- ```Path``` contains the full path to the System folder under the Rhino folder.

## Hints

Look in the Registry with *REGEDIT.EXE* and confirm that existing plugins follow these conventions.

Use the right-click context menu in *REGEDIT.EXE* to access the "Copy Key Name" and "Rename" functions so you can get accurate copies of names and values in the Registry.

Test your installer to handle all of these situations:

1. No Rhino is installed on the computer.
2. Only the Rhino Evaluation or Beta editions are installed.
3. Rhino is too old to run your plugin.
4. Your plugin is already installed.
5. The user wants to uninstall your plugin and its Registry entries.
