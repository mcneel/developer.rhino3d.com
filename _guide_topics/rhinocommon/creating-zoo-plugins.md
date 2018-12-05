---
title: Creating Zoo Plugins
description: This guide discusses how to create plugins for Zoo.
authors: ['dale_fugier']
author_contacts: ['dale']
sdk: ['RhinoCommon']
languages: ['C#']
platforms: ['Windows']
categories: ['Zoo']
origin: http://wiki.mcneel.com/developer/zooplugin
order: 2
keywords: ['Zoo', 'Plugin']
layout: toc-guide-page
---


## Overview

Zoo lets third party plugin developers add licensing support for their products to the Zoo.

When a customer attempts to add a product license to the Zoo, the product's plugin is called to validate the user's request.  Upon validation, the plugin will return the product's licensing information back to the Zoo.  In turn, the Zoo will serialize, maintain, and distribute this license.

## Prerequisites

Zoo plugins are .NET Framework 4.5 assemblies.  To create a plugins for Zoo, you need one of the following development tools:

1. Microsoft Visual C# 2017.
2. Microsoft Visual Basic .NET 2017.

Also, all plugins that use the Zoo license system must be signed with an *Authenticode* certificate issued by *McNeel Plugin Security*.  These certificates are free, but must be requested by each developer.  Developers must agree to the *Terms of Use* before a certificate is issued.  For more information on plugin signing, see [Digitally Signing Plugins for Zoo]({{ site.baseurl }}/guides/rhinocommon/digitally-signing-plugins-for-zoo).

## Writing a Zoo Plugin

The general steps required to create a Zoo plugin are:

1. Make sure you have Zoo installed.
2. Launch Microsoft Visual Studio.
3. Create a new *Class Library* project using either Visual C# or Visual Basic .NET.
4. Add a reference to *ZooPlugin.dll*, which is found in the Zoo installation folder.  Make sure to set the reference's *Copy Local* property to `False`.
5. Create a new public class that inherits from the `IZooPlugin3` interface.
6. Implement the interface members.  (For detailed information about the interface members, see the sample Zoo plugin listed below.)
7. Build your plugin.
8. [Digitally sign your plugin]({{ site.baseurl }}/guides/rhinocommon/digitally-signing-plugins-for-zoo).

## Installing a Zoo Plugin

Once you have built your Zoo plugin, you can install it and test it:

1. Run *ZooAdmin.exe* and make sure the Zoo licensing service has stopped.
2. Copy your plugin assembly (*.dll*) and any dependent support libraries to the Zoo's plugin folder (i.e. *C:\Program Files\Zoo 6\Plugins*).
3. Restart the Zoo license service.
4. When the service has restarted, click the *Add License* button. Y our product should be one of the available products for which to add a license.

## Related Topics

- [Digitally Signing Plugins for Zoo]({{ site.baseurl }}/guides/rhinocommon/digitally-signing-plugins-for-zoo)
- [Creating Plugins that use the Zoo (RhinoCommon)]({{ site.baseurl }}/guides/rhinocommon/rhinocommon-zoo-plugins)
- [Creating Plugins that use the Zoo (C/C++)]({{ site.baseurl }}/guides/cpp/creating-zoo-plugins)
- [Sample Zoo Plugin Projects (on GitHub)](https://github.com/mcneel/rhino-developer-samples/tree/6/zoo)

