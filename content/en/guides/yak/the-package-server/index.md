+++
authors = [ "will" ]
categories = [ "Fundamentals" ]
description = "This guide introduces the Rhino Package Manager server - https://yak.rhino3d.com"
keywords = [ "yak" ]
sdk = [ "Yak" ]
title = "The Package Server"
type = "guides"
weight = 1

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

We host a public package server for everyone to use. You don't need to configure anything. Both the Yak CLI tool and Rhino already know where to look.

Packages shared on the public package server are free to download and install. They may be free to use or require a license – see the [Cloud Zoo](/guides/rhinocommon/cloudzoo/cloudzoo-overview/) and [Zoo](/guides/rhinocommon/rhinocommon-zoo-plugins/) guides for ways to implement licensing in your plug-in using our tools.

Below are a few useful facts about our package server.

## Authentication and authorization

Authentication, provided by [Rhino Accounts](https://accounts.rhino3d.com), is only required for [publishing packages](../pushing-a-package-to-the-server), not for downloading/installing.

Once a package author has published a package, only they can publish future versions using the same package name.

{{< call-out "note" "Note" >}}
Functionality to add "collaborators" will be added in the future.
{{< /call-out >}}

## Conventions

The package server has a few conventions that must be followed.

### Naming

Package names are pretty strict. They only allow letters, numbers, hyphens and underscores, e.g. `Hello_World` or `hello-world1`.

Package names adopt the case used in the very first version that was uploaded. Future uploads ignore the case of the package name and all queries are case-insensitive.

### Versioning

Package version numbers must either follow [Semantic Versioning 2.0.0](http://semver.org/spec/v2.0.0.html) (e.g. `1.1.0-beta`) or `System.Version` a.k.a. Microsoft's four-digit standard (e.g. `1.2.3.4`).

It's recommended to use Semantic Versioning because it allows package authors to specify prerelease versions. These are handy for limited testing, since by default the latest _stable_ version is installed.

Four-digit version numbers were added in v0.8 (August 2019) to support existing plug-ins that use `System.Version`-style version numbers. They do not support pre-release or build metadata.

#### Partial version numbers and normalisation

When a package is created you may notice that the version number in the filename is different to the one in `manifest.yml`. This is due to version number normalisation. This same process happens behind the scenes on the package server and is done to avoid ambiguity between semantically equivalent versions.

There are two cases where version numbers can be semantically equivalent.

* Semantic versions that only differ in build metadata[^1], i.e. `1.0.0+build.1` and `1.0.0+build.2`
* A four-digit version and semantic version that are identical except for a "0" fourth digit (no prerelease or build metadata), e.g. `1.2.3` and `1.2.3.0`

Normalisation is different to expansion of partial (e.g. `1.0`) version numbers. Partial versions numbers are expanded and stored in their full form. For example, if you upload a package as `1.0`, it will actually be saved as `1.0.0`. Subsequently, any requests (REST, CLI, etc.) for version `1.0` will be automatically redirected.

[^1]: [_"Build metadata MUST be ignored when determining version precedence. Thus two versions that differ only in the build metadata, have the same precedence."_](https://semver.org/#spec-item-10)