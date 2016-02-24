---
title: Open a 3DM file
description: This brief guide demonstrates how to open a Rhino 3DM file from a plugin command using C/C++.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/sdksamples/open3dm
order: 1
keywords: ['rhino', 'open', '3dm']
layout: toc-guide-page
---

# Open a 3DM file

{{ page.description }}

## Problem

You would like to open a 3DM file, or an STL file, or any other file type that Rhino supports, from your C/C++ plugin.

## Solution

As each type of file, support by Rhino for opening or importing, has a different set of options, it not possible to write a single, generic file open function and hope to support all formats.  Thus, if you want to open or import a file from a plugin command, then simply script either Rhino's *Open* or *Import* command using `CRhinoApp::RunScript()`.

## Sample

The following example command demonstrates how to open a Rhino 3DM file from a plugin command.  You can use this same technique to open other support file types, such as STL, IGES, DWG, and others.

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  // Prompt the user for the name of a 3dm file to open
  ON_wString filename;
  CWnd* pParentWnd = CWnd::FromHandle( RhinoApp().MainWnd() );

  CRhinoGetFileDialog gf;
  gf.SetScriptMode( context.IsInteractive() ? FALSE : TRUE );
  BOOL rc = gf.DisplayFileDialog( CRhinoGetFileDialog::open_rhino_only_dialog, filename, pParentWnd );
  if( !rc )
    return CRhinoCommand::cancel;

  // Verify the file name string
  filename = gf.FileName();
  filename.TrimLeftAndRight();
  if( filename.IsEmpty() )
    return CRhinoCommand::nothing;

  // Verify the file
  if( !CRhinoFileUtilities::FileExists(filename) )
  {
    RhinoApp().Print( L"File not found.\n" );
    return CRhinoCommand::failure;
  }

  // Script Rhino's open command. Note, in case the file name
  // string contains spaces, we will want to surround the string
  // with double-quote characters so the command line parser
  // will deal with the string property.
  ON_wString script;
  script.Format( L"_-Open \"%s\"", filename );
  RhinoApp().RunScript( script, 0 );

  return CRhinoCommand::success;
}
```
