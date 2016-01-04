---
title: RhinoCommon Zoo Plugins
description: unset
author: dale@mcneel.com
apis: ['Zoo', 'RhinoCommon']
languages: ['C#']
platforms: ['Windows']
categories: ['Advanced']
origin: http://wiki.mcneel.com/developer/zoorhinocommonplugin
order: 3
keywords: ['Zoo', 'Plugin']
layout: toc-guide-page
---

# RhinoCommon Zoo Plugins

This guide discusses how to create Rhino plugins, based on RhinoCommon, that can obtain licenses from the Rhino license manager and the Zoo.

## Overview

Zoo 5.0 allows 3rd party plugin developers to add licensing support for their products to the Zoo.  RhinoCommon allows developers to write plugins for Rhino that use the Rhino license manager and obtain licenses from Zoo servers.

## Prerequisites

RhinoCommon plugins are .NET Framework 4.0 assemblies. Thus, to create a RhinoCommon plugin for Rhino 5, you will need one of the following development tools:

- Microsoft Visual C# 2010
- Microsoft Visual Basic .NET 2010
- RhinoCommon

Also, all Rhino plugins that use the Rhino license manager to access the Zoo must be signed with an Authenticode certificate issued by McNeel Plugin Security.  These certificates are free, but must be requested by each developer.  Developers must agree to the Terms of Use before a certificate is issued. For more information on plug-in signing, see the [Digitally Signing Plugins for Zoo]({{ site.baseurl }}/guides/zoo/digitally_signing_plugins_for_zoo) guide.

It is presumed you have a RhinoCommon plugin you wish to add license support to.  See the [Your First Plugin (Windows)]({{ site.baseurl }}/guides/rhinocommon/your_first_plugin_windows/) guide for instructions.

## Add License Support

After you have built and tested your basic plugin, you can add licensing support as follows:

#### Step-by-Step
1. In your plugin's `Rhino.PlugIns` inherited class, create a new method with the same signature as the `Rhino.PlugIns.ValidateProductKeyDelegate` delegate.  Rhino will call into this function whenever it needs your plugin to validate a license that is entered by a user, returned by the Rhino license manager (standalone node), or returned from a Zoo server (network node).  For details, see the [Zoo 5 Developer Samples](https://github.com/mcneel/Zoo5).
1. In your plugin's `OnLoad` method, call `Rhino.PlugIns.GetLicense` and pass it the build type of the license required by your product, and your delegate function.
1. Build your plugin.
1. [Digitally sign your plugin]({{ site.baseurl }}/guides/zoo/digitally_signing_plugins_for_zoo).
1. Launch Rhino and test your plugin.  When your plugin is loaded for the first time, you will be prompted to enter a license...

![License Not Found]({{ site.baseurl }}/images/rhinocommon_zoo_plugins_01.png)

## Managing Licenses

Rhino plugins that use the Rhino license manager appear in the Licenses page of the Options dialog.  Here, the user is allowed to view and manage the license...

![License Manager]({{ site.baseurl }}/images/rhinocommon_zoo_plugins_02.png)

---

## Related Topics

- [Creating Plugins for Zoo]({{ site.baseurl }}/guides/zoo/creating_plugins_for_zoo)
- [Digitally Signing Plugins for Zoo]({{ site.baseurl }}/guides/zoo/digitally_signing_plugins_for_zoo)
- [Zoo 5 Developer Samples](https://github.com/mcneel/Zoo5)
