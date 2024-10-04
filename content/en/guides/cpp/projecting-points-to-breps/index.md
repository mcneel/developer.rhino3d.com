+++
aliases = ["/en/5/guides/cpp/projecting-points-to-breps/", "/en/6/guides/cpp/projecting-points-to-breps/", "/en/7/guides/cpp/projecting-points-to-breps/", "/wip/guides/cpp/projecting-points-to-breps/"]
authors = [ "dale" ]
categories = [ "Advanced" ]
description = "This brief guide demonstrates how to project points onto Brep objects using C/C++."
keywords = [ "rhino", "projecting", "points", "breps" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Projecting Points to Breps"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/projectpointstobreps"
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

You would like to project a 2D point (x,y) onto a brep object in order to acquire the z-coordinate.

## Solution

Use the `RhinoProjectPointsToBreps` function.  In order to use this function you will need to provide the following:

1. An array of one or more Brep objects.
1. An array of one or more points to project.
1. A projection direction (vector).

## Sample

The following sample code demonstrates how you can use this function...

```cpp
CRhinoCommand::result CCommandFoobarCpp::RunCommand( const CRhinoCommandContext& context )
{
  CRhinoGetObject go;
  go.SetCommandPrompt(L"Select surface or polysurface");
  go.SetGeometryFilter(
    CRhinoGetObject::surface_object |
    CRhinoGetObject::polysrf_object
    );
  go.GetObjects(1, 1);
  if (go.CommandResult() != CRhinoCommand::success)
    return go.CommandResult();

  const ON_Brep* brep = go.Object(0).Brep();
  if (0 == brep)
    return CRhinoCommand::failure;

  ON_3dPoint point(0.0, 0.0, 0.0); // some point on the world x-y plane

  // Prepare input to RhinoProjectPointsToBreps

  ON_SimpleArray<const ON_Brep*> Breps;
  Breps.Append(brep);

  ON_3dPointArray Points;
  Points.Append(point);

  ON_3dVector ProjDir(0.0, 0.0, 1.0); // world z-axis

  ON_3dPointArray OutPoints;
  ON_SimpleArray<int> Indices;

  bool rc = RhinoProjectPointsToBreps(
    Breps,
    Points,
    ProjDir,
    OutPoints,
    Indices,
    context.m_doc.AbsoluteTolerance()
    );

  if (rc == true)
  {
    for (int i = 0; i < OutPoints.Count(); i++)
    {
      ON_3dPoint pt = OutPoints[i];
      context.m_doc.AddPointObject(pt);
    }
    context.m_doc.Redraw();
  }

  return CRhinoCommand::success;
}
```
