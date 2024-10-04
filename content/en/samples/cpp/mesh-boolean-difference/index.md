+++
aliases = ["/en/5/samples/cpp/mesh-boolean-difference/", "/en/6/samples/cpp/mesh-boolean-difference/", "/en/7/samples/cpp/mesh-boolean-difference/", "/wip/samples/cpp/mesh-boolean-difference/"]
authors = [ "dale" ]
categories = [ "Other" ]
description = "Demonstrates how to use the RhinoMeshBooleanDifference function."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Mesh Boolean Difference"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/meshbooleandifference"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  CRhinoGetObject go0;
  go0.SetCommandPrompt( L"Select first set of meshes" );
  go0.SetGeometryFilter( CRhinoGetObject::mesh_object );
  go0.GetObjects( 1, 0 );
  if( go0.CommandResult() != success )
    return go0.CommandResult();

  CRhinoGetObject go1;
  go1.SetCommandPrompt( L"Select second set of meshes" );
  go1.SetGeometryFilter( CRhinoGetObject::mesh_object );
  go1.EnablePreSelect( false );
  go1.EnableDeselectAllBeforePostSelect( false );
  go1.GetObjects( 1, 0 );
  if( go1.CommandResult() != success )
    return go1.CommandResult();

  ON_SimpleArray<const CRhinoObject*> DeleteList( go0.ObjectCount() + go1.ObjectCount() );
  int i = 0;

  ON_SimpleArray<const ON_Mesh*> InMeshes0( go0.ObjectCount() );
  ON_SimpleArray<const ON_3dmObjectAttributes*> InAttributes0( go0.ObjectCount() );
  for( i = 0; i < go0.ObjectCount(); i++ )
  {
    const CRhinoObject* p = go0.Object(i).Object();
    if( !p )
      return failure;

    const ON_Mesh* mesh = ON_Mesh::Cast( p->Geometry() );
    if( !mesh )
      return failure;

    InMeshes0.Append( mesh );
    InAttributes0.Append( &p->Attributes() );

    DeleteList.Append( p );
  }

  ON_SimpleArray<const ON_Mesh*> InMeshes1( go1.ObjectCount() );
  for( i = 0; i < go1.ObjectCount(); i++ )
  {
    const CRhinoObject* p = go1.Object(i).Object();
    if( !p )
      return failure;

    const ON_Mesh* mesh = ON_Mesh::Cast( p->Geometry() );
    if( !mesh )
      return failure;

    InMeshes1.Append( mesh );

    DeleteList.Append( p );
  }

  ON_SimpleArray<ON_Mesh*> OutMeshes;
  ON_SimpleArray<const ON_3dmObjectAttributes*> OutAttributes;
  bool bResult = false;
  bool rc = RhinoMeshBooleanDifference(
        InMeshes0,
        InMeshes1,
        ON_SQRT_EPSILON*10,
        ON_SQRT_EPSILON*10,
        &bResult,
        OutMeshes,
        &InAttributes0,
        &OutAttributes
        );

  if( !rc )
    return failure;

  for( i = 0; i < OutMeshes.Count(); i++ )
  {
    CRhinoMeshObject* pMeshObj = 0;
    if( i < OutAttributes.Count() )
      pMeshObj = new CRhinoMeshObject( *OutAttributes[i] );
    else
      pMeshObj = new CRhinoMeshObject();

    if( pMeshObj )
    {
      pMeshObj->SetMesh( OutMeshes[i] );
      context.m_doc.AddObject( pMeshObj );
    }
    else
    {
      delete OutMeshes[i];
    }
    OutMeshes[i] = 0;
  }

  for( i = 0; i < DeleteList.Count(); i++ )
  {
    if( DeleteList[i] )
      context.m_doc.DeleteObject( DeleteList[i] );
  }

  context.m_doc.Redraw();

  return success;
}
```
