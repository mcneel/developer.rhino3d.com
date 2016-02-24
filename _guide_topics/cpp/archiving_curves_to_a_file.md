---
title: Archiving Curves to a File
description: This guide demonstrates how to write and read curves to a file using C/C++.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Uncategorized']
origin: http://wiki.mcneel.com/developer/sdksamples/archivecurve
order: 1
keywords: ['rhino', 'curves', 'serializing']
layout: toc-guide-page
---

# Archiving Curves to a File

{{ page.description }}

## Problem

Writing curves to a file has some special considerations.  Curves come in many variations: the curve could be a circle, simple curve, or a polycurve.  You cannot know in advance what the user will be selecting.  As such, the class containing my data declares it as an `ON_Curve`.

Writing the data is not an issue.  You simply call `ON_Curve::Write`.  However, things don't go so well when you try to read the data.  You need a way to simply read curve data without going to a non-abstract class. What is needed is a way to read/write curve data that represents any kind of curve possible.

## Solution

It is probably best not to call `ON_Curve::Write` for this very reason.  When serializing anything derived from `ON_Object`, just use `ON_BinaryArchive::WriteObject` and `ON_BinaryArchive::ReadObject`...

### Write
```cpp
static bool WriteCurveFile( FILE* fp, const ON_Curve* curve )
{
  if( 0 == fp || 0 == curve )
    return false;

  ON_BinaryFile archive( ON::write3dm, fp );

  int major_version = 1;
  int minor_version = 0;
  bool rc = archive.BeginWrite3dmChunk( TCODE_ANONYMOUS_CHUNK, major_version, minor_version );
  if( !rc )
    return false;

  for(;;)
  {
    // version 1.0 fields
    rc = ( archive.WriteObject(curve) ? true : false );
    if( !rc ) break;

    // todo...

    break;
  }

  if( !archive.EndWrite3dmChunk() )
    rc = false;

  return rc;
}
```

### Read

```cpp
static bool ReadCurveFile( FILE* fp, ON_Curve*& curve )
{
  if( 0 == fp )
    return false;

  ON_BinaryFile archive( ON::read3dm, fp );

  int major_version = 0;
  int minor_version = 0;
  bool rc = archive.BeginRead3dmChunk( TCODE_ANONYMOUS_CHUNK, &major_version, &minor_version );
  if( !rc )
    return false;

  for(;;)
  {
    rc = ( 1 == major_version );
    if( !rc ) break;

    // version 1.0 fields
    ON_Object* object = 0;
    rc = ( archive.ReadObject(&object) ? true : false );
    if( !rc ) break;

    curve = ON_Curve::Cast( object );

    // todo...

    break;
  }

  if( !archive.EndRead3dmChunk() )
    rc = false;

  return ( rc && curve );
}
```

## Sample

To use the above functions, you could do the following:

```cpp
bool rc = false;

FILE* fp = ON::OpenFile( filename, L"wb" );
if( fp )
{
  rc = WriteCurveFile( fp, curve );
  ON::CloseFile( fp );
}

if( rc )
  RhinoApp().Print( L"Successfully wrote %s.\n", filename.Array() );
else
  RhinoApp().Print( L"Errors while writing %s.\n", filename.Array() );
```

and

```cpp
bool rc = false;
ON_Curve* curve = 0

FILE* fp = ON::OpenFile( filename, L"rb" );
if( fp )
{
  ReadCurveFile( fp, curve );
  ON::CloseFile( fp );
}

if( rc )
{
  CRhinoCurveObject* curve_object = new CRhinoCurveObject();
  curve_object->SetCurve( curve );
  context.m_doc.AddObject( curve_object );
  context.m_doc.Redraw();
}
else
  RhinoApp().Print( L"Errors while reading %s.\n", filename.Array() );
```
