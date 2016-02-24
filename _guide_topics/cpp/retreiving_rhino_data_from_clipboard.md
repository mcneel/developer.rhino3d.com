---
title: Retrieving Rhino Data from the Clipboard
description: This guide demonstrates how to access Rhino data from the Windows Clipboard using C/C++.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Advanced']
origin: http://wiki.mcneel.com/developer/sdksamples/clipboard
order: 1
keywords: ['rhino', 'clipboard']
layout: toc-guide-page
---

# Retrieving Rhino Data from the Clipboard

{{ page.description }}

## Overview

Like most Windows applications, Rhino can cut, copy, and paste information to and from the Windows Clipboard.  When Rhino either cuts or copies geometry to the clipboard, it creates a temporary 3DM file that contains the selected geometry.  Rhino then stores the temporary filename in the Clipboard.  When a paste operation is invoked, Rhino determines if the Clipboard contains the name of a temporary Rhino file.  If found, Rhino simply imports the temporary file.

Rhino registers custom Clipboard formats to store the temporary file names: a unique Clipboard format for each Rhino version.

## Sample

The following sample demonstrates how to determine of there is Rhino information in the Windows Clipboard.  If there is Rhino data in the Clipboard, the sample will retrieve the name of the temporary file.  Once this file name is known, you can whatever means necessary to retrieve the data.  For example, if you are using this code from a Rhino plugin, you could script the running of Rhino's *Paste* command to insert the geometry into the current document.  If you are in a standalone application, you would use the opennurbs toolkit to read the temporary .3DM file.

