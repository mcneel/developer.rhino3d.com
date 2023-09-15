+++
aliases = ["/5/guides/cpp/triangulating-polygons/", "/6/guides/cpp/triangulating-polygons/", "/7/guides/cpp/triangulating-polygons/", "/wip/guides/cpp/triangulating-polygons/"]
authors = [ "dale" ]
categories = [ "Advanced" ]
description = "This guide demonstrates how to triangulate polygons using C/C++."
keywords = [ "rhino", "polygons" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Triangulating Polygons"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/triangulatepolygon"
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

Rhino's mesh representation, `ON_Mesh`, only support three and four sided faces. This can pose a problem when trying to write an import plugin for a mesh file format that supports n-sided polygons. If you search the Internet, you can probably find a number of algorithms that will triangulate n-sided polygons so they can be used with `ON_Mesh`. The Rhino C/C++ SDK also includes a tool for doing this.

The `RhinoTriangulate3dPolygon` SDK function will triangulate an n-sided polygon. The polygon must project onto a plane and the projected polygon must be a simple closed curve. For more information on the `RhinoTriangulate3dPolygon`, see the comments in *rhinoSdkMeshUtilities.h*.

## Sample

The following sample code demonstrates how to triangulate a closed planar polygon that has more than three sides using the `RhinoTriangulate3dPolygon` function.  Although this sample demonstrates the function on polyline curves, the code could be easily converted to work on mesh vertices.

```cpp
CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
{
  CRhinoGetObject go;
  go.SetCommandPrompt(L"Select closed planar polygon to triangulate");
  go.SetGeometryFilter(CRhinoGetObject::curve_object);
  go.SetGeometryFilter(CRhinoGetObject::closed_curve);
  go.EnableSubObjectSelect(FALSE);
  go.GetObjects(1, 1);
  if (go.CommandResult() != success)
    return go.CommandResult();

  ON_3dPointArray vertices;

  const CRhinoObjRef& ref = go.Object(0);
  const ON_PolylineCurve* pc = ON_PolylineCurve::Cast(ref.Curve());
  if (pc)
  {
    vertices = pc->m_pline;
  }
  else
  {
    const ON_NurbsCurve* nc = ON_NurbsCurve::Cast(ref.Curve());
    if (nc)
      nc->IsPolyline(&vertices);
  }

  if (vertices.Count() < 5)
  {
    RhinoApp().Print(L"Curve not polygon with at least four sides.\n");
    return CRhinoCommand::nothing;
  }

  int* triangles = (int*)onmalloc((vertices.Count() - 3) * sizeof(int) * 3);
  if (nullptr == triangles)
    return CRhinoCommand::failure; // out of memory

  memset(triangles, 0, (vertices.Count() - 3) * sizeof(int) * 3);

  int rc = RhinoTriangulate3dPolygon(vertices.Count() - 1, 3, (const double*)vertices.Array(), 3, triangles);
  if (0 == rc)
  {
    for (int i = 0; i < vertices.Count() - 3; i++)
    {
      ON_Polyline pline;
      pline.Append(vertices[triangles[i * 3]]);
      pline.Append(vertices[triangles[i * 3 + 1]]);
      pline.Append(vertices[triangles[i * 3 + 2]]);
      pline.Append(pline[0]);
      context.m_doc.AddCurveObject(pline);
    }
    context.m_doc.Redraw();
  }

  onfree(triangles); // don't leak

  return CRhinoCommand::success;
}
```
