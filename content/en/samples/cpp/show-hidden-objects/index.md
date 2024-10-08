+++
aliases = ["/en/5/samples/cpp/show-hidden-objects/", "/en/6/samples/cpp/show-hidden-objects/", "/en/7/samples/cpp/show-hidden-objects/", "/en/wip/samples/cpp/show-hidden-objects/"]
authors = [ "dale" ]
categories = [ "Other" ]
description = "Demonstrates how to iterate through the geometry table and unhide hidden objects."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Show Hidden Objects"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/showallhiddenobjects"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0
+++

```cpp
int ShowAllHiddenObjects( CRhinoDoc& doc, bool bRedraw )
{
  CRhinoObjectIterator it(
        doc,
        CRhinoObjectIterator::undeleted_objects,
        CRhinoObjectIterator::active_and_reference_objects
        );
  it.IncludeLights();

  int count = 0;
  CRhinoObject* obj = 0;
  for( obj = it.First(); obj; obj = it.Next() )
  {
    // Ignore objects that are not hidden
    if( obj->Attributes().Mode() != ON::hidden_object )
      continue;
    // Ignore objects on hidden or locked layers
    if( ON::normal_layer != obj->ObjectLayer().Mode() )
      continue;
    if( doc.ShowObject(obj) )
      count++;
  }

  if( count > 0 && bRedraw )
    doc.Redraw();
  return count;
}
```
