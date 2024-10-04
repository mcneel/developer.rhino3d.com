+++
aliases = ["/en/5/samples/cpp/duplicate-object/", "/en/6/samples/cpp/duplicate-object/", "/en/7/samples/cpp/duplicate-object/", "/wip/samples/cpp/duplicate-object/"]
authors = [ "dale" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to make a copy of a CRhinoObject-derived object."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Duplicate Object"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/duplicateobject"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```cpp
const CRhinoObject* object = ..... // some object
CRhinoObject* duplicate = object->Duplicate();
if( duplicate )
{
  if( context.m_doc.AddObject(duplicate) )
    context.m_doc.Redraw;
  else
    delete duplicate;
}
```
