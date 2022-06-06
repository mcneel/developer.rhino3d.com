+++
aliases = ["/5/guides/rhinocommon/creating-zoo-plugins/", "/6/guides/rhinocommon/creating-zoo-plugins/", "/7/guides/rhinocommon/creating-zoo-plugins/", "/wip/guides/rhinocommon/creating-zoo-plugins/"]
authors = [ "dale" ]
categories = [ "Zoo" ]
description = "This guide discusses how to create plugins for the LAN Zoo."
keywords = [ "Zoo", "Plugin" ]
languages = [ "C#" ]
sdk = [ "RhinoCommon" ]
title = "Creating LAN Zoo Plugins"
type = "guides"
weight = 2
override_last_modified = "2021-06-25T14:03:44Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/zooplugin"
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

The LAN Zoo allows third party plugin developers add licensing support for their products.

When a customer attempts to add a product license to the LAN Zoo, the product's plugin is called to validate the user's request. Upon validation, the plugin will return the product's licensing information back to the Zoo. In turn, the LAN Zoo will serialize, maintain, and distribute this license.

## Prerequisites

LAN Zoo plugins are .NET Framework 4.8 assemblies. To create a plugins for the LAN Zoo, you need one of the following development tools:

1. Microsoft Visual C#.
2. Microsoft Visual Basic .NET.

Also, all plugins that use the LAN Zoo license system must be signed with an *Authenticode* certificate issued by *McNeel Plugin Security*.  These certificates are free, but must be requested by each developer. Developers must agree to the *Terms of Use* before a certificate is issued. For more information on plugin signing, see [Digitally Signing Plugins for LAN Zoo](/guides/rhinocommon/digitally-signing-plugins-for-zoo).

## Writing a LAN Zoo Plugin

The general steps required to create a Zoo plugin are:

1. Make sure you have the LAN Zoo installed.
2. Launch Microsoft Visual Studio.
3. Create a new *Class Library* project using either Visual C# or Visual Basic .NET.
4. Add a reference to *ZooPlugin.dll*, which is found in the LAN Zoo installation folder. Make sure to set the reference's *Copy Local* property to `False`.
5. Create a new public class that inherits from the `IZooPlugin3` interface.
6. Implement the interface members.  (For detailed information about the interface members, see the sample LAN Zoo plugin listed below.)
7. Build your plugin.
8. [Digitally sign your plugin](/guides/rhinocommon/digitally-signing-plugins-for-zoo).

## Installing a LAN Zoo Plugin

Once you have built your LAN Zoo plugin, you can install it and test it:

1. Run *ZooAdmin.Wpf.exe* and make sure the LAN Zoo licensing service has stopped.
2. Copy your plugin assembly (*.dll*) and any dependent support libraries to the lan Zoo's plugin folder (i.e. *C:\Program Files\Zoo 7\Plugins*).
3. Restart the Zoo license service.
4. When the service has restarted, click the *Add License* button. Your product should be one of the available products for which to add a license.

## Related Topics

- [Digitally Signing Plugins for LAN Zoo](/guides/rhinocommon/digitally-signing-plugins-for-zoo)
- [Creating Plugins that use the LAN Zoo (RhinoCommon)](/guides/rhinocommon/rhinocommon-zoo-plugins)
- [Creating Plugins that use the LAN Zoo (C/C++)](/guides/cpp/creating-zoo-plugins)
- [Sample LAN Zoo Plugin Projects (on GitHub)](https://github.com/mcneel/rhino-developer-samples/tree/6/zoo)

