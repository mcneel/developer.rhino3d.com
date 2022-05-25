+++
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This guide is an overview of the Rhino geometric object types."
keywords = [ "rhino", "objects" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Object Types"
type = "guides"
weight = 3

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/rhinoobject"
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

`CRhinoObject` is the base class for all runtime Rhino geometric objects.  `ON_Geometry` is the base class for all geometry class.  All `CRhinoObject` derived object maintain a `ON_Geometry` derived class as a data member.

The following is an inventory of the geometric objects you are most likely to encounter in Rhino:

- `CRhinoAnnotationObject` - Virtual base class for annotation objects.
    - `ON_Annotation2`
- `CRhinoAngularDimension` - Angular dimension.
    - `ON_AngularDimension2`
- `CRhinoAnnotationLeader` - Annotation leader.
    - `ON_Leader2`
- `CRhinoLinearDimension` - Linear dimension.
    - `ON_LinearDimension2`
- `CRhinoOrdinateDimension` - Ordinate dimension.
    - `ON_OrdinateDimension2`
- `CRhinoRadialDimension` - Radial dimension.
    - `ON_RadialDimension2`
- `CRhinoAnnotationText` - Annotation text.
    - `ON_TextEntity2`
- `CRhinoBrepObject` - Surface or polysurface.
    - `ON_Brep`
- `CRhinoClippingPlaneObject` - Clipping plane.
    - `ON_ClippingPlane`
- `CRhinoCurveObject` - Curve.
- `ON_Curve` - Virtual base class for curve objects.
    - `ON_ArcCurve`
    - `ON_CurveOnSurface`
    - `ON_CurveProxy`
    - `ON_LineCurve`
    - `ON_NurbsCurve`
    - `ON_PolyCurve`
    - `ON_PolylineCurve`
- `CRhinoDetailViewObject` - Detail view.
    - `ON_DetailView`
- `CRhinoExtrusionObject` - Lightweight extrusion
    - `ON_Extrusion`
- `CRhinoGripObject` - Grip object. Note grip objects are not stored in the document.
    - `ON_Point`
- `CRhinoHatch` - Area hatching.
    - `ON_Hatch`
- `CRhinoInstanceObject` - Block instance.
    - `ON_InstanceRef`
- `CRhinoLight` - Rendering light.
    - `ON_Light`
- `CRhinoMeshObject` - Polygon mesh.
    - `ON_Mesh`
- `CRhinoPointCloudObject` - Point cloud.
    - `ON_PointCloud`
- `CRhinoPointObject` - Point.
    - `ON_Point`
- `CRhinoSurfaceObject` - Untrimmed surface.
    - `ON_Surface`
    - `ON_NurbsSurface`
    - `ON_PlaneSurface`
    - `ON_RevSurface`
    - `ON_SumSurface`
- `CRhinoTextDot` - Text dot.
    - `ON_TextDot`
