---
title: The Anatomy of a Package
description: This guide explains the structure of a Yak package.
authors: ['will_pearson']
author_contacts: ['will']
sdk: ['Yak']
languages: # empty
platforms: ['Windows', 'Mac']
categories: ['Fundamentals']
order: 1
keywords: ['developer', 'yak']
layout: toc-guide-page
---

## Package Structure

Packages are simply ZIP archives. Take this simple example...

```
plankton-0.4.0.zip
├── manifest.yml
├── Plankton.gha
├── Plankton.dll
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
4. Versioning is critical to package management. The version number given to the
   package **must** adhere to [SemVer 2.0.0](http://semver.org/spec/v2.0.0.html).
   We’ve adopted SemVer to make ordering straightforward and also for easy
   identification of pre-release versions – handy when releasing beta plug-ins
   for limited testing! Please ask any questions about versioning on the [Yak Forum](https://discourse.mcneel.com/c/serengeti/yak).
5. If you're packaging a `.gha` plug-in, you **should** ensure that the package
   name and version number in the `GH_AssemblyInfo` sub-class match those in the
   `manifest.yml` file, otherwise [package restore][1] may not work

[1]: {{ site.baseurl }}/guides/yak/package-restore-in-grasshopper

---

## Next Steps

Now that you've have seen what is in a package, why not create a package:

* [Create a Grasshopper package](../pushing-a-package-to-the-server) of your plugin.
* [Create a Rhino package](../pushing-a-package-to-the-server) for everyone.
