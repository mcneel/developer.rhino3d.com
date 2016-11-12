---
title: Plugin Search Order
description: This guide discusses the order in which Rhino searches and loads plugins.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Getting Started']
origin: http://wiki.mcneel.com/developer/sdksamples/pluginsearchorder
order: 7
keywords: ['rhino']
layout: toc-guide-page
TODO: 'needs to be reviewed and consolidated with other plugin guides'
---

# {{ page.title }}

{% include byline.html %}

{{ page.description }}

## Overview

Rhino plugins are Windows Dynamic Link Libraries, or DLLs.  As such, Rhino uses Windows to load your plugin.  Rhino attempts to load your plugin, and any dependent DLLs, in the following manner:

1. Alternate Search Order - uses `LoadLibraryEx` with the `LOAD_WITH_ALTERED_SEARCH_PATH` flag.
1. Standard Search Order - uses `LoadLibrary`.

**NOTE**: starting with Windows XP and later, the dynamic-link library (DLL) search order used by the system depends on the setting of the `HKLM\System\CurrentControlSet\Control\Session Manager\SafeDllSearchMode` value.  For Windows Server 2003: The default value is 1.  Windows XP: The default value is 0.

## Alternate Search Order

The `LoadLibraryEx` function supports an alternate search order if the call specifies `LOAD_WITH_ALTERED_SEARCH_PATH` and the `lpFileName` parameter specifies a path.  If `SafeDllSearchMode` is 1, the alternate search order is as follows:

1. The directory specified by `lpFileName`.
1. The system directory.  Use the `GetSystemDirectory` function to get the path of this directory.
1. The 16-bit system directory.  There is no function that obtains the path of this directory, but it is searched.
1. The Windows directory.  Use the `GetWindowsDirectory` function to get the path of this directory.
1. The current directory.
1. The directories that are listed in the `PATH` environment variable.

If `SafeDllSearchMode` is 0, the alternate search order is as follows:

1. The directory specified by `lpFileName`.
1. The current directory.
1. The system directory.  Use the `GetSystemDirectory` function to get the path of this directory.
1. The 16-bit system directory. There is no function that obtains the path of this directory, but it is searched.
1. The Windows directory.  Use the `GetWindowsDirectory` function to get the path of this directory.
1. The directories that are listed in the `PATH` environment variable.

## Standard Search Order

If `SafeDllSearchMode` is 1, the search order is as follows:

1. The directory from which the application loaded.
1. The system directory.  Use the `GetSystemDirectory` function to get the path of this directory.
1. The 16-bit system directory.  There is no function that obtains the path of this directory, but it is searched.
1. The Windows directory.  Use the `GetWindowsDirectory` function to get the path of this directory.
1. The current directory.
1. The directories that are listed in the `PATH` environment variable.

If `SafeDllSearchMode` is 0, the search order is as follows:

1. The directory from which the application loaded.
1. The current directory.
1. The system directory.  Use the `GetSystemDirectory` function to get the path of this directory.
1. The 16-bit system directory.  There is no function that obtains the path of this directory, but it is searched.
1. The Windows directory.  Use the `GetWindowsDirectory` function to get the path of this directory.
1. The directories that are listed in the `PATH` environment variable.

Note, Windows 2000 does not support the `SafeDllSearchMode` value. T he search order for Windows 2000 is as follows:

1. The directory from which the application loaded.
1. The current directory.
1. The system directory.  Use the `GetSystemDirectory` function to get the path of this directory.
1. The 16-bit system directory.  There is no function that obtains the path of this directory, but it is searched.
1. The Windows directory.  Use the `GetWindowsDirectory` function to get the path of this directory.
1. The directories that are listed in the `PATH` environment variable.

## Related Topics

- [Plugin Loading]({{ site.baseurl }}/guides/cpp/plugin-loading)
