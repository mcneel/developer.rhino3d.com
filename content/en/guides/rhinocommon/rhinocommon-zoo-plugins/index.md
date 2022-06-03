+++
authors = [ "dale" ]
categories = [ "Zoo" ]
description = "This guide discusses how to create RhinoCommon plugins that can obtain licenses the LAN Zoo."
keywords = [ "Zoo", "Plugin" ]
languages = [ "C#" ]
sdk = [ "RhinoCommon" ]
title = "Creating Plugins that use the LAN Zoo"
type = "guides"
weight = 3
override_last_modified = "2020-12-10T10:39:09Z"

[admin]
TODO = "needs to be compared with creating-zoo-plugins"
origin = "http://wiki.mcneel.com/developer/zoorhinocommonplugin"
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

The LAN Zoo supports 3rd party plugins. RhinoCommon allows developers to write plugins for Rhino that use the Rhino license manager and obtain licenses from LAN Zoo servers.

When a customer attempts to add a product license to the LAN Zoo, the product's plugin is called to validate the user's request. Upon validation, the plugin will return the product's licensing information back to the LAN Zoo. In turn, the LAN Zoo will serialize, maintain, and distribute this license.

## Prerequisites

It is presumed you already have the necessary tools installed and are ready to go.  If you are not there yet, see [Installing Tools (Windows)](/guides/rhinocommon/installing-tools-windows).

Also, all plugins that use the LAN Zoo license system must be signed with an Authenticode certificate issued by McNeel Plugin Security.  These certificates are free, but must be requested by each developer.  Developers must agree to the Terms of Use before a certificate is issued.  For more information on plugin signing, see [Digitally Signing Plugins for LAN Zoo](/guides/rhinocommon/digitally-signing-plugins-for-zoo).

It is also presumed you have a RhinoCommon plugin you wish to add license support to.  See the [Your First Plugin (Windows)](/guides/rhinocommon/your-first-plugin-windows/) guide for instructions.

## Add License Support

After you have built and tested your basic plugin, you can add licensing support as follows:

#### Step-by-Step
1. In your plugin's `Rhino.PlugIns.PlugIn` inherited class, create a new method with the same signature as the `Rhino.PlugIns.ValidateProductKeyDelegate` delegate.  Rhino will call into this function whenever it needs your plugin to validate a license that is entered by a user, returned by the Rhino license manager (standalone node), or returned from a LAN Zoo server (network node).
2. In your plugin's `Rhino.PlugIns.PlugIn` inherited class, create a new method with the same signature as the `Rhino.PlugIns.OnLeaseChangedDelegate` delegate.  Rhino will call into this function if your product supports Rhino Accounts. When Rhino Accounts gets a new lease, this function is called. 
3. In your plugin's `Rhino.PlugIns.PlugIn.OnLoad` override, call `Rhino.PlugIns.GetLicense` and pass it your licenses's capabilities (enum), a text mask to assist the user in entering a license, and your two delegate functions.
4. Build your plugin.
5. [Digitally sign your plugin](/guides/rhinocommon/digitally-signing-plugins-for-zoo).
6. Launch Rhino and test your plugin.  When your plugin is loaded for the first time, you will be prompted to enter a license...

## Related Topics

- [Creating LAN Zoo Plugins](/guides/rhinocommon/creating-zoo-plugins)
- [Digitally Signing Plugins for LAN Zoo](/guides/rhinocommon/digitally-signing-plugins-for-zoo)
- [Sample RhinoCommon plugin project (GitHub)](https://github.com/mcneel/rhino-developer-samples/tree/6/rhinocommon/cs/SampleCsWithLicense)


