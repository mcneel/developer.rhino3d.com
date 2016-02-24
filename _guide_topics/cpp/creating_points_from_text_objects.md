---
title: Creating Points from Text Objects
description: This brief guide demonstrates how to create point objects based on text entities using C/C++.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Uncategorized']
origin: http://wiki.mcneel.com/developer/sdksamples/pointsfromtext
order: 1
keywords: ['rhino', 'points', 'text', 'objects']
layout: toc-guide-page
---

# Creating Points from Text Objects

{{ page.description }}

## Problem

Imagine you have many text elements that display numeric values that identify elevation and you would like to convert these elements to points objects using the C/C++.  The text elements denote the elevations of the locations and you would like create the 2D point by the location of the text and then use the number of the text as the z-coordinate.

## Solution

To make picking text entities easier for the user, we will use a custom object picker that just filters `CRhinoAnnotationText` objects...

```cpp
class CRhGetTextObject : public CRhinoGetObject
{
public:
  bool CustomGeometryFilter(
        const CRhinoObject* object,
        const ON_Geometry* geometry,
        ON_COMPONENT_INDEX component_index
        ) const
  {
    if( object && CRhinoAnnotationText::Cast(object) )
      return true;
    return false;
  }
};
```

Here is the portion of the command that creates points from the text entities...

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  CRhGetTextObject go;
  go.SetCommandPrompt( L"Select text" );
  go.GetObjects( 1, 0 );
  if( go.CommandResult() != success )
    return go.CommandResult();

  int i;
  for( i = 0; i < go.ObjectCount(); i++ )
  {
    const CRhinoAnnotationText* text_obj = CRhinoAnnotationText::Cast( go.Object(i).Object() );
    if( 0 == text_obj )
      continue;

    ON_wString text_str( text_obj->String() );
    text_str.TrimLeftAndRight();

    double z = 0.0;
    if( RhinoParseNumber(text_str, &z) )
    {
      ON_3dPoint text_pt = text_obj->m_text_block.Plane().Origin();
      text_pt.z = z;
      context.m_doc.AddPointObject( text_pt );
    }
  }

  context.m_doc.Redraw();

  return success;
}
```
