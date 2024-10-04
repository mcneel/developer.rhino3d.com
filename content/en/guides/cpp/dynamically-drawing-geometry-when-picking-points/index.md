+++
aliases = ["/en/5/guides/cpp/dynamically-drawing-geometry-when-picking-points/", "/en/6/guides/cpp/dynamically-drawing-geometry-when-picking-points/", "/en/7/guides/cpp/dynamically-drawing-geometry-when-picking-points/", "/wip/guides/cpp/dynamically-drawing-geometry-when-picking-points/"]
authors = [ "dale" ]
categories = [ "Advanced" ]
description = "This guide demonstrates how to derive a new class to dynamically draw geometry during a point picking operation using C/C++."
keywords = [ "rhino", "drawing", "picking" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Dynamically Drawing Geometry when Picking Points"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/getpointdynamicdraw"
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

 
## Overview

When using Rhino, you have probably noticed that many of the object creation commands, such as *Line* and *Circle*, and transformation commands, such as *Move* and *Copy*, dynamically draw objects as they are being created or transformed.  This operation is performed by deriving a new class from Rhino's point pick class, `CRhinoGetPoint`, and overriding two member functions: `OnMouseMove()` and `DynamicDraw()`.

`OnMouseMove()` is called every time the mouse moves.  This is a great place to perform calculations, such as transformations.

`DynamicDraw()` is called as the mouse moves, as well.  Every time the mouse moves, `DynamicDraw()` will be called once per viewport.  

**NOTE**: Rhino calls `DynamicDraw()` happen after the call to `OnMouseMove()`.

## Sample

The following sample demonstrates how to derive a new class from `CRhinoGetPoint` and override `OnMouseMove()` and `DynamicDraw()` to dynamically draw geometry.  In this sample, we are going to dynamically draw a circle while the user is specifying its radius.

```cpp
class CGetCircleRadiusPoint : public CRhinoGetPoint
{
public:
  CGetCircleRadiusPoint();
  void SetCenterPoint( const ON_3dPoint center_point );
  bool CalculateCircle( CRhinoViewport& vp, const ON_3dPoint& pt );

  void OnMouseMove( CRhinoViewport& vp,
                    UINT flags,
                    const ON_3dPoint& pt,
                    const CPoint* pt2d );

  void DynamicDraw( HDC hDC, CRhinoViewport& vp, const ON_3dPoint& pt );
  const ON_Circle& Circle() const;
private:
  ON_Circle m_circle;
  ON_3dPoint m_center_point;
  bool m_draw_circle;
};

CGetCircleRadiusPoint::CGetCircleRadiusPoint()
{
  m_draw_circle = false;
}

void CGetCircleRadiusPoint::SetCenterPoint( const ON_3dPoint center_point )
{
  m_center_point = center_point;
}

bool CGetCircleRadiusPoint::CalculateCircle( CRhinoViewport& vp, const ON_3dPoint& pt )
{
  double radius = m_center_point.DistanceTo( pt );
  if( radius < ON_SQRT_EPSILON )
    return false;

  ON_Plane plane = vp.ConstructionPlane().m_plane;
  plane.SetOrigin( m_center_point );
  m_circle.Create( plane, radius );
  return m_circle.IsValid() ? true : false;
}

void CGetCircleRadiusPoint::OnMouseMove( CRhinoViewport& vp,
                                         UINT flags,
                                         const ON_3dPoint& pt,
                                         const CPoint* pt2d )
{
  m_draw_circle = CalculateCircle( vp, pt );
  CRhinoGetPoint::OnMouseMove( vp, flags, pt, pt2d );
}

void CGetCircleRadiusPoint::DynamicDraw( HDC hDC,
                                         CRhinoViewport& vp,
                                         const ON_3dPoint& pt )
{
  if( m_draw_circle )
  {
    ON_Color color = RhinoApp().AppSettings().TrackingColor();
    ON_Color saved_color = vp.SetDrawColor( color );
    vp.DrawCircle( m_circle );
    vp.SetDrawColor( saved_color );
  }
  CRhinoGetPoint::DynamicDraw( hDC, vp, pt );
}
const ON_Circle& CGetCircleRadiusPoint::Circle() const
{
  return m_circle;
}
```

Finally, here is our `CRhinoGetPoint` derived class in action:

```cpp
CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
{
  CRhinoGetPoint gp;
  gp.SetCommandPrompt( L"Center point" );
  gp.ConstrainToConstructionPlane( FALSE );
  gp.GetPoint();
  if( gp.CommandResult() != CRhinoCommand::success )
    return gp.CommandResult();

  ON_3dPoint center_point = gp.Point();

  CGetCircleRadiusPoint gc;
  gc.SetCommandPrompt( L"Radius" );
  gc.ConstrainToConstructionPlane( FALSE );
  gc.SetBasePoint( center_point );
  gc.DrawLineFromPoint( center_point, TRUE );
  gc.SetCenterPoint( center_point );
  gc.GetPoint();
  if( gc.CommandResult() != CRhinoCommand::success )
    return gc.CommandResult();

  if( gc.CalculateCircle( gc.View()->Viewport(), gc.Point() ))
  {
    ON_Circle circle = gc.Circle();
    context.m_doc.AddCurveObject( circle );
    context.m_doc.Redraw();
  }
  return CRhinoCommand::success;
}
```
