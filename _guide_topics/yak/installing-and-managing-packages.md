---
title: Installing and Managing Packages
description: This is a step by step guide to installing a Yak package.
authors: ['will_pearson']
sdk: ['Yak']
languages: # empty
platforms: ['Windows']
categories: ['Step By Step']
origin: unset
order: 3
keywords: ['developer', 'yak']
layout: toc-guide-page
---

<div class="alert alert-info" role="alert">
<strong>Note:</strong> Yak is cross-platform. Not everything is hooked up on the Mac side
yet, however. So, for now, this guide is aimed at <strong>Windows users only</strong>.
</div>

## Install

Installing a yak package with the CLI tool is simple.

```commandline
> "C:\Program Files\Rhino 6\System\Yak.exe" install marmoset

Downloading marmoset (1.0.0)...
Downloaded marmoset (1.0.0)
Installing marmoset (1.0.0)...
Successfully installed marmoset (1.0.0)
```

<div class="alert alert-info" role="alert">
<strong>Note:</strong> Rhino will load new packages the next time it starts.
</div>

You can also ask Yak to install a specific version.

```commandline
> "C:\Program Files\Rhino 6\System\Yak.exe" install marmoset 1.0.0

...
```

The package is installed to a special folder, similar to the Grasshopper
Libraries folder but with a folder/file structure that Yak controls.


## Uninstall

Packages can also be easily uninstalled using the Yak CLI tool.

```commandline
> "C:\Program Files\Rhino 6\System\Yak.exe" uninstall marmoset

marmoset successfully uninstalled
```

<div class="alert alert-info" role="alert">
<strong>Note:</strong> Rhino will register that the package has been uninstalled
the next time it starts.
</div>


## List

At any point you can check which packages are currently installed.

```commandline
> "C:\Program Files\Rhino 6\System\Yak.exe" list

marmoset (1.0.0)
```

---

## Related Topics

- [Yak Guides and Tutorials]({{ site.baseurl }}/guides/yak/)
- [Creating a Grasshopper Plug-in Package]({{ site.baseurl }}/guides/yak/creating-a-grasshopper-plugin-package/)
- [Creating a Rhino Plug-in Package]({{ site.baseurl }}/guides/yak/creating-a-rhino-plugin-package/)
