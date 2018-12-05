---
title: Adding a Custom Menu
description: This short guide demonstrates how to add a custom menu to Rhino's menu using C/C++.
authors: ['dale_fugier']
author_contacts: ['dale']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/sdksamples/insertpluginmenu
order: 1
keywords: ['rhino', 'menu']
layout: toc-guide-page
---

 
## Problem

Imagine you would like to add a submenu to Rhino's File menu.  You might start fiddling around with the `Insert­Plug­In­Menu­To­Rhino­Menu()` and ­`Insert­Plug­In­Item­To­Rhino­Menu()` functions but not seem to be getting anywhere.  `Insert­Plug­In­Menu­To­Rhino­Menu()` adds a menu into the Rhino's main menu bar. `Insert­Plug­In­Item­To­RhinoMenu()` adds a menu item anywhere in the Rhino menu.  To solve this problem, you want a little of both...

## Solution

To insert a menu item, or a submenu, into Rhino's menu, do the following:

1. Use `CRhinoApp::FindMenuItem` to search through Rhino's menu structure for an existing menu item that's where you want to insert your menu item.
1. Use `CRhinoPlugIn::InsertPlugInItemToRhinoMenu` to insert your menu into Rhino's menu.

## Sample

The following example command demonstrates how to add and remove a custom menu from Rhino's menu:

```cpp
////////////////////////////////////////////////////////////////
// cmdMyMenu.cpp

#include "StdAfx.h"
#include "MyTestPlugIn.h"
#include "Resource.h"

////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
//
// BEGIN MyMenu command
//

class CCommandMyMenu : public CRhinoCommand
{
public:
  CCommandMyMenu() {}
  ~CCommandMyMenu() {}
  UUID CommandUUID()
  {
    static const GUID MyMenuCommand_UUID =
    { <TODO: add your command uuid here> };
    return MyMenuCommand_UUID;
  }
  const wchar_t* EnglishCommandName() { return L"MyMenu"; }
  const wchar_t* LocalCommandName() { return L"MyMenu"; }
  CRhinoCommand::result RunCommand( const CRhinoCommandContext& );

  BOOL LoadMyMenu();
  BOOL UnloadMyMenu();

private:
  CMenu m_menu;
};

// The one and only CCommandMyMenu object
static class CCommandMyMenu theMyMenuCommand;

CRhinoCommand::result CCommandMyMenu::RunCommand( const CRhinoCommandContext& context )
{
  bool bVisible = ( m_menu.GetSafeHmenu() ) ? true : false;

  ON_wString prompt;
  prompt.Format( L"%s is %s. New value",
    EnglishCommandName(),
    bVisible ? L"visible" : L"hidden"
    );

  CRhinoGetOption go;
  go.SetCommandPrompt( prompt );
  int s_opt = go.AddCommandOption( RHCMDOPTNAME(L"Show") );
  int h_opt = go.AddCommandOption( RHCMDOPTNAME(L"Hide") );
  int t_opt = go.AddCommandOption( RHCMDOPTNAME(L"Toggle") );
  go.GetOption();
  if( go.CommandResult() != success )
    return go.CommandResult();

  const CRhinoCommandOption* opt = go.Option();
  if( 0 == opt )
    return failure;

  if( opt->m_option_index == s_opt )
  {
    if( false == bVisible )
      LoadMyMenu();
  }
  else if( opt->m_option_index == h_opt )
  {
    if( true == bVisible )
      UnloadMyMenu();
  }
  else
  {
    if( true == bVisible )
      UnloadMyMenu();
    else
      LoadMyMenu();
  }

  return success;
}

BOOL CCommandMyMenu::LoadMyMenu()
{
  // Switch the module state so resources are read
  // from our plugin (DLL), not Rhino.
  AFX_MANAGE_STATE( AfxGetStaticModuleState() );

  // Try to load our menu resource from our plugin.
  // Note, m_my_menu is a CMenu member variable.
  if( 0 == m_menu.GetSafeHmenu() )
  {
    if( !m_menu.LoadMenu(IDR_MY_MENU) )
      return FALSE;
  }

  // Find a location in Rhino's menu to insert our
  // menu item. For this example, we will insert our
  // menu on the "Tools" menu just below the "Commands"
  // item.
  HMENU hParent = 0;
  int index = 0;
  //if( !RhinoApp().FindRhinoMenuItem(L"&File::&Print...Ctrl+P", hParent, index) )
  if( !RhinoApp().FindRhinoMenuItem(L"Too&ls::&Commands", hParent, index) )
  {
    m_menu.DestroyMenu();
    return FALSE;
  }

  // Create and initialize a MENUITEMINFO struct.
  MENUITEMINFO mi;
  memset( &mi, 0, sizeof(mi) );
  mi.cbSize = sizeof(mi);

  // Fill in our menu info
  mi.fMask = MIIM_ID | MIIM_TYPE | MIIM_STATE | MIIM_SUBMENU;
  mi.wID = MF_POPUP;
  mi.fType = MFT_STRING;

  ON_wString wstr = L"MyMenu";
  mi.dwTypeData = wstr.Array();

  mi.fState = MFS_ENABLED;
  mi.hSubMenu = m_menu.GetSafeHmenu();
  mi.hSubMenu = ::GetSubMenu( mi.hSubMenu, 0 );
  mi.wID = IDR_MY_MENU;

  // Add our menu to Rhino's menu
  BOOL rc = MyTestPlugIn().InsertPlugInItemToRhinoMenu( hParent, index + 1, &mi );
  if( !rc )
    m_menu.DestroyMenu();

  return rc;
}

BOOL CCommandMyMenu::UnloadMyMenu()
{
  BOOL rc = FALSE;

  // Find our menu item in Rhino's menu.
  HMENU hParent = 0;
  int index = 0;
  if( RhinoApp().FindRhinoMenuItem(L"Too&ls::MyMenu", hParent, index) )
  {
    // Remove our menu item.
    if( ::RemoveMenu(hParent, index, MF_BYPOSITION) )
    {
      // Redraw Rhino's menu bar.
      DrawMenuBar( RhinoApp().MainWnd() );
      m_menu.DestroyMenu();
      rc = TRUE;
    }
  }

  return rc;
}

//
// END MyMenu command
//
////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
```
