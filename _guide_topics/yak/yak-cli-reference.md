---
title: Yak Command Line Tool Reference
description: A reference for the Yak command line tool.
authors: ['will_pearson']
sdk: ['Yak']
languages: # empty
platforms: ['Windows', 'Mac']
categories: ['Fundamentals']
origin: unset
order: 1
keywords: ['developer', 'yak']
layout: toc-guide-page
---

The Yak command line tool is included with Rhino 7 WIP. On Windows the tool is located at `"{{ site.rhino.windows_path }}\System\yak.exe"`. On macOS there is a convenience script at `"{{ site.rhino.mac_path }}/Contents/Resources/bin/yak"`.

{% include yak-mac-path-note.html %}

## Build

* _Since 0.2: Command added_
* _Since 0.4: Supports multiple .gha files, .rhp files or anything else for that matter_
* _Since 0.9: Appends distribution tag to filename and expands $version placeholder_
* _Since 0.10.1: Adds `--platform` argument_

When run in a directory containing a valid `manifest.yaml` file, creates a package containing all files in the directory.

```commandline
Usage: yak build [options]

Options:
    --platform PLATFORM  The platform where the package will run ('win', 'mac' or 'any')
    -h, --help           Get help (equivalent to `yak help build`)
```

<div class="alert alert-info" role="alert">
  <strong>Note:</strong> A <a href="../the-anatomy-of-a-package#distributions">distribution tag</a> (e.g. <code>rh7-win</code>) is appended to the filename of the created package. The tag is determined by inspecting the contents of the package during creation. The <code>--platform=any</code> argument can be used if the author wants to publish a cross-platform distribution, e.g. <code>rh7-any</code>. Only .rhp and .gha files can currently be inspected. If a package contains none of these, it will have a distribution tag of <code>any-any</code>.
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

_Since 0.2: Command added_
_Since 0.10: User registered during login_

Authenticates with Rhino Accounts and stores a time-limited OAuth2 access token so that the user can use commands which require authentication.

```commandline
Usage: yak login [options]

Options:
    --ci              Generate a non-expiring API key and display it
    -s, --source URL  Package repository location [default: https://yak.rhino3d.com/].
    -h, --help        Get help (equivalent to `yak help login`)
```

On Windows, the token is stored in `%appdata%\McNeel\yak.yml`. On macOS, it is stored in `~/.mcneel/yak.yml`.

During login, the user is registered on the server.

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

* _Since 0.1: Command added_
* _Since 0.5: Adds `--all` and `--prerelease` flags_

Searches the server for packages which match `query`.

```commandline
Usage: yak search [options] <query>

  Options:
    --prerelease      Display prerelease package versions
    -a, --all         Display all package versions
    -s, --source URL  Package repository location
    -h, --help        Get help (equivalent to `yak help search`)
```

## Spec

* _Since 0.2: Command added_
* _Since 0.4: Adds support for inspecting .rhp files (RhinoCommon only)_

Creates a skeleton `manifest.yml` file based on the contents of the current directory.
When run in a directory containing a Grasshopper assembly (`.gha`) or a RhinoCommon
plug-in (`.rhp`) the file will be inspected and used to pre-populate the `manifest.yml`
file.

```commandline
yak spec
```

## Uninstall

_Since 0.1_

Uninstalls a package.

```commandline
yak uninstall <package>
```
<!-- deactivation fallback removed in v0.6-->
<!-- <div class="alert alert-info" role="alert">
  <strong>Note:</strong> Since 0.3, Yak will attempt to remove the package from the machine. If this isn't possible -- likely because Rhino is running -- then the package will be <em>deactivated</em> instead.
</div> -->

## Yank

_Since 0.6_

Removes a version from the package index.

```commandline
yak yank <package> <version>
```

<div class="alert alert-info" role="alert">
  <strong>Note:</strong> Requires <a href="#login">authentication</a>.
</div>

Yanked versions do not appear in searches but can still be installed if the exact package version is known. To all intents and purposes they are hidden.

It is not possible to re-push a package version that has been yanked. If you find yourself in this situation, then simply roll the version number of your package and push again.

<div class="alert alert-info" role="warning">
  <strong>Deleting a package from the McNeel server</strong>
  </br>
  If you absolutely need to delete your package from the public server, please email <a href="mailto:will@mcneel.com">will@mcneel.com</a>. Once a package has been deleted, the name can no longer be used.
</div>

## Owner

_Since 0.10_

Adds, removes of lists the owners of a package. Package owners can push new versions of the package and (un)yank existing versions.

```commandline
Usage:
    yak owner add [--source=URL] <package> <email>
    yak owner remove [--source=URL] <package> <email>
    yak owner list [--source=URL] <package>
    
Options:
    -h, --help
    -s, --source URL  Package repository location [default: https://yak.rhino3d.com/].
```

New owners can do everything that the original owner can do. Please bear this in mind!

---

## Related Topics

- [Yak Guides and Tutorials]({{ site.baseurl }}/guides/yak/)
- [Anatomy of a Package]({{ site.baseurl }}/guides/yak/the-anatomy-of-a-package/)
- [The Package Manifest]({{ site.baseurl }}/guides/yak/the-package-manifest/)
