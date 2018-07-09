---
title: The Package Manifest
description: What is a 'package manifest' and what should it include?
authors: ['Will Pearson']
author_contacts: ['will']
sdk: ['Yak']
languages: # empty
platforms: ['Windows', 'Mac']
categories: ['Fundamentals']
order: 1
keywords: ['developer', 'yak']
layout: toc-guide-page
---

## Overview

Each package should have a manifest file containing a spec that can be distilled into the database when the package is pushed to the server. The manifest should be written in [YAML](http://www.yaml.org), following the structure of the example below.

The manifest file should be named `manifest.yml` and should live in the root of the zipped package (renamed to \*.yak or whatever).

The manifest's purpose is to help with streamlining (and potentially automating) the process of releasing packages, removing the need for any web forms when publishing packages.

**Required Attributes**
 - [Name](#name)
 - [Version](#version)
 - [Authors](#authors)
 - [Description](#description)

**Recommended Attributes**
 <!-- - [`license`](#license) -->
 - [URL](#url)

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

The version string given to the package, adhering strictly to [SemVer 2.0.0](http://semver.org/spec/v2.0.0.html). We've adopted SemVer to make ordering straightforward and also for easy identification of pre-release versions – handy when releasing beta plug-ins for limited testing! 

Partial version numbers are expanded to the full `major.minor.patch` by the server, e.g. `0.1 -> 0.1.0`.

```yaml
version: 0.3.4
```

For specific questions about versioning, please direct those to the [Yak Forum](https://discourse.mcneel.com/c/serengeti/yak)

### Authors

A list of author(s) of the package.

```yaml
authors:
  - Daniel Piker
  - Will Pearson
```

Being a YAML format, a single author would look have this syntax:

```yaml
authors:
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
```


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

A webpage for the package. This can be any URL that may be used by customer for contact information, forums, tutorials or any other information about the plugin.

<!-- NOTE: I'm thinking that, where this is a github repository, there is the possibility to build direct from HEAD. -->

```yaml
url: "https://github.com/meshmash/Plankton"
```


<!-- ## Optional Attributes

### Dependencies

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
​``` -->

---

## Related Topics

- [Yak Guides and Tutorials]({{ site.baseurl }}/guides/yak/)
- [Anatomy of a Package]({{ site.baseurl }}/guides/yak/the-anatomy-of-a-package/)
- [Yak CLI Reference]({{ site.baseurl }}/guides/yak/yak-cli-reference)

```