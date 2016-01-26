---
title: Reading Notes from a 3dm
description: Demonstrates how to read the user-added notes field from a 3DM file using either C/C++ or the openNURBS toolkit.
author: dalelear@mcneel.com
apis: ['openNURBS', 'C/C++']
languages: ['C/C++']
platforms: ['Cross-Platform']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/onreadnotes
order: 1
keywords: ['openNURBS', 'notes']
layout: code-sample-cpp
---

```cpp
bool ReadNotesFromRhino3dmFile( const wchar_t* filename, ON_wString& notes )
{
  if( 0 == filename || 0 == filename[0] )
    return false;

  // STEP 1: Open the file
  FILE* archive_fp = ON::OpenFile( filename, L"rb" );
  if( 0 == archive_fp )
    return false;

  // STEP 2: Create a binary archive object
  ON_BinaryFile archive( ON::read3dm, archive_fp );

  // STEP 3: Read 3dm start section
  int file_version = 0;
  ON_String start_section_comments;
  if( !archive.Read3dmStartSection(&file_version, start_section_comments) )
  {
    ON::CloseFile( archive_fp );
    return false;
  }

  // STEP 4: Read 3dm properties section
  ON_3dmProperties properties;
  if( !archive.Read3dmProperties(properties) )
  {
    ON::CloseFile( archive_fp );
    return false;
  }

  // STEP 5: Close the file
  ON::CloseFile( archive_fp );

  // return the notes
  notes = properties.m_Notes.m_notes;

  return true;
}
```
