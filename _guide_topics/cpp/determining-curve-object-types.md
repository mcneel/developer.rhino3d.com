---
title: Determining Curve Object Types
description: This guide demonstrates how to determine the curve type using C/C++.
authors: ['dale_fugier']
author_contacts: ['dale']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/sdksamples/curvecast
order: 1
keywords: ['rhino', 'curve']
layout: toc-guide-page
---

 
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
