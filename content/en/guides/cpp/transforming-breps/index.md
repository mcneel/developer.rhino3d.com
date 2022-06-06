+++
aliases = ["/5/guides/cpp/transforming-breps/", "/6/guides/cpp/transforming-breps/", "/7/guides/cpp/transforming-breps/", "/wip/guides/cpp/transforming-breps/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This brief guide demonstrates two ways of transforming Breps using C/C++"
keywords = [ "rhino", "transform", "brep" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Transforming Breps"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = "needs more explanatory content."
origin = "http://wiki.mcneel.com/developer/sdksamples/transformbrep"
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

 
## Samples

### The Short Way

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select brep" );
  go.SetGeometryFilter( ON::brep_object );
  go.GetObjects(1,1);
  if( go.CommandResult() != success )
    return go.CommandResult();

  CRhinoObjRef ref = go.Object(0);

  // Simple translation transformation
  ON_Xform xform;
  xform.Translation( ON_3dVector(18,-18,-25) );

  context.m_doc.TransformObject( ref, xform );
  context.m_doc.Redraw();

  return success;
}
```

### The Long Way

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select brep" );
  go.SetGeometryFilter( ON::brep_object );
  go.GetObjects(1,1);
  if( go.CommandResult() != success )
    return go.CommandResult();

  const CRhinoObjRef& ref = go.Object(0);
  const CRhinoObject* obj = ref.Object();
  if( !obj )
    return failure;
  const ON_Brep* brep = ref.Brep();
  if( !brep )
    return failure;
  ON_Brep* dupe = brep->Duplicate();
  if( !dupe )
    return failure;

  // Simple translation transformation
  ON_Xform xform;
  xform.Translation( ON_3dVector(18,-18,-25) );

  if( !dupe->Transform( xform ) )
  {
    RhinoApp().Print( L"Unable to transform object.\n" );
    delete dupe;
    return failure;
  }

  ON_3dmObjectAttributes attribs = obj->Attributes();
  context.m_doc.AddBrepObject( *dupe, &attribs );

  // Since CRhinoDoc::AddBrepObject() make a copy of the input
  // brep, we are responsible for deleting the original. Otherwise
  // we will leak memory;
  delete dupe;
  // Delete the selected object
  context.m_doc.DeleteObject( ref );
  context.m_doc.Redraw();
  return success;
}
```
