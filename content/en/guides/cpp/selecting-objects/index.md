+++
aliases = ["/en/5/guides/cpp/selecting-objects/", "/en/6/guides/cpp/selecting-objects/", "/en/7/guides/cpp/selecting-objects/", "/wip/guides/cpp/selecting-objects/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This guide demonstrates interactively selecting objects using C/C++."
keywords = [ "rhino", "selecting" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Selecting Objects"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/selectobjects"
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

 
## Overview

The Rhino C/C++ SDK provides the class `CRhinoGetObject` that will let you interactively select objects on the screen.  This is a large class with many options.  We recommend that you read through the header file, *rhinoSdkGetObject.h*, before using.

To use the `CRhinoGetObject` class, put one on the stack and call its `GetObjects()` member.  It is possible to derive custom classes from `CRhinoGetObject`.  But, the class is powerful enough that deriving new classes from it is usually unnecessary.

If an instance of `CRhinoGetObject` was successful in selecting one or more objects, then use its `Object()` member to retrieve information about the selected object.  The `Object()` member returns a `CRhinoObjRef` class which has several member functions to help you quickly get to the information you are looking for.

## Samples

This sample selects a single object...

```cpp
CRhinoGetObject go;
go.SetCommandPrompt( L"Select object" );
CRhinoGet::result res = go.GetObjects( 1, 1 );
if( res == CRhinoGet::object )
{
  const CRhinoObjRef& obj_ref = go.Object( 0 );
  const CRhinoObject* obj = obj_ref.Object();
  if( obj )
  {
    // TODO
  }
}
```

This sample selects one or more objects...

```cpp
CRhinoGetObject go;
go.SetCommandPrompt( L"Select objects" );
CRhinoGet::result res = go.GetObjects( 1, 0 );
if( res == CRhinoGet::object )
{
  int i, count = go.ObjectCount();
  for( i = 0; i < count; i++ )
  {
    const CRhinoObjRef& obj_ref = go.Object( 0 );
    const CRhinoObject* obj = obj_ref.Object();
    if( obj )
    {
      // TODO
    }
  }
}
```

This sample selects a single curve object...

```cpp
CRhinoGetObject go;
go.SetCommandPrompt( L"Select curve" );
go.SetGeometryFilter( CRhinoGetObject::curve_object );
CRhinoGet::result res = go.GetObjects( 1, 1 );
if( res == CRhinoGet::object )
{
  const CRhinoObjRef& obj_ref = go.Object( 0 );
  const ON_Curve* crv = obj_ref.Curve();
  if( crv )
  {
    // TODO
  }
}
```
