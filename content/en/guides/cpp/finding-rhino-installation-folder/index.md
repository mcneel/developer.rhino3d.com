+++
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This guide discusses how to find Rhino's installation folder using C/C++."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Finding Rhino's Installation Folder"
type = "guides"
weight = 1

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
