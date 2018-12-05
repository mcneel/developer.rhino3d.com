---
title: Add a Linear Dimension
description: Demonstrates how to add a linear dimension object.
authors: ['dale_fugier']
author_contacts: ['dale']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Adding Objects']
origin: http://wiki.mcneel.com/developer/sdksamples/addlineardimension
order: 1
keywords: ['rhino']
layout: code-sample-cpp
---

```cpp
// The following is a demonstration of how to interactively add a linear dimension object to Rhino.
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  CRhinoLinearDimension* pDim = 0;

  CArgsRhinoDimLinear args;
  args.SetFirstPointPrompt( L"First dimension point" );
  args.SetSecondPointPrompt( L"Second dimension point" );
  args.SetDragPointPrompt( L"Dimension location" );
  args.SetIsInteractive( context.IsInteractive() ? true : false );

  CRhinoCommand::result rc = RhinoGetDimLinear( args, pDim, 0 );

  if( rc == success && pDim )
  {
    context.m_doc.AddObject( pDim, FALSE);
    context.m_doc.Redraw();
  }

  return rc;
}
```
