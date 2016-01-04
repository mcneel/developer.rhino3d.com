---
title: Screen Capture Viewport
description: Demonstrates how to screen capture a viewport to a file.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Unsorted']
origin: http://wiki.mcneel.com/developer/sdksamples/screencaptureview
order: 1
keywords: ['rhino']
layout: code-sample-cpp
---

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  CWnd* pMainWnd = CWnd::FromHandle( RhinoApp().MainWnd() );
  if( 0 == pMainWnd )
    return failure;

  CRhinoGetFileDialog gf;
  gf.SetScriptMode( context.IsInteractive() ? FALSE : TRUE );
  BOOL rc = gf.DisplayFileDialog( CRhinoGetFileDialog::save_bitmap_dialog, 0, pMainWnd );
  if( !rc )
    return cancel;

  ON_wString filename = gf.FileName();
  filename.TrimLeftAndRight();
  if( filename.IsEmpty() )
    return nothing;

  CRhinoView* view = RhinoApp().ActiveView();
  if( view )
  {
    CRect rect;
    view->GetClientRect( rect );

    CRhinoDib dib;
    if( dib.CreateDib(rect.Width(), rect.Height(), 24, true) )
    {
      // Set these flags as you wish.
      BOOL bIgnoreHighlights = TRUE;
      BOOL bDrawTitle = FALSE;
      BOOL bDrawConstructionPlane = FALSE;
      BOOL bDrawWorldAxes = FALSE;

      CRhinoObjectIterator it( CRhinoObjectIterator::normal_or_locked_objects,
                               CRhinoObjectIterator::active_and_reference_objects
                               );

      if( view->ActiveViewport().DisplayMode() == ON::wireframe_display )
      {
        context.m_doc.DrawToDC( it, dib, dib.Width(), dib.Height(),
          view->ActiveViewport().View(),
          bIgnoreHighlights,
          bDrawTitle,
          bDrawConstructionPlane,
          bDrawWorldAxes
          );
      }
      else
      {
        context.m_doc.RenderToDC( it, dib, dib.Width(), dib.Height(),
          view->ActiveViewport().View(),
          bIgnoreHighlights,
          bDrawTitle,
          bDrawConstructionPlane,
          bDrawWorldAxes,
          view->ActiveViewport().GhostedShade()
          );
      }

      dib.WriteToFile( filename );
    }
  }

  return success;
}
```
