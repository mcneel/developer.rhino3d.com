+++
aliases = ["/en/5/guides/cpp/duplicating-objects-with-group/", "/en/6/guides/cpp/duplicating-objects-with-group/", "/en/7/guides/cpp/duplicating-objects-with-group/", "/en/wip/guides/cpp/duplicating-objects-with-group/"]
authors = [ "dale" ]
categories = [ "Advanced" ]
description = "This guide demonstrates how to duplicate objects that are members of one or more object groups using C/C++."
keywords = [ "rhino", "group", "copy" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Duplicating Objects with Group"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/copygroups"
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

When you duplicate a Rhino object which happens to be a member of a group, the duplicate object is (also) a member of that same group.  Is there a quick way to duplicate a Rhino object and have the duplicated object be a member of a new group?

## Solution

You can use the `RhinoUpdateObjectGroups` function.  See *rhinoSdkGrips.h* for details.

Here is a sample of its usage:

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select objects to copy in-place" );
  go.EnableGroupSelect( TRUE );
  go.EnableSubObjectSelect( FALSE );
  go.GetObjects( 1, 0 );
  if( go.CommandResult() != CRhinoCommand::success )
    return go.CommandResult();

  ON_Xform xform;
  xform.Identity();

  ON_2dexMap group_map;

  for( int i = 0; i < go.ObjectCount(); i++ )
  {
    const CRhinoObject* object = go.Object(i).Object();
    if( object )
    {
      CRhinoObject* duplicate = context.m_doc.TransformObject( object, xform, true, false, true );
      if( duplicate )
        RhinoUpdateObjectGroups( duplicate, group_map );
    }
  }

  context.m_doc.Redraw();

  return CRhinoCommand::success;
}
```
