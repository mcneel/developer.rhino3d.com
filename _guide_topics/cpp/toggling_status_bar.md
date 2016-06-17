---
title: Toggling the Status Bar
description: This brief guide demonstrates how to show or hide the Rhino status bar using C/C++.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Advanced']
origin: http://wiki.mcneel.com/developer/sdksamples/showrhinostatusbar
order: 1
keywords: ['rhino', 'status', 'toggle']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## Overview

When you run the Options command, all Rhino's options or application settings that you see are maintained by a `CRhinoAppSettings` class stored on the Rhino application object.  This class is a container class as it holds several other `CRhinoApp_xxx_Settings` classes that help to organize all the options.

The process for modifying any Rhino option is:

1. Find the container class in `CRhinoAppSettings` that holds the option you want to change.
1. Make a copy of that container class.
1. Change the appropriate members.
1. Replace Rhino's copy of that container class with yours by calling one of `CRhinoAppSettings`' `Set_xxx_Settings()` member functions.

## Sample

The following sample source code demonstrates how to show or hide Rhino's status bar using the Rhino C/C++ SDK...

```cpp
void ShowRhinoStatusBar( BOOL bShow )
{
  // Copy the CRhinoAppAppearanceSettings class
  CRhinoAppAppearanceSettings settings = RhinoApp().AppSettings().AppearanceSettings( true );
  if( settings.m_show_statusbar != bShow )
  {
    // Modify the desired setting
    settings.m_show_statusbar = bShow;
    // Replace the CRhinoAppAppearanceSettings with the modified version
    RhinoApp().AppSettings().SetAppearanceSettings( settings );
  }
}
```
