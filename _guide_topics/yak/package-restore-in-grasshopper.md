---
title: Package Restore in Grasshopper
description: How can Grasshopper use Yak to make your life easier?
authors: ['Will Pearson']
author_contacts: ['will']
sdk: ['Yak']
languages:
platforms: ['Windows']
categories: ['Features']
order: 1
keywords: ['yak', 'grasshopper']
layout: toc-guide-page
---

# Overview

For starters, this is less of a developer guide and more of a description of how
this feature works, so that you, the developer, can better understand how your
package and plug-in needs to be set up in order to leverage it.

It can be frustrating to open a Grasshopper definition only to find that the
required plug-ins aren't installed on the system. Yak can help by streamlining
the process of satisfying those dependencies.

Yak hooks into the "Unrecognized Objects" dialog and presents the user with a
new "Install" option.

![Grasshopper package restore]({{ site.base_url }}/images/yak-gh-restore.gif)

Yak uses the name and version of the "libraries" (plug-ins) to which the missing
components belong to search the server. If any packages match the search query
then they will be installed and made available the next time Grasshopper loads.

## Naming constraints (and GUID fallback)

In case the package name doesn't match[^1] the plug-in name (as defined in the
`GH_AssemblyInfo` derived class), Yak will fall back to searching by plug-in ID.

![Package restore can still operate when the plug-in name doesn't match the package]({{ site.base_url }}/images/yak-gh-restore-guid2.gif)

Here's a closer look.

![Package restore can still operate when the plug-in name doesn't match the package]({{ site.base_url }}/images/yak-gh-restore-guid.png)

The plug-in ID (GUID) is extracted from the `.gha` assembly when you run
`yak build` and added to `manifest.yml`. When the package is pushed, the server
extracts the ID (along with the name, version, etc.) and makes it searchable.
This is to say, if you don't want to change the name of your Grasshopper plug-in
to conform with the constraints[^1], _please_ make sure you build the package
using `yak build` so this can all work happily!

## Version number constraints

Similar to the naming, the Yak server is strict in its use of Semantic
Versioning[^2] for packages. The server will however attempt to coerce version
strings that don't exactly match the specification, for example: `1 -> 1.0.0`.
If the "Unrecognized Objects" dialog kicks up a plug-in that doesn't match
Semantic Versioning (and can't be coerced), then it won't find any matches.

```commandline
404: No package found by the name of 'plankton' with version number 'semwhat'.
```

That said, you won't be able to upload a package without adopting Semantic
Versioning, so...

---

[^1]: Package names are pretty strict. They only allow letters, numbers, hyphens and underscores.
[^2]: [http://semver.org/spec/v2.0.0.html](http://semver.org/spec/v2.0.0.html)
