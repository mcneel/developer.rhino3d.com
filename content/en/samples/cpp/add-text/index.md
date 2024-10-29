+++
aliases = ["/en/5/samples/cpp/add-text/", "/en/6/samples/cpp/add-text/", "/en/7/samples/cpp/add-text/", "/en/wip/samples/cpp/add-text/"]
authors = [ "dale" ]
categories = [ "Adding Objects", "Text" ]
description = "Demonstrates how to use ON_TextEntity2 to add text to Rhino."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Add Text"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/addtext"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0
+++

```cpp
bool AddAnnotationText(
      CRhinoDoc& doc,       // reference to active document
      const ON_3dPoint& pt, // location of anotation text
      const wchar_t* text,  // the text
      double height,        // height of text item
      const wchar_t* font,  // font or face name
      int style             // style 0=normal, 1=bold,
      )                     //       2=italic, 3=bold and italic
{
  bool rc = false;

  ON_wString wText( text );
  if( wText.IsEmpty() )
    return rc;

  if( height <= 0 )
    height = 1.0;

  ON_wString wFont( font );
  if( wFont.IsEmpty() )
    wFont = L"Arial";

  if( style < 0 | style > 3 )
    style = 0;

  ON_Plane plane = RhinoActiveCPlane();
  plane.SetOrigin( pt );

  ON_TextEntity2* text_entity = new ON_TextEntity2;
  CRhinoAnnotationText* text_object = new CRhinoAnnotationText;
  text_object->SetAnnotation( text_entity );
  text_object->SetTextHeight( height );
  text_object->SetString( wText );
  text_object->SetPlane( plane );
  int idx = doc.m_font_table.FindOrCreateFont( wFont, style & 1, style & 2 );
  text_object->SetFontIndex( idx );

  if( doc.AddObject(text_object) )
  {
    rc = true;
    doc.Redraw();
  }
  else
  {
    delete text_object;
    text_object = 0;
  }
  return rc;
}
```
