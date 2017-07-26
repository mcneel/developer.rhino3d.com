---
title: Creating a Grasshopper Plug-In Package
description: >
  This is a step by step guide to creating a package for a Grasshopper plug-in.
authors: ['Will Pearson']
author_contacts: ['will']
sdk: ['Yak']
languages: # empty
platforms: ['Windows']
categories: ['Step By Step']
order: 1
keywords: ['developer', 'yak']
layout: toc-guide-page
---

<div class="bs-callout">

<strong>Note</strong>: Yak is cross-platform. Not everything is hooked up on the Mac side
yet, however. So, for now, this guide is aimed at <strong>Windows users only</strong>.

</div>

<!-- The Yak CLI tool is located at `C:\Program Files\Rhino WIP\System\Yak.exe`. -->

First, let's assume you have a folder on your computer which contains all the
files that you would like to distribute in your package. Some like this...

```commandline
C:\Users\Bozo\dist
├── Marmoset.gha
├── Marmoset.dll
└── misc/
    ├── README.md
    └── LICENSE.txt
```

We're going to use the Yak CLI tool to create the package, so open up a Command
Prompt and navigate to the directory above.

```commandline
> cd C:\Users\Bozo\dist
```

Now, we need a `manifest.yml` file! You can easily create your own by studying
the [reference](../the-package-manifest). Alternatively, you can use the `spec`
command to generate a skeleton file. We'll do the latter here.

```commandline
> "C:\Program Files\Rhino WIP\System\Yak.exe" spec

Found a Grasshopper plug-in: Plankton.gha

---
name: marmoset
version: 1.0.0
authors:
- <author>
description: <description>
url: <url>
secret:
  id: 8dd38fd1-c572-dc53-ab35-c82d14e1ed08


Saved to C:\Users\Bozo\dist\manifest.yml
```

The `spec` command takes a look at the current directory and, if present, will
glean useful information from the `.gha` assembly and use it generate a
`manifest.yml` with name, version, authors, etc. pre-populated. If you haven't
added this information, then placeholders will be used.

<div class="bs-callout">

<strong>Note</strong>: You might notice your plug-in's GUID lurking in the
<code>secret/id</code> key. More information on how this is used can be found in
the <a href="../package-restore-in-grasshopper">"Package Restore in Grasshopper"
</a> guide.

</div>

Open the manifest file with your [favourite editor](http://atom.io) and fill in
the gaps.
