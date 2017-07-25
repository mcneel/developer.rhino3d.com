---
title: Yak CLI Reference
description: A reference for the Yak command line tool.
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

## Commands

* [`build`](#build)
* [`install`](#install)
* [`list`](#list)
* [`login`](#login)
* [`push`](#push)
* [`search`](#search)
* [`spec`](#spec)
* [`uninstall`](#uninstall)

## `build`

_Since 0.2_

When run in a directory containing a valid `manifest.yaml` file, creates a package containing all files in the directory.

```commandline
yak build
```

**Note**: Currently this only works if there is exactly **one** `.gha` file in the directory.
<!-- During the build, the component GUID is extracted to help with searching for the package later. -->

## `install`

_Since 0.1_

Installs a package (optionally with a specific version).

```commandline
yak install [--source=URL] <package> [<version>]
```

## `list`

_Since 0.2_

Lists the packages installed on the machine.

```commandline
yak list
```

## `login`

_Since 0.2_

Authenticates with Rhino Accounts and stores a time-limited OAuth2 access token so that the user can use commands which require authentication.

```commandline
yak login
```

On macOS, credentials are stored in `~/.mcneel/yak.yml`. On Windows, they are stored in `%appdata%\McNeel\yak.yml`.

## `push`

_Since 0.1_

Pushes a package to the server.

```commandline
yak push [--source=URL] <filename>
```

**Note**: Requires [authentication](#login).

## `search`

_Since 0.1_

Searches the server for packages which match `query`.

```commandline
yak search [--source=URL] <query>
```

## `spec`

_Since 0.2_

When run in a directory containing a `*.gha` file, creates a `manifest.yml` file populated with metadata from the Grasshopper plug-in.

```commandline
yak spec
```

**Note**: Currently this only works if there is exactly **one** `.gha` file in the directory.

**Note 2**: This command is only useful if you've implemented `GH_AssemblyInfo` in the Grasshopper plug-in.

## `uninstall`

_Since 0.1_

Uninstalls a package.

**Note**: This doesn't actually remove the package from the machine, it just removes the `manifest.txt` file that tells Rhino which version to load.

```commandline
yak uninstall <package>
```
