---
title: Creating a Custom CRhinoGetObject Class
description: This guide demonstrates how to derive a class from CRhinoGetObject to handle special case object picking.
author: ['Dale Fugier', '@dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Advanced']
origin: http://wiki.mcneel.com/developer/sdksamples/customgeometryfilter
order: 1
keywords: ['rhino', 'picking']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## Overview

The `CRhinoGetObject` class that is used for interactively picking one or more objects is a large, full-featured class (see *rhinoSdkGetObject.h* for details). But, on occasion, the class does not offer enough options.  For example, `CRhinoGetObject` is capable of picking curve objects.  But, it is not capable of picking polyline curve objects that are closed.  When the required object filtering exceeds the capabilities of the base class, it's time to derive your own.

`CRhinoGetObject` has a virtual function named `CustomGeometryFilter()` that is called after all obvious geometry filter checks have been performed.  Thus, if you derive a new class from `CRhinoGetObject` and override this virtual member, you can filter for most any geometric object or property.

## Sample

The following example code demonstrates deriving from `CRhinoGetObject`.  In this example, we want to allow the user to only select closed polylines...

```cpp
class CRhGetClosedPolylineObject : public CRhinoGetObject
{
public:
  bool CustomGeometryFilter(
        const CRhinoObject* obj,
        const ON_Geometry* geom,
        RHINO_COMPONENT_INDEX idx
        ) const;
};

bool CRhGetClosedPolylineObject::CustomGeometryFilter(
        const CRhinoObject* obj,
        const ON_Geometry* geom,
        RHINO_COMPONENT_INDEX idx
        ) const
{
  if( geom )
  {
    // is it a polyline?
    if( const ON_PolylineCurve* p = ON_PolylineCurve::Cast(geom) )
    {
      if( p->IsClosed() && p->IsPolyline() > 3 )
        return true;
    }
    // is is a polycurve that looks like a polyline?
    if( const ON_PolyCurve* p = ON_PolyCurve::Cast(geom) )
    {
      if( p->IsClosed() && p->IsPolyline() > 3 )
        return true;
    }
    // is it a [[rhino:nurbs|NURBs]] curve that looks like a polyline?
    if( const ON_Curve* p = ON_Curve::Cast(geom) )
    {
      ON_NurbsCurve n;
      if( p->GetNurbForm(n) )
      {
        if( n.IsClosed() && n.IsPolyline() > 3 )
          return true;
      }
    }
  }
  return false;
}
```

We can use the above class as follows:

```cpp
CRhGetClosedPolylineObject go;
go.SetCommandPrompt( L"Select closed polyline" );
go.SetGeometryFilter( CRhinoGetObject::curve_object );
go.GetObjects( 1, 1 );
if( go.CommandResult() == CRhinoCommand::success )
{
  // TODO...
}
```
