---
title: Dynamically Drawing Polylines
description: This guide demonstrates how to derive a new class from CRhinoGetPoint to dynamically draw a polyline.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Advanced']
origin: http://wiki.mcneel.com/developer/sdksamples/getpoints
order: 1
keywords: ['rhino', 'polylines']
layout: toc-guide-page
---

 
## Problem

What is the best way to draw dynamically a geometry based on a polyline?  How is it possible to compute an object geometry based on a polyline picked by the user?

## Solution

If you are not interested in writing your own drawing routine and you want to just use Rhino's built-in polyline drawing tool, then you can just use Rhino's `RhinoGetPolyline` function.  See *rhinoSdkGetLine.h* for more information.

If you need more control over how the polyline is define or how it is drawn, then you can derive your own class from `CRhinoGetPoint` and draw the polyline yourself.

## Sample

The following sample code demonstrates a simple class, derived from `CRhinoGetPoint`, that dynamically draws a polyline based on the points picked by a user.

```cpp
/////////////////////////////////////////////////////////////////////////////
// CRhGetPoints declaration

class CRhGetPoints : public CRhinoGetPoint
{
public:
  CRhGetPoints();
  void DynamicDraw( HDC hdc, CRhinoViewport& vp, const ON_3dPoint& pt );
  CRhinoGet::result GetPoints( CRhinoHistory* history = NULL, bool bOnMouseUp = false );
  int Points( ON_3dPointArray& points );

public:
  ON_3dPointArray m_P;
};

/////////////////////////////////////////////////////////////////////////////
// CRhGetPoints definition

CRhGetPoints::CRhGetPoints()
{
  m_P.SetCapacity( 64 );
}

CRhinoGet::result CRhGetPoints::GetPoints( CRhinoHistory* history, bool bOnMouseUp )
{
  m_P.Empty();

  SetCommandPrompt( L"First point" );

  CRhinoGet::result res = GetPoint( history, bOnMouseUp );

  if( res == CRhinoGet::point )
  {
    m_P.Append( Point() );

    SetCommandPrompt( L"Next point" );
    PermitOrthoSnap();
    AcceptNothing();

    for( ;; )
    {
      SetBasePoint( Point() );

      res = GetPoint( history, bOnMouseUp );

      if( res == CRhinoGet::point )
      {
        m_P.Append( Point() );
        continue;
      }

      else if( res == CRhinoGet::nothing )
        res = CRhinoGet::point;

      else if( res == CRhinoGet::cancel )
        m_P.Empty();

      break;
    }
  }

  return res;
}

void CRhGetPoints::DynamicDraw( HDC hdc, CRhinoViewport& v, const ON_3dPoint& pt )
{
  if( m_P.Count() > 0 )
  {
    int i;
    for( i = 1; i < m_P.Count(); i++ )
    {
      v.DrawPoint( m_P[i-1] );
      v.DrawLine( m_P[i-1], m_P[i] );
    }
    v.DrawPoint( m_P[i-1] );
    v.DrawPoint( pt );
    v.DrawLine( m_P[i-1], pt );
  }
  CRhinoGetPoint::DynamicDraw( hdc, v, pt);
}

int CRhGetPoints::Points( ON_3dPointArray& points )
{
  int count = m_P.Count();
  if( count > 0 )
    points.Append( count, m_P.Array() );
  return count;
}
```

You would use the above class as follows:

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  CRhGetPoints gp;
  CRhinoGet::result res = gp.GetPoints();
  if( res == CRhinoGet::point )
  {
    // TODO...
  }
  return CRhinoCommand::success;
}
```

## Notes

Some additional features that would make this class better are:

- The code should evaluate the distance between the current point and the previous point before adding them to the point array to ensure the points are not duplicate.
- The code should allow for an undo feature.
- After a few points have been picked, the drawing tends to flicker. This is because the entire polyline is being drawn on every mouse move. To prevent flickering, portions of the polyline that do not need to be drawn on every mouse move should drawn with a conduit.
