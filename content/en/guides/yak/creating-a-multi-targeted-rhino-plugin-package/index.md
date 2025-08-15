+++
aliases = ["/5/guides/yak/creating-a-rhino-plugin-package/", "/6/guides/yak/creating-a-rhino-plugin-package/", "/7/guides/yak/creating-a-rhino-plugin-package/", "/wip/guides/yak/creating-a-rhino-plugin-package/"]
authors = [ "callum" ]
categories = [ "Getting Started" ]
description = "This is a step by step guide to creating a package for a Rhino plug-in (.rhp)."
keywords = [ "developer", "yak", "C#", "multi", "target", "C/C++", "plugin", "installer" ]
sdk = [ "Yak", "C#" ]
title = "Creating a Multi-targeted Rhino Plug-In Package"
type = "guides"
weight = 10

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

The [Package Manager](/guides/yak/) was introduced in Rhino 7. It makes it easier to discover, install and manage Rhino plug-ins from within Rhino. This guide will describe how to create a package from a Rhino plug-in that can be published to the package server.

{{< call-out "note" "Note" >}}
The package manager is cross-platform. The examples below are for Windows. For Mac, replace the path to the Yak CLI tool with <code>"/Applications/Rhino {{< latest-rhino-version >}}.app/Contents/Resources/bin/yak"</code>.
{{< /call-out >}}

First, let's assume you have a build directory on your computer which contains all the files that you would like to distribute in your multi-targeted package. Something like below.

```commandline
C:\Users\Bozo\dist\
├───net48                            
│   │   icon.png                     
│   │   Tamarin.rhp                  
│   └───misc                         
│           License.txt              
│           README.md                
└───net7.0                           
    │   icon.png                     
    │   Tamarin.rhp                  
    └───misc                         
            License.txt              
            README.md                
```

{{< call-out "note" "Note" >}}
This is just an example. The only files that matter are Tamarin.rhp and icon.png (we'll reference the icon in the manifest.yml file later).
{{< /call-out >}}

We're going to use the Yak CLI tool to create the package, so open up a Command Prompt and navigate to the directory above.

``` commandline
cd C:\Users\Bozo\dist\
```

Now, we need a `manifest.yml` file! You can easily create your own by studying the [Manifest Reference Guide](../the-package-manifest). Alternatively, you can use the `spec` command to generate a skeleton file. We'll do the latter here.

``` commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" spec

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

The `spec` command takes a look at the current directory and, if present, will glean useful information from the `.rhp` assembly and use it generate a `manifest.yml` with name, version, description etc. pre-populated. If you haven't added this information, then placeholders will be used.

The RhinoCommon plug-in inspector extracts the assembly attributes that you set when creating your plug-in. The `AssemblyInformationalVersion` attribute is used to populate the version field, since this attribute isn't bound to the Microsoft four-digit version spec and can contain a SemVer-compatible version string. The `AssemblyVersion` attribute is used as a fallback.

{{< call-out "note" "Note" >}}
The `spec` command is useful for generating the manifest.yml file initially. Once you have one, keep it with your project and update it for each release.
{{< /call-out >}}

Next, open the manifest file with your [favourite editor](https://code.visualstudio.com) and fill in the gaps.

Afterwards, you should have something that looks a little like this...

``` yaml
---
name: tamarin
version: 1.0.0
authors:
- Park Ranger
description: >
  This plug-in does something. I'm not really sure exactly what it's supposed to
  do, but it does it better than any other plug-in.
url: https://example.com
icon: icon.png
keywords:
- something
```

Now that we have a manifest file, we can build the package!

``` commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" build

Building package from contents of C:\Users\Bozo\dist

Found manifest.yml for package: tamarin (1.0.0)
Inspecting content: Tamarin.rhp
Creating tamarin-1.0.0-rh8_0-any.yak

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

C:\Users\Bozo\dist\tamarin-1.0.0-rh8_0-any.yak
├── manifest.yml
├── net48/
│   ├── Tamarin.dll
│   ├── Tamarin.rhp
│   ├── icon.png
│   └── misc/
│       ├── License.txt
│       └── README.md
└── net7.0/
    ├── Tamarin.dll
    ├── Tamarin.rhp
    ├── icon.png
    └── misc/
        ├── License.txt
        └── README.md
```

{{< call-out "note" "Note" >}}
The filename includes a <a href="../the-anatomy-of-a-package#distributions" class="alert-link">"distribution tag"</a> (in this case <code>rh8_0-any</code>). The first part, <code>rh8_0</code>, is inferred from the version of Rhinocommon.dll or Rhino C++ SDK that is referenced in the plug-in project. The second part, <code>any</code>, refers to the platform that the plug-in is intended for. To build a platform-specfic package, run the <code>build</code> command again with the <code>&#45;&#45;platform &lt;platform&gt;</code> argument, where <code>&lt;platform&gt;</code> can be either <code>win</code> or <code>mac</code>.
{{< /call-out >}}

{{< call-out "note" "Note" >}}
You might notice your plug-in's GUID lurking in the keywords. More information on how this is used can be found in the <a href="../package-restore-in-grasshopper" class="alert-link">"Package Restore in Grasshopper"</a> guide.
{{< /call-out >}}

Congratulations! 🙌 You've just created a multi-targeted package for your Rhino plug-in.

## Next Steps

Now that you've created a package, [push it to the package server](../pushing-a-package-to-the-server) to make it available in the package manager!

## Related Topics

- [Creating a Grasshopper Plug-in Package](/guides/yak/creating-a-grasshopper-plugin-package/)
- [RhinoCommon: Your First Plugin (Windows)](/guides/rhinocommon/your-first-plugin-windows)
- [RhinoCommon: Your First Plugin (Mac)](/guides/rhinocommon/your-first-plugin-mac)
- [Creating your first C/C++ plugin for Rhino](/guides/cpp/your-first-plugin-windows/)
