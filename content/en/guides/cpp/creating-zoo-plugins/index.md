+++
authors = [ "dale" ]
categories = [ "Zoo" ]
description = "This guide discusses how to create C/C++ plugins that can obtain licenses from the LAN Zoo."
keywords = [ "Zoo", "Plugin" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Creating Plugins that use the LAN Zoo"
type = "guides"
weight = 2

[admin]
TODO = "needs to be compared to RhinoCommon version"
origin = "http://wiki.mcneel.com/developer/zoorhinoplugin"
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

The LAN Zoo supports 3rd party plugins. The Rhino C/C++ SDK allows developers to write plugins for Rhino that use the Rhino license manager and obtain licenses from LAN Zoo servers.

When a customer attempts to add a product license to the LAN Zoo, the product's plugin is called to validate the user's request.  Upon validation, the plugin will return the product's licensing information back to the LAN Zoo.  In turn, the LAN Zoo will serialize, maintain, and distribute this license.

## Prerequisites

It is presumed you already have the necessary tools installed and are ready to go.  If you are not there yet, see [Installing Tools (Windows)](/guides/cpp/installing-tools-windows).

Also, all plugins that use the LAN Zoo license system must be signed with an Authenticode certificate issued by McNeel Plugin Security.  These certificates are free, but must be requested by each developer.  Developers must agree to the Terms of Use before a certificate is issued.  For more information on plugin signing, see [Digitally Signing Plugins for LAN Zoo](/guides/rhinocommon/digitally-signing-plugins-for-zoo).

It is also presumed you have a C/C++ plugin you wish to add license support to. See the [Your First Plugin (Windows)](http://developer.rhino3d.com/guides/cpp/your-first-plugin-windows/) guide for instructions.

## Adding Licensing Support

After you have built and tested your basic plugin, you can add licensing support as follows:

#### Step-by-Step

1. Add a new *.cpp* file to your project.
2. In this *.cpp* file, declare a new class that is derived from `CRhinoLicenseValidator`.
3. Override the `CRhinoLicenseValidator::ProductBuildType` virtual function and return the build type of the license that your product requires.
4. Override and implement the `CRhinoLicenseValidator::VerifyLicenseKey` virtual function.  Rhino will call into this function whenever it needs your plugin to validate a license that is entered by a user, returned by the Rhino license manager (standalone node), or returned from a LAN Zoo server (network node).
5. Override and implement the `CRhinoLicenseValidator::VerifyPreviousVersionLicense` virtual function.  Rhino will call into this function if a license key from a previous version of your product is required to validate the license key being verified.
6. Override and implement the `CRhinoLicenseValidator::OnLeaseChanged` virtual function.  Rhino will call into this function if your product supports Rhino Accounts. When Rhino Accounts gets a new lease, this function is called. 
7. Create one (and only one) static instance of your `CRhinoLicenseValidator`-derived object.
8. In your plugin's `CRhinoPlugIn::OnLoadPlugIn` member, call `CRhinoPlugIn::SetLicenseCapabilities` and pass it the required user interface parameters.
9. In your plugin's `CRhinoPlugIn::OnLoadPlugIn` member, `CRhinoPlugIn::GetLicense` to get a license. 
10. Build your plugin.
11. [Digitally sign your plugin](/guides/rhinocommon/digitally-signing-plugins-for-zoo).
12. Launch Rhino and test your plugin.  When your plugin is loaded for the first time, you will be prompted to enter a license.

## Related Topics

- [Creating LAN Zoo Plugins](/guides/rhinocommon/creating-zoo-plugins)
- [Digitally Signing Plugins for LAN Zoo](/guides/rhinocommon/digitally-signing-plugins-for-zoo)
- [Sample C/C++ plugin project (on GitHub)](https://github.com/mcneel/rhino-developer-samples/tree/6/cpp/SampleWithLicensing)

