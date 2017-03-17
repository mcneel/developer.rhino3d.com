---
title: Show Toolbar in Workspace File
description: Demonstrates how to display a toolbar in a toolbar collection, or workspace, file.
authors: ['Dale Fugier']
author_contacts: ['dale']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/sdksamples/showtoolbar
order: 1
keywords: ['rhino']
layout: code-sample-cpp
---

```cpp
BOOL LoadAndShowPlugInToolbar()
{
  // Get reference to our plugin object
  CTestPlugIn& plugin = GetTestPlugIn();

  // Get the full path to plugin file
  ON_wString file_name;
  plugin.GetPlugInFileName( file_name );

  // Build the toolbar collection file name
  wchar_t drive[_MAX_DRIVE];
  wchar_t dir[_MAX_DIR];
  wchar_t fname[_MAX_FNAME];
  _wsplitpath( file_name, drive, dir, fname, 0 );

  ON_wString collection_name;
  collection_name.Format( L"%s%s%s.tb", drive, dir, fname );

  BOOL rc = FALSE;

  // Get reference to Rhino's toolbar manager
  CRhinoAppUiToolBarManager& tm = RhinoApp().RhinoUiToolBarManager();

  // Load the toolbar collection, if necessary.
  if( tm.ReadFile(collection_name, true, true, true) )
  {
    // Get the toolbar collection
    const CRhinoUiToolBarCollection* col = tm.Collection( tm.CollectionIndex(collection_name, false) );
    if( col )
    {
      // Find the "Default" toolbar
      const CRhinoUiToolBar* tb = col->ToolBar( col->FindToolBar(L"Default") );
      if( tb && tm.ShowToolBar(tb, true, false) ) // Load it
        rc = TRUE;
    }
  }

  return rc;
}
```

Alternatively:

```cpp
BOOL ShowPlugInToolbar()
{
  // Get reference to our plugin object
  CTestPlugIn& plugin = GetTestPlugIn();

  // Get the full path to plugin file
  ON_wString file_name;
  plugin.GetPlugInFileName( file_name );

  // Build the toolbar collection file name
  wchar_t drive[_MAX_DRIVE];
  wchar_t dir[_MAX_DIR];
  wchar_t fname[_MAX_FNAME];
  _wsplitpath( file_name, drive, dir, fname, 0 );

  ON_wString collection_name;
  collection_name.Format( L"%s%s%s.tb", drive, dir, fname );

  // Get reference to Rhino's toolbar manager
  CRhinoToolBarManager& tm = ToolBarManager();

  // See if the toolbar collection is already open
  int collection_index = tm.CollectionIndex( collection_name, FALSE );
  if( collection_index < 0 )
  {
    // Open the toolbar collection
    collection_index = tm.OpenCollection( collection_name );
    if( collection_index >= 0 )
    {
      // Help Rhino figure out where all toolbars are supposed
      // to be positioned
      AFX_MANAGE_STATE( ::RhinoApp().RhinoModuleState() );
      ((CFrameWnd*)AfxGetMainWnd())->RecalcLayout();
    }
  }

  BOOL rc = FALSE;

  if( collection_index < 0 )
    return rc;

  // See if our toolbar is available
  int toolbar_index = tm.ToolBarIndex( collection_index, L"Default" );
  if( toolbar_index >= 0 )
  {
    // If the toolbar is not visible, display it
    if( !tm.IsToolBarVisisble(collection_index, toolbar_index) )
      rc = tm.ShowToolBar( collection_index, toolbar_index, TRUE );
    else
      rc = TRUE;
  }
  return rc;
}
```
