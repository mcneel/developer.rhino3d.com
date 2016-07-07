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

Super high resolution displays are now common on Windows-based systems, and those using Rhino expect it and 3rd party plug-ins to display correctly on them. Developers need to make sure their plug-in are DPI–aware. DPI-aware plug-in adjust UI elements to scale appropriately to the system DPI. Plug-ins that are not DPI–aware, but are running on a high-DPI display setting, can suffer from many visual artifacts, including incorrect scaling of UI elements, clipped text, and blurry images.

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





