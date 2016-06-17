---
title: Failed to Create VBScript Error
description: This guide discusses the Failed to create instance of VBScript engine error and how to fix it.
author: dale@mcneel.com
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Miscellaneous', 'Troubleshooting']
origin: http://wiki.mcneel.com/developer/scriptsamples/vbsfailed
order: 1
keywords: ['script', 'Rhino', 'vbscript']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## Symptom

When you run Rhino, you receive the following error message:

**"Failed to create instance of VBScript engine"**

## Cause

The RhinoScript plugin included with Rhino uses Microsoft's Visual Basic Script, or VBScript.  The "Failed to create instance of VBScript engine" message is a result of RhinoScript's inability to connect with VBScript.

This error can be caused by the following:

- VBScript is not installed.
- VBScript is not properly registered.
- Script blocking software is preventing VBScript from running.
- Security settings are preventing VBScript from being accessed.

## VBScript is not installed

Rhino 3.0, 4.0, and 5 (32-bit) use the 32-bit version of the VBScript dynamic-link library, *vbscript.dll*. On English-language versions of 32-bit Windows, *vbscript.dll* is located here:

```
C:\Windows\System32
```

On English-language versions of 64-bit Windows, 32-bit *vbscript.dll* is located here:

```
C:\Windows\SysWOW64
```

Rhino 5 (64-bit) use the 64-bit version of *vbscript.dll*. On English-language versions of 64-bit Windows, *vbscript.dll* is located here:

```
C:\Windows\System32
```

If you search these folders and you are unable to locate *vbscript.dll*, then you will need to reinstall VBScript.

### Installing VBScript

Install the latest Visual Basic Script engine from Microsoft for your Windows version:

- [Windows XP](http://www.microsoft.com/downloads/details.aspx?familyid=47809025-D896-482E-A0D6-524E7E844D81)
- Windows Vista, 7, 8, 10: No download necessary. The latest VBScript is already included with Windows.

**NOTE**: You can also install the latest VBScript by simply downloading and installing the latest version of Microsoft Internet Explorer.

## VBScript is not registered

In order for applications to use VBScript, it must be properly registered in the Windows Registry.

Rhino 3.0, 4.0, and 5 (32-bit) use the 32-bit version of VBScript.  On English-language versions of 32-bit Windows, VBScript is registered here:

```
HKEY_CLASSES_ROOT\CLSID\{B54F3741-5B07-11cf-A4B0-00AA004A55E8}
```

On English-language versions of 64-bit Windows, 32-bit VBScript is registered here:

```
HKEY_CLASSES_ROOT\Wow6432Node\CLSID\{B54F3741-5B07-11cf-A4B0-00AA004A55E8}
```

Rhino 5 (64-bit) use the 64-bit version of VBScript.  On English-language versions of 64-bit Windows, VBScript is registered here:

```
HKEY_CLASSES_ROOT\CLSID\{B54F3741-5B07-11cf-A4B0-00AA004A55E8}
```

If, using *REGEDIT.EXE*, you search for these keys and you are unable to locate them, then you will need to reregister VBScript by following the directions below...

<div class="bs-callout bs-callout-danger">
  <h4>WARNING</h4>
  <p>Modifying the registry incorrectly can have negative consequences on your system's stability and even damage the system.  You must be logged in as administrator or logged in as a user with administrator privileges for the computer to execute these steps.</p>
</div>

1. Click Start > All Programs > Accessories > Command Prompt. (Windows 7 users: right-click on Command Prompt and select "Run as administrator").
1. In the command prompt window, change to the folder where *vbscript.dll* resides by typing either `CD C:\Windows\System32` or `CD C:\Windows\SysWOW64` and then press <kbd>Enter</kbd>.
1. In the command prompt window, type `REGSVR32 VBSCRIPT.DLL` and then press <kbd>Enter</kbd>.
1. A message should appear stating "DllRegisterServer in VBSCRIPT.DLL succeeded". If you see a message with error code 0x80004005, the command window was not opened as an administrator.  You might also need to disable anti-virus, personal security, and firewall applications before performing this task.

## Script Blocking Software

Many anti-virus, personal security, and firewall applications contain script blocking features that will prevent applications from accessing VBScript.  For example, Norton Antivirus has a Script Blocking feature what will disable VBScript.  McAfee also has one that is even more destructive.  Kaspersky also was found to be blocking VBScripting.

If you are running anti-virus, personal security, and firewall applications, you may have to disable their script blocking features.  Check your product documentation for details.

### McAfee

McAfee anti-virus can cause serious problems with VBScript, even if it is uninstalled.  Even after uninstalling McAfee, it may have modified the two registry keys listed above, pointing to place-holder DLLs in the McAfee folders instead of where the two *vbscript.dll* files should be.  If you encounter this issue, use PSEXEC as described below to restore full permissions to the Administrator account in order to manuallyy change the keys to point back to the 32 and 64-bit *vbscript.dll* files.

There are two keys that tell Windows where VBScript.dll is on the local drive.  If McAfee has modified your VBScript installation, these keys will be pointing to the wrong file and locations.

It is likely that:

```
[HKEY_CLASSES_ROOT\CLSID{B54F3741-5B07-11cf-A4B0-00AA004A55E8}\InprocServer32]
```

points to:

```
C:\Program Files\McAfee\VirusScan Enterprise\scriptcl.dll
```

which is wrong.

This causes VBScript to fail when any application tries to use it.  A complete uninstall of McAfee will leave this key unmodified, causing VBScript to fail since this McAfee dll no longer exists.

Manually changing the registry key to the windows default:
```
\[HKEY_CLASSES_ROOT\CLSID{B54F3741-5B07-11cf-A4B0-00AA004A55E8}\InprocServer32]
```
to:

```
\\C:\Windows\System32\vbscript.dll\\
```

fixes the problem for Rhino 5 for Windows (64-bit).

For 32-bit Rhino 5 on 64-bit Windows, this key:

```
 \HKEY_CLASSES_ROOT\Wow6432Node\CLSID{B54F3741-5B07-11cf-A4B0-00AA004A55E8\InprocServer32}\\
```

should point to:

```
 \\C:\Windows\SysWOW64\vbscript.dll\\
```

## Security Settings

If *vbscript.dll* is present on your system and the module is properly registered, then you might not have enough rights to read the Windows Registry.

<div class="bs-callout bs-callout-danger">
  <h4>WARNING</h4>
  <p>Modifying the registry incorrectly can have negative consequences on your system's stability and even damage the system.  You must be logged in as administrator or logged in as a user with administrator privileges for the computer to execute these steps.</p>
</div>

Run *REGEDIT.EXE* and find the appropriate registry key in `HKEY_CLASSES_ROOT`, either:

```
HKEY_CLASSES_ROOT\CLSID\{B54F3741-5B07-11cf-A4B0-00AA004A55E8}
```

or

```
HKEY_CLASSES_ROOT\Wow6432Node\CLSID\{B54F3741-5B07-11cf-A4B0-00AA004A55E8}
```

Right-click on the key and pick Permissions... from the context menu.

Users should have the Read permission checked.  If this is not the case, then the users permissions have been modified, which is causing RhinoScript to not be able to read this key.  Registry permissions issues are often caused by security policies have been pushed down onto the workstations that are members of an Active Directory domain.

To set the permissions, navigate to the top of the hive, `HKEY_CLASSES_ROOT`, and try to set the proper permissions from there.  In doing this, all keys below this will inherit the permissions (and hopefully the problem will be solved).  If you are unable to do this, then you will need to contact your IT department and ask for assistance.
