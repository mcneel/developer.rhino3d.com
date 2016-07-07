---
title: Supporting High DPI Displays
description: This guide discusses the support of high resolution monitors.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Advanced']
order: 1
keywords: ['C/C++', 'Rhino', 'Plugin']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## Overview

Super high resolution displays are now common on Windows-based systems, and those using Rhino expect it and 3rd party plug-ins to display correctly on them. Plug-in developers need to make sure their applications are DPI–aware. DPI-aware plug-ins adjust UI elements to scale appropriately to the system DPI. Plug-ins that are not DPI–aware, but are running on a high-DPI display setting, can suffer from many visual artifacts, including incorrect scaling of UI elements, clipped text, and blurry images.

Plug-in developers should run Rhino on high-DPI displays so they can find and fix display issues. Here is how you can configure Windows for high-DPI display:

### Windows 10

1. Right-click on your desktop and click **Display settings**.
1. Use the slider to select the text scaling and click **Apply**.
1. Logout of Windows and log back in.

### Windows 8/8.1

1. Right-click on your desktop and click **Screen resolution**.
1. Click the **Make text and other items larger or smaller**.
1. Use the slider to select the text scaling and click **Apply**.
1. Logout of Windows and log back in.

### Windows 7

1. Right-click on your desktop and click *Screen resolution**.
1. Click **Make text and other items larger or smaller**.
1. Select the text scaling and click **Apply**.
1. Logout of Windows and log back in.

## Common Issues

Most high DPI issues that plug-ins will encounter are due to owner-drawn control. Here, developers have hard-coded sizes or locations, assuming the standard DPI setting. In these cases, custom drawn elements don’t appear correctly, or custom controls don’t work properly.

Other issues have to do with the use of bitmaps or icons that are too small at higher DPI settings or that don’t scale well.

The Rhino SDK has some new tools that developers can use to help make UI elements DPI-aware. See the ```CRhinoDpi``` class declaration in ```RhinoSdkDpi.h``` for more information.

### General

The ```CRhinoDpi``` class contains several static function to help with DPI-aware issues.

```CRhinoDpi::DpiScale``` returns the display DPI scale factor when Rhino started. Use this value as a multiplier when owner drawing.

```CRhinoDpi::Scale``` scales a value by the current DPI scale factor.

### Icons

Windows recommends that icon resources contain the following sizes: 16, 32, 48, and 256. All of the icon files (ICO) used by Rhino have been updated to support these sizes.

When loading icons, use ```CRhinoDpi::LoadIcon```. For example:

```cpp
virtual HICON Icon()
{ 
  const int const_icon_size = 24;
  int icon_size = CRhinoDpi::Scale(const_icon_size);
  return CRhinoDpi::LoadIcon(AfxGetInstanceHandle(), IDI_ICON, icon_size);
}
```

and:

```cpp
virtual HICON Icon(const CSize& size) const
{ 
  return CRhinoDpi::LoadIcon(AfxGetInstanceHandle(), IDI_ICON, size.cx, size.cy);
}
```

Note, if the requested icon is not a standard size, the ```CRhinoDpi::LoadIcon``` function scales down a larger image.
