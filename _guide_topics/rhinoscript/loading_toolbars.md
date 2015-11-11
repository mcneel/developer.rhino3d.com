---
layout: toc-guide-page
title: Loading Toolbars
author: dale@mcneel.com
categories: ['Miscellaneous']
platforms: ['Windows']
apis: ['RhinoScript']
languages: ['RhinoScript']
keywords: ['script', 'Rhino', 'vbscript']
TODO: 0
origin: http://wiki.mcneel.com/developer/scriptsamples/loadingtoolbars
order: 1
---

# Loading Toolbars

This guide demonstrates how to load a toolbar when Rhino starts using RhinoScript.

## Problem

Imagine you are in the early stages of creating an installer that will add a small custom toolbar in Rhino.  You would like Rhino to autoload a toolbar collection file upon startup, but you are not writing a plugin, so you would like to do this from a script.

## Solution

Since you do not have a plugin to control the loading of your toolbar, then you are going to have to add either a startup command or a startup RhinoScript.

The following RhinoScript file will load a specified toolbar collection and a toolbar.  If this script is added to RhinoScript's list of startup scripts, it will load a toolbar collection and toolbar when Rhino starts.  To have this script load your toolbar collection and toolbar, you will have to edit the script and replace my strings with yours in the `TODO` portion of the script...

```vbnet
Option Explicit

Sub LoadMyToolbarAtStartup

  Dim strCollection, strToolbar, strName

  ' TODO: Replace the following with the
  ' full path to your toolbar collection to load.
  strCollection = "C:\Program Files\Rhinoceros 5.0\MyToolbar.tb"

  ' TODO: Replace the following with the
  ' name of the toolbar in your collection to open.
  strToolbar = "Default"

  ' Try opening our toolbar collection
  strName = Rhino.IsToolbarCollection(strCollection)
  If IsNull(strName) Then
    strName = Rhino.OpenToolbarCollection(strCollection)
    If IsNull(strName) Then Exit Sub ' failed
  End If

  ' If we got here, then our toolbar collection is open.
  ' So, show our toolbar.
  Call Rhino.ShowToolbar(strName, strToolbar)

  ' Now that our toolbar has been open, remove this script
  ' from RhinoScript's list of startup scripts. This way,
  ' if the user chooses to close our toolbar, it does not
  ' keep showing up everytime they run Rhino (irritating).
  Call Rhino.DeleteStartupScript(Rhino.LastLoadedScriptFile)

End Sub

' Now that our subroutine is defined, run it!
Call LoadMyToolbarAtStartup
```

RhinoScript stores its list of startup commands in the following registry key:

```vbs
HKEY_CURRENT_USER\Software\McNeel\Rhinoceros\5.0\Scheme: Default\Plug-ins\1c7a3523-9a8f-4cec-a8e0-310f580536a7\Settings\StartupFileList.
```

<div class="bs-callout bs-callout-danger">
  <h4>WARNING</h4>
  <p>Modifying the registry incorrectly can have negative consequences on your system's stability and even damage the system.</p>
</div>

Each startup file is a `REG_SZ` key value with the name of `File<num>` and a value which is the full path to the script file.
