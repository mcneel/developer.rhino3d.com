---
title: Picking Brep Components
description: This brief guide discusses picking components of a Brep using C/C++.
author: ['Dale Fugier', '@dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/sdksamples/pickfaceedge
order: 1
keywords: ['rhino', 'picking', 'brep']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## Problem

You would like to pick a brep component (e.g. face or edge) and then take action depending on what was picked.  If you write an object picker as such:

```cpp
CRhinoGetObject go;
go.SetCommandPrompt( L"Select face or edge" );
go.SetGeometryFilter( CRhinoGetObject::surface_object |
CRhinoGetObject::edge_object );
go.EnableSubObjectSelect( true );
go.GetObjects( 1, 1 );
```

and then use it to try to pick the edge of a box, for example, only the faces show up on the "choose one object" menu.

## Solution

You need to enable "choose one question" to get multiple subobject types on one brep to work.  So, this should work:

```cpp
CRhinoGetObject go;
go.SetCommandPrompt( L"Select face or edge" );
go.SetGeometryFilter( CRhinoGetObject::surface_object |
CRhinoGetObject::edge_object );
go.EnableSubObjectSelect( true );
go.EnableChooseOneQuestion( true ); // ADD THIS...
go.GetObjects( 1, 1 );
```
