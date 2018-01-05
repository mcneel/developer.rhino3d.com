---
title: Yak CLI Reference
description: A reference for the Yak command line tool.
authors: ['Will Pearson']
author_contacts: ['will']
sdk: ['Yak']
languages: # empty
platforms: ['Windows']
categories: ['Fundamentals']
order: 1
keywords: ['developer', 'yak']
layout: toc-guide-page
---

## Build

_Since 0.2_

When run in a directory containing a valid `manifest.yaml` file, creates a package containing all files in the directory.

```commandline
yak build
```

<div class="alert alert-info" role="alert">
  <strong>Note:</strong> Currently this only works if there is exactly <strong>one</strong> <code>.gha</code> file in the directory.
</div>
<!-- During the build, the component GUID is extracted to help with searching for the package later. -->

## Install

_Since 0.1_

Installs a package (optionally with a specific version).

```commandline
yak install [--source=URL] <package> [<version>]
```

## List

_Since 0.2_

Lists the packages installed on the machine.

```commandline
yak list
```

## Login

_Since 0.2_

Authenticates with Rhino Accounts and stores a time-limited OAuth2 access token so that the user can use commands which require authentication.

```commandline
yak login
```

On macOS, credentials are stored in `~/.mcneel/yak.yml`. On Windows, they are stored in `%appdata%\McNeel\yak.yml`.

## Push

_Since 0.1_

Pushes a package to the server.

```commandline
yak push [--source=URL] <filename>
```

<div class="alert alert-info" role="alert">
  <strong>Note:</strong> Requires <a href="#login">authentication</a>.
</div>

## Search

_Since 0.1_

Searches the server for packages which match `query`.

```commandline
yak search [--source=URL] <query>
```

## Spec

_Since 0.2_

When run in a directory containing a `*.gha` file, creates a `manifest.yml` file populated with metadata from the Grasshopper plug-in.

```commandline
yak spec
```

<div class="alert alert-info" role="alert">
  <strong>Note:</strong> Currently this only works if there is exactly <strong>one</strong> <code>.gha</code> file in the directory.
</div>

<div class="alert alert-info" role="alert">
  <strong>Note:</strong> This command is only useful if you've implemented <code>GH_AssemblyInfo</code> in the Grasshopper plug-in.
</div>

## Uninstall

_Since 0.1_

Uninstalls a package.

```commandline
yak uninstall <package>
```
<div class="alert alert-info" role="alert">
  <strong>Note:</strong> This doesn't actually remove the package from the machine, it just removes the <code>manifest.txt</code> file that tells Rhino which version to load.
</div>
