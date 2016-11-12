---
title: Creating Zoo Plugins
description: This guide discusses how to create plugins for Zoo using C/C++
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Zoo']
origin: http://wiki.mcneel.com/developer/zoorhinoplugin
order: 1
keywords: ['Zoo', 'Plugin']
layout: toc-guide-page
TODO: 'needs to be compared to RhinoCommon version'
---

# {{ page.title }}

{% include byline.html %}

{{ page.description }}

## Overview

Zoo lets third party plugin developers add licensing support for their products to the Zoo.

The Rhino C/C++ SDK allows developers to write plugins for Rhino that use the Rhino license manager and obtain licenses from Zoo servers.

When a customer attempts to add a product license to the Zoo, the product's plugin is called to validate the user's request.  Upon validation, the plugin will return the product's licensing information back to the Zoo.  In turn, the Zoo will serialize, maintain, and distribute this license.

## Prerequisites

Rhino C/C++ plugins are MFC dynamic link libraries.  Thus, to create a plugin for Rhino, you will need one of the following development tools:

1. Microsoft Visual C++ 2005 (required for Rhino 5.0 32-bit)
1. Microsoft Visual C++ 2010 (required for Rhino 5.0 64-bit)
1. Rhino 5.0 C/C++ SDK

**NOTE**: Express Editions of Microsoft Visual Studio will not work, as they do not include MFC.

Also, all plugins that use the Zoo license system must be signed with an *Authenticode* certificate issued by *McNeel Plugin Security*.  These certificates are free, but must be requested by each developer.  Developers must agree to the *Terms of Use* before a certificate is issued.  For more information on plugin signing, see [Digitally Signing Plugins for Zoo]({{ site.baseurl }}/guides/rhinocommon/digitally-signing-plugins-for-zoo).

## Writing a Rhino Plugin

The general steps required to create a Rhino plugin are:

1. Make sure you have Zoo installed.
1. Make sure you have the Rhino installed.
1. Make sure you have the Rhino C/C++ SDK installed.
1. Launch Microsoft Visual Studio 2010.
1. Create a new project, in C/C++, based on the Rhino 5.0 Plugin project template.
1. Build your plugin.
1. Launch Rhino and use the *PlugInManager* command to install your plugin (to verify that it was built properly).

## Adding Licensing Support

After you have built and tested your basic plugin, you can add licensing support as follows:

1. Add a new *.cpp* file to your project.
1. In this *.cpp* file, declare a new class that is derived from `CRhinoLicenseValidator`.
1. Override the `CRhinoLicenseValidator::ProductBuildType` virtual function and return the build type of the license that your product requires.
1. Override and implement the `CRhinoLicenseValidator::ValidateProductKey` virtual function.  Rhino will call into this function whenever it needs your plugin to validate a license that is entered by a user, returned by the Rhino license manager (standalone node), or returned from a Zoo server (network node).  For details, see the sample Rhino C/C++ plugins in Related Topics below.
1. Create one (and only one) static instance of your object.
1. In your plugin's `CRhinoPlugIn::OnLoadPlugIn` member, call `CRhinoPlugIn::GetLicense` to get a license.
1. Build your plugin.
1. [Digitally sign your plugin]({{ site.baseurl }}/guides/rhinocommon/digitally-signing-plugins-for-zoo).
1. Launch Rhino and test your plugin.  When your plugin is loaded for the first time, you will be prompted to enter a license.

## Related Topics

- [Digitally Signing Plugins for Zoo]({{ site.baseurl }}/guides/rhinocommon/digitally-signing-plugins-for-zoo)
- [Sample Zoo Plugin Projects (on GitHub)](https://github.com/mcneel/Zoo5)
