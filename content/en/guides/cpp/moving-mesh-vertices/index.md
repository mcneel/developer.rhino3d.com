+++
authors = [ "dale" ]
categories = [ "Advanced" ]
description = "This brief guide demonstrates how to move mesh vertices using C/C++."
keywords = [ "rhino", "mesh", "vertices" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Moving Mesh Vertices"
type = "guides"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/movemeshvertext"
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

You would like to modify a particular point, or vertex, of `CRhinoMeshObject` object.

## Solution

A `CRhinoMeshObject`'s geometric data member is an `ON_Mesh` object.  For information on the `ON_Mesh` class, the *opennurbs_mesh.h* header file.

Mesh vertices are stored on an `ON_Mesh` in an `m_V` data member, which is simply an array of points.  So, if you want to modify the vertices of a mesh, you need to modify the data in this array.

In order to modify anything in Rhino, you might:

1. Get the object.
1. Make a copy of the object.
1. Modify this copied object.
1. Call one of the `CRhinoDoc::ReplaceObject` overrides to update the object.

## Sample

The following sample demonstrates how you might do this from a command...

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  CRhinoGetObject gv;
  gv.SetCommandPrompt( L"Select mesh vertex to move" );
  gv.SetGeometryFilter( CRhinoGetObject::meshvertex_object );
  gv.GetObjects( 1, 1 );
  if( gv.CommandResult() != success )
    return gv.CommandResult();

  const CRhinoObject* obj = gv.Object(0).Object();
  const ON_MeshVertexRef* vertex = gv.Object(0).MeshVertex();
  if( 0 == obj | 0 == vertex )
    return failure;

  const ON_Mesh* mesh = vertex->m_mesh;
  if( 0 == mesh )
   return failure;

  ON_3dPoint pt = mesh->m_V[vertex->m_mesh_vi];

  CRhinoGetPoint gp;
  gp.SetCommandPrompt( L"New location" );
  gp.SetBasePoint( pt );
  gp.DrawLineFromPoint( pt, TRUE );
  gp.GetPoint();
  if( gp.CommandResult() != success )
    return gp.CommandResult();

  ON_Mesh dupe_mesh( *mesh );
  dupe_mesh.SetVertex( vertex->m_mesh_vi, gp.Point() );

  // Since we've modified ON_Mesh.m_V array,
  // we need to invalidate a few things so they
  // can be recalculated based on the new data.
  dupe_mesh.InvalidateVertexBoundingBox();
  dupe_mesh.InvalidateVertexNormalBoundingBox();
  dupe_mesh.InvalidateCurvatureStats();
  dupe_mesh.m_FN.SetCount(0);
  dupe_mesh.m_N.SetCount(0);
  dupe_mesh.ComputeFaceNormals();
  dupe_mesh.ComputeVertexNormals();
  dupe_mesh.SetClosed(-1);

  if( dupe_mesh.IsValid() )
  {
    context.m_doc.ReplaceObject( CRhinoObjRef(obj), dupe_mesh );
    context.m_doc.Redraw();
  }

  return success;
}
```
