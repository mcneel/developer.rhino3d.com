---
title: Package Restore in Grasshopper
description: How can Grasshopper use Yak to make your life easier?
authors: ['will_pearson']
sdk: ['Yak']
languages: # empty
platforms: ['Windows']
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
required plug-ins aren't installed on the system. Yak can help by streamlining
the process of satisfying those dependencies.

Yak hooks into the "Unrecognized Objects" dialog and presents the user with a
new "Install" option.

![Grasshopper package restore]({{ site.baseurl }}/images/yak-gh-restore.gif)

Yak uses the name and version of the "libraries" (plug-ins) to which the missing
components belong to search the server. If any packages match the search query
then they will be installed and, if possible, loaded prior to opening the definition[^3].

<iframe width="560" height="315" src="https://www.youtube.com/embed/MsjRdRtHW08" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Constraints

### Naming (and GUID fallback)

In case the package name doesn't match[^1] the plug-in name (as defined in the
`GH_AssemblyInfo` derived class), Yak will fall back to searching by plug-in ID.

![Package restore can still operate when the plug-in name doesn't match the package]({{ site.baseurl }}/images/yak-gh-restore-guid.gif)

The plug-in ID (GUID) is extracted from the `.gha` assembly when you run
`yak build` and added to `manifest.yml`. When the package is pushed, the server
extracts the ID (along with the name, version, etc.) and makes it searchable.
This is to say, if you don't want to change the name of your Grasshopper plug-in
to conform with the constraints[^1], _please_ make sure you build the package
using `yak build` so this can all work happily!

### Version numbers

Package version numbers can either follow the [Semantic Versioning 2.0.0](https://semver.org) (SemVer) spec or they can be four-digits[^2], as per `System.Version`. See the [package server](../the-package-server) guide for more details on the allowed version number formats.

The server allows both SemVer and four-digit because some Grasshopper plug-ins will specify their version number as a `string` in a class derived from `GH_AssemblyInfo` whereas others will rely on the `AssemblyVersionAttribute`.

If the "Unrecognized Objects" dialog comes across a package/version pair that doesn't exist on the server, it will drop down to searching by GUID and grab the latest version if there's a match.

---

[^1]: Package names are pretty strict. They only allow letters, numbers, hyphens and underscores.
[^2]: Support for four-digit (`System.Version`) version numbers was added in Yak 0.8.
[^3]: Added to Grasshopper in December 2019. On-the-fly loading is only possible if another version of the Grasshopper library is not already installed and loaded. Otherwise, Rhino will need to be restarted to load the new version of the library.
