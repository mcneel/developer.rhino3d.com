+++
aliases = ["/en/5/guides/cpp/running-rhino-from-command-line/", "/en/6/guides/cpp/running-rhino-from-command-line/", "/en/7/guides/cpp/running-rhino-from-command-line/", "/en/wip/guides/cpp/running-rhino-from-command-line/"]
authors = [ "dale" ]
categories = [ "Advanced" ]
description = "This guide explains how to run Rhino from the command line."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Running Rhino from the Command Line"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = "needs to be reclassified as a General guide if we can add macOS specifics"
origin = "http://wiki.mcneel.com/developer/commandline"
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

Under some circumstances, it is useful to run Rhino from the command prompt.  Perhaps you are batch processing many files, or maybe you need to run Rhino from a render farm management system.  Rhino provides command line options (arguments) to allow you to do exactly this.

## Rhino for Windows

The format is:

```cmd
Rhino.exe /runscript="-command -secondCommand"
```

For example, if you want to start Rhino with a file called `hdri_test.3dm`, render it with the built-in renderer, save the file, and exit Rhino, you would pass this:

```cmd
"C:\Program Files\Rhinoceros 5 (64-bit)\System\Rhino.exe" /runscript="_SetCurrentRenderPlugIn Rhinoceros _Render _-SaveRenderWindowAs test.jpg _-CloseRenderWindow _-Exit" test.3dm
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

