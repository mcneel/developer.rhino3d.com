---
title: Move a Construction Plane
description: Demonstrates how to move the origin of a construction plane.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/sdksamples/movecplane
order: 1
keywords: ['rhino']
layout: code-sample-cpp
---

```cpp
class CTestMoveCPlanePoint : public CRhinoGetPoint
{
public:
  CTestMoveCPlanePoint( const ON_3dmConstructionPlane& cplane );
  ~CTestMoveCPlanePoint() {}
  void SetConstructionPlane(const ON_3dmConstructionPlane& cplane);
  void OnMouseMove( CRhinoViewport& vp,
                    UINT flags,
                    const ON_3dPoint& pt,
                    const CPoint* pt2d );
  void DynamicDraw( HDC hdc,
                    CRhinoViewport& vp,
                    const ON_3dPoint& pt );
private:
  ON_3dmConstructionPlane m_cplane;
};

CTestMoveCPlanePoint::CTestMoveCPlanePoint(const ON_3dmConstructionPlane& cplane)
: m_cplane(cplane)
{
}

void CTestMoveCPlanePoint::OnMouseMove( CRhinoViewport& vp, UINT flags,
                                        const ON_3dPoint& pt, const CPoint* pt2d )
{
  m_cplane.m_plane.CreateFromFrame( pt, m_cplane.m_plane.xaxis, m_cplane.m_plane.yaxis );
  CRhinoGetPoint::OnMouseMove( vp, flags, pt, pt2d );
}

void CTestMoveCPlanePoint::DynamicDraw(HDC hdc, CRhinoViewport& vp, const ON_3dPoint& pt)
{
  vp.DrawConstructionPlane( m_cplane, FALSE, TRUE );
  CRhinoGetPoint::DynamicDraw( hdc, vp, pt );
}

CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
{
  CRhinoView* view = ::RhinoApp().ActiveView();
  if( !view )
    return CRhinoCommand::failure;

  ON_3dmConstructionPlane cplane = view->Viewport().ConstructionPlane();
  ON_3dPoint origin = cplane.m_plane.origin;

  CTestMoveCPlanePoint gp( cplane );
  gp.SetCommandPrompt( L"CPlane origin" );
  gp.SetBasePoint( origin );
  gp.DrawLineFromPoint( origin, TRUE );
  gp.GetPoint();

  if( gp.CommandResult() != CRhinoCommand::success )
    return gp.CommandResult();

  ON_3dPoint pt = gp.Point();
  ON_3dVector v = origin - pt;
  if( v.IsTiny() )
    return CRhinoCommand::nothing;

  cplane.m_plane.CreateFromFrame( pt, cplane.m_plane.xaxis,
                                  cplane.m_plane.yaxis );
  view->Viewport().SetConstructionPlane( cplane );
  view->Redraw();
  return CRhinoCommand::success;
}
```
