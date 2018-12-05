---
title: Add a Brep Box
description: Demonstrates how to add a Brep Box from a Rhino C++ plugin.
authors: ['dale_fugier']
author_contacts: ['dale']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Adding Objects']
origin: http://wiki.mcneel.com/developer/sdksamples/addbrepbox
order: 1
keywords: ['rhino']
layout: code-sample-cpp
---

```cpp
CRhinoCommand::result CCommandTestSdk::RunCommand(const CRhinoCommandContext& context)
{
  CRhinoCommand::result rc = CRhinoCommand::nothing;

  // define the corners of the box
  ON_3dPointArray corners;
  corners.Append( ON_3dPoint( 0.0,  0.0,  0.0) );
  corners.Append( ON_3dPoint(10.0,  0.0,  0.0) );
  corners.Append( ON_3dPoint(10.0, 10.0,  0.0) );
  corners.Append( ON_3dPoint( 0.0, 10.0,  0.0) );
  corners.Append( ON_3dPoint( 0.0,  0.0, 10.0) );
  corners.Append( ON_3dPoint(10.0,  0.0, 10.0) );
  corners.Append( ON_3dPoint(10.0, 10.0, 10.0) );
  corners.Append( ON_3dPoint( 0.0, 10.0, 10.0) );

  // Build the brep  
  ON_Brep* pBrep = ON_BrepBox( corners );
  if( pBrep )
  {
    CRhinoBrepObject* pObject = new CRhinoBrepObject();
    pObject->SetBrep( pBrep );
    if( context.m_doc.AddObject(pObject) )
    {
      context.m_doc.Redraw();
      rc = CRhinoCommand::success;
    }
    else
    {
      delete pObject;
      pObject = 0;
      rc = CRhinoCommand::failure;
    }
  }
  return rc;
}
```
