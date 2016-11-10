---
title: Showing Objects Transforming Dynamically
description: This guide demonstrates how to dynamically draw transforming objects using C/C++.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Advanced']
origin: http://wiki.mcneel.com/developer/sdksamples/setmodelxform
order: 1
keywords: ['rhino', 'transform']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## Overview

The `CRhinoViewport` class has two member functions, `GetModelXform()` and `SetModelXform()`, that either retrieve or modify the model transformation matrix that is applied to objects before they are drawn.  The model transformation matrix is intended to be used for dynamic drawing of objects.  Note, the default model transformation matrix is the identity.

Some of the Rhino command that use this technique to dynamically draw transforming objects include the *Move*, *Copy*, *Scale*, and *Rotate* commands.  These commands derive new `CRhinoGetPoint` classes and override the virtual `DynamicDraw()` member function to draw objects dynamically as the mouse moves during a point picking operation.

## Sample

The following is an sample `CRhinoGetPoint`-derived class that demonstrates how to dynamically draw transforming objects during a point picking operation.  In this sample, the transformation is a simple translation, like used in the *Move* command.

First, the class declaration...

```cpp
////////////////////////////////////////////////////////////////////
// CRhinoGetTranslationPoint declaration

class CRhinoGetTranslationPoint : public CRhinoGetPoint
{
public:

  CRhinoGetTranslationPoint();
  ~CRhinoGetTranslationPoint() {}

  // CRhinoGetPoint overrides  
  void SetBasePoint( ON_3dPoint base_point, BOOL bShowDistanceInStatusBar = false );
  void OnMouseMove( CRhinoViewport& vp, UINT flags, const ON_3dPoint& pt, const CPoint* p );
  void DynamicDraw( HDC hdc, CRhinoViewport& vp, const ON_3dPoint& pt );

  // Additional helpers
  void AddObject( const CRhinoObject* object );
  void CalculateTranslation( const ON_3dPoint& pt, ON_Xform& xform );

private:
  ON_3dPoint m_start_point; // starting point of translation
  ON_Xform m_xform; // transformation matrix
  ON_SimpleArray<const CRhinoObject*> m_objects; //objects to transform
};

////////////////////////////////////////////////////////////////////
// CRhinoGetTranslationPoint definition

CRhinoGetTranslationPoint::CRhinoGetTranslationPoint()
{
  m_xform.Identity();
}

void CRhinoGetTranslationPoint::AddObject( const CRhinoObject* object )
{
  m_objects.Append( object );
}

void CRhinoGetTranslationPoint::SetBasePoint(
      ON_3dPoint base_point,
      BOOL bShowDistanceInStatusBar
      )
{
  m_start_point = base_point;
  CRhinoGetPoint::SetBasePoint( base_point, bShowDistanceInStatusBar );
}

void CRhinoGetTranslationPoint::CalculateTranslation(
      const ON_3dPoint& pt,
      ON_Xform& xform
      )
{
  ON_3dVector v = pt - m_start_point;
  if( v.IsTiny() )
    xform.Identity();
  else
    xform.Translation( v );
}

void CRhinoGetTranslationPoint::OnMouseMove(
     CRhinoViewport& vp,
     UINT flags,
     const ON_3dPoint& pt,
     const CPoint* p
     )
{
  // Everytime the mouse moves, calculate the translation
  CalculateTranslation( pt, m_xform );
  CRhinoGetPoint::OnMouseMove( vp, flags, pt, p );
}

void CRhinoGetTranslationPoint::DynamicDraw(
     HDC hdc,
     CRhinoViewport& vp,
     const ON_3dPoint& pt
     )
{
  // Time to draw our objects dynamically
  int i, count = m_objects.Count();
  if( m_xform.IsIdentity() == false && count > 0 )
  {
    ON_Color saved_color = vp.DrawColor();
    ON_Xform saved_model_xform;
    // Save the current model transformation, we will
    // need to restore it later
    vp.GetModelXform( saved_model_xform );
    // Set the model transformation to ours
    vp.SetModelXform( m_xform );
    // Draw all of the objects in our array
    for( i = 0; i < m_objects.Count(); i++ )
    {
      const CRhinoObject* object = m_objects[i];
      if( object == 0 )
        continue;
      vp.SetDrawColor( object->ObjectDrawColor(TRUE) );
      object->Draw( vp );
      if( vp.InterruptDrawing() )
        break;
    }
    // Reset modified viewport members
    vp.SetModelXform( saved_model_xform );
    vp.SetDrawColor( saved_color );
  }

  // Let the base class do its drawing too
  CRhinoGetPoint::DynamicDraw( hdc, vp, pt );
}
```
