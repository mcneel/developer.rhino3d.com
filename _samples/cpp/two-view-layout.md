---
title: Two View Layout
description: Demonstrates how to create a two-view viewport layout.
authors: ['dale_fugier']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Viewports and Views']
origin: http://wiki.mcneel.com/developer/sdksamples/twoviewlayout
order: 1
keywords: ['rhino']
layout: code-sample-cpp
---

```cpp
CRhinoCommand::result CCommand2View::RunCommand( const CRhinoCommandContext& context )
{
  ON_3dmView views[2];
  double def_size = 15.0;
  ON_BoundingBox bbox;
  bbox.m_min.Set( -def_size, -def_size, -def_size );
  bbox.m_max.Set(  def_size, def_size, def_size );
  ON_3dPoint target = ON_origin;
  const CRhinoAppViewSettings& view_settings = RhinoApp().AppSettings().ViewSettings();

  // top view
  {
    views[0].m_name = L"Top";
    views[0].m_target = target;
    ON_3dVector dir( 0.0, 0.0, -100.0 );
    views[0].m_vp.SetCameraLocation( views[0].m_target - dir );
    views[0].m_vp.SetCameraDirection( dir );
    views[0].m_vp.SetCameraUp( ON_yaxis );
    views[0].m_vp.SetProjection( ON::parallel_view );
    views[0].m_vp.SetScreenPort( 0, 100, 100, 0, 0, 1 );
    views[0].m_vp.Extents( atan(12.0 / view_settings.m_camera_lense_length), bbox );
    views[0].m_cplane.m_plane = ON_xy_plane;
    views[0].m_position.m_wnd_left = 0.0;
    views[0].m_position.m_wnd_right = 0.5;
    views[0].m_position.m_wnd_top = 0.0;
    views[0].m_position.m_wnd_bottom = 1.0;
  }

  // perspective view
  {
    views[1].m_name = L"Perspective";
    views[1].m_target = target;
    ON_3dVector dir( -43.30, 75.00, -50.00 );
    views[1].m_vp.SetCameraLocation( views[1].m_target - dir );
    views[1].m_vp.SetCameraDirection( dir );
    views[1].m_vp.SetCameraUp( ON_zaxis );
    views[1].m_vp.SetProjection( ON::perspective_view );
    views[1].m_vp.SetScreenPort( 0, 100, 100, 0, 0, 1 );
    views[1].m_vp.Extents( atan(12.0 / view_settings.m_camera_lense_length), bbox );
    views[0].m_cplane.m_plane = ON_xy_plane;
    views[1].m_position.m_wnd_left = 0.5;
    views[1].m_position.m_wnd_right = 1.0;
    views[1].m_position.m_wnd_top = 0.0;
    views[1].m_position.m_wnd_bottom = 1.0;
  }

  context.m_doc.ReplaceModelViews( 2, views );
  context.m_doc.Redraw();

  return CRhinoCommand::success;
}
```
