+++
aliases = ["/en/5/guides/cpp/orienting-objects-on-surfaces/", "/en/6/guides/cpp/orienting-objects-on-surfaces/", "/en/7/guides/cpp/orienting-objects-on-surfaces/", "/en/wip/guides/cpp/orienting-objects-on-surfaces/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This guide demonstrates how to orient objects on a surface using C/C++."
keywords = [ "rhino", "orient" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Orienting Objects on Surfaces"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/orientonsrf"
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

Rhino orients objects onto a surface by defining a rotation transformation.  With the Rhino C/C++ SDK, you define transformations with the `ON_Xform` class.  See *opennurbs_xform.h* for details.  The transformation that is defined rotates objects from one plane to another.  The source plane is defined from the active view's construction plane and a user-selected base point.  The target plane is defined by the location the user picks on the surface.

## Sample

The following sample code demonstrates how to orient objects on a surface.  

**NOTE**: This sample does not contain all of the options available in the Rhino command, nor does it show the objects transforming dynamically, but it is a good example on how to build the transformation.

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  // Select objects to orient
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select objects to orient" );
  go.EnableSubObjectSelect( FALSE );
  go.EnableGroupSelect( TRUE );
  go.GetObjects( 1, 0 );
  if( go.CommandResult() != success )
    return go.CommandResult();

  // Point to orient from
  CRhinoGetPoint gp;
  gp.SetCommandPrompt( L"Point to orient from" );
  gp.GetPoint();
  if( gp.CommandResult() != success )
    return gp.CommandResult();

  // Define source plane
  CRhinoView* view = gp.View();
  if( 0 == view )
  {
    view = RhinoApp().ActiveView();
    if( 0 == view )
      return failure;
  }
  ON_Plane source_plane( view->Viewport().ConstructionPlane().m_plane );
  source_plane.SetOrigin( gp.Point() );

  // Surface to orient on
  CRhinoGetObject gs;
  gs.SetCommandPrompt( L"Surface to orient on" );
  gs.SetGeometryFilter( CRhinoGetObject::surface_object );
  gs.EnableSubObjectSelect( TRUE );
  gs.EnableDeselectAllBeforePostSelect( false );
  gs.EnableOneByOnePostSelect();
  gs.GetObjects( 1, 1 );
  if( gs.CommandResult() != success )
    return gs.CommandResult();

  const CRhinoObjRef& ref = gs.Object(0);
  // Get selected surface object
  const CRhinoObject* obj = ref.Object();
  if( 0 == obj )
    return failure;
  // Get selected surface (face)
  const ON_BrepFace* face = ref.Face();
  if( 0 == face )
    return failure;
  // Unselect surface
  obj->Select( false );

  // Point on surface to orient to
  gp.SetCommandPrompt( L"Point on surface to orient to" );
  gp.Constrain( *face );
  gp.GetPoint();
  if( gp.CommandResult() != success )
    return gp.CommandResult();

  // Do transformation
  CRhinoCommand::result rc = failure;
  double u = 0.0, v = 0.0;
  if( face->GetClosestPoint(gp.Point(), &u, &v) )
  {
    ON_Plane target_plane;
    if( face->FrameAt(u, v, target_plane) )
    {
      // If the face orientation is opposite
      // of natural surface orientation, then
      // flip the plane's zaxis.
      if( face->m_bRev )
      {
        target_plane.yaxis.Reverse();
        target_plane.zaxis.Reverse();
        target_plane.UpdateEquation();
      }

      // Build transformation
      ON_Xform xform;
      xform.Rotation( source_plane, target_plane );

      // Do the transformation. In this example,
      // we will copy the original objects
      bool bDeleteOriginal = false;
      int i;
      for( i = 0; i < go.ObjectCount(); i++ )
        context.m_doc.TransformObject( go.Object(i), xform, bDeleteOriginal );
      context.m_doc.Redraw();
      rc = success;
    }
  }

  return rc;
}
```
