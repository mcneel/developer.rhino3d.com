---
title: Logging Debug Info
description: This brief guide discusses the use of the ON_TextLog class for debugging C/C++ plugins.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/sdksamples/textlog
order: 1
keywords: ['rhino', 'log', 'debug']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## Overview

The openNURBS C/C++ SDK, which is also included with the Rhino C/C++ SDK, contains a `ON_TextLog` class that makes it very simple to write, or dump, information to a text file.  The class can be very handy when trying to debug geometric objects, for most objects have the ability to dump their contents to a log file.

## Sample

The following is an example of using the `ON_TextLog` class to dump the contents of a brep object to a text file.  For more information on `ON_TextLog`, see *opennurbs_textlog.h*

```cpp
CRhinoCommand::result CCommandTest::RunCommand(
    const CRhinoCommandContext& context )
{
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select brep" );
  go.SetGeometryFilter(
       CRhinoGetObject::surface_object |
       CRhinoGetObject::polysrf_object );
  go.GetObjects( 1, 1 );
  if( go.CommandResult() == CRhinoCommand::success )
  {
    const ON_Brep* brep = go.Object(0).Brep();
    if( brep )
    {
      FILE* fp = ON::OpenFile( L"c:\\bug_report.txt", L"w" );
      if( fp )
      {
        ON_TextLog text_log( fp );
        text_log.Print( L"Dumping Brep...\n" );
        brep->Dump( text_log );
        ON::CloseFile( fp );
      }
    }
  }
  return CRhinoCommand::success;
}
```
