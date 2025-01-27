+++
aliases = ["/en/5/guides/yak/package-sources/", "/en/6/guides/yak/package-sources/", "/en/7/guides/yak/package-sources/", "/en/wip/guides/yak/package-sources/"]
authors = [ "will" ]
categories = [ "Fundamentals" ]
description = "This is a quick guide to configuring custom package repositories in Rhino."
keywords = [ "developer", "yak" ]
sdk = [ "Yak" ]
title = "Custom Package Repositories"
type = "guides"
weight = 20
override_last_modified = "2021-02-12T11:31:53Z"

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

<!-- {{< call-out "note" "Note" >}}
This feature requires modifying advanced settings in Rhino!
{{< /call-out >}} -->

By default Rhino uses the official McNeel package server - https://yak.rhino3d.com. In addition (or instead!), it's possible to configure Rhino to use your own package repositories.

A custom package repository is simply a folder that contains .yak package files. The folder can be on the local machine or on a shared file server. You can configure Rhino to include packages from this repository in the Package Manager by following the steps below.


1. Go to _Options > Advanced_ and look for the `Rhino.Options.PackageManager.Sources` setting.
1. Add the full path to your package repository folder, separating it from the default package server with a semi-colon, e.g. `https://yak.rhino3d.com;C:\rhino_packages`.
1. Run the `_PackageManager` command and search for one of the packages that you added to the new package repository.

for now it just supports whatever Directory.EnumerateFiles() supports, which as far as I can tell is regular paths, mapped drives (Windows), UNC paths (Windows) and mounted shares (macOS)

### Tips for shared folders

On Windows use the UNC path, i.e. `\\server\share\packages`. If the share requires credentials then first navigate to `\\server` in Explorer, log in and check the "remember my credentials" box.

On macOS the file share needs to be mounted first in Finder via _Go > Connect to Server..._ (<kbd>⌘</kbd> + <kbd>K</kbd>). Enter the address (`smb://server/share`) and provide credentials if required. Now the mounted path can be used as a package source, i.e. `/Volumes/share/packages`. The mount isn't persistent, so it'll need to be remounted in future.

### Administrator-Enforced Settings

See [Administrator-Enforced Settings](https://docs.mcneel.com/rhino/8/help/en-us/index.htm#information/admin-enforced_settings.htm) for tips on how to deploy and enforce this setting for Windows users in your organisation.

### Performance

Rhino 8.15 included some performance improvements for private package repositories.

The yak.exe tool has a new “cache” command that, when run inside the private package folder, will generate an index of the available packages. When the package manager sees this index file, it will use it _instead of_ traversing the directory. This greatly reduces the time it takes for the Package Manager to load when dealing with private repositories with many packages, large packages, or slow network connections.

```
$ cd X:\private\repo\directory
$ "C:\Program Files\Rhino 8\System\yak.exe" cache

Building cache for local package repository in X:\private\repo\directory

[...]
```

Make sure to re-build the cache if package files are added or removed from the directory. Remove the _.cache*_ files from the directory to revert to the old behaviour.
