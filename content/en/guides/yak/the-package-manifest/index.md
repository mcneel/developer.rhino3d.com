+++
aliases = ["/5/guides/yak/the-package-manifest/", "/6/guides/yak/the-package-manifest/", "/7/guides/yak/the-package-manifest/", "/wip/guides/yak/the-package-manifest/"]
authors = [ "will" ]
categories = [ "Fundamentals" ]
description = "What is a 'package manifest' and what should it include?"
keywords = [ "developer", "yak" ]
sdk = [ "Yak" ]
title = "The Package Manifest"
type = "guides"
weight = 1
override_last_modified = "2021-07-21T10:09:56Z"

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

## Overview

Each package should have a manifest file containing a spec that can be distilled into the database when the package is pushed to the server. The manifest should be written in [YAML](http://www.yaml.org), following the structure of the example below.

The manifest file should be named `manifest.yml` and should live in the root of the package. (Don't worry, the Yak CLI tool's [`build` command](/guides/yak/yak-cli-reference#build) takes care of this for you!)

The manifest's purpose is to help with streamlining (and potentially automating) the process of releasing packages, removing the need for any web forms when publishing packages.

**Required Attributes**
 - [Name](#name)
 - [Version](#version)
 - [Authors](#authors)
 - [Description](#description)

**Recommended Attributes**
 <!-- - [`license`](#license) -->
 - [URL](#url)
 - [Keywords](#keywords)
 - [Icon](#icon)

<!-- ### Optional Attributes
 - [`dependencies`](#dependencies) -->

## Example

Here's an example for a Grasshopper plug-in.

```yaml
name: plankton
version: 0.3.4
authors:
  - Daniel Piker
  - Will Pearson
description: >
  Plankton is a flexible and efficient library for handling n-gonal meshes.
  Plankton is written in C# and implements the halfedge data structure. The
  structure of the library is loosely based on Rhinocommon's mesh classes and
  was originally created for use within C#/VB scripting components in
  Grasshopper.
url: "https://github.com/meshmash/Plankton"
```

## Required Attributes

### Name

The short name describing the package. Preferably one world although multiple words can be separated by underscores or hyphens.

_**Note:** Package name can only include letters, numbers, dashes, and underscores_

_**Note 2:** Package names adopt the case used in the very first version that was uploaded. Future uploads ignore the case of the package name and all queries are case-insensitive._

```yaml
name: plankton
```

### Version

_Since 0.8: four-digit version numbers allowed_
_Since 0.9: `$version` placeholder_

The version number given to the package.

Package version numbers **must** either follow [Semantic Versioning 2.0.0](http://semver.org/spec/v2.0.0.html) (e.g. `1.1.0-beta`) or `System.Version` a.k.a. Microsoft's four-digit standard (e.g. `1.2.3.4`). It's recommended to use Semantic Versioning because it allows package authors to specify prerelease versions. These are handy for limited testing, since by default the latest _stable_ version is installed.

To make the authoring process easier, it's possible to replace the version number with `$version` – the version number will be inferred from the contents of the package and substituted during `yak build`.

```yaml
version: 0.3.4
```

### Authors

A list of author(s) of the package.

```yaml
authors:
  - Daniel Piker
  # list additional package authors below
  - Will Pearson
```

### Description

Describe the package. Be as in-depth or as brief as you feel is appropriate.

```yaml
description: This is an awesome package.
```

If you want to write more, you can use use YAML's [folded style](http://www.yaml.org/spec/1.2/spec.html#id2796251).

```yaml
description: >
  This is such an awesome package
  that I'm going to write a whole
  bunch of text describing it!

  This sentence will be on a new line.
```

<!-- Or, if you want to preserve newlines, use the [literal style](https://yaml.org/spec/1.2-old/spec.html#id2795688)

```yaml
description: |
  This is the first line of the description.
  This sentence is (and will be) on a new line!
``` -->


## Recommended Attributes

<!-- ### License

The license for this package. This should be no more than 64 characters and should be one of the standard [SPDX identifiers](spdx.org/licenses/).

```yaml
license: MIT
```

If the intention is to make the package open source then ideally you should pick one that is [OSI (Open Source Initiative)](opensource.org/licenses/alphabetical) approved. The most commonly used OSI approved licenses are BSD-3-Clause and MIT. GitHub also provides a license picker at http://choosealicense.com.

This should just be the name of your license. The full text of the license should be included in the package as `LICENSE[.ext]` (at the top level) when you build it.

You should specify a license for your package so that people know how they are permitted to use it, and any restrictions you're placing on it. Not specifying a license means all rights are reserved; others have no rights to use the code for any purpose. -->

### URL

A webpage for the package. This can be any URL i.e. author contact info, forums, tutorials or any other information about the plugin.

<!-- NOTE: I'm thinking that, where this is a github repository, there is the possibility to build direct from HEAD. -->

```yaml
url: "https://github.com/meshmash/Plankton"
```

### Keywords

A list of keywords that will help users to find the package.

```yaml
keywords:
- one
- two
```

### Icon

An icon file in the package. It should be small (e.g. 64x64) and it must be either a PNG or a JPEG.

```yaml
icon: icon.png
```


<!-- ## Optional Attributes -->

<!-- ### Dependencies

A list of packages upon which this package depends. Can also include optional version specifications, again adhering to Semantic Versioning.

_Not currently used, however the server is capable of storing dependencies so this needs hooking up!_

```yaml
dependencies:
  - name: plankton
    spec: "< 0.4.0, >= 0.3.0"
  - name: package_without_spec
​``` -->


<!--## Alternative (JSON)

​```json
{
  "name": "plankton",
  "version": "0.3.4",
  "author": [
    "Daniel Piker",
    "Will Pearson"
  ],
  "dependencies": [

  ],
  "description": "Plankton is a flexible and efficient library for handling n-gonal meshes. Plankton is written in C# and implements the halfedge data structure. The structure of the library is loosely based on Rhinocommon's mesh classes and was originally created for use within C#/VB scripting components in Grasshopper.",
  "license": "LGPL-3",
  "url": "https://github.com/meshmash/Plankton",
  "type": "gh-plugin"
}
``` -->

## Obsolete Attributes

### Icon URL

{{< call-out "warning" "Warning" >}}
⚠️ Replaced by the <a href="#icon" class="alert-link">icon</a> attribute.
{{< /call-out >}}

Specify a **direct** link to an icon that will be used by the Package Manager in Rhino. It should be small (32x32 is ideal) and it must be either a PNG or a JPEG.

```yaml
icon_url: "https://example.com/path/to/icon.png"
```

## Related Topics

- [Yak Guides and Tutorials](/guides/yak/)
- [Anatomy of a Package](/guides/yak/the-anatomy-of-a-package/)
- [Yak CLI Reference](/guides/yak/yak-cli-reference)

