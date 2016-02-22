---
title: Creating Zoo Plugins
description: This guide discusses how to create plugins for Zoo.
author: dale@mcneel.com
apis: ['RhinoCommon']
languages: ['C#']
platforms: ['Windows']
categories: ['Zoo']
origin: http://wiki.mcneel.com/developer/zooplugin
order: 2
keywords: ['Zoo', 'Plugin']
layout: toc-guide-page
---

# Creating Zoo Plugins

{{ page.description }}

## Overview

Zoo lets third party plugin developers add licensing support for their products to the Zoo.

When a customer attempts to add a product license to the Zoo, the product's plugin is called to validate the user's request.  Upon validation, the plugin will return the product's licensing information back to the Zoo.  In turn, the Zoo will serialize, maintain, and distribute this license.

## Prerequisites

Zoo plugins are .NET Framework 4.0 assemblies.  To create a plugins for Zoo, you need one of the following development tools:

1. Microsoft Visual C# 2010.
1. Microsoft Visual Basic .NET 2010.

Also, all plugins that use the Zoo license system must be signed with an *Authenticode* certificate issued by *McNeel Plugin Security*.  These certificates are free, but must be requested by each developer.  Developers must agree to the *Terms of Use* before a certificate is issued.  For more information on plugin signing, see [Digitally Signing Plugins for Zoo]({{ site.baseurl }}/guides/zoo/digitally_signing_plugins_for_zoo).

## Writing a Zoo Plugin

The general steps required to create a Zoo plugin are:

1. Make sure you have Zoo installed.
1. Launch Microsoft Visual Studio 2010.
1. Create a new *Class Library* project using either Visual C# or Visual Basic .NET.
1. Add a reference to *ZooPlugin.dll*, which is found in the Zoo installation folder.  Make sure to set the reference's *Copy Local* property to `False`.
1. Create a new public class that inherits from the `IZooPlugin` interface.
1. Implement the interface members.  (For detailed information about the interface members, see the sample Zoo plugin listed below.)
1. Build your plugin.
1. [Digitally sign your plugin](({{ site.baseurl }}/guides/zoo/digitally_signing_plugins_for_zoo)).

## Installing a Zoo Plugin

Once you have built your Zoo plugin, you can install it and test it:

1. Run *ZooAdmin.exe* and make sure the Zoo licensing service has stopped.
1. Copy your plug-in assembly (*.dll*) and any dependent support libraries to the Zoo's plugin folder (i.e. *C:\Program Files\Zoo 5.0\Plugins*).
1. Restart the Zoo license service.
1. When the service has restarted, click the *Add License* button. Y our product should be one of the available products for which to add a license.

## Related Topics

- [Digitally Signing Plugins for Zoo]({{ site.baseurl }}/guides/zoo/digitally_signing_plugins_for_zoo)
- [Sample Zoo Plugin Projects (on GitHub)](https://github.com/mcneel/Zoo5)
