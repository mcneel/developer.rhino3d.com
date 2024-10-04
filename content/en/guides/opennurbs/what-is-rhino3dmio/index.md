+++
aliases = ["/en/5/guides/opennurbs/what-is-rhino3dmio/", "/en/6/guides/opennurbs/what-is-rhino3dmio/", "/en/7/guides/opennurbs/what-is-rhino3dmio/", "/wip/guides/opennurbs/what-is-rhino3dmio/"]
authors = [ "dan" ]
categories = [ "Overview" ]
description = "This guide covers Rhino3dm builds of openNURBS."
keywords = [ "openNURBS", "C#", ".NET", "Rhino3dm", "Python", "JavaScript" ]
languages = [ "C/C++", "C#" ]
sdk = [ "openNURBS" ]
title = "What is Rhino3dm?"
type = "guides"
weight = 2

[admin]
TODO = ""
origin = "https://github.com/mcneel/rhinocommon/wiki/Rhino3dmIO-Toolkit-(OpenNURBS-build)"
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

Rhino3dm is a set of libraries based on the [OpenNURBS](/guides/opennurbs/what-is-opennurbs) geometry library. They provide the ability to access and manipulate geometry through .NET, Python or JavaScript applications independent of Rhino.

Functionality includes:

- Create, interrogate, and store all geometry types supported in Rhino. This includes points, point clouds, NURBS curves and surfaces, polysurfaces (BReps), meshes, annotations, extrusions, and SubDs.
- Work with non-geometry classes supported in Rhino like layers, object attributes, transforms and viewports.
- Read and write all of the above information to and from the .3dm file format.
- Use as a client to make calls into the [Rhino.Compute](/guides/compute/) cloud server for advanced manipulation of geometry objects.
- Available on most platforms (Windows, macOS, Linux).

Rhino3dm is [open source](https://github.com/mcneel/rhino3dm).

Explore all of the rhino3dm samples: [rhino3dm samples](https://github.com/mcneel/rhino-developer-samples/tree/8/rhino3dm)

<div class="bs-callout bs-callout-danger">
  <h4>WARNING</h4>
  <p>Rhino3dm is NOT meant for any Rhino plug-in development. You should only be using Rhino3dm if you are attempting to read/write 3dm files from an application other than Rhino!</p>
</div>

Rhino3dm comes in three flavors.

## Rhino3dm.py

[Rhino3dm.py](https://pypi.org/project/rhino3dm/) is a Python package that can be used on all current versions of CPython (3.7 - 3.11) and is available on all platforms (Windows, macOS, Linux).

Rhino3dm.pys packages are available on the [Python Package Index (PyPI)](https://pypi.org/project/rhino3dm/).

See our [Python documentation](https://github.com/mcneel/rhino3dm/blob/main/docs/python/RHINO3DM.PY.md) for details.

## Rhino3dm.js

[Rhino3dm.js](https://www.npmjs.com/package/rhino3dm) is a JavaScript library with an associated web assembly (rhino3dm.wasm). Rhino3dm.js should run on all major browsers as well as [node.js](https://nodejs.org).

Rhino3dm.js packages are available on [npm](https://www.npmjs.com/package/rhino3dm).

See our [JavaScript documentation](https://github.com/mcneel/rhino3dm/blob/main/docs/javascript/RHINO3DM.JS.md) for details.

## Rhino3dm.NET

[Rhino3dm.NET](https://www.nuget.org/packages/Rhino3dm/), formerly known as Rhino3dmIO, allows you to write standalone .NET applications.

Rhino3dm.NET packages are available on [NuGet](https://www.nuget.org/packages/Rhino3dm/).
