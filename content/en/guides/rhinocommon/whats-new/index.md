+++
authors = [ "steve" ]
categories = [ "Overview" ]
description = "This brief guide outlines the changes in the RhinoCommon SDK."
keywords = [ "C#", "plugin" ]
languages = [ "C#" ]
sdk = [ "RhinoCommon" ]
title = "What's New?"
type = "guides"
weight = 2

[admin]
TODO = "needs review"
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

The following document describes what has been added, what has changed, and how to deal with these changes in the RhinoCommon SDK. A lot of effort has been put into keeping the RhinoCommon SDK in Rhino 6 as compatible with the Rhino 5 version as possible, but in a small number of cases this was impossible. One goal of this document is to describe these breaking changes and what to do about them.

## Additions

TODO: what has been added?

## Changes

- InstanceDefinition and InstanceDefinitionGeometry are no longer derived from GeometryBase
  - https://mcneel.myjetbrains.com/youtrack/issue/RH-34036
  - TODO: describe what this means
