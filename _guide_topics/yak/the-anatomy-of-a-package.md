---
title: The Anatomy of a Package
description: This guide explains the structure of a Yak package.
authors: ['Will Pearson']
author_contacts: ['will']
sdk: ['Yak']
languages: # empty
platforms: ['Windows', 'Mac']
categories: ['Getting Started']
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

1. Packages **must** have a top-level [`manifest.yml`](manifest.md) file
2. Any plug-ins (`.rhp` or `.gha` files) **must** be in the top-level directory
   so that Rhino and Grasshopper can find and load them
3. If you're packaging a `.gha` plug-in, you **should** ensure that the package
   name and version number in the `GH_AssemblyInfo` sub-class match those in the
   `manifest.yml` file, otherwise [package restore][1] won't work\*

\*OK, it will probably still work _a bit_.

[1]: {{ site.baseurl }}/guides/yak/package-restore-in-grasshopper
