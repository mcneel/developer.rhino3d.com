+++
aliases = ["/en/5/guides/cpp/picking-point-objects/", "/en/6/guides/cpp/picking-point-objects/", "/en/7/guides/cpp/picking-point-objects/", "/wip/guides/cpp/picking-point-objects/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This brief guide demonstrates how to use CRhinoGetObject to pick point objects using C/C++."
keywords = [ "rhino", "point", "picking" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Picking Point Objects"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/pickpoint"
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

 
## How To

If you need the user to define a 3D point location, you can use a `CRhinoGetPoint` object.  But, if the points already exist as objects in Rhino, you will need to use a `CRhinoGetObject` object to pick them.  Then, you can determine the 3D coordinates of that point object, for example:

```cpp
CRhinoGetObject go;
go.SetCommandPrompt( L"Select point" );
go.SetGeometryFilter( CRhinoGetObject::point_object );
CRhinoGet::result res = go.GetObjects( 1, 1 );
if( res == CRhinoGet::object )
{
  const CRhinoObjRef& objref = go.Object(0);
  const ON_Point* pt = objref.Point();
  if( pt )
    RhinoApp().Print(L"Point: %f,%f,%f", pt->point.x, pt->point.y, pt->point.z);
}
```

If you needed access to the `CRhinoPointObject` object, you could do this:

```cpp
CRhinoGetObject go;
go.SetCommandPrompt( L"Select point" );
go.SetGeometryFilter( CRhinoGetObject::point_object );
CRhinoGet::result res = go.GetObjects( 1, 1 );
if( res == CRhinoGet::object )
{
  const CRhinoObjRef& objref = go.Object(0);
  const CRhinoPointObject* point_object = CRhinoPointObject::Cast( objref.Object() );
  if( point_object )
  {
    const ON_Point& pt = point_object->Point();
    RhinoApp().Print(L"Point: %f,%f,%f", pt.point.x, pt.point.y, pt.point.z);
  }
}
```

Here is how you can pick one or more point objects:

```cpp
CRhinoGetObject go;
go.SetCommandPrompt( L"Select points" );
go.SetGeometryFilter( CRhinoGetObject::point_object );
CRhinoGet::result res = go.GetObjects( 1, 0 );
if( res == CRhinoGet::object )
{
  int i;
  for( i = 0; i < go.ObjectCount(); i++ )
  {
    const CRhinoObjRef& objref = go.Object(i);
    const ON_Point* point = objref.Point();
    if( point )
      RhinoApp().Print( L"Point %d: %f,%f,%f",
                        i,
                        point->point.x,
                        point->point.y,
                        point->point.z );
  }
}
```
