+++
aliases = ["/en/5/guides/rhinopython/python-rhinoscriptsyntax-nurbs/", "/en/6/guides/rhinopython/python-rhinoscriptsyntax-nurbs/", "/en/7/guides/rhinopython/python-rhinoscriptsyntax-nurbs/", "/en/wip/guides/rhinopython/python-rhinoscriptsyntax-nurbs/"]
authors = [ "dale" ]
categories = [ "Python in Rhino" ]
description = "This guide provides an introduction to Rhino's NURBS Geometry from a Python perspective."
keywords = [ "script", "Rhino", "python" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "Rhino NURBS Geometry Overview"
type = "guides"
weight = 99
override_last_modified = "2020-11-11T22:06:09Z"
draft = false

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Mac", "Windows" ]
since = 7
until = ""

[page_options]
block_webcrawlers = false
byline = true
toc = true
toc_type = "single"
+++

## Overview

Rhino uses various geometry types.  There are some basic types like [Points](/guides/rhinopython/python-rhinoscriptsyntax-points), [Vectors](/guides/rhinopython/python-rhinoscriptsyntax-vectors), [Lines](/guides/rhinopython/python-rhinoscriptsyntax-lines) and [Planes](/guides/rhinopython/python-rhinoscriptsyntax-planes).  In Python, simple geometry can be described with simple lists.

More complicated geometry objects such as NURBS curves, surfaces, and poly-surfaces can be created by Rhino. [Rhino Geometry Objects](/guides/rhinopython/python-rhinoscriptsyntax-objects) are referenced by an object ID by RhinoScriptSyntax

Although not required, having some understanding of the computational methods used in 3D modeling and computer graphics can be helpful when developing in Rhino.  A good introductory resource is the [Essential Mathematics for Computational Design](/guides/general/essential-mathematics/parametric-curves-surfaces/#32-nurbs-curves).  Although all concepts are explained visually using Grasshopper®, they are directly applicable to RhinoScriptSyntax.

#### NURBS Geometry

All NURBS curves and surfaces share terminology and behave similarly.  Since curves are easiest to describe, we will cover them in detail.

A NURBS curve is defined by four things: degree, control points, knots, and an evaluation rule. 

#### Degree

The degree of a curve is a positive whole number. 

This number is usually 1, 2, 3 or 5, but can be any positive whole number.  NURBS lines and polylines are usually degree 1, NURBS circles are degree 2, and most free-form curves are degree 3 or 5.  Sometimes the terms "linear," "quadratic," "cubic," and "quintic" are used.  "Linear" means degree 1, "quadratic" means degree 2, "cubic" means degree 3, and "quintic" means degree 5. 

You may see references to the "order" of a NURBS curve.  The order of a NURBS curve is positive whole number equal to the degree plus one (degree+1).  Consequently, the degree is equal to the order minus one (order-1). 

It is possible to increase the degree of a NURBS curve and not change its shape.  Generally, it is not possible to reduce a NURBS curve’s degree without changing its shape.

#### Control Points

The control points are a list of at least degree+1 points. 

One of easiest ways to change the shape of a NURBS curve is to move its control points. 

The control points have an associated number called a "weight."  With a few exceptions, weights are positive numbers.  When a curve’s control points all have the same weight (usually 1), the curve is called "non-rational"; otherwise the curve is called rational.  The *R* in NURBS stands for *rational* and indicates that a NURBS curve has the possibility of being rational.  In practice, most NURBS curves are *non-rational*.  A few NURBS curves, circles and ellipses being notable examples, are always rational. 

#### Knots

The knots are a list of degree+N-1 numbers, where N is the number of control points.  Sometimes this list of numbers is called the "knot vector."  In this case, the word "vector" does not mean 3D direction. 

This list of knot numbers must satisfy several technical conditions.  The standard way to ensure that the technical conditions are satisfied is to require the numbers to stay the same or get larger as you go down the list and to limit the number of duplicate values to no more than the degree.  For example, for a degree 3 NURBS curve with 11 control points, the list of numbers 0,0,0,1,2,2,2,3,7,7,9,9,9 is a satisfactory list of knots. The list 0,0,0,1,2,2,2,2,7,7,9,9,9 is unacceptable because there are four 2s and four is larger than the degree. 

The number of times a knot value is duplicated is called the knot’s multiplicity.  In the preceding example of a satisfactory list of knots, the knot value 0 has multiplicity three, the knot value 1 has multiplicity one, the knot value 2 has multiplicity three, the knot value 3 has multiplicity one, the knot value 7 has multiplicity two, and the knot value 9 has multiplicity three. A knot value is said to be a full-multiplicity knot if it is duplicated degree many times.  In the example, the knot values 0, 2, and 9 have full multiplicity. A knot value that appears only once is called a simple knot.  In the example, the knot values 1 and 3 are simple knots. 

If a list of knots starts with a full multiplicity knot, is followed by simple knots, terminates with a full multiplicity knot, and the values are equally spaced, then the knots are called uniform.  For example, if a degree 3 NURBS curve with 7 control points has knots 0,0,0,1,2,3,4,4,4, then the curve has uniform knots.  The knots 0,0,0,1,2,5,6,6,6 are not uniform.  Knots that are not uniform are called non-uniform.  The *N* and *U* in NURBS stand for *non-uniform* and indicate that the knots in a NURBS curve are permitted to be non-uniform. 

Duplicate knot values in the middle of the knot list make a NURBS curve less smooth.  At the extreme, a full multiplicity knot in the middle of the knot list means there is a place on the NURBS curve that can be bent into a sharp kink.  For this reason, some designers like to add and remove knots and then adjust control points to make curves have smoother or kinkier shapes.  Since the number of knots is equal to (N+degree-1), where N is the number of control points, adding knots also adds control points and removing knots removes control points.  Knots can be added without changing the shape of a NURBS curve.  In general, removing knots will change the shape of a curve. 

#### Knots and Control Points

A common misconception is that each knot is paired with a control point.  This is true only for degree 1 NURBS (polylines).  For higher degree NURBS, there are groups of 2 x degree knots that correspond to groups of degree+1 control points.  For example, suppose we have a degree 3 NURBS with 7 control points and knots 0,0,0,1,2,5,8,8,8.  The first four control points are grouped with the first six knots.  The second through fifth control points are grouped with the knots 0,0,1,2,5,8.  The third through sixth control points are grouped with the knots 0,1,2,5,8,8.  The last four control points are grouped with the last six knots. 

Some modelers that use older algorithms for NURBS evaluation require two extra knot values for a total of degree+N+1 knots.  When Rhino is exporting and importing NURBS geometry, it automatically adds and removes these two superfluous knots as the situation requires. 

#### Evaluation Rule

A curve evaluation rule is a mathematical formula that takes a number and assigns a point. 

The NURBS evaluation rule is a formula that involves the degree, control points, and knots. In the formula there are some things called B-spline basis functions.  The B and S in NURBS stand for “basis spline.” The number the evaluation rule starts with is called a parameter.  You can think of the evaluation rule as a black box that eats a parameter and produces a point location. The degree, knots, and control points determine how the black box works. 

## Related Topics

- [Essential Mathematics for Computational Design](/guides/general/essential-mathematics/parametric-curves-surfaces/#32-nurbs-curves)
- [Rhino Geometry Objects](/guides/rhinopython/python-rhinoscriptsyntax-objects)
