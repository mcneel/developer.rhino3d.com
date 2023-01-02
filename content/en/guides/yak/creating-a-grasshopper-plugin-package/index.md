+++
aliases = ["/5/guides/yak/creating-a-grasshopper-plugin-package/", "/6/guides/yak/creating-a-grasshopper-plugin-package/", "/7/guides/yak/creating-a-grasshopper-plugin-package/", "/wip/guides/yak/creating-a-grasshopper-plugin-package/"]
authors = [ "will" ]
categories = [ "Getting Started" ]
description = "This is a step by step guide to creating a package for a Grasshopper plug-in (.gha)."
keywords = [ "developer", "yak" ]
sdk = [ "Yak" ]
title = "Creating a Grasshopper Plug-In Package"
type = "guides"
weight = 10
override_last_modified = "2021-02-04T18:27:17Z"

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

The [Package Manager](../yak/) is a new feature in Rhino 7 WIP. It makes it easier to discover, install and manage Grasshopper plug-ins from within Rhino. This guide will describe how to create a package from a Grasshopper plug-in that can be published to the package server.

{{< call-out "note" "Note" >}}
The package manager is cross-platform. The examples below are for Windows.
For Mac, replace the path to the Yak CLI tool with
<code>"/Applications/Rhino {{< latest-rhino-version >}}.app/Contents/Resources/bin/yak"</code>.
{{< /call-out >}}



First, let's assume you have a folder on your computer which contains all the
files that you would like to distribute in your package. Something like this...

```commandline
C:\Users\Bozo\dist
├── Marmoset.gha
├── Marmoset.dll
├── icon.png
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
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" spec

Inspecting content: Marmoset.gha

---
name: marmoset
version: 1.0.0
authors:
- Park Ranger
description: >
  This plug-in does something. I'm not really sure exactly what it's supposed to
  do, but it does it better than any other plug-in.
url: https://example.com


Saved to C:\Users\Bozo\dist\manifest.yml
```

The `spec` command takes a look at the current directory and, if present, will
glean useful information from the `.gha` assembly and use it generate a
`manifest.yml` with name, version, authors, etc. pre-populated. If you haven't
added this information, then placeholders will be used.

{{< call-out "note" "Note" >}}
The `spec` command is useful for generating the
manifest.yml file initially. Once you have one, keep it with your project and
update it for each release.
{{< /call-out >}}

Open the manifest file with your [favourite editor](https://code.visualstudio.com)
and fill in the gaps.

Afterwards, you should have something that looks a little like this...

```yaml
---
name: marmoset
version: 1.0.0
authors:
- Park Ranger
description: >
  This plug-in does something. I'm not really sure exactly what it's supposed to
  do, but it does it better than any other plug-in.
url: https://example.com
icon: icon.png
keywords:
- mammal
```

Now that we have a manifest file, we can build the package!

```commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" build

Building package from contents of C:\Users\Bozo\dist

Found manifest.yml for package: marmoset (1.0.0)
Inspecting content: Marmoset.gha
Creating marmoset-1.0.0-rh6_18-any.yak

---
name: marmoset
version: 1.0.0
authors:
- Will Pearson
description: >
  This plug-in does something. I'm not really sure exactly what it's supposed to
  do, but it does it better than any other plug-in.
url: example.com
keywords:
- mammal
- guid:c9beedb9-07ec-4974-a0a2-44670ddb17e4

C:\Users\Bozo\dist\marmoset-1.0.0-rh6_18-any.yak
├── Marmoset.dll
├── Marmoset.gha
├── manifest.yml
├── misc\LICENSE.txt
└── misc\README.md
```

{{< call-out "note" "Note" >}}
The filename includes a <a href="../the-anatomy-of-a-package#distributions" class="alert-link">"distribution tag"</a> (in this case <code>rh6_18-any</code>). The first part, <code>rh6_18</code>, is inferred from the version of Grasshopper.dll or Rhinocommon.dll that is referenced in the plug-in project. The second part, <code>any</code>, refers to the platform that the plug-in is intended for. To build a platform-specfic package, run the <code>build</code> command again with the <code>&#45;&#45;platform &lt;platform&gt;</code> argument, where <code>&lt;platform&gt;</code> can be either <code>win</code> or <code>mac</code>.
{{< /call-out >}}

{{< call-out "warning" "Warning" >}}
Currently, if you publish a package with a <code>rh6*</code> distribution tag, it will not be installable for Rhino 7. If your plug-in also works in Rhino 7, please mark it as compatible by copying the .yak file, updating the distribution tag part of the filename (i.e. <code>rh6_18</code> ➡ <code>rh7_0</code>) and <a href="../pushing-a-package-to-the-server" class="alert-link">pushing both to the package server</a>.
{{< /call-out >}}

{{< call-out "note" "Note" >}}
You might notice your plug-in's GUID lurking in the
keywords. More information on how this is used can be found in the
<a href="../package-restore-in-grasshopper" class="alert-link">"Package Restore in Grasshopper"
</a> guide.
{{< /call-out >}}

Congratulations! 🙌 You've just created a package for your Grasshopper plug-in.

## Next Steps

Now that you've created a package, [push it to the package server](../pushing-a-package-to-the-server) to make it
available in the package manager!

## Related Topics

- [Package Manager Guides and Tutorials](/guides/yak/)
- [Creating a Rhino Plug-in Package](/guides/yak/creating-a-rhino-plugin-package/)
- [Package Restore in Grasshopper](/guides/yak/package-restore-in-grasshopper/)
- [Grasshopper: Your First Component (Windows)](/guides/grasshopper/your-first-component-windows/)
- [Grasshopper: Your First Component (Mac)](/guides/grasshopper/your-first-component-mac/)
