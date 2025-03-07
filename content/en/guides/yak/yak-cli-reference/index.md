+++
aliases = ["/en/5/guides/yak/yak-cli-reference/", "/en/6/guides/yak/yak-cli-reference/", "/en/7/guides/yak/yak-cli-reference/", "/en/wip/guides/yak/yak-cli-reference/"]
authors = [ "will" ]
categories = [ "Fundamentals" ]
description = "A reference for the Yak command line tool."
keywords = [ "developer", "yak" ]
sdk = [ "Yak" ]
title = "Yak Command Line Tool Reference"
type = "guides"
weight = 1

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

The Yak command line tool is included with Rhino 7 WIP. On Windows the tool is located at `"C:\Program Files\Rhino {{< latest-rhino-version >}}\System\yak.exe"`. On macOS there is a convenience script at `"/Applications/Rhino {{< latest-rhino-version >}}.app/Contents/Resources/bin/yak"`.

## Commands

### Build

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

{{< call-out "note" "Note" >}}
  A <a class="alert-link" href="../the-anatomy-of-a-package#distributions">distribution tag</a> (e.g. <code>rh7-win</code>) is appended to the filename of the created package. The tag is determined by inspecting the contents of the package during creation. The <code>&#45;&#45;platform=any</code> argument can be used if the author wants to publish a cross-platform distribution, e.g. <code>rh7-any</code>. Only .rhp and .gha files can currently be inspected. If a package contains none of these, it will have a distribution tag of <code>any-any</code>.
{{< /call-out >}}

<!-- During the build, the component GUID is extracted to help with searching for the package later. -->

### Install

* _Since 0.1: Command added_
* _Since 0.13.0: Supports installing local .yak files_

Installs a package (optionally with a specific version).

```commandline
Usage:
    yak install [--source=URL] <package> [<version>]
    yak install <package>
```

Where `<package>` is either the name of a package or the path to a local .yak file.

### List

_Since 0.2_

Lists the packages installed on the machine.

```commandline
yak list
```

### Login

* _Since 0.2: Command added_
* _Since 0.10: User registered during login_

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

### Push

_Since 0.1_

Pushes a package to the server.

```commandline
yak push [--source=URL] <filename>
```

{{< call-out "note" "Note" >}}
  Requires <a class="alert-link" href="#login">authentication</a>.
{{< /call-out >}}

### Search

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

### Spec

* _Since 0.2: Command added_
* _Since 0.4: Adds support for inspecting .rhp files (RhinoCommon only)_

Creates a skeleton `manifest.yml` file based on the contents of the current directory.
When run in a directory containing a Grasshopper assembly (`.gha`) or a RhinoCommon
plug-in (`.rhp`) the file will be inspected and used to pre-populate the `manifest.yml`
file.

```commandline
yak spec
```

### Uninstall

_Since 0.1_

Uninstalls a package.

```commandline
yak uninstall <package>
```
<!-- deactivation fallback removed in v0.6-->
<!-- {{< call-out "note" "Note" >}}
  Since 0.3, Yak will attempt to remove the package from the machine. If this isn't possible -- likely because Rhino is running -- then the package will be <em>deactivated</em> instead.
{{< /call-out >}} -->

### Yank

_Since 0.6_

Removes a version from the package index.

```commandline
yak yank <package> <version>
```

{{< call-out "note" "Note" >}}
  Requires <a class="alert-link" href="#login">authentication</a>.
{{< /call-out >}}

Yanked versions do not appear in searches but can still be installed if the exact package version is known. To all intents and purposes they are hidden.

It is not possible to re-push a package version that has been yanked. If you find yourself in this situation, then simply roll the version number of your package and push again.

If all versions of a package are removed, it will no longer show up in the package index.

{{< call-out "danger" "Danger" >}}
  <p><strong>Deleting a package from the McNeel server</strong></p>
  <p>If you absolutely need to delete your package from the public server, please email <a href="mailto:support@mcneel.com">support@mcneel.com</a>. Once a package has been deleted, the name can no longer be used.</p>
{{< /call-out >}}

### Unyank

Works in the same way as the yank command, but in reverse!

### Owner

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

New owners must be registered on the server before they can be added to a package. They can do this by running the [`login`](#login) command.

## Downloads

The `yak` CLI is available as a standalone executable for use in environments where Rhino isn't installed, such as on automated build machines.

* https://files.mcneel.com/yak/tools/0.13.0/yak.exe
* https://files.mcneel.com/yak/tools/0.13.0/win-arm64/yak.exe
* https://files.mcneel.com/yak/tools/0.13.0/mac/yak
* https://files.mcneel.com/yak/tools/0.13.0/linux-x64/yak
* https://files.mcneel.com/yak/tools/0.13.0/linux-arm64/yak


## Related Topics

- [Yak Guides and Tutorials](/guides/yak/)
- [Anatomy of a Package](/guides/yak/the-anatomy-of-a-package/)
- [The Package Manifest](/guides/yak/the-package-manifest/)
