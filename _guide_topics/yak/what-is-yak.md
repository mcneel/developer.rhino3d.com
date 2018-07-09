---
title: What is Yak?(Work in Progress)
description: This guide introduces the Yak package manager.
authors: ['Will Pearson']
author_contacts: ['will']
sdk: ['Yak']
languages: # empty
platforms: ['Windows']
categories: ['Overview']
order: 1
keywords: ['developer', 'yak']
layout: toc-guide-page
---

## Overview

Yak is a package manager for the Rhino ecosystem. Yak assists in the discovery, installation, and management of Rhino and Grasshopper resources. Examples include plug-ins, components, scripts, and material definitions.  

Yak has several goals.

- Make it easier for users to discover and manage plug-ins and more
- Help developers to share their work
- Provide simple system administration tools

Not wanting to reinvent the wheel, we've taken inspiration from Linux and the software development world. The package management system can be broken down into three main areas.

1. [Server](#server)
2. [Command line tool](#command-line-tool)
3. [Integrations](#integrations)

## Server

The package server is the heart of the system. Once packages are created, they must be posted up to a package server.

McNeel & Associates hosts a public package server which is available worldwide. This is the best option to post plugins to the public. The rest of the guides cover using the public server.

In the future a private package server can be hosted almost anywhere and keeps the packages organized for its clients – the command line tool and Rhino (via integrations). We would like to hear of any requests for future Yak feature on the [Yak Forum](https://discourse.mcneel.com/c/serengeti/yak).

## Integrations

To see how the package manager provides direct access to the package ecosystem from inside of Rhino there are two current integrations.

Thus far Yak has been integrated into Grasshopper's "Unrecognized Objects"
dialog, providing [package restore](../package-restore-in-grasshopper) functionality when Grasshopper reads and unknown component from a file.  This will allow the proper plugin to be loaded to run any definition.

![Package restore can still operate when the plug-in name doesn't match the package]({{ site.baseurl }}/images/yak-gh-restore-guid.gif)

As a In Rhino 6 there is also a test command of a prototype interface:

![TestPackageManager in Rhino 6 brings up the interface.]({{ site.baseurl }}/images/testpackagemanager-wip.jpg)![Test Package Manager]

## Command Line Tool

The command line tool provides a basic interface but with full functionality.
It is modelled on well known domain-specific package managers such as Ruby's
`gem` and Python's `pip`. It communicates with the server as well as hooking
into Rhino Accounts for authentication.

---

## Related Topics

- [Yak Guides and Tutorials]({{ site.baseurl }}/guides/yak/)
- [Anatomy of a Package]({{ site.baseurl }}/guides/yak/the-anatomy-of-a-package/)
- [The Package Manifest]({{ site.baseurl }}/guides/yak/the-package-manifest/)
- [Yak CLI Reference]({{ site.baseurl }}/guides/yak/yak-cli-reference)
