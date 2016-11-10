---
title: openNURBS Latest Release Notes
description: This brief guide covers what is new in the latest update to openNURBS 11-July-2013.
authors: ['Dale Lear']
author_contacts: ['dalelear']
apis: ['openNURBS']
languages: ['C/C++']
platforms: ['Windows', 'Mac']
categories: ['Overview']
origin: http://wiki.mcneel.com/developer/opennurbs/opennurbs_5_20130711_release_notes
order: 4
keywords: ['openNURBS', 'release', 'notes', 'whats new']
layout: toc-guide-page
---

# {{ page.title }}

{% include byline.html %}

{{ page.description }}

## What's New

### Extrusion object render mesh support

Rhino 5 SR6 saves extrusion object render meshes in *.3dm* files.  The *11-July-2013* openNURBS toolkit reads and writes these meshes.  If you are a developer using openNURBS to read and display *.3dm* files in viewer applications, handle extrusion objects (`ON_Extrusion`) the same way you handle polysurface objects (`ON_Brep`).

Earlier versions of Rhino simply calculated extrusion object render meshes as needed.  They did not save them in *.3dm* files.  openNURBS toolkit users had to write their own extrusion object meshing code.

### Strings and Unicode

- Fixes and enhancements for parsing and converting strings in UTF-8, UTF-16, and UTF-32 formats.
- All openNURBS code treats char strings as UTF-8 encoded unicode strings.
- All openNURBS code treats wchar_t strings as UTF-X encoded in native CPU byte order, where `X = 8*sizeof(wchar_t)`. (UTF-16 on Microsoft Windows 2000 or later, UTF-32 on Apple macOS).
- If you encounter [mojibake](https://en.wikipedia.org/wiki/Mojibake) when working with strings in openNURBS, make sure you are using them as UTF-X encoded unicode strings.

### More sample files

Files containing extrusion objects with render meshes were added to the collection of *.3dm* example files.

## Why this release?

We delayed the public distribution of the 11-July-2013 openNURBS toolkit until we released Rhino 5 SR6 in October of 2013.  Rhino 5 SR6 is the first version of Rhino to save extrusion object render meshes.  We felt that publishing an openNURBS toolkit with the ability to read information that the shipping version of Rhino 5 could not create or use would be more frustrating and confusing than helpful.
