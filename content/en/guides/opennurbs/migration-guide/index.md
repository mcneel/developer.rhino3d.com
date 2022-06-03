+++
authors = [ "dalelear" ]
categories = [ "Getting Started" ]
description = "This guide contains information to help you use the current version of openNURBS."
keywords = [ "openNURBS", "migrating", "versions" ]
languages = [ "C/C++" ]
sdk = [ "openNURBS" ]
title = "What's New and Update Guide"
type = "guides"
weight = 2
override_last_modified = "2018-12-05T14:59:06Z"

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

The openNURBS toolkit reads and writes Rhino 3DM files.

To get the current openNURBS toolkit or technical support, visit [openNURBS](https://www.rhino3d.com/opennurbs).

## Updating

For most developers, updating from the previous verson of openNURBS will involve recompiling and minor changes. As before, the easiest way to read a 3DM file is to use one of the ONX_Model::Read() functions. The easiest way to write a 3DM file is to use one of the ONX_Model::Write() functions.

## New Requirements - January 2018

You must use a C++ compiler that supports C++11. Microsoft's Visual Studio 2017 or Apple's XCode 9 support C++11.

## New Features - January 2018


Use iterators to go through the contents of an ONX_Model. For an example, look at the source code for ONX_Model::DumpComponentList() in opennurbs_extensions.cpp.

ON_ComponentManifest is a manifest of every component in a model or 3DM file. It provides simple ways fo find components by id or name. The function ONX_Model.Manifest() returns the manifest of the ONX_Model. When merging models, ON_ManifestMap can be used to efficiently manage name and id collisions.
