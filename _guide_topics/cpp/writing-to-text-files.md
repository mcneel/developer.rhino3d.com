---
title: Writing to Text Files
description: This brief guide discuss writing text files using C/C++.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/sdksamples/writetextfile
order: 1
keywords: ['rhino', 'text', 'file']
layout: toc-guide-page
---

 
## Problem

You need to write to a text file from my general utility plugin.

## Solution

Rhino C/C++ SDK does not have any special functions or classes to help you read or write text files.

With that said, there are a number of ways to read and write text files in C/C++.

1. Use the C-runtime library's `fopen`, `fputs`, `fwrite` and `fclose` functions.
1. You can use the `iostream` library's `ofstream` class.
1. You can use Win32's `CreateFile`, `WriteFile`, and `CloseHandle` functions.
1. You can use MFC's `CFile` and `CStdioFile` classes.

## Sample

Here is a simple example that uses the C-runtime library.

```cpp
/*
Description:
  Writes a string to a text file
Parameters:
  text     - [in] The string to write
  filename - [in] The name of the file to write. If the file does not
                  exist, it will be created. If the file does exist,
                  it will be overwritten.
Returns:
  true if successful, false otherwise.
*/
bool WriteStringToFile( const wchar_t* text, const wchar_t* filename )
{
  bool rc = false;
  if( (text && text[0]) && (filename && filename[0]) )
  {
    FILE* fp = _wfopen( filename, L"w" );
    if( fp )
    {
      size_t num_write = wcslen( text );
      size_t num_written = fwrite( text, sizeof(wchar_t), num_write, fp );
      fclose( fp );
      rc = ( num_written == num_write );
    }
  }
  return rc;
}
```
