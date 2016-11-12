---
title: Applying Non-Uniform Transformations to Objects
description: This brief guide discusses similarity transformations and how to use them on objects.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/sdksamples/nonuniformscale
order: 1
keywords: ['rhino', 'transformations', 'non-uniform']
layout: toc-guide-page
---

# {{ page.title }}

{% include byline.html %}

{{ page.description }}

## Discussion

Imagine you are trying to apply a non-uniform scale to a cylinder.  If the same scale operation is applied to another object type, it works as expected; but not a cylinder.  Why?

Not all `ON_Geometry` derived classes can be can be accurately modified with "squishy" transformations like projections, shears, an non-uniform scaling.  For example, if you were to apply a non-uniform scale to a circle, which is represented by an `ON_ArcCurve` curve, the resulting geometry is no longer a circle.

Before transforming your object, you will want to first test to see if the the transformation is a similarity transformation.  This can be done by using `ON_XForm::IsSimilarity()`.  See *opennurbs_xform.h* for more information.

If the transformation is not a similarity, then you should convert the geometry into a form that can be accurately modified.  This can be done by using the `ON_Geometry::MakeDeformable()` override on the geometric object.
