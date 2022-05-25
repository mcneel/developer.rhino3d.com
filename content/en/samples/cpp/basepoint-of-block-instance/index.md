+++
authors = [ "dale" ]
categories = [ "Blocks" ]
description = "Demonstrates how to find the basepoint coordinates of a block instance."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Basepoint of Block Instance"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/blockinsertionpoint"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```cpp
ON_3dPoint BlockInstanceInsertionPoint(const CRhinoInstanceObject* instance_obj)
{
  ON_3dPoint pt = ON_UNSET_POINT;
  if (instance_obj != 0)
  {
    pt = ON_origin;
    pt.Transform(instance_obj->InstanceXform());
  }
  return pt;
}
```
