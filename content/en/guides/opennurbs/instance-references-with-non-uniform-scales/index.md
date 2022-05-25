+++
authors = [ "dalelear" ]
categories = [ "Advanced" ]
description = "This guide discusses non-uniform scaling issues when using the openNURBS toolkit"
keywords = [ "openNURBS", "Block", "Instance", "Reference", "Scale" ]
languages = [ "C/C++" ]
sdk = [ "openNURBS" ]
title = "Instance References with Non-Uniform Scales"
type = "guides"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/onblockscalenonuniform"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

 
## Problem

In Rhino, you can insert an instance of a block and give it a non-uniform scale (transformation).  But, when you read the model, using the openNURBS toolkit, and try to explode the block into its geometric form, the geometry is no longer non-uniformly scaled.

## Solution

Not all `ON_Geometry`-derived classes can be accurately modified with transformations like projections, shears, and non-uniform scaling. For example, if you were to apply a non-uniform scale to a circle, which is represented by an `ON_ArcCurve` curve, the resulting geometry is no longer a circle.

When exploding an instance reference into its geometric form, first test to see if the instance reference's transformation is a similarity transformation.  This can be done by using `ON_XForm::IsSimilarity()`.  See *opennurbs_xform.h* for more information.

If the transformation is not a similarity, then convert the geometry into a form that can be accurately modified.  This can be done by using the `ON_Geometry::MakeDeformable()` override on the geometric object...

```cpp
if (bNeedXform)
{
 // If not a similarity transformation, make sure geometry
 // can be deformed. Generally, this involves convert non-NURBS
 // geometry into NURBS geometry.
 if (0 == xform.IsSimilarity() )
   geometry->MakeDeformable();

 // Do the transformation
 geometry->Transform(xform);
}
```
