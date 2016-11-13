---
title: Screen Capture All Viewports
description: Demonstrates how to screen capture all the visible viewports to a file.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Viewports and Views']
origin: http://wiki.mcneel.com/developer/sdksamples/screencapture
order: 1
keywords: ['rhino']
layout: code-sample-cpp
---

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  AFX_MANAGE_STATE( ::RhinoApp().RhinoModuleState() );

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

  // Wait for the dialog to disappear. Otherwise,
  // we might see dialog artifacts in our image.
  RhinoApp().Wait( 500 );

  CMDIFrameWnd* pFrameWnd = (CMDIFrameWnd*)pMainWnd;
  if( pFrameWnd )
  {
    CWnd* pClientWnd = CWnd::FromHandle( pFrameWnd->m_hWndMDIClient );
    if( pClientWnd )
    {
      CClientDC srcDC( pClientWnd );

      CRect rect;
      pClientWnd->GetClientRect( rect );

      CRhinoDib dib;
      if( dib.CreateDib(rect.Width(), rect.Height(), 24, true) )
      {
        CDC* dstDC = dib;
        if( dstDC )
        {
          dstDC->BitBlt( 0, 0, rect.Width(), rect.Height(), &srcDC, 0, 0, SRCCOPY );
          dib.CopyToClipboard( 0 );
          dib.WriteToFile( filename );
        }
      }
    }
  }

  return success;
}
```