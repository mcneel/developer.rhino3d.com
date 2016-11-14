---
title: Extracting Thumbnail Preview Images
description: This guide demonstrates how to extract the thumbnail preview image from a 3dm file using C/C++.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Advanced']
origin: http://wiki.mcneel.com/developer/sdksamples/extractthumbnail
order: 1
keywords: ['rhino', 'thumbnail']
layout: toc-guide-page
---

 
## Problem

You would like to be able to display a 3dm file's thumbnail preview image in a dialog box.

## Solution

When Rhino reads a 3dm file, it ignores the thumbnail preview image stored in the file (since it is never used).  Thus, if you want to obtain the thumbnail preview image for the current document, or any 3dm file, you will have to read the 3dm file yourself.  Fortunately, you only need to read a very small portion of the 3dm file to get the thumbnail preview image.

Rhino stores a document's thumbnail preview image as an `ON_WindowsBitmap`, which is just an uncompressed Windows device independent bitmap, or DIB. At the heart of `ON_WindowsBitmap` is simply a Windows `BITMAPINFO` structure.

## Sample

The following sample code demonstrates how to read the thumbnail preview image from a 3dm file.

```cpp
bool Read3dmThumbnailPreviewImage( const wchar_t* filename, ON_WindowsBitmap& bitmap )
{
  if( 0 == filename | 0 == filename[0] )
    return false;

  try
  {
    FILE* archive_fp = ON::OpenFile( filename, L"rb" );
    if( 0 == archive_fp )
      return false;

    ON_BinaryFile archive( ON::read3dm, archive_fp );

    // STEP 1: REQUIRED - Read start section
    int file_version = 0;
    ON_String strComments;
    if( !archive.Read3dmStartSection(&file_version, strComments) )
    {
      ON::CloseFile( archive_fp );
      return false;
    }

    // STEP 2: REQUIRED - Read properties section
    ON_3dmProperties properties;
    if( !archive.Read3dmProperties(properties) )
    {
      ON::CloseFile( archive_fp );
      return false;
    }

    ON::CloseFile( archive_fp );

    if( !properties.m_PreviewImage.IsValid() )
      return false;

    bitmap = properties.m_PreviewImage;
  }

  catch(...) // Handle all exceptions
  {
    return false;
  }

  return true;
}
```
