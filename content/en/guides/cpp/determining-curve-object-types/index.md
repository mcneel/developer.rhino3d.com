+++
aliases = ["/5/guides/cpp/determining-curve-object-types/", "/6/guides/cpp/determining-curve-object-types/", "/7/guides/cpp/determining-curve-object-types/", "/wip/guides/cpp/determining-curve-object-types/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This guide demonstrates how to determine the curve type using C/C++."
keywords = [ "rhino", "curve" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Determining Curve Object Types"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/curvecast"
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

Given an `ON_Curve`, how can one determine which kind of `ON_Curve`-derived object it really is?  (e.g. `ON_LineCurve`, `ON_ArcCurve`, `ON_PolylineCurve`, `ON_PolyCurve`, `ON_NurbsCurve`, etc.)?

## Solution

Basically, you try to cast the `ON_Curve` object to one of the `ON_Curve`-derived classes using its `Cast` operator.  If the cast operation is success, you are good to go.  If it fails, then you know the test object is some other `ON_Curve`-derived object.

## Sample

```cpp
const ON_LineCurve* GetLineCurve( const ON_Curve* crv )
{
  const ON_LineCurve* p = 0;
  if( crv != 0 )
    p = ON_LineCurve::Cast( crv );
  return p;
}

const ON_ArcCurve* GetArcCurve( const ON_Curve* crv )
{
  const ON_ArcCurve* p = 0;
  if( crv != 0 )
    p = ON_ArcCurve::Cast( crv );
  return p;
}

const ON_PolylineCurve* GetPolylineCurve( const ON_Curve* crv )
{
  const ON_PolylineCurve* p = 0;
  if( crv != 0 )
    p = ON_PolylineCurve::Cast( crv );
  return p;
}

const ON_PolyCurve* GetPolyCurve( const ON_Curve* crv )
{
  const ON_PolyCurve* p = 0;
  if( crv != 0 )
    p = ON_PolyCurve::Cast( crv );
  return p;
}

const ON_NurbsCurve* GetNurbsCurve( const ON_Curve* crv )
{
  const ON_NurbsCurve* p = 0;
  if( crv != 0 )
    p = ON_NurbsCurve::Cast( crv );
  return p;
}
```
