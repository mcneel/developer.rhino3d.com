---
title: Linking with openNURBS
description: This guide discusses openNURBS linking.
author: dalelear@mcneel.com
apis: ['openNURBS']
languages: ['C/C++']
platforms: ['Windows', 'Mac']
categories: ['Getting Started']
origin: http://wiki.mcneel.com/developer/opennurbs/linkingpragma
order: 1
keywords: ['openNURBS', 'linking', 'toolkit', 'pragma', 'pragmas']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## Problem

You are trying to write a simple console application like the *example_write* sample included with the openNURBS toolkit.  However, you are having problems linking.  You are using the *opennurbs_staticlib_linking_pragmas.h* header included with openNURBS, but it does not seem to work.

## Solution

The *opennurbs_staticlib_linking_pragmas.h* header, included with openNURBS, is only designed to help build the example projects included with the toolkit.  That is, it only works if your project is inside the openNURBS folder.

Unlike the `#include` statement, `#pragma` statements, used in this header, are not very path smart.  The library paths used by `#pragma` statement must be relative to the project, not the `#include` file in which it is used.

You certainly don't have to use *opennurbs_staticlib_linking_pragmas.h* in your project.  You can always add the required openNURBS libraries to your project's *Additional Dependencies* link settings.  You can also just include the required libraries in your project, like you would a *.cpp* or *.h* file.

But, if you like the flexibility that providing linking instructions via `#pragma` statements provide, then you can always change *opennurbs_staticlib_linking_pragmas.h* to reflect the path to your project.  That said, if you use openNURBS in more than one project and the projects are not all stored in the same relative location, this will not work.

## Sample

Below is sample that contains two header files that you can include in any project that needs to link with openNURBS.  One of the headers provides instruction for statically linking openNURBS, and the other one for dynamically linking.  Once these files are included in your project, you can edit them to reflect your project's relative path to the openNURBS toolkit.

### opennurbs_static_linking.h
```cpp
/////////////////////////////////////////////////////////////////////////////
// linking_pragmas_static.h

// This file is specific to Micrsoft's compiler.

#pragma once

#if defined(ON_DLL_IMPORTS) || defined(ON_DLL_EXPORTS)
#error This file contains STATIC LIBRARY linking pragmas.
#endif

#if defined(WIN64)

// x64 (64 bit) static libraries

#if defined(NDEBUG)

// Release x64 (64 bit) libs
#pragma message( " --- openNURBS Release x64 (64 bit) build." )
#pragma comment(lib, "../opennurbs/zlib/x64/Release/zlibx64.lib")
#pragma comment(lib, "../opennurbs/x64/ReleaseStaticLib/opennurbsx64_static.lib")

#else // _DEBUG

// Debug x64 (64 bit) libs
#pragma message( " --- openNURBS Debug x64 (64 bit) build." )
#pragma comment(lib, "../opennurbs/zlib/x64/Debug/zlibx64_d.lib")
#pragma comment(lib, "../opennurbs/x64/DebugStaticLib/opennurbsx64_staticd.lib")

#endif // NDEBUG else _DEBUG

#else // WIN32

// x86 (32 bit) static libraries

#if defined(NDEBUG)

// Release x86 (32 bit) libs
#pragma message( " --- openNURBS Release x86 (32 bit) build." )
#pragma comment(lib, "../opennurbs/zlib/Release/zlib.lib")
#pragma comment(lib, "../opennurbs/ReleaseStaticLib/opennurbs_static.lib")

#else // _DEBUG

// Debug x86 (32 bit) libs
#pragma message( " --- openNURBS Debug x86 (32 bit) build." )
#pragma comment(lib, "../opennurbs/zlib/Debug/zlib_d.lib")
#pragma comment(lib, "../opennurbs/DebugStaticLib/opennurbs_staticd.lib")

#endif // NDEBUG else _DEBUG

#endif // WIN64 else WIN32
```

### opennurbs_dynamic_linking.h

```cpp
/////////////////////////////////////////////////////////////////////////////
// linking_pragmas_static.h

// This file is specific to Micrsoft's compiler.

#pragma once

#if !defined(ON_DLL_IMPORTS)
#error This file contains DYNAMIC LIBRARY linking pragmas.
#endif

#if defined(WIN64)

// x64 (64 bit) dynamic libraries

#if defined(NDEBUG)

// Release x64 (64 bit) libs
#pragma message( " --- openNURBS Release x64 (64 bit) build." )
#pragma comment(lib, "../opennurbs/zlib/x64/Release/zlibx64.lib")
#pragma comment(lib, "../opennurbs/x64/Release/opennurbsx64.lib")

#else // _DEBUG

// Debug x64 (64 bit) libs
#pragma message( " --- openNURBS Debug x64 (64 bit) build." )
#pragma comment(lib, "../opennurbs/zlib/x64/Debug/zlibx64_d.lib")
#pragma comment(lib, "../opennurbs/x64/Debug/opennurbsx64_d.lib")

#endif // NDEBUG else _DEBUG

#else // WIN32

// x86 (32 bit) dynamic libraries

#if defined(NDEBUG)

// Release x86 (32 bit) libs
#pragma message( " --- openNURBS Release x86 (32 bit) build." )
#pragma comment(lib, "../opennurbs/zlib/Release/zlib.lib")
#pragma comment(lib, "../opennurbs/Release/opennurbs.lib")

#else // _DEBUG

// Debug x86 (32 bit) libs
#pragma message( " --- openNURBS Debug x86 (32 bit) build." )
#pragma comment(lib, "../opennurbs/zlib/Debug/zlib_d.lib")
#pragma comment(lib, "../opennurbs/Debug/opennurbs_d.lib")

#endif // NDEBUG else _DEBUG

#endif // WIN64 else WIN32
```

To use these headers, just include them to your project's *stdafx.h* file like this:

```cpp
// stdafx.h

#pragma once

#include "targetver.h"

#include <stdio.h>
#include <tchar.h>

// TODO: reference additional headers your program requires here

// Uncomment the following if you want to use the openNURBS dynamic link library
//#define ON_DLL_IMPORTS

#include "../opennurbs/opennurbs.h"

#if defined(ON_DLL_IMPORTS)
#include "opennurbs_dynamic_linking.h"
#else
#include "opennurbs_static_linking.h"
#endif
```
