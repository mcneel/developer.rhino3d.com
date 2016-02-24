---
title: What's New?
description: This brief guide outlines the new object types and features in the Rhino C/C++ SDK.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Overview']
origin: http://wiki.mcneel.com/developer/rhino/5/sdkfeatures
order: 2
keywords: ['c', 'C/C++', 'plugin']
layout: toc-guide-page
TODO: 'needs review and the original contained links to empty wiki entries.'
---

# What's New?

{{ page.description }}

## Overview

Rhino 5.0 has several new object types and C/C++ SDK features.  Be sure your plugin supports them appropriately.

## New Object Types

### Extrusion Objects

Extrusion objects allow creation of simple extruded shapes using a much more lightweight representation than BRep (polysurface) objects.

Be sure your plugin can handle these extrusion objects.  Download our sample models with extrusion objects in them.

### Double Precision Meshes

Rhino supports double precision meshes.  This allows mesh computations to be more accurate, and also enables display of objects that are very far from the origin (for example, architectural or civil engineering models using state-plane coordinate systems).

Rhino handles conversion between single-precision and double-precision automatically as needed.

## New Annotation Features

Dimension styles, text, and hatches support scale factors.  Rhino also supports scaling for the model-space viewports and in each layout.

If your plugin needs to support these new features, please contact our developer support group for more details.
