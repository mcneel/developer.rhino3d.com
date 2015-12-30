---
layout: code-sample-cpp
title: Test if an Object is a Circle
author: dale@mcneel.com
platforms: ['Windows']
apis: ['C/C++']
languages: ['C/C++']
keywords: ['rhino']
categories: ['Unsorted']
origin: http://wiki.mcneel.com/developer/sdksamples/iscircle
description: Demonstrates how to test if an object looks like a circle.
order: 1
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
