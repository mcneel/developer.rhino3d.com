---
title: Dynamically Inserting Blocks
description: This guide demonstrates how to insert a block instance at a user specified location using C/C++.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Miscellaneous']
origin: http://wiki.mcneel.com/developer/sdksamples/insertblock
order: 1
keywords: ['rhino', 'block']
layout: toc-guide-page
---

# Dynamically Inserting Blocks

{{ page.description }}

## Overview

To dynamically insert and draw blocks, you can take advantage of the new display pipeline technology, which is capable of drawing block instance definitions.  For example, the following code demonstrates how to draw a block instance definition from a `CRhinoGetPoint`-derived object's DynamicDraw member...

```cpp
class CGetBlockInsertPoint : public CRhinoGetPoint
{
public:
  CGetBlockInsertPoint( const CRhinoInstanceDefinition* idef );

  // CRhinoGetPoint overrides
  void OnMouseMove( CRhinoViewport&, UINT, const ON_3dPoint&, const CPoint* );
  void DynamicDraw( HDC, CRhinoViewport&, const ON_3dPoint& );

  bool CalculateTransform( CRhinoViewport&, const ON_3dPoint&, ON_Xform& );

private:
  const CRhinoInstanceDefinition* m_idef;
  ON_Xform m_xform;
  bool m_bDraw;
};

CGetBlockInsertPoint::CGetBlockInsertPoint( const CRhinoInstanceDefinition* idef )
: m_idef(idef)
{
  m_xform.Identity();
  m_bDraw = false;
}

void CGetBlockInsertPoint::OnMouseMove(
    CRhinoViewport& vp,
    UINT flags,
    const ON_3dPoint& pt,
    const CPoint* p
    )
{
  m_bDraw = CalculateTransform( vp, pt, m_xform );
  CRhinoGetPoint::OnMouseMove( vp, flags, pt, p );
}

void CGetBlockInsertPoint::DynamicDraw(
    HDC hdc,
    CRhinoViewport& vp,
    const ON_3dPoint& pt
    )
{
  if( m_idef && m_bDraw )
  {
    CRhinoDisplayPipeline* dp = vp.DisplayPipeline();
    if( dp )
    {
      dp->PushObjectColor( 0 );
      dp->DrawObject( m_idef, &m_xform );
      dp->PopObjectColor();
    }
  }
  CRhinoGetPoint::DynamicDraw( hdc, vp, pt );
}

bool CGetBlockInsertPoint::CalculateTransform(
    CRhinoViewport& vp,
    const ON_3dPoint& pt,
    ON_Xform& xform
    )
{
  bool rc = false;
  ON_3dVector v = pt - BasePoint();
  if( v.IsTiny() )
    xform.Identity();
  else
    xform.Translation( v );
  return xform.IsValid();
}
```

## Sample

The following sample code demonstrates how to insert a block definition into the Rhino document and allow the user to interactively pick the insertion point.

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  // Prompt for instance definition to insert
  CRhinoGetString gs;
  gs.SetCommandPrompt( L"Name of block to insert" );
  gs.GetString();
  if( gs.CommandResult() != success )
    return gs.CommandResult();

  ON_wString idef_name = gs.String();
  idef_name.TrimLeftAndRight();
  if( idef_name.IsEmpty() )
    return nothing;

  // Find specified instance definition
  CRhinoInstanceDefinitionTable& idef_table = context.m_doc.m_instance_definition_table;
  int idef_index = idef_table.FindInstanceDefinition( idef_name );
  if( idef_index < 0 )
  {
    RhinoApp().Print( L"Unable to insert \"%s\". Block not found.\n", idef_name );
    return nothing;
  }

  // Get instance definition
  const CRhinoInstanceDefinition* idef = idef_table[idef_index];
  if( !idef | idef->IsDeleted() )
    return nothing;

  // Pick an insert point
  CGetBlockInsertPoint gp( idef );
  gp.SetCommandPrompt( L"Insertion point" );
  gp.SetBasePoint( ON_origin );
  gp.GetPoint();
  if( gp.CommandResult() != success )
    return gp.CommandResult();

  // Get active view
  CRhinoView* view = gp.View();
  if( !view )
  {
    view = RhinoApp().ActiveView();
    if( !view )
      return failure;
  }

  // Calculate final xform
  ON_Xform xform;
  if( gp.CalculateTransform(view->ActiveViewport(), gp.Point(), xform) )
  {
    idef_table.AddInstanceObject( idef_index, xform );
    context.m_doc.Redraw();
  }

  return success;
}
```

## Related Topics

- [Creating Blocks]({{ site.baseurl }}/guides/cpp/creating_blocks)
