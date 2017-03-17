---
title: Loading Plugins at Startup
description: This guide discusses how to configure plugins to load at startup using C/C++.
authors: ['Dale Fugier']
author_contacts: ['dale']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Advanced']
origin: http://wiki.mcneel.com/developer/sdksamples/pluginloadtime
order: 1
keywords: ['rhino']
layout: toc-guide-page
---

 
## Problem

You would like your plugin to load at Rhino's startup.

## Solution

Rhino will load plugins in two ways:

1. When Needed (Default). Plugin will not be loaded when Rhino starts.  Plugin will be loaded when a plugin defined command is run, when a user selects a plugin defined file import/export type, or if a 3DM file has user data that was created by your plugin.
1. At Startup. Plugin is loaded when Rhino is loaded and initialized.

To set your plugin to load on startup, you need to override your plugin object's `CRhinoPlugIn::PlugInLoadTime()` virtual function and return the `CRhinoPlugIn::load_plugin_at_startup` enumerated value.  See *rhinoSdkPlugIn.h* for details.

## Sample

```cpp
// Description:
//    Called by Rhino when writing plug-in information to the registry.  This
//    information will be read the next time Rhino starts to identify properly
//    installed plug-ins.
CRhinoPlugIn::plugin_load_time CTestPlugIn::PlugInLoadTime()
{
  return CRhinoPlugIn::load_plugin_at_startup;
}
```

## Details

If you have already loaded your plugin using Rhino's plugin manager, when debugging for example, then you will need to either remove your plugin's registry key, which can be found here:

```
HKEY_LOCAL_MACHINE\SOFTWARE\McNeel\Rhinoceros\<version>\<rhino_build_date>\Plug-Ins\<your_plugin_guid>
```

<div class="bs-callout bs-callout-danger">
  <h4>WARNING</h4>
  <p>if you are running on a system with limited rights, with user-account control enabled for example, then there will be a corresponding key in HKEY_CURRENT_USER</p>
</div>

Or, you can just modify your plugin's "LoadMode" registry key value.  The available values for this key are as follows:

| Load mode      | | | Registry Value    | | | Description     |
| :------------- | | | :------------- | | | :------------- |
| load_plugin_when_needed      | | | 2 - REG_DWORD, Decimal       | | | Default. Load the first time a plugin command used     |
| load_plugin_at_startup      | | | 1 - REG_DWORD, Decimal       | | | Load when Rhino is loaded
    |

The reason this step is required is that the "LoadMode" Registry key value is only written the first time the plugin is loaded (when it is initially installed or registered).  This will not be an issue for customers of your plugin for the correct registry key value will be written the first time they load your plugin.
