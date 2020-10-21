---
title: Package Restore in Grasshopper
description: How can Grasshopper use Yak to make your life easier?
authors: ['will_pearson']
sdk: ['Yak']
languages: # empty
platforms: ['Windows', 'Mac']
categories: ['Features']
origin: unset
order: 1
keywords: ['yak', 'grasshopper']
layout: toc-guide-page
---

## Overview

For starters, this is less of a developer guide and more of a description of how
this feature works, so that you, the developer, can better understand how your
package and plug-in needs to be set up in order to leverage it.

It can be frustrating to open a Grasshopper definition only to find that the
required plug-ins aren't installed on the system. The package manager can help by streamlining
the process of satisfying those dependencies.

Since Rhino 6, the "Unrecognized Objects" dialog presents the user with an option to _download and install_ missing plug-ins. This feature is called Package Restore.

![Grasshopper package restore]({{ site.baseurl }}/images/yak-gh-restore.gif)

Package Restore uses the name, ID and version of the missing plug-ins to search the package server. If any packages match the search query
then they will be installed and, if possible, loaded prior to opening the definition[^3].

<iframe width="560" height="315" src="https://www.youtube.com/embed/MsjRdRtHW08" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Matching

### Naming

Ideally, the name of the Grasshopper plug-in and the package will match. In case this isn't possible – due to either the constraints of the package naming scheme[^1] or the fact that there are multiple plug-ins in a package each with a different name – the correct package can also be identified by the plug-in ID.

For each .gha file, the plug-in ID is extracted and added to the `manifest.yml` when you run `yak build`.

### Version numbers

Package version numbers can either follow the [Semantic Versioning 2.0.0](https://semver.org) (SemVer) spec or they can be four-digits[^2], as per `System.Version`. See the [package server](../the-package-server) guide for more details on the allowed version number formats.

The server allows both SemVer and four-digit because some Grasshopper plug-ins will specify their version number as a `string` in a class derived from `GH_AssemblyInfo` whereas others will rely on the `AssemblyVersionAttribute`.

While restoring packages, if a package exists on the server that matches either the name or ID of the missing plug-in, but the exact version doesn't exist, the latest stable version will be installed.

---

[^1]: Package names are pretty strict. They only allow letters, numbers, hyphens and underscores.
[^2]: Support for four-digit (`System.Version`) version numbers was added in Yak 0.8.
[^3]: Added to Grasshopper in December 2019. On-the-fly loading is only possible if another version of the Grasshopper library is not already installed and loaded. Otherwise, Rhino will need to be restarted to load the new version of the library.
