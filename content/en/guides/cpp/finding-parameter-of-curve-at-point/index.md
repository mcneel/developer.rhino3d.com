+++
aliases = ["/en/5/guides/cpp/finding-parameter-of-curve-at-point/", "/en/6/guides/cpp/finding-parameter-of-curve-at-point/", "/en/7/guides/cpp/finding-parameter-of-curve-at-point/", "/wip/guides/cpp/finding-parameter-of-curve-at-point/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This brief guide demonstrates how to find the parameter of a curve at a given 3D point using C/C++."
keywords = [ "rhino", "curve", "point" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Finding the Parameter of a Curve at a Point"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/curveclosestpoint"
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

 
## Overview

In general, to find the parameter of a point on a curve that is closest to a test point, use `ON_Curve::GetClosestPoint()`.  See *opennurbs_curve.h* for more information.

## Sample

The following sample code demonstrates how to find the parameter of a curve at a point.  The code demonstrates how to select a curve object, and how to pick a point on a curve.

For more information on the `CRhinoObjRef` class, see *rhinoSdkObject.h*.

```cpp
CRhinoCommand::result CCommandTest::RunCommand(
    const CRhinoCommandContext& context )
{
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select curve" );
  go.SetGeometryFilter( CRhinoGetObject::curve_object );
  go.GetObjects( 1, 1 );
  if( go.CommandResult() != CRhinoCommand::success )
    return go.CommandResult();

  const CRhinoObjRef& objref = go.Object( 0 );
  const ON_Curve* crv = objref.Curve();
  if( !crv )
    return CRhinoCommand::failure;

  CRhinoGetPoint gp;
  gp.SetCommandPrompt( L"Pick a location on the curve" );
  gp.Constrain( *crv ); // constrain to curve
  gp.GetPoint();
  if( gp.CommandResult() != CRhinoCommand::success )
    return gp.CommandResult();

  ON_3dPoint pt = gp.Point();
  double t = 0.0;
  if( crv->GetClosestPoint(pt, &t) )
    RhinoApp().Print(
      L"Curve parameter at (%f,%f,%f) is %g.\n",
      pt.x, pt.y, pt.z, t );

  return CRhinoCommand::success;
}
```

It is possible to save a step by examining the `CRhinoObjRef` class.  The class return information on the picking operation that just occurred, including the object that was picked, the point that the user picked, and in this case, the parameter of the curve that was closest to the picked point.

```cpp
CRhinoCommand::result CCommandTest::RunCommand(
      const CRhinoCommandContext& context )
{
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select curve" );
  go.SetGeometryFilter( CRhinoGetObject::curve_object );
  go.GetObjects( 1, 1 );
  if( go.CommandResult() != CRhinoCommand::success )
    return go.CommandResult();

  const CRhinoObjRef& objref = go.Object( 0 );

  ON_3dPoint pt;
  objref.SelectionPoint( pt )
  double t = 0.0;
  const ON_Curve* crv = objref.CurveParameter( &t );
  if( crv )
    RhinoApp().Print(
        L"Curve parameter at (%f,%f,%f) is %g.\n",
        pt.x, pt.y, pt.z, t );

  return CRhinoCommand::success;
}
```
