+++
aliases = ["/en/5/samples/cpp/add-linear-dimension/", "/en/6/samples/cpp/add-linear-dimension/", "/en/7/samples/cpp/add-linear-dimension/", "/en/wip/samples/cpp/add-linear-dimension/"]
authors = [ "dale" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how to add a linear dimension object."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Add a Linear Dimension"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/addlineardimension"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0
+++

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
