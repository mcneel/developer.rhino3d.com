+++
aliases = ["/5/guides/cpp/creating-points-from-text-objects/", "/6/guides/cpp/creating-points-from-text-objects/", "/7/guides/cpp/creating-points-from-text-objects/", "/wip/guides/cpp/creating-points-from-text-objects/"]
authors = [ "dale" ]
categories = [ "Advanced" ]
description = "This brief guide demonstrates how to create point objects based on text entities using C/C++."
keywords = [ "rhino", "points", "text", "objects" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Creating Points from Text Objects"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/pointsfromtext"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

 
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
