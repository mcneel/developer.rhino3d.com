---
title: Instance References with Non-Uniform Scales
description: This guide discusses non-uniform scaling issues when using the openNURBS toolkit
authors: ['Dale Lear']
author_contacts: ['dalelear']
sdk: ['openNURBS']
languages: ['C/C++']
platforms: ['Windows', 'Mac']
categories: ['Advanced']
origin: http://wiki.mcneel.com/developer/onblockscalenonuniform
order: 1
keywords: ['openNURBS', 'Block', 'Instance', 'Reference', 'Scale']
layout: toc-guide-page
---

 
## Problem

In Rhino, you can insert an instance of a block and give it a non-uniform scale (transformation).  But, when you read the model, using the openNURBS toolkit, and try to explode the block into its geometric form, the geometry is no longer non-uniformly scaled.

## Solution

Not all `ON_Geometry`-derived classes can be accurately modified with squishy transformations like projections, shears, and non-uniform scaling.  For example, if you were to apply a non-uniform scale to a circle, which is represented by an `ON_ArcCurve` curve, the resulting geometry is no longer a circle.

When exploding an instance reference into its geometric form, first test to see if the instance reference's transformation is a similarity transformation.  This can be done by using `ON_XForm::IsSimilarity()`.  See *opennurbs_xform.h* for more information.

If the transformation is not a similarity, then convert the geometry into a form that can be accurately modified.  This can be done by using the `ON_Geometry::MakeDeformable()` override on the geometric object...

```cpp
if( bNeedXform )
{
 // If not a similarity transformation, make sure geometry
 // can be deformed. Generally, this involves convert non-NURBS
 // geometry into NURBS geometry.
 if( 0 == xform.IsSimilarity() )
   geom->MakeDeformable();

 // Do the transformation
 geom->Transform( xform );
}
```

## Sample

The following sample explodes a block in a 3dm file using the method outlined above...

```cpp
#include "../opennurbs.h"

int main( int argc, const char *argv[] )
{
  ON::Begin();

	FILE* archive_fp = ON::OpenFile( L"c:\\Sphere Non-uniform Scale.3dm", L"rb" );
  if( 0 == archive_fp )
    return 0;

  ON_BinaryFile archive( ON::read3dm, archive_fp );

  ONX_Model model;
  bool rc = model.Read( archive );

  ON::CloseFile( archive_fp );

  if( !rc )
    return 0;

  int i, j;
  for( i = 0; i < model.m_object_table.Count(); i++ )
  {
    const ONX_Model_Object& object = model.m_object_table[i];

    // Only look for instance reference objects
		const ON_InstanceRef* iref = ON_InstanceRef::Cast( object.m_object );
    if( 0 == iref )
      continue;

    ON_Xform xform = iref->m_xform;
    const bool bNeedXform = ( xform.IsValid() && !xform.IsZero() && !xform.IsIdentity() );

    int idef_index = model.IDefIndex( iref->m_instance_definition_uuid );
    if( idef_index >= 0 )
    {
      const ON_InstanceDefinition& idef = model.m_idef_table[idef_index];

      for( j = 0; j < idef.m_object_uuid.Count(); j++ )
      {
        int idef_object_index = model.ObjectIndex( idef.m_object_uuid[j] );
        if( idef_object_index >= 0 )
        {
          const ONX_Model_Object& idef_object = model.m_object_table[idef_object_index];

          ON_Geometry* geom = ON_Geometry::Cast( idef_object.m_object->Duplicate() );
          if( geom )
          {
            if( bNeedXform )
            {
              // If not a similarity transformation, make sure geometry
              // can be deformed. Generally, this involves convert non-NURBS
              // geometry into NURBS geometry.
              if( 0 == xform.IsSimilarity() )
                geom->MakeDeformable();

              // Do the transformation
              geom->Transform( xform );
            }

            // Save the geometry to a 3dm file
            ON_wString filename;
            filename.Format( L"c:\\Instance_Definition_Object_%d.3dm", j );
            FILE* fp = ON::OpenFile( filename, L"wb" );
            if( fp )
            {
              ON_BinaryFile archive( ON::write3dm, fp );
              ON_WriteOneObjectArchive( archive, 4, *geom );
              ON::CloseFile( fp );
            }

            // Don't leak...
            delete geom;
            geom = 0;
          }
        }
      }
    }
  }

  model.Destroy();

  ON::End();

  return 1;
}
```
