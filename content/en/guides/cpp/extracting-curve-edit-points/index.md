+++
aliases = ["/5/guides/cpp/extracting-curve-edit-points/", "/6/guides/cpp/extracting-curve-edit-points/", "/7/guides/cpp/extracting-curve-edit-points/", "/wip/guides/cpp/extracting-curve-edit-points/"]
authors = [ "dale" ]
categories = [ "Advanced" ]
description = "This brief guide demonstrates how to extract a curve's edit points using C/C++."
keywords = [ "rhino", "curve", "points" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Extracting Curve Edit Points"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/curveeditpoints"
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

You would like to extract a curve's edit points - the points you see when you run the *EditPtOn* command, but you do not see any methods on `ON_Curve` or `ON_NurbsCurve` to do this.

## Solution

Unlike control points, edit points are not part of a NURBS curve's data structure.  Rather, they are calculated when needed.

The following code demonstrates to get obtain the edit points for a NURBS curve and then create point objects at those locations.

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select curve" );
  go.SetGeometryFilter( CRhinoGetObject::curve_object );
  go.GetObjects( 1, 1 );
  if( go.CommandResult() != success )
    return go.CommandResult();

  const ON_Curve* crv = go.Object(0).Curve();
  if( 0 == crv )
    return failure;

  ON_NurbsCurve nc;
  if( crv->GetNurbForm(nc) )
  {
    // For every control point, we can calculate
    // a cooresponding edit point.
    ON_SimpleArray<double> t( nc.CVCount() );
    t.SetCount( nc.CVCount() );

    if( nc.GetGrevilleAbcissae(t.Array()) )
    {
      int i;
      for( i = 0; i < t.Count(); i++ )
        context.m_doc.AddPointObject( nc.PointAt(t[i]) );
      context.m_doc.Redraw();
    }
  }

  return success;
}
```
