+++
aliases = ["/en/5/guides/cpp/toggling-status-bar/", "/en/6/guides/cpp/toggling-status-bar/", "/en/7/guides/cpp/toggling-status-bar/", "/en/wip/guides/cpp/toggling-status-bar/"]
authors = [ "dale" ]
categories = [ "Advanced" ]
description = "This brief guide demonstrates how to show or hide the Rhino status bar using C/C++."
keywords = [ "rhino", "status", "toggle" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Toggling the Status Bar"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/showrhinostatusbar"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"
+++

 
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
