---
title: Running Rhino from the Command Line
description: This guide explains how to run Rhino from the command line.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Uncategorized']
origin: http://wiki.mcneel.com/developer/commandline
order: 1
keywords: ['rhino']
layout: toc-guide-page
TODO: 'needs to be reclassified as a General guide if we can add OS X specifics'
---

# Running Rhino from the Command Line

{{ page.description }}

## Overview

Under some circumstances, it is useful to run Rhino from the command prompt.  Perhaps you are batch processing many files, or maybe you need to run Rhino from a render farm management system.  Rhino provides command line options (arguments) to allow you to do exactly this.

## Rhino for Windows

The format is:

```cmd
Rhino.exe /runscript="-command -secondCommand"
```

For example, if you want to start Rhino with a file called `hdri_test.3dm`, render it with the built-in renderer, save the file, and exit Rhino, you would pass this:

```cmd
"C:\Program Files\Rhinoceros 5 (64-bit)\System\Rhino.exe" /runscript="_SetCurrentRenderPlugIn RhinoRender render -saverenderwindowas test.jpg closerenderwindow -exit" hdri_test.3dm
```

### Command line options

The following command line options are available in Rhino for Windows:

- `/safemode`: Start in safe mode.
- `/nosplash`: Suppress startup splash screen.
- `/bigdump`: When Rhino crashes, include the full memory content and, also, call stack information. This can generate huge crash dumps – as big as the amount of RAM Rhino is using when it crashes.
- `/notemplate`: Start Rhino with a default model based on hard-coded defaults.
- `/language`: Set the startup language. For example, to start in Spanish, pass `/language=1034`.
- `/scheme`: Use a custom scheme. This is used by third party developers that include custom schemes.
- `/runscript`: Run a script at startup.

## Rhino for Mac

Forthcoming.
