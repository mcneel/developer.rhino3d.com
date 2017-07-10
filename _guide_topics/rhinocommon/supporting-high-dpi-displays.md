---
title: Supporting High DPI Displays
description: This guide discusses the support of high resolution monitors.
authors: ['Dale Fugier']
author_contacts: ['dale']
sdk: ['RhinoCommon']
languages: ['C#']
platforms: ['Windows']
categories: ['Advanced']
origin: unset
order: 1
keywords: ['RhinoCommon', 'Rhino', 'Plugin']
layout: toc-guide-page
---

 
## Overview

Super high resolution displays are now common on Windows-based systems, and those using Rhino expect it and 3rd party plugins to display correctly on them. Plugin developers need to make sure their applications are DPI–aware. DPI-aware plugins adjust UI elements to scale appropriately to the system DPI. Plugins that are not DPI–aware, but are running on a high-DPI display setting, can suffer from many visual artifacts, including incorrect scaling of UI elements, clipped text, and blurry images.

Plugin developers should run Rhino on high-DPI displays so they can find and fix display issues. Here is how you can configure Windows for high-DPI display:

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

1. Right-click on your desktop and click **Screen resolution**.
1. Click **Make text and other items larger or smaller**.
1. Select the text scaling and click **Apply**.
1. Logout of Windows and log back in.

## Common WinForms Issues

Most high DPI issues that plugins will encounter are due to owner-drawn control. Here, developers have hard-coded sizes or locations, assuming the standard DPI setting. In these cases, custom drawn elements don’t appear correctly, or custom controls don’t work properly.

Other issues have to do with the use of bitmaps or icons that are too small at higher DPI settings or that don’t scale well.

But WinForms has other challenges too. One observation is that if you spend too much time using the Forms designer, hard-coding font sizes and other values, will will have DPI display issues.

### General

WinForms has its own scaling mechanism which calculates the scaling difference between the system that the form has been designed on and the system it is running on. Thus, **always design your forms at default 96 DPI and then test at higher DPI settings**.

All container controls must be set to the same ```AutoScaleMode = Font```. This will handle both DPI changes and changes to the system font size setting; DPI will only handle DPI changes, not changes to the system font size setting.

Make sure you **use the default font size*** on all your containers (forms, panels, tab page, user controls etc). 8.25 px. Preferably this should not be set in the *\<container\>.Designer.cs* file at all for all containers so that it uses the default font from the container class.

All container controls must also be set with ```AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F)```, assuming 96 DPI, in the *\<container\>.Designer.cs* file.

If you need to set different font sizes on labels, textboxes, etc. set them per control instead of setting the font on the container class because WinForms uses the containers font setting to scale it's contents.

Design the interface of your forms using **Anchored**, **Docked**, **AutoSized** controls where possible. Using the built-in layout controls (**FlowLayoutPanel** and **TableLayoutPanel**) can also be helpful.

If you have some custom layout logic, always keep in mind that the sizes and the locations of the controls will be different if the form is scaled. Also keep in mind that you should manually scale any constants you use if they denote pixels.

### Rhino-Specific

The ```RhinoWindows``` assembly has a new ```RhinoWindows.Forms.Dpi``` class that is similar to the ```CRhinoDpi``` class in the Rhino C++ SDK. The class contains static functions to return the current DPI scale factor and to scale values per the current DPI scale factor. For example:

```cs
/// <summary>
/// MainWindow Constructor
/// </summary>
public MainWindow()
{
  // This call is required by the Windows Form Designer.
  InitializeComponent();

  var width = RhinoWindows.Forms.Dpi.ScaleInt(m_toolbar.ImageScalingSize.Width);
  var height = RhinoWindows.Forms.Dpi.ScaleInt(m_toolbar.ImageScalingSize.Height);
  m_toolbar.ImageScalingSize = new Size(width, height);

  // ...
```

Use the ```DrawingUtilities::LoadBitmapWithScaleDown``` and ```DrawingUtilities::LoadIconWithScaleDown``` static functions, found in the ```Rhino.UI``` assembly, to assist with loading bitmaps and icons from icon resources. For example:

```cs
using Rhino.UI;

//...

var size = RhinoWindows.Forms.Dpi.ScaleInt(32);
using (var icon = DrawingUtilities.LoadIconWithScaleDown("logo.ico", (int)size, GetType().Assembly))
  m_image = icon.ToBitmap();

// ...
```

If the icon is not a standard size, ```DrawingUtilities::LoadIconWithScaleDown``` scales down a larger image.
