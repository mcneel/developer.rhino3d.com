+++
authors = [ "will" ]
categories = [ "Overview" ]
description = "This guide introduces the Rhino Package Manager (a.k.a. Yak)."
keywords = [ "developer", "yak" ]
sdk = [ "Yak" ]
title = "What is the Package Manager?"
type = "guides"
weight = 1
override_last_modified = "2020-11-12T12:17:36Z"

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

## Overview

The Rhino Package Manager assists in the discovery, installation, and management resources in the Rhino ecosystem (Grasshopper included!). Currently it supports Rhino and Grasshopper plug-ins, but the goal is to include things like scripts, materials, viewports, etc. in the future!

{{< call-out "note" "Note" >}}
The Rhino Package Manager was initially referred to by the codename "Yak". The name Yak is still used for the command line tool that creates and publishes packages.
{{< /call-out >}}

The package manager has several goals.

- Make it easier for users to discover and manage plug-ins and more
- Help developers and reusable content authors to share their work
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

{{< call-out "note" "Note" >}}
Currently the only available package server is our
<a href="https://yak.rhino3d.com">public server</a>. Self-hosted/private servers
are on the roadmap however for now all guides will assume you're using the
public server.
{{< /call-out >}}

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

![Package restore for Grasshopper](/images/yak-gh-restore-guid.gif)

### Package Manager UI

The package manager UI is avilable via the `_PackageManager` command. It provides a NuGet-style interface that allows
users to search for packages, install them and see if any updates are avilable
to currently installed packages.

![The package manager UI](/images/testpackagemanager-wip.jpg)

## Command Line Tool

The command line tool provides a basic interface but with full functionality.
It is modelled on well known domain-specific package managers such as Ruby's
`gem` and Python's `pip`. It communicates with the server as well as hooking
into Rhino Accounts for authentication.

On Windows, the tool can be found at `"C:\Program Files\Rhino {{< latest-rhino-version >}}\System\yak.exe"`.
On Mac there is a script, `"/Applications/Rhino {{< latest-rhino-version >}}.app/Contents/Resources/bin/yak"`.

Type `<path_to_yak> help` to get started.



## Related Topics

- [Anatomy of a Package](/guides/yak/the-anatomy-of-a-package/)
- [The Package Manifest](/guides/yak/the-package-manifest/)
- [Yak CLI Reference](/guides/yak/yak-cli-reference)
