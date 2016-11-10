---
title: Finding Rhino's Installation Folder
description: This guide discusses how to find Rhino's installation folder using C/C++.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/sdksamples/installfolder
order: 1
keywords: ['rhino']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## Problem

You are putting together an installer for your Rhino plugin.  You would like to know how you can, programatically, get Rhino's installation folder.

## Solution

### Rhino 64-bit

If you are looking for Rhino 64-bit, then you can find the location of Rhino's installation folder by looking in the Windows Registry in this location:

```
Hive:  HKEY_LOCAL_MACHINE
Key:   SOFTWARE\McNeel\Rhinoceros\<version>x64\Install
Name:  InstallPath
Type:  REG_SZ
```

### Rhino 32-bit

If you are looking for Rhino 5 32-bit on a system running a 64-bit version of Windows, then you can find the location of Rhino's installation folder by looking in the Windows Registry in this location:

```
Hive:  HKEY_LOCAL_MACHINE
Key:   SOFTWARE\Wow6432Node\McNeel\Rhinoceros\<version>\Install
Name:  InstallPath
Type:  REG_SZ
```

If you are looking for Rhino 5 32-bit on a system running a 32-bit version of Windows, then you can find the location of Rhino's installation folder by looking in the Windows Registry in this location:

```
Hive:  HKEY_LOCAL_MACHINE
Key:   SOFTWARE\McNeel\Rhinoceros\<version>\Install
Name:  InstallPath
Type:  REG_SZ
```
