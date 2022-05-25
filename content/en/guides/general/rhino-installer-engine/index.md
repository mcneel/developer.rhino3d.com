+++
authors = [ "brian", "will" ]
categories = [ "Fundamentals" ]
description = "This guide is a brief introduction to the Rhino Installer Engine."
keywords = [ "developer", "rhino", "installer" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "Rhino Installer Engine"
type = "guides"
weight = 6

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinoinstallerengine/overview"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

{{< call-out "warning" "Warning" >}}
⚠️ This technology is obsolete as of Rhino 7 and has been replaced by the <a href="/guides/yak/">yak format along with the PackageManager.</a>
{{< /call-out >}}

## Overview (Windows)

The Rhino Installer Engine simplifies distribution, installation and updating of plug-ins for Rhino for Windows.

## How It Works

### File and folder structure

A Rhino Installer package is a zip file with an *.rhi* extension. The package can include more than one version of a plug-in however all versions must share the same GUID (i.e. they're different versions of the _same_ plug-in).

There are no file structure or naming requirements. For example the two packages below are functionally equivalent. Both contain versions of "Marmoset" – a fictitious C++ plug-in compiled for Rhino 5 (32-bit and 64-bit) and Rhino 6[^1].

```
Marmoset_tree.rhi/
├── Rhino 6/
│   ├── Marmoset.rhp
│   ├── Marmoset.dll
│   └── Marmoset.rui
└── Rhino 5.0/
    ├── x86/
    │   ├── Marmoset.rhp
    │   └── ...
    └── x64/
        ├── Marmoset.rhp
        └── ...
```

```
Marmoset_flat.rhi/
├── Marmoset_rhino6.rhp
├── Marmoset_rhino5_x86.rhp
├── Marmoset_rhino5_x64.rhp
├── Marmoset_rhino6.dll
├── ...
└── Marmoset.rui
```

You can include anything you want in the *.rhi* package – supporting DLLs, help files, documentation, [toolbar (*.rui*) files](/guides/rhinocommon/create-deploy-plugin-toolbar.md), etc. The entire contents are unzipped to a directory on the user's machine.

### Installation and compatibility

The Rhino Installer Engine examines each *.rhp* file and extracts the plugin GUID, Title, Version, the SDK used (e.g. RhinoCommon, C++) and the SDK version. This information is used to determine which version of the plug-in will be installed for which installed version of Rhino for Windows; the newest compatible plugin is registered with the corresponding version of Rhino. RhinoCommon plug-ins compiled as `AnyCPU` will be installed for both 32- and 64-bit Rhino 5[^1].

{{< call-out "note" "Note" >}}
<strong>Since Rhino 6:</strong> Where a RhinoCommon plug-in is found that has been compiled against an earlier _major_ version of Rhino than is installed, an in-depth compatibility check will be performed to determine whether the SDK of the installed Rhino still supports the functionality used by the plug-in. If the check is successful then the outdated plug-in will be installed.
{{< /call-out >}}

## Limitations

- The Rhino Installer Engine will copy files from the *.rhi* archive, and will register the plug-ins it finds. No other execution is done.
- Currently, it is not possible to digitally sign *.rhi* files in order to verify the source of *.rhi* files.
- The Rhino Installer Engine is available with Rhino 5 and later.

## Related Topics

- [Plugin Installers (Windows)](/guides/rhinocommon/plugin-installers-windows)
- [Plugin Installers (Mac)](/guides/rhinocommon/plugin-installers-mac)

**Footnotes**

[^1]: Since version 6 Rhino for Windows has been 64-bit only.
