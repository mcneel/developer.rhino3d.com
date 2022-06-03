+++
authors = [ "will" ]
categories = [ "Getting Started" ]
description = "This is a step by step guide to installing and uninstalling a Yak package using the CLI."
keywords = [ "developer", "yak" ]
sdk = [ "Yak" ]
title = "Installing and Managing Packages"
type = "guides"
weight = 30
override_last_modified = "2020-11-12T12:17:36Z"

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

{{< call-out "note" "Note" >}}
Yak is cross-platform. The examples below are for Windows.
For Mac, replace the path to the Yak CLI tool with
<code>"/Applications/Rhino {{< latest-rhino-version >}}.app/Contents/Resources/bin/yak"</code>.
{{< /call-out >}}



## Install

Installing a yak package with the CLI tool is simple.

```commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" install marmoset

Downloading marmoset (1.0.0)...
Downloaded marmoset (1.0.0)
Installing marmoset (1.0.0)...
Successfully installed marmoset (1.0.0)
```

{{< call-out "note" "Note" >}}
Rhino will load new packages the next time it starts.
{{< /call-out >}}

You can also ask Yak to install a specific version.

```commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" install marmoset 1.0.0

...
```

The package is installed to a special folder, similar to the Grasshopper
Libraries folder but with a folder/file structure that Yak controls.


## Uninstall

Packages can also be easily uninstalled using the Yak CLI tool.

```commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" uninstall marmoset

marmoset successfully uninstalled
```

{{< call-out "note" "Note" >}}
Rhino will register that the package has been uninstalled
the next time it starts.
{{< /call-out >}}


## List

At any point you can check which packages are currently installed.

```commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" list

marmoset (1.0.0)
```

## Related Topics

- [Yak Guides and Tutorials](/guides/yak/)
- [Creating a Grasshopper Plug-in Package](/guides/yak/creating-a-grasshopper-plugin-package/)
- [Creating a Rhino Plug-in Package](/guides/yak/creating-a-rhino-plugin-package/)
