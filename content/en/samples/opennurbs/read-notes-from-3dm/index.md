+++
authors = [ "dalelear" ]
categories = [ "Fundamentals" ]
description = "Demonstrates how to read the user-added notes field from a 3DM file using either C/C++ or the openNURBS toolkit."
keywords = [ "openNURBS", "notes" ]
languages = [ "C/C++" ]
sdk = [ "openNURBS", "C/C++" ]
title = "Reading Notes from a 3dm"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/onreadnotes"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

+++

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
