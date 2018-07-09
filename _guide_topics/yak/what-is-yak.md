---
title: What is Yak?
description: This guide introduces the Rhino Package Manager (a.k.a. Yak).
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

<div class="alert alert-info" role="alert">
<strong>Note:</strong> The Rhino Package Manager is a
<strong>work-in-progress</strong> and we're adding new features all the time!
</div>

## Overview

Yak is a package manager for the Rhino ecosystem. Yak assists in the discovery,
installation, and management of Rhino and Grasshopper resources. Examples
include plug-ins, components, scripts, and material definitions.  

Yak has several goals.

- Make it easier for users to discover and manage plug-ins and more
- Help developers to share their work
- Provide simple system administration tools

Not wanting to reinvent the wheel, we've taken inspiration from Linux and the
software development world. The package management system can be broken down
into three main areas.

1. [Server](#server)
2. [Integrations](#integrations)
3. [Command line tool](#command-line-tool)

## Server

The package server is the heart of the system. Once created, packages are pushed
to the server to share them with others. It keeps the packages organised for its
clients – the command line tool and Rhino (via integrations).

<div class="alert alert-info" role="alert">
<strong>Note:</strong> Currently the only available package server is our
<a href="https://yak.rhino3d.com">public server</a>. Self-hosted/private servers
are on the roadmap however for now all guides will assume you're using the
public server.
</div>

## Integrations

Integrations provide direct access to the package ecosystem from inside of
Rhino. Currently this has been done in two ways; "package restore" for
Grasshopper and the package manager UI.

### Package restore for Grasshopper

The Rhino Package Manager has been integrated into Grasshopper's "Unrecognized
Objects" dialog, providing [package restore](../package-restore-in-grasshopper)
functionality. When opening a new file which contains components from a plug-in
not installed on the machine, the user is given the option to check the package
server for the missing plug-ins and install them directly.

![Package restore for Grasshopper]({{ site.baseurl }}/images/yak-gh-restore-guid.gif)

### Package Manager UI

The package manager UI (work-in-progress) is currently avilable via the
`TestPackageManager` command. It provides a NuGet-style interface that allows
users to search for packages, install them and see if any updates are avilable
to currently installed packages.

![The package manager UI in Rhino 6]({{ site.baseurl }}/images/testpackagemanager-wip.jpg)

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
