---
title: Test if an Object is a Circle
description: Demonstrates how to test if an object looks like a circle.
authors: ['dale_fugier']
author_contacts: ['dale']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/sdksamples/iscircle
order: 1
keywords: ['rhino']
layout: code-sample-cpp
---

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
