+++
aliases = ["/5/guides/cpp/finding-rhino-installation-folder/", "/6/guides/cpp/finding-rhino-installation-folder/", "/7/guides/cpp/finding-rhino-installation-folder/", "/wip/guides/cpp/finding-rhino-installation-folder/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This guide discusses how to find Rhino's installation folder."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Finding Rhino's Installation Folder"
type = "guides"
weight = 1
override_last_modified = "2024-08-26"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/installfolder"
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

## Problem

You are putting together an installer for your Rhino plugin. You would like to know how you can, programatically, get Rhino's installation folder.

## Solution

### Rhino 8, 7, and 6

If you are looking for Rhino 8, 7, or 6, then you can find the location of Rhino's installation folder by looking in the Windows Registry in this location:

```text
Hive:  HKEY_LOCAL_MACHINE
Key:   SOFTWARE\McNeel\Rhinoceros\<version>\Install
Name:  InstallPath
Type:  REG_SZ
```

If you are looking for Rhino 8, for example, replace `<version>` with `8.0`.

### Rhino 5

If you are looking for Rhino 5 64-bit, then you can find the location of Rhino's installation folder by looking in the Windows Registry in this location:

```text
Hive:  HKEY_LOCAL_MACHINE
Key:   SOFTWARE\McNeel\Rhinoceros\5.0x64\Install
Name:  InstallPath
Type:  REG_SZ
```

If you are looking for Rhino 5 32-bit, then you can find the location of Rhino's installation folder by looking in the Windows Registry in this location:

```text
Hive:  HKEY_LOCAL_MACHINE
Key:   SOFTWARE\WOW6432Node\McNeel\Rhinoceros\5.0\Install
Name:  InstallPath
Type:  REG_SZ
```
