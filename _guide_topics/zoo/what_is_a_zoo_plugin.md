---
layout: toc-guide-page
title: What is a Zoo Plugin?
author: dale@mcneel.com
categories: ['Overview']
platforms: ['Windows']
apis: ['Zoo']
languages: ['All']
keywords: ['Zoo', 'Plugin']
TODO: 0
origin: http://wiki.mcneel.com/developer/zoowhat
order: 1
---

# What is a Zoo Plugin?

A Zoo plug-in is a software module, developed by a 3rd party, that extends the functionality of Zoo 5.0 by allowing it to validate product licenses.

The Zoo lets you share licenses, or CD-Keys, among users. Prior to Zoo 5.0, the only licenses that could be shared by the Zoo were from McNeel-based products (i.e. Rhino, Flamingo, Penguin, Brazil, and Bongo). With Zoo 5.0, 3rd party Rhino plug-in developers can now add support for their products to the Zoo.

![zoo with plugins]({{ site.baseurl }}/images/what_is_a_zoo_plugin_01.png)

When Rhino and Rhino-based products are installed as workgroup nodes, instead of standalone nodes, licensing works like this:

- When a workgroup node starts, it requests a license from the Zoo.
- An unused license is assigned to the node.
- When a node shuts down, the license is returned to the Zoo's license pool.

#### What is required to build a plug-in?

Zoo plug-ins are .NET Framework 4.0 assemblies. Thus, to create a plug-in for Zoo 5.0, you will need one of the following development tools:

1. Microsoft Visual C# 2010
1. Microsoft Visual Basic .NET 2010

Also, all plug-ins that use the Zoo license system must be signed with an Authenticode certificate issued by McNeel Plugin Security. These certificates are free, but must be requested by each developer. Developers must agree to the Terms of Use before a certificate is issued. For more information on plug-in signing, see [Digitally Signing Plugins for Zoo]({{ site.baseurl }}/guides/zoo/digitally_signing_plugins_for_zoo).

---

## Next Steps

Check out the [Creating Plugins for Zoo]({{ site.baseurl }}/guides/zoo/creating_plugins_for_zoo) guide for instructions building - your guessed it - a Zoo Plugin.


---

## Related Topics

- [Creating Plugins for Zoo]({{ site.baseurl }}/guides/zoo/creating_plugins_for_zoo)
- [Digitally Signing Plugins for Zoo]({{ site.baseurl }}/guides/zoo/digitally_signing_plugins_for_zoo)
