---
title: Setting Viewport Titles
description: This brief guide demonstrates how to set the title of a viewport using C/C++.
authors: ['dale_fugier']
author_contacts: ['dale']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/sdksamples/setviewname
order: 1
keywords: ['rhino', 'viewport']
layout: toc-guide-page
---

 
## Problem

You would like to change the name, or title, or a viewport using the the Rhino C/C++ SDK.  For example, you would like to rename the "Front" viewport to say "Facade."

## Solution

To change the title of a viewport, use `CRhinoViewport::SetName`.  A Rhino view contains a "main viewport" that fills the entire view client window.  To get a view's main viewport, you can call `CRhinoView::MainViewport`.

For example:

```cpp
CRhinoView* view = RhinoApp().ActiveView();
if (view)
  view->MainViewport().SetName("Facade");
```
