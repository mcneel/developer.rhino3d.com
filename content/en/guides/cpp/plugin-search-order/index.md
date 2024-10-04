+++
aliases = ["/en/5/guides/cpp/plugin-search-order/", "/en/6/guides/cpp/plugin-search-order/", "/en/7/guides/cpp/plugin-search-order/", "/wip/guides/cpp/plugin-search-order/"]
authors = [ "dale" ]
categories = [ "Advanced" ]
description = "This guide discusses the order in which Rhino searches and loads plugins."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Plugin Search Order"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = "needs to be reviewed and consolidated with other plugin guides"
origin = "http://wiki.mcneel.com/developer/sdksamples/pluginsearchorder"
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

- [Plugin Loading](/guides/cpp/plugin-loading)
