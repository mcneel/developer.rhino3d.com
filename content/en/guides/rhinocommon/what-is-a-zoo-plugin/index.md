+++
authors = [ "dale" ]
categories = [ "Zoo" ]
description = "This guide describes what a LAN Zoo Plugin is and what is does."
keywords = [ "Zoo", "Plugin" ]
languages = [ "All" ]
sdk = [ "RhinoCommon", "C/C++" ]
title = "What is a LAN Zoo Plugin?"
type = "guides"
weight = 1
override_last_modified = "2021-06-25T14:03:04Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/zoowhat"
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

The LAN Zoo keeps your licenses on your private LAN server and lets you share them among the Rhino users on your network.

A LAN Zoo plugin is a software module, developed by a 3rd party, that extends the functionality of the LAN Zoo by allowing it to validate product licenses.

![zoo with plugins](/images/what-is-a-zoo-plugin-01.png)

When Rhino and Rhino-based products are installed as workgroup nodes, instead of standalone nodes, licensing works like this:

- When a workgroup node starts, it requests a license from the LAN Zoo.
- An unused license is assigned to the node.
- When a node shuts down, the license is returned to the LAN Zoo's license pool.

#### What is required to build a plugin?

LAN Zoo plugins are .NET Framework 4.8 assemblies. Thus, to create a plugin for the LAN Zoo, you will need one of the following development tools:

1. Microsoft Visual C#
1. Microsoft Visual Basic .NET

Also, all plugins that use the LAN Zoo license system must be signed with an Authenticode certificate issued by McNeel Plugin Security. These certificates are free, but must be requested by each developer. Developers must agree to the Terms of Use before a certificate is issued. For more information on plugin signing, see [Digitally Signing Plugins for LAN Zoo](/guides/rhinocommon/digitally-signing-plugins-for-zoo).

## Next Steps

Check out the [Creating LAN Zoo Plugins](/guides/rhinocommon/creating-zoo-plugins) guide for instructions building - your guessed it - a LAN Zoo Plugin.


## Related Topics

- [Creating LAN Zoo Plugins](/guides/rhinocommon/creating-zoo-plugins)
- [Digitally Signing Plugins for LAN Zoo](/guides/rhinocommon/digitally-signing-plugins-for-zoo)
