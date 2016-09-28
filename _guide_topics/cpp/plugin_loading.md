---
title: Plugin Loading
description: This guide discusses how Rhino loads C/C++ plugins.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Advanced']
origin: http://wiki.mcneel.com/developer/sdksamples/loadlibraryex
order: 1
keywords: ['rhino', 'plugins']
layout: toc-guide-page
TODO: 'needs to be reviewed or consolidated with other plugin guides'
---

# {{ page.title }}

{{ page.description }}

## Loading

Rhino plugins are loaded twice.  The first time as follows:

```cpp
hModule = ::LoadLibraryEx(
    lpFileName,
    0,
    DONT_RESOLVE_DLL_REFERENCES | LOAD_WITH_ALTERED_SEARCH_PATH
    );
```

By using the `DONT_RESOLVE_DLL_REFERENCES` flag, the system does not call the plugin's `DllMain` for process and thread initialization and termination.  Also, the system does not load additional executable modules that are referenced by the specified module.  This allows Rhino to quickly verify the Rhino SDK version and that the proper plugin exports are available.

The `LOAD_WITH_ALTERED_SEARCH_PATH` flag is used so `LoadLibraryEx` looks for dependent DLLs in the directory specified by `lpFileName`, not by *Rhino.exe*.

The plugin module is freed as follows:

```cpp
::FreeLibrary( hModule );
```

If the above was successful, the plugin is loaded for a final time as follows:

```cpp
hModule = ::LoadLibraryEx(
    lpFileName,
    0,
    LOAD_WITH_ALTERED_SEARCH_PATH
    );
```

Again, the altered search path flag is used.
