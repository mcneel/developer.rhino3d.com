+++
aliases = ["/en/5/samples/cpp/test-if-object-is-circle/", "/en/6/samples/cpp/test-if-object-is-circle/", "/en/7/samples/cpp/test-if-object-is-circle/", "/en/wip/samples/cpp/test-if-object-is-circle/"]
authors = [ "dale" ]
categories = [ "Other" ]
description = "Demonstrates how to test if an object looks like a circle."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Test if an Object is a Circle"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/iscircle"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0
+++

```cpp
bool IsCircle( const CRhinoObject* obj )
{
  bool rc = false;
  if( obj )
  {
    // Is the object a circle?
    if( const ON_ArcCurve* arc = ON_ArcCurve::Cast(obj->Geometry()) )
    {
      if( arc->IsCircle() )
        rc = true;
    }
    // Is the object an curve that just looks like a circle?
    else if( const ON_Curve* crv = ON_Curve::Cast(obj->Geometry()) )
    {
      ON_NurbsCurve nurb;
      if( crv->GetNurbForm(nurb) )
      {
        ON_Arc arc;
        double tol = ::RhinoApp().ActiveDoc()->AbsoluteTolerance();
        if( nurb.IsArc(0, &arc, tol) && arc.IsCircle()  )
          rc = true;
      }
    }
  }
  return rc;
}
```
