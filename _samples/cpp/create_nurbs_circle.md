---
title: Create a NURBS Circle
description: Demonstrates how to use ON_NurbsCurve to create a circle.
author: ['Dale Fugier', '@dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Adding Objects']
origin: http://wiki.mcneel.com/developer/sdksamples/createnurbscircle
order: 1
keywords: ['rhino']
layout: code-sample-cpp
---

```cpp
CRhinoCommand::result CCommandTest::RunCommand(
        const CRhinoCommandContext& context )
{
  int dimension = 3;
  BOOL bIsRational = TRUE;
  int order = 3;
  int cv_count = 9;

  ON_NurbsCurve nc( dimension, bIsRational, order, cv_count );
  nc.SetCV( 0, ON_4dPoint(1.0, 0.0, 0.0, 1.0) );
  nc.SetCV( 1, ON_4dPoint(0.707107, 0.707107, 0.0, 0.707107) );
  nc.SetCV( 2, ON_4dPoint(0.0, 1.0, 0.0, 1.0) );
  nc.SetCV( 3, ON_4dPoint(-0.707107, 0.707107, 0.0, 0.707107) );
  nc.SetCV( 4, ON_4dPoint(-1.0, 0.0, 0.0, 1.0) );
  nc.SetCV( 5, ON_4dPoint(-0.707107, -0.707107, 0.0, 0.707107) );
  nc.SetCV( 6, ON_4dPoint(0.0, -1.0, 0.0, 1.0) );
  nc.SetCV( 7, ON_4dPoint(0.707107, -0.707107, 0.0, 0.707107) );
  nc.SetCV( 8, ON_4dPoint(1.0, 0.0, 0.0, 1.0) );
  nc.SetKnot( 0, 0.0 );
  nc.SetKnot( 1, 0.0 );
  nc.SetKnot( 2, 0.5*ON_PI );
  nc.SetKnot( 3, 0.5*ON_PI );
  nc.SetKnot( 4, ON_PI );
  nc.SetKnot( 5, ON_PI );
  nc.SetKnot( 6, 1.5*ON_PI );
  nc.SetKnot( 7, 1.5*ON_PI );
  nc.SetKnot( 8, 2.0*ON_PI );
  nc.SetKnot( 9, 2.0*ON_PI );

  if( nc.IsValid() )
  {
    context.m_doc.AddCurveObject( nc );
    context.m_doc.Redraw();
  }

  return CRhinoCommand::success;
}
```
