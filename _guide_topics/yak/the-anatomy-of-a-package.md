---
title: The Anatomy of a Package
description: This guide explains the structure of a Yak package.
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

## Package Structure

Packages are simply ZIP archives with a .yak extension. Take this simple example...

```
howler-0.4.0-any-any.yak
├── manifest.yml
├── Howler.rhp
├── Howler.rui
├── HowlerCommon.dll
├── HowlerGrasshopper.gha
└── misc/
    ├── README.md
    └── LICENSE.txt
```

## Important Things to Note

1. Packages **must** have a top-level [`manifest.yml`](manifest.md) file.
   Details about the manifest can be found in the [Manifest Reference Guide](../the-package-manifest).
2. Any plug-ins (`.rhp`, `.gha`, `.ghpy` files) **must** be in the top-level directory
   so that Rhino and Grasshopper can find and load them
3. Each package **should** have only one plug-in (`.gha`, `.rhp` or `.ghpy`). It
   is possible to combine plug-ins in one package (e.g. `.gha` and `.rhp`)
   however [package restore](../package-restore-in-grasshopper) will only work
   for the plug-in which matches the details in the `manifest.yml` file.
4. Package version numbers **must** either follow [Semantic Versioning 2.0.0](http://semver.org/spec/v2.0.0.html) (e.g. `1.1.0-beta`) or `System.Version` a.k.a. Microsoft's four-digit standard (e.g. `1.2.3.4`). It's recommended to use Semantic Versioning because it allows package authors to specify prerelease versions. These are handy for limited testing, since by default the latest _stable_ version is installed.
5. If you're packaging a `.gha` plug-in, you **should** ensure that the package
   name and version number in the `GH_AssemblyInfo` sub-class match those in the
   `manifest.yml` file, otherwise [package restore](../package-restore-in-grasshopper) may not work

## Distributions

Prior to v0.9 of the package server, each new .yak package uploaded represented a new version. Now, for a single version it's possible to upload multiple "distributions" to target different Rhino versions and platforms. This information is encoded in a "distribution tag" that is appended to the filename of the package, e.g. _example-1.0.0-rh7-win.yak_.

The distribution tag consists of an "app" identifier and version, and a platform. Currently the only supported apps are `rh` and `any` – Grasshopper ships with Rhino so it doesn't need its own identifier. Unless the app is `any`, an app version must be included in the form `<major>_<minor>`. The minor version is optional and is useful if a plug-in relies on an SDK change made in a service release. The platform can be `win`, `mac` or `any` (i.e. cross-platform).

A few examples...

* `rh7-win` - Rhino 7 for Windows >= 7.0
* `rh6_14-mac` - Rhino 6 for Mac >= 6.14
* `rh6_9-any` - Rhino 6 (both platforms) >= 6.9
* `any-any` - anything goes! (existing behaviour)

When installing packages, the server will check the version of Rhino[^1] and determine whether a compatible distribution exists for the requested version.

The updated server works seamlessly with existing packages and old versions of Rhino. Pre-existing versions on the server (without distributions) will be treated as `any-any` when installing. New package versions that do not include a distribution tag, e.g. those created by previous versions of the CLI, will also be treated as `any-any` when publishing.

<div class="alert alert-info" role="alert">
<strong>Note:</strong> Distributions are new and may change slightly before the release of Rhino 7!
</div>

---

## Next Steps

Now that you've have seen what is in a package, why not create a package:

* [Create a Grasshopper package](../pushing-a-package-to-the-server) of your plugin.
* [Create a Rhino package](../pushing-a-package-to-the-server) for everyone.

---

[^1]: Each installation of Rhino comes with it's own version of the package manager.
