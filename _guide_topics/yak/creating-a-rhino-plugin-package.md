---
title: Creating a Rhino Plug-In Package
description: This is a step by step guide to creating a package for a Rhino plug-in.
authors: ['will_pearson']
sdk: ['Yak']
languages: # empty
platforms: ['Windows']
categories: ['Step By Step']
origin: unset
order: 1
keywords: ['developer', 'yak']
layout: toc-guide-page
---

<div class="alert alert-info" role="alert">
<strong>Note:</strong> Yak is cross-platform. The examples below are for Windows.
For Mac, replace the path to the Yak CLI tool with
<code>/Applications/RhinoWIP.app/Contents/Resources/bin/yak</code>.
</div>

First, let's assume you have a folder on your computer which contains all the
files that you would like to distribute in your package. Something like this...

```commandline
C:\Users\Bozo\dist
├── Tamarin.rhp
├── Tamarin.dll
└── misc\
    ├── README.md
    └── LICENSE.txt
```

We're going to use the Yak CLI tool to create the package, so open up a Command
Prompt and navigate to the directory above.

```commandline
> cd C:\Users\Bozo\dist
```

Now, we need a `manifest.yml` file! You can easily create your own by studying
the [Manifest Reference Guide](../the-package-manifest). Alternatively, you can use the `spec`
command to generate a skeleton file. We'll do the latter here.

```commandline
> "C:\Program Files\Rhino 7 WIP\System\Yak.exe" spec

Inspecting content: Tamarin.rhp

---
name: tamarin
version: 1.0.0
authors:
- Park Ranger
description: An example RhinoCommon plug-in
url: https://example.com


Saved to C:\Users\Bozo\dist\manifest.yml
```

The `spec` command takes a look at the current directory and, if present, will
glean useful information from the `.rhp` assembly and use it generate a
`manifest.yml` with name, version, description etc. pre-populated. If you haven't
added this information, then placeholders will be used.

The RhinoCommon plug-in inspector extracts the assembly attributes that you set
when creating your plug-in. The `AssemblyInformationalVersion` attribute is used
to populate the version field, since this attribute isn't bound to the Microsoft
four-digit version spec and can contain a SemVer-compatible version string. The
`AssemblyVersion` attribute is used as a fallback.

Next, open the manifest file with your [favourite editor](https://code.visualstudio.com)
and fill in the gaps.

Afterwards, you should have something that looks a little like this...

```yaml
---
name: tamarin
version: 1.0.0
authors:
- Park Ranger
description: >
  This plug-in does something. I'm not really sure exactly what it's supposed to
  do, but it does it better than any other plug-in.
url: https://example.com
keywords:
- something
```

Now that we have a manifest file, we can build the package!

```commandline
> "C:\Program Files\Rhino 7 WIP\System\Yak.exe" build

Building package from contents of C:\Users\Bozo\dist

Found manifest.yml for package: tamarin (1.0.0)
Inspecting content: Tamarin.rhp
Creating tamarin-1.0.0-rh6_18-any.yak

---
name: tamarin
version: 1.0.0
authors:
- Will Pearson
description: >
  This plug-in does something. I'm not really sure exactly what it's supposed to
  do, but it does it better than any other plug-in.
url: https://example.com
keywords:
- something
- guid:c9beedb9-07ec-4974-a0a2-44670ddb17e4

C:\Users\Bozo\dist\tamarin-1.0.0-rh6_18-any.yak
├── Tamarin.dll
├── Tamarin.rhp
├── manifest.yml
└── misc/
    ├── LICENSE.txt
    └── README.md
```

<div class="alert alert-info" role="alert">
<strong>Note:</strong> The filename includes a <a href="../the-anatomy-of-a-package#distributions">"distribution tag"</a> (in this case <code>rh6_18-any</code>). The first part, `rh6_18`, is inferred from the version of Rhinocommon.dll or Rhino C++ SDK that is referenced in the plug-in project. The second part, `any`, refers to the platform that the plug-in is intended for. To build a platform-specfic package, run the `build` command again with the `--platform <platform>` argument, where `<platform>` can be either `win` or `mac`.
</div>

<div class="alert alert-info" role="alert">
<strong>Note:</strong> You might notice your plug-in's GUID lurking in the
keywords. More information on how this is used can be found in the
<a href="../package-restore-in-grasshopper">"Package Restore in Grasshopper"
</a> guide.
</div>

Congratulations! 🙌 You've just created a Yak package for your Rhino
plug-in.

---

## Next Steps

Now that you've created a package, why not
[push it to the Yak server](../pushing-a-package-to-the-server) to make it
available to everyone else!