```cpp
/////////////////////////////////////////////////////////////////////////////
// clipboard.cpp

#include "StdAfx.h"
#include <afxole.h> // MFC OLE clipboard support

// TODO: Fill this in with your own message printing
static void myPrintMessage( LPCTSTR lpMessage )
{
  if( 0 == lpMessage || 0 == lpMessage[0] )
    return;
#ifdef RHINO_SDK_CLASS
  RhinoApp().Print( ON_wString(lpMessage) );
#else
  MessageBox( 0, lpMessage, _T("Clipboard Message"), MB_SYSTEMMODAL|MB_OK|MB_ICONINFORMATION);
#endif
}

// TODO: Return your application main window handle
static HWND myMainWnd()
{
#ifdef RHINO_SDK_CLASS
  return RhinoApp().MainWnd();
#else
  return AfxGetMainWnd()->m_hWnd;
#endif
}

static UINT myGetClipboardFormat( int ver = 4 )
{
  UINT v = 0;

  if( 1 == ver )      // Rhino 1.0
  {
    static UINT v1 = 0;
    if( v1 < 1 )
      v1 = RegisterClipboardFormat( _T("Rhino 1.0 3DM Clip") );
    v = v1;
  }
  else if( 2 == ver ) // Rhino 2.0
  {
    static UINT v2 = 0;
    if( v2 < 1 )
      v2 = RegisterClipboardFormat( _T("Rhino 2.0 3DM Clip") );
    v = v2;
  }
  else if( 3 == ver ) // Rhino 3.0
  {
    static UINT v3 = 0;
    if( v3 < 1 )
      v3 = RegisterClipboardFormat( _T("Rhino 3.0 3DM Clip") );
    v = v3;
  }
  else if( 4 == ver ) // Rhino 4.0
  {
    static UINT v4 = 0;
    if( v4 < 1 )
      v4 = RegisterClipboardFormat( _T("Rhino 4.0 3DM Clip global mem") );
    v = v4;
  }

  return v;
}

static BOOL myGetTempFileName( CString& strResult )
{
  CString strPath, strFileName;

  int rc = GetTempPath( _MAX_PATH, strPath.GetBuffer(_MAX_PATH) );
  strPath.ReleaseBuffer();

  if( rc == 0 )
    return false;

  rc = GetTempFileName( strPath, _T("rh$"), 0, strFileName.GetBuffer(_MAX_PATH) );
  strFileName.ReleaseBuffer();

  if( rc == 0 )
    return false;

  strResult = strFileName;
  return true;
}

static BOOL CopyClipboardToTempFile( CString& strTempFileName, UINT clipboard_format )
{
  if( !IsClipboardFormatAvailable(clipboard_format) )
  {
    myPrintMessage( _T("CopyClipboardV2ToTempFile() - Rhino clipboard format is not available.\n") );
    return false;
  }

  CString strFileName;
  if( !myGetTempFileName(strFileName) )
  {
    myPrintMessage( _T("CopyClipboardV2ToTempFile() - Unable to calculate temporary file name.\n" ));
    return false;
  }

  if( !OpenClipboard(myMainWnd()) )
  {
    myPrintMessage( _T("CopyClipboardV2ToTempFile() - Unable to open clipboard.\n") );
    return false;
  }

  HANDLE hMem = GetClipboardData( clipboard_format );
  if( 0 == hMem )
  {
    myPrintMessage( _T("CopyClipboardV2ToTempFile() - Unable to get clipboard data.\n") );
    CloseClipboard();
    return false;
  }

  DWORD* ptr = (ULONG*)GlobalLock( hMem );
  if( 0 == ptr )
  {
    myPrintMessage( _T("CopyClipboardV2ToTempFile() - Unable to lock global memory block.\n") );
    CloseClipboard();
    return false;
  }

  // size is encoded in the first dword
  int size = (int)ptr[0];
  if( size <= 0)
  {
    myPrintMessage( _T("CopyClipboardV2ToTempFile() - Unable to determine size of clipboard memory block.\n") );
    GlobalUnlock( hMem );
    CloseClipboard();
    return false;
  }

  FILE* fp = _tfopen( strFileName, _T("wb") );

#define CopyClipboardV2ToTempFile_BAIL( msg )\
{\
  GlobalUnlock( hMem );\
  CloseClipboard();\
  if( fp )\
  {\
    fclose( fp );\
    ::DeleteFile( strFileName );\
  }\
  CloseClipboard();\
  myPrintMessage( msg );\
}

  if( 0 == fp )
    CopyClipboardV2ToTempFile_BAIL( _T("CopyClipboardV2ToTempFile() - Unable to open temporary file.\n") );

  if( fwrite(&ptr[1], size, 1, fp) != 1 )
    CopyClipboardV2ToTempFile_BAIL( _T("CopyClipboardV2ToTempFile() - Unable to write information to temporary file.\n") );

  if( ferror(fp) )
    CopyClipboardV2ToTempFile_BAIL( _T("CopyClipboardV2ToTempFile() - Error in temporary file stream.\n") );

  if( fflush(fp) )
    CopyClipboardV2ToTempFile_BAIL( _T("CopyClipboardV2ToTempFile() - Error in flushing temporary file buffers.\n"));

  if( fclose(fp) )
    CopyClipboardV2ToTempFile_BAIL( _T("CopyClipboardV2ToTempFile() - Error in closing temporary file.\n") );

  GlobalUnlock( hMem );

  if( 0 == CloseClipboard() )
  {
    DeleteFile( strFileName );
    myPrintMessage( _T("CopyClipboardV2ToTempFile() - Unable to close the clipboard.\n") );
    return false;
  }

  strTempFileName = strFileName;
  return true;
}

static BOOL ReadFileNameFromClipboard( const wchar_t* lpFileName, CString& strOutputFile )
{
  CString strFileName( lpFileName );
  strFileName.TrimLeft();
  strFileName.TrimRight();
  if( strFileName.IsEmpty() )
    return false;

  if( !myGetTempFileName(strOutputFile) )
    return false;

  return CopyFile( strFileName, strOutputFile, false );
}

static BOOL GetFileFromClipboard( CString& strFileName, int& file_version )
{
  FORMATETC fe = { 0, 0, DVASPECT_CONTENT, -1, TYMED_FILE };
  STGMEDIUM stgm;

  COleDataObject odo;
  odo.AttachClipboard();

  // V4 file in clipboard
  UINT v4_cbformat = myGetClipboardFormat( 4 );
  fe.cfFormat = v4_cbformat;
  if( odo.GetData(v4_cbformat, &stgm, &fe) && stgm.tymed == TYMED_FILE )
  {
    file_version = 4;
    return ReadFileNameFromClipboard( stgm.lpszFileName, strFileName );
  }

  // V3 file in clipboard
  UINT v3_cbformat = myGetClipboardFormat( 3 );
  fe.cfFormat = v3_cbformat;
  if( odo.GetData(v3_cbformat, &stgm, &fe) && stgm.tymed == TYMED_FILE )
  {
    file_version = 3;
    return ReadFileNameFromClipboard( stgm.lpszFileName, strFileName );
  }

  // V1 or V2 file in clipboard
  UINT v1_cbformat = myGetClipboardFormat( 1 );
  UINT v2_cbformat = myGetClipboardFormat( 2 );
  UINT clipboard_format = 0;
  if( ::IsClipboardFormatAvailable(v2_cbformat) )
  {
    file_version = 2;
    clipboard_format = v2_cbformat;
  }
  else if( ::IsClipboardFormatAvailable(v1_cbformat) )
  {
    file_version = 1;
    clipboard_format = v1_cbformat;
  }

  if( clipboard_format > 0 )
    return CopyClipboardToTempFile( strFileName, clipboard_format );

  return false;
}
```
