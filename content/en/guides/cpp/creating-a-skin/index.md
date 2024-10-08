+++
aliases = ["/en/5/guides/cpp/creating-a-skin/", "/en/6/guides/cpp/creating-a-skin/", "/en/7/guides/cpp/creating-a-skin/", "/en/wip/guides/cpp/creating-a-skin/"]
authors = [ "dale" ]
categories = [ "Advanced" ]
description = "This guide outlines the tools for C/C++ developers to wrap their application around Rhino by creating custom Skin."
keywords = [ "skin", "RAP", "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Creating a Skin"
type = "guides"
weight = 4
override_last_modified = "2022-05-09T09:40:08Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/skin"
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

Rhino allows developers to customize most of Rhino's interface so that the application appears to be their own.  We call this a custom *Skin*.  With a custom Skin, you can change the application icon, splash screen, the application name etc.

Creating a custom Skin for Rhino involves creating a custom skin assembly:

1. *skin name.rhs* This is a regular MFC DLL (*.dll*) that implements the skin's icon, splash screen, application name, etc.  In this guide, we will refer this to the "Skin DLL."
1. *skin name.rhp* is a Rhino utility plugin that implements the menu handler, if necessary, and one or more custom commands.  In this article, we refer to this as the "Skin Plugin."

## Create the Skin DLL

To create the Skin DLL:

1. Launch *Visual Studio* and run the *Rhino Skin DLL wizard* installed by the Rhino C/C++ SDK.
1. The Rhino Skin DLL wizard creates three classes:
  1. A `CWinApp`-derived class.  This is the entry point of the DLL.
  1. A `CRhinoSkinDLL`-derived class.  This class lets you specify Rhino's icon, splash screen, and menu.  For more information on this class, see *rhinoSdkSkinDLL.h*.
  1. `CSplashWnd`.  This is a basic implementation of a splash screen class.  If you need something fancier, feel free to replace it with your own implementation.
1. Modify the project's icon and splash screen bitmap.  If your Skin is going to override Rhino's main menu, then you need to create your menu resources as well.
1. Remember to fill out the developer information block found at the top of your *DLL's .cpp* file. This block is similar to that of Rhino plugins.

## Create the Skin Plugin

To create a Skin Plugin:

1. Launch *Visual Studio* and run the *Rhino Plugin wizard* installed by the Rhino C/C++ SDK.  When picking the wizard to run, make sure to add the new project to the open solution instead of creating a new solution.  This way, your Skin project is organized into a single solution.
1. If the Skin DLL provides a custom menu, then copy the *UUID* generated by the plugin *AppWizard* and found in your plugin's `CRhinoPlugIn::PlugInID()` member to your Skin's `CRhinoSkinDLL::SkinPlugInID()` member.
1. These two methods must return the same *UUID*.  This is a critical step as it identifies the main plugin that Rhino will load to manage its menus and extend the Rhino command set.
1. Add the following overrides to the header file of your `CRhinoPlugIn`-derived class:

```cpp
// Skin DLL menu update handler
void OnInitPlugInMenuPopups(WPARAM wparam, LPARAM lparam);
// Skin DLL menu command handler
BOOL OnPlugInMenuCommand(WPARAM wparam );
// Change to CRhinoPlugIn::load_plugin_at_startup
plugin_load_time PlugInLoadTime();
```
1. Add the following definition to the *.cpp* file of your `CRhinoPlugIn`-derived class:

```cpp
CRhinoPlugIn::plugin_load_time CSkinPlugInSamplePlugIn::PlugInLoadTime()
{
  // Override to change load time to "at startup"
  return CRhinoPlugIn::load_plugin_at_startup;
}
```
1. If your Skin DLL is providing a custom menu, then add a source file named *MenuHandler.cpp* to the plugin project and put the definition of `CRhinoPlugIn::OnInitPlugInMenuPopups()` and `CRhinoPlugIn::OnPlugInMenuCommand()` in this file.
1. Include the Skin DLL's *Resource.h* file in *MenuHandler.cpp* to provide access to the Skin DLL's menu resource identifiers.  For example:

```cpp
#include "stdafx.h"
#include "MySkinPlugIn.h"
#include "../MySkinDLL/Resource.h"

// Put these to overrides in a separate CPP file so they could
// include the MySkinDLL/Resource.h file without conflicting
// with this projects resource.h

void CSkinPlugInSamplePlugIn::OnInitPlugInMenuPopups(WPARAM wParam, LPARAM lParam)
{
  HMENU hMenu = (HMENU)wParam;
  if( NULL == hMenu )
    return;

  switch( GetMenuItemID(hMenu, LOWORD(lParam)) )
  {
    case IDM_SAMPLE_DISABLE:
      ::EnableMenuItem( hMenu, IDM_SAMPLE_DISABLE, MF_BYCOMMAND|MF_DISABLED|MF_GRAYED );
      break;
    case IDM_SAMPLE_SUB_DISABLE:
      ::EnableMenuItem( hMenu, IDM_SAMPLE_SUB_DISABLE, MF_BYCOMMAND|MF_DISABLED|MF_GRAYED );
      break;
    // TODO...
  }
}

BOOL CSkinPlugInSamplePlugIn::OnPlugInMenuCommand(WPARAM wParam)
{
  ON_wString w;
  switch( (UINT)wParam )
  {
    case IDM_SAMPLE_ONE:
      w = L"Test Item One";
      break;
    case IDM_SAMPLE_TWO:
      w = L"Two";
      break;
    case IDM_SAMPLE_DISABLE:
      w = L"Disabled";
      break;
    case IDM_SAMPLE_SUB_A:
      w = L"Sub Menu A";
      break;
    case IDM_SAMPLE_SUB_B:
      w = L"Sub Menu B";
      break;
    case IDM_SAMPLE_SUB_DISABLE:
      w = L"Sub Menu Disabled";
      break;
    default:
      return true;
  }

  ::RhinoMessageBox( w, L"OnMenu", MB_OK );
  return true;
}
```
1. Compile the Skin Plugin.
1. Load the Skin Plugin using Rhino's *PluginManager* command so it has a chance to self-register.
1. Compile the Skin DLL.

## Installation

<div class="bs-callout bs-callout-danger">
  <h4>WARNING</h4>
  <p>Modifying the registry incorrectly can have negative consequences on your system's stability and even damage the system.</p>
</div>

To install your custom Skin, use **REGEDIT.EXE** to add a scheme key to your registry with a path to your Skin DLL. For example:

| **Item** |    |    | **Value** |
|:--------|:----:|:----:|:--------|
| Subkey   |    |    | HKEY_LOCAL_MACHINE\SOFTWARE\McNeel\Rhinoceros\MajorVersion.0\Scheme: MySkin   || Entry name   |    |    | SkinDLLPath   |
| Type   |    |    | REG_SZ   |
| Data value   |    |    | C:\Src\MySkin\Bin\Release\MySkin.rhs   |

Where `MajorVersion` is the major version of Rhino (e.g. 6, 7, 8).

## Testing

You can now test your custom Skin by creating shortcut to your Rhino executable with `/scheme="<scheme name from the previous step>"` as command line argument.  For example:

*C:\Program Files\Rhino 8\System\Rhino.exe" /scheme=MySkin*

## Additional Info

If the user chooses not to run your skinned version of Rhino, you might want to prevent your Skin plugin loading.  You can do this by checking to see if the name of the scheme that Rhino is using matches your Skin's scheme name.  Do this by checking in your plugin's `CRhinoPlugIn::OnLoadPlugIn()` member:

```cpp
BOOL CSkinPlugInSamplePlugIn::OnLoadPlugIn()
{
  ON_wString scheme = RhinoApp().RegistrySchemeName();
  if( scheme.CompareNoCase(L"Scheme: MySkin") != 0 )
    return -1; // Fail silently...

  // TODO...

  return CRhinoUtilityPlugIn::OnLoadPlugIn();
}
```
