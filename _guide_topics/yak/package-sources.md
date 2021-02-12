---
title: Custom Package Repositories
description: This is a quick guide to configuring custom package repositories in Rhino.
authors: ['will_pearson']
sdk: ['Yak']
languages: # empty
platforms: ['Windows', 'Mac']
categories: ['Getting Started']
origin: unset
order: 20
keywords: ['developer', 'yak']
layout: toc-guide-page
---

<div class="alert alert-warning" role="alert">
⚠️ This feature requires modifying advanced settings in Rhino!
</div>

By default Rhino uses the official McNeel package server - https://yak.rhino3d.com. In addition (or instead!), it's possible to configure Rhino to use your own package repositories.

A custom package repository is simply a folder that contains .yak package files. The folder can be on the local machine or on a shared file server. You can configure Rhino to include packages from this repository in the Package Manager by following the steps below.


1. Go to _Options > Advanced_ and look for the `Rhino.PackageManager.Sources` setting.
1. Add the full path to your package repository folder, separating it from the default package server with a semi-colon, e.g. `https://yak.rhino3d.com;C:\rhino_packages`.
1. Run the `_PackageManager` command and search for one of the packages that you added to the new package repository.

for now it just supports whatever Directory.EnumerateFiles() supports, which as far as I can tell is regular paths, mapped drives (Windows), UNC paths (Windows) and mounted shares (macOS)

### Tips for shared folders

On Windows use the UNC path, i.e. `\\server\share\packages`. If the share requires credentials then first navigate to `\\server` in Explorer, log in and check the "remember my credentials" box.

On macOS the file share needs to be mounted first in Finder via _Go > Connect to Server..._ (<kbd>⌘</kbd> + <kbd>K</kbd>). Enter the address (`smb://server/share`) and provide credentials if required. Now the mounted path can be used as a package source, i.e. `/Volumes/share/packages`. The mount isn't persistent, so it'll need to be remounted in future.