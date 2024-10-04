+++
aliases = ["/en/5/guides/cpp/getting-script-added-objects/", "/en/6/guides/cpp/getting-script-added-objects/", "/en/7/guides/cpp/getting-script-added-objects/", "/wip/guides/cpp/getting-script-added-objects/"]
authors = [ "dale" ]
categories = [ "Advanced" ]
description = "This guide demonstrates how to locate objects that were added to Rhino by a script using C/C++."
keywords = [ "rhino", "script" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Getting Script-Added Objects"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/scriptcommandobjects"
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

You have a command, derived from `CRhinoScriptCommand`, that scripts several Rhino command that add objects.  After running the scripts, with `CRhinoApp::RunScript`, you would like to get the addresses, or pointers, of the added objects.  But the commands that create the new objects do not select then.  Is there a way to get the added objects' addresses in this case?

## Solution

See of the following sample gives you any ideas...

```cpp
static int CompareObjectPtr( const CRhinoObject* const * a, const CRhinoObject* const * b )
{
  INT_PTR d = (*a) - (*b);
  return ( (d < 0) ? -1 : ( (d > 0) ? 1 : 0 ) );
}

CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  // Disable redrawing
  CRhinoView::EnableDrawing( FALSE );

  // Get the next runtime object serial number before scripting
  unsigned int first_sn = CRhinoObject::NextRuntimeObjectSerialNumber();

  // Do some scripting...
  RhinoApp().RunScript( L"_-Line 0,0,0 10,10,0", 0 );
  RhinoApp().RunScript( L"_SelLast", 0 );
  RhinoApp().RunScript( L"_-Properties _Object _Color _Object 255,0,0 _Enter _Enter", 0 );
  RhinoApp().RunScript( L"_-Circle 0,0,0 10", 0 );
  RhinoApp().RunScript( L"_SelLast", 0 );
  RhinoApp().RunScript( L"_-Properties _Object _Color _Object 0,0,255 _Enter _Enter", 0 );

  // Get the next runtime object serial number after scripting
  unsigned int next_sn = CRhinoObject::NextRuntimeObjectSerialNumber();

  // Enable redrawing
  CRhinoView::EnableDrawing( TRUE );

  // if the two are the same, then nothing happened
  if( first_sn == next_sn )
    return CRhinoCommand::nothing;

  // The the pointers of all of the objects that were added during scripting
  ON_SimpleArray<const CRhinoObject*> objects;
  for( unsigned int sn = first_sn; sn < next_sn; sn++ )
  {
    const CRhinoObject* obj = context.m_doc.LookupObjectByRuntimeSerialNumber( sn );
    if( obj && !obj->IsDeleted() )
      objects.Append( obj );
  }

  // Sort and cull the list, as there may be duplicates
  if( objects.Count() > 1 )
  {
    objects.HeapSort( CompareObjectPtr );
    const CRhinoObject* last_obj = objects[objects.Count()-1];
    for( int i = objects.Count()-2; i >= 0; i-- )
    {
      const CRhinoObject* prev_obj = objects[i];
      if( last_obj == prev_obj )
        objects.Remove(i);
      else
        last_obj = prev_obj;
    }
  }

  // Do something with the list...
  for( int i = 0; i < objects.Count(); i++ )
  {
    const CRhinoObject* obj = objects[i];
    if( obj->IsSelectable(true) )
      obj->Select( true );
  }

  context.m_doc.Redraw();

  return CRhinoCommand::success;
}
```
